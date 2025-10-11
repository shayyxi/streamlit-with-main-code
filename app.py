import streamlit as st
import pandas as pd
import plotly.express as px
from dataclasses import asdict
from typing import Any
import datetime

import api_response_processor.helpers
from api_response_processor.data_classes import (
PropertySummary, UnitsSummary, ResidentRetentionSummaryForNoticeAndMTM,
ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths,
RentSummaryForCurrentAndLastTwoMonths,
MaintenanceSummaryForThreeWeeks,
LeadsSummaryForThreeWeeks
)

from api_response_processor import (
api_response_processor_property_summary, api_response_processor_units_summary,
api_response_processor_rent_summary, api_response_processor_units_summary,
api_response_processor_resident_retention, api_response_processor_leads_summary,
api_response_processor_maintenance_summary
)

from metrics_persistence.metrics_persistence import MetricsPersistence
from metrics_persistence import summary_table_name


# =========================
# GLOBALS / THEME
# =========================
ACCENT = "#0f988f"  # teal


# =========================
# PAGE SETUP & STYLES
# =========================
def setup_page():
    st.set_page_config(page_title="Property Dashboard", page_icon="🏢", layout="wide")

def inject_css():
    st.markdown(f"""
    <style>
    .main > div:first-child {{ padding-top: 0rem; }}
    .block-container {{ padding-top: 1rem; }}

    /* KPI cards */
    .kpi-grid {{ margin: .25rem 0 1rem; }}
    .kpi-card {{
      background: #dfeeea;               /* soft green */
      border-radius: 14px;
      padding: 14px 18px;
      box-shadow: 0 2px 14px rgba(0,0,0,.05);
      border: 1px solid rgba(0,0,0,.06);
    }}
    .kpi-label {{ font-size: 0.95rem; color: #4b5563; }}
    .kpi-value {{ font-size: 2rem; font-weight: 700; line-height: 1.1; }}

    div[data-testid="stPlotlyChart"] {{
      background: #f6faf9; border: 1px solid rgba(0,0,0,.08);
      border-radius: 14px; padding: 12px 12px 6px; box-shadow: 0 2px 12px rgba(0,0,0,.05);
    }}

    /* Segmented centered tabs */
    div[data-baseweb="tab-list"] {{
      width: 100%; max-width: 900px; margin: 0rem auto 0.75rem; padding: 6px;
      background: #eaf2f1; border-radius: 14px; box-shadow: 0 2px 16px rgba(0,0,0,.06);
      display: flex; gap: 6px;
    }}
    button[data-baseweb="tab"] {{
      flex: 1 1 0; justify-content: center; border-radius: 10px; background: transparent;
      color: #0b2b2b; font-weight: 700; font-size: 1.02rem; padding: .7rem 1.2rem;
      border: 2px solid transparent; transition: all .15s ease-in-out;
    }}
    button[data-baseweb="tab"]:hover {{ background: rgba(15,152,143,.08); }}
    button[data-baseweb="tab"][aria-selected="true"] {{
      background: {ACCENT}; color: #fff; border-color: {ACCENT};
      box-shadow: 0 1px 6px rgba(15,152,143,.35);
    }}
    button[data-baseweb="tab"] > div:first-child {{ border-bottom: none !important; }}
    </style>
    """, unsafe_allow_html=True)


# =========================
# HELPERS
# =========================
def safe_num(v: Any) -> float:
    """Convert Union[int,str,None] to float (NaN on fail)."""
    try:
        if v is None: return float("nan")
        if isinstance(v, str) and v.strip() == "": return float("nan")
        return float(v)
    except Exception:
        return float("nan")

def k(value, currency=False):
    if value in (None, "NA", ""): return "—"
    try:
        v = float(value)
        if currency: return f"${v/1000:,.2f} K"
        if v.is_integer(): return f"{int(v):,}"
        return f"{v:,.2f}"
    except Exception:
        return str(value)

def pct(value):
    if value in (None, "NA", ""): return "—"
    try:
        v = float(str(value).replace("%",""))
        return f"{v:,.2f} %"
    except Exception:
        return str(value)

def kpi_card(label: str, value: str):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def dc_to_df(obj) -> pd.DataFrame:
    """Dataclass -> one-row DataFrame (flat)."""
    return pd.DataFrame([asdict(obj)])

def cardify(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="center", x=0.5,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="rgba(0,0,0,0.1)", borderwidth=1
        )
    )
    return fig


# =========================
# DEMO DATA (replace with your real instances)
# =========================
def create_demo_models():
    db_url = st.secrets["DB_URL"]
    metrics_persistence = MetricsPersistence(db_url)
    property_id = 100082999 #4060 preferred place
    property_summary = api_response_processor_property_summary.get_property_summary(property_id)
    # rent summary
    rent_summary = api_response_processor_rent_summary.get_rent_summary(property_id, metrics_persistence)
    # units summary
    units_summary = api_response_processor_units_summary.get_units_summary(property_id)
    #persist property summary and units summary
    # put db data for property summary
    metrics_persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(property_id, property_summary,
                                                                                        summary_table_name.SummaryTableName.PROPERTY_SUMMARY.value)
    # put db data for units summary
    metrics_persistence.insert_property_metrics_if_day_is_sunday_or_5th_in_rent_summary(property_id, units_summary,
                                                                                        summary_table_name.SummaryTableName.UNITS_SUMMARY.value)
    #getting previous data for property and units summary
    # property summary dict
    previous_property_summary = metrics_persistence.get_property_metrics(property_id,
                                                                         summary_table_name.SummaryTableName.PROPERTY_SUMMARY.value)

    if len(previous_property_summary.keys()) > 0:
        all_property_summary = {datetime.date.today(): property_summary, **previous_property_summary}
    else:
        all_property_summary = {datetime.date.today(): property_summary}

    # units summary dict
    previous_units_summary = metrics_persistence.get_property_metrics(property_id,
                                                                      summary_table_name.SummaryTableName.UNITS_SUMMARY.value)

    if len(previous_units_summary.keys()) > 0:
        all_units_summary = {datetime.date.today(): units_summary, **previous_units_summary}
    else:
        all_units_summary = {datetime.date.today(): units_summary}

    # resident retention summary
    (resident_retention_summary_for_expiry_and_renewal_for_three_months,
     resident_retention_summary_for_notice_and_mtm) = api_response_processor_resident_retention.get_resident_retention_summary(
        property_id)
    # leads summary
    leads_summary_for_three_weeks = api_response_processor_leads_summary.get_leads_summary(property_id)
    # maintenance summary
    maintenance_summary_for_three_weeks = api_response_processor_maintenance_summary.get_maintenance_summary(
        property_id)
    metrics_persistence.close()
    return (all_property_summary,
            all_units_summary,
            resident_retention_summary_for_notice_and_mtm,
            resident_retention_summary_for_expiry_and_renewal_for_three_months,
            rent_summary,
            maintenance_summary_for_three_weeks,
            leads_summary_for_three_weeks)


# =========================
# RENDERERS (tabs)
# =========================
def render_overview(ps_by_date: dict[str, PropertySummary],
                    rs: RentSummaryForCurrentAndLastTwoMonths):
    """
    ps_by_date: Ordered dict {date_string: PropertySummary, ...}
                First item = latest date.
    rs: RentSummaryForCurrentAndLastTwoMonths dataclass.
    """

    # ---- KPIs from latest ----
    latest_date, latest_ps = next(iter(ps_by_date.items()))

    st.markdown('<div class="kpi-grid"></div>', unsafe_allow_html=True)
    a,b,c,d,e,f,g = st.columns(7, gap="small")
    with a: kpi_card("Total Units", k(latest_ps.total_units))
    with b: kpi_card("Rentable Units", k(latest_ps.total_rentable_units))
    with c: kpi_card("Excluded Units", k(latest_ps.excluded_units))
    with d: kpi_card("Occupied %", pct(latest_ps.occupied_units_percentage))
    with e: kpi_card("Leased %", pct(latest_ps.leased_units_percentage))
    with f: kpi_card("Trend %", pct(latest_ps.trend_percentage))
    with g: kpi_card("Evictions/Skips (MTD)", k(latest_ps.evictions_and_skips_occurred_for_current_month))

    # ---- Rent billed vs collected (3 months) ----
    rent_rows = [
        {
            "Period": "Current",
            "Billed": safe_num(rs.current_month_total_rent_billed),
            "Collected": safe_num(rs.current_month_total_rent_collected),
            "Range": f'{rs.current_month_first_date} → {rs.current_month_today_date}'
        },
        {
            "Period": "Last",
            "Billed": safe_num(rs.last_month_total_rent_billed),
            "Collected": safe_num(rs.last_month_total_rent_collected),
            "Range": f'{rs.last_month_first_date} → {rs.last_month_last_date}'
        },
        {
            "Period": "Month Before Last",
            "Billed": safe_num(rs.month_before_last_total_rent_billed),
            "Collected": safe_num(rs.month_before_last_total_rent_collected),
            "Range": f'{rs.month_before_last_first_date} → {rs.month_before_last_last_date}'
        },
    ]
    rent_df = pd.DataFrame(rent_rows)
    rent_long = rent_df.melt(id_vars=["Period","Range"],
                             value_vars=["Billed","Collected"],
                             var_name="Type", value_name="Amount")

    left, right = st.columns(2)
    with left:
        st.subheader("Rent billed vs collected")
        fig = px.bar(rent_long, x="Period", y="Amount", color="Type", barmode="group",
                     hover_data=["Range"], text_auto=".2s")
        st.plotly_chart(cardify(fig), use_container_width=True, key="rent_billed_collected")

    with right:
        st.subheader("Collection %")
        coll = pd.DataFrame({
            "Period": ["Current","Last","Month Before Last"],
            "Collected %": [
                safe_num(str(rs.current_month_total_rent_collected_percentage).replace("%","")),
                safe_num(str(rs.last_month_total_rent_collected_percentage).replace("%","")),
                safe_num(str(rs.month_before_last_total_rent_collected_percentage).replace("%","")),
            ]
        })
        fig2 = px.bar(coll, x="Period", y="Collected %", text_auto=".1f")
        st.plotly_chart(cardify(fig2), use_container_width=True, key="collection_pct")

    # ---- Raw property summaries table ----
    raw_rows = []
    for date_key, ps in ps_by_date.items():
        row = {"Date": date_key, **asdict(ps)}
        raw_rows.append(row)
    raw_df = pd.DataFrame(raw_rows)

    st.write("---")
    st.subheader("Property summary (raw)")
    st.dataframe(raw_df, use_container_width=True, hide_index=True, key="ps_table")


def render_operations(us_by_date: dict[str, UnitsSummary],
                      maint: MaintenanceSummaryForThreeWeeks,
                      leads: LeadsSummaryForThreeWeeks):
    """
    us_by_date: Ordered dict {date_string: UnitsSummary, ...}
                First item = latest date.
    maint: MaintenanceSummaryForThreeWeeks dataclass.
    leads: LeadsSummaryForThreeWeeks dataclass.
    """

    # ---- KPIs from latest UnitsSummary ----
    latest_date, latest_us = next(iter(us_by_date.items()))

    # get last monday date string
    last_monday_date = api_response_processor.helpers.get_last_monday_date(latest_date)
    date_label = f"{last_monday_date} - {latest_date}"

    st.markdown('<div class="kpi-grid"></div>', unsafe_allow_html=True)
    a,b,c,d = st.columns(4, gap="large")
    with a: kpi_card("Occupied Units", k(latest_us.count_of_occupied_units))
    with b: kpi_card("Vacant Units", k(latest_us.count_of_vacant_units))
    with c: kpi_card(f"Move-ins ({date_label})", k(latest_us.count_of_total_move_ins))
    with d: kpi_card(f"Move-outs ({date_label})", k(latest_us.count_of_total_move_out))

    # ---- Maintenance (3 weeks) ----
    maint_df = pd.DataFrame([
        {"Week":"Current", "Open":safe_num(maint.current_week_open_work_orders_count),
         "Completed":safe_num(maint.current_week_completed_work_orders_count),
         "Range": f"{maint.current_week_monday_date} → {maint.current_week_end_date}"},
        {"Week":"Last", "Open":safe_num(maint.last_week_open_work_orders_count),
         "Completed":safe_num(maint.last_week_completed_work_orders_count),
         "Range": f"{maint.last_week_monday_date} → {maint.last_week_sunday_date}"},
        {"Week":"Week Before Last", "Open":safe_num(maint.week_before_last_open_work_orders_count),
         "Completed":safe_num(maint.week_before_last_completed_work_orders_count),
         "Range": f"{maint.week_before_last_monday_date} → {maint.week_before_last_sunday_date}"},
    ])
    maint_long = maint_df.melt(id_vars=["Week","Range"], value_vars=["Open","Completed"],
                               var_name="Status", value_name="Count")

    # ---- Leads (3 weeks) ----
    leads_df = pd.DataFrame([
        {"Week":"Current", "Range": f"{leads.current_week_monday_date} → {leads.current_week_end_date}",
         "New Leads":safe_num(leads.current_week_new_leads_count),
         "Apps Started":safe_num(leads.current_week_applications_started_count),
         "Approved":safe_num(leads.current_week_approved_applications_count),
         "Cancelled":safe_num(leads.current_week_cancelled_applications_count)},
        {"Week":"Last", "Range": f"{leads.last_week_monday_date} → {leads.last_week_end_date}",
         "New Leads":safe_num(leads.last_week_new_leads_count),
         "Apps Started":safe_num(leads.last_week_applications_started_count),
         "Approved":safe_num(leads.last_week_approved_applications_count),
         "Cancelled":safe_num(leads.last_week_cancelled_applications_count)},
        {"Week":"Week Before Last", "Range": f"{leads.week_before_last_monday_date} → {leads.week_before_last_end_date}",
         "New Leads":safe_num(leads.week_before_last_new_leads_count),
         "Apps Started":safe_num(leads.week_before_last_applications_started_count),
         "Approved":safe_num(leads.week_before_last_approved_applications_count),
         "Cancelled":safe_num(leads.week_before_last_cancelled_applications_count)},
    ])
    leads_long = leads_df.melt(id_vars=["Week","Range"], var_name="Stage", value_name="Count")

    # ---- Charts ----
    left, right = st.columns(2)
    with left:
        st.subheader("Maintenance — Open vs Completed (3 weeks)")
        fig3 = px.bar(maint_long, x="Week", y="Count", color="Status", barmode="group",
                      hover_data=["Range"], text_auto=".0f")
        st.plotly_chart(cardify(fig3), use_container_width=True, key="maint_3w")
    with right:
        st.subheader("Leads & Applications (3 weeks)")
        fig4 = px.bar(leads_long, x="Week", y="Count", color="Stage", barmode="group",
                      hover_data=["Range"], text_auto=".0f")
        st.plotly_chart(cardify(fig4), use_container_width=True, key="leads_3w")

    # ---- Raw UnitsSummary table ----
    raw_rows = []
    for date_key, us in us_by_date.items():
        last_monday_date = api_response_processor.helpers.get_last_monday_date(date_key)
        date_str = f"{last_monday_date} - {date_key}"
        row = {"Date": date_str, **asdict(us)}
        raw_rows.append(row)
    raw_df = pd.DataFrame(raw_rows)

    st.write("---")
    st.subheader("Units summary (raw)")
    st.dataframe(raw_df, use_container_width=True, hide_index=True, key="us_table")


def render_retention(notice_mtm: ResidentRetentionSummaryForNoticeAndMTM,
                     expiry3: ResidentRetentionSummaryForExpiryAndRenewalForThreeMonths):
    st.markdown('<div class="kpi-grid"></div>', unsafe_allow_html=True)
    a,b,c = st.columns(3, gap="large")
    with a: kpi_card("Notice - Non-renewed", k(notice_mtm.notice_non_renewed_leases_count))
    with b: kpi_card("Notice - Eviction", k(notice_mtm.notice_eviction_leases_count))
    with c: kpi_card("MTM - Need Renewal", k(notice_mtm.need_renewal_mtm_leases_count))

    # Expiring/Renewal — 3 months side-by-side
    exp_df = pd.DataFrame([
        {"Month":"Current", "Expiring":safe_num(expiry3.current_month_total_expiring_leases_count),
         "Renewed":safe_num(expiry3.current_month_renewed_leases_count),
         "Under Renewal":safe_num(expiry3.current_month_under_renewal_leases_count),
         "Need Renewal":safe_num(expiry3.current_month_need_renewal_leases_count),
         "Range": f"{expiry3.current_month_first_date} → {expiry3.current_month_last_date}"},
        {"Month":"Next", "Expiring":safe_num(expiry3.next_month_total_expiring_leases_count),
         "Renewed":safe_num(expiry3.next_month_renewed_leases_count),
         "Under Renewal":safe_num(expiry3.next_month_under_renewal_leases_count),
         "Need Renewal":safe_num(expiry3.next_month_need_renewal_leases_count),
         "Range": f"{expiry3.next_month_first_date} → {expiry3.next_month_last_date}"},
        {"Month":"Next to next", "Expiring":safe_num(expiry3.next_to_next_month_total_expiring_leases_count),
         "Renewed":safe_num(expiry3.next_to_next_month_renewed_leases_count),
         "Under Renewal":safe_num(expiry3.next_to_next_month_under_renewal_leases_count),
         "Need Renewal":safe_num(expiry3.next_to_next_month_need_renewal_leases_count),
         "Range": f"{expiry3.next_to_next_month_first_date} → {expiry3.next_to_next_month_last_date}"},
    ])
    exp_long = exp_df.melt(id_vars=["Month","Range"], var_name="Status", value_name="Count")

    left, right = st.columns(2)
    with left:
        st.subheader("Expiring / Renewal status (3 months)")
        fig = px.bar(exp_long, x="Month", y="Count", color="Status", barmode="group",
                     hover_data=["Range"], text_auto=".0f")
        st.plotly_chart(cardify(fig), use_container_width=True, key="expiry3")
    with right:
        st.subheader("Notice & MTM (raw)")
        st.dataframe(dc_to_df(notice_mtm), use_container_width=True, hide_index=True, key="notice_table")

    st.write("---")
    st.subheader("Expiry & Renewal (raw)")
    st.dataframe(exp_df, use_container_width=True, hide_index=True, key="expiry_table")


# =========================
# ENTRY POINT
# =========================
def main():
    setup_page()
    inject_css()

    # Replace the following line with your real dataclass instances
    ps, us, notice_mtm, expiry3, rent3, maint3, leads3 = create_demo_models()

    st.title("🏢 Property Dashboard for 4060 Preferred Place")

    t1, t2, t3 = st.tabs(["Overview", "Operations", "Resident Retention"])
    with t1:
        render_overview(ps, rent3)
    with t2:
        render_operations(us, maint3, leads3)
    with t3:
        render_retention(notice_mtm, expiry3)

if __name__ == "__main__":
    main()
