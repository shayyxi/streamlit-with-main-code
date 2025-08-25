import json
from dataclasses import asdict
from datetime import date
import psycopg2
from api_response_processor import data_classes
from metrics_persistence import summary_table_name as summary_table_enum

class MetricsPersistence:
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url,
                                     sslmode="require",
                                     connect_timeout=10,
                                     keepalives=1,
                                     keepalives_idle=30,
                                     keepalives_interval=10,
                                     keepalives_count=3)
        self.cursor = self.conn.cursor()
        self.create_table_if_not_exist()

    def create_table_if_not_exist(self):
        self.cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'summary_table_enum') THEN
                    CREATE TYPE summary_table_enum AS ENUM (
                        'property_summary',
                        'units_summary',
                        'rent_summary'
                    );
                END IF;
            END
            $$;
            """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS property_metrics (
            id SERIAL PRIMARY KEY,
            property_id INTEGER NOT NULL,
            date DATE NOT NULL,
            summary_table_name summary_table_enum NOT NULL,
            data JSONB NOT NULL
        );
        """)
        self.conn.commit()

    def insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(self, property_id, data, summary_table_name):
        if data is None or summary_table_name is None or property_id is None:
            return
        values_in_enum = [item.value for item in summary_table_enum.SummaryTableName]
        if not summary_table_name in values_in_enum:
            return
        metric_jsonb = json.dumps(asdict(data))
        today_date = date.today()
        if today_date.weekday() == 6 or (summary_table_name == summary_table_enum.SummaryTableName.RENT_SUMMARY.value and today_date.day == 5):
        # if True:
            insert_query = """
                           INSERT INTO property_metrics (property_id, date, summary_table_name, data)
                           VALUES (%s, %s, %s, %s) \
                           """
            self.cursor.execute(insert_query, (property_id, today_date, summary_table_name, metric_jsonb))
            self.conn.commit()

    def get_property_metrics(self, property_id, summary_table_name):
        if property_id is None or summary_table_name is None:
            return {}
        # get the metrics from table and parse them to dataclass
        try:
            self.cursor.execute("""
                SELECT date, data
                FROM property_metrics
                WHERE property_id = %s AND summary_table_name = %s
                ORDER BY date DESC
            """, (property_id, summary_table_name))
            rows = self.cursor.fetchall()
            match summary_table_name:
                case summary_table_enum.SummaryTableName.PROPERTY_SUMMARY.value:
                    cls = data_classes.PropertySummary
                case summary_table_enum.SummaryTableName.UNITS_SUMMARY.value:
                    cls = data_classes.UnitsSummary
                case summary_table_enum.SummaryTableName.RENT_SUMMARY.value:
                    cls = data_classes.RentSummaryForPersistence
                case _:
                    return {}
            return {row[0]: cls(**row[1]) for row in rows}
        except Exception as e:
            print(f"Error fetching property metrics: {e}")
            return {}

    def close(self):
        self.cursor.close()
        self.conn.close()

# add the clean up method to clean old rows