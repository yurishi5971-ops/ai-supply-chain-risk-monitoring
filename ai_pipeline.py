# ============================================
# AI-Assisted Warehouse Risk Monitoring
# Conceptual Analytics Pipeline
# ============================================

import pandas as pd

# ============================================
# STEP 1 — Load Sample KPI Data
# ============================================

df = pd.read_csv("../sample_data/sample_kpi.csv")

print("KPI data loaded successfully")

# ============================================
# STEP 2 — Risk Detection Logic
# ============================================

alerts = []

warehouse_util = float(
    df.loc[
        df["KPI"] == "Warehouse Utilization",
        "Value"
    ].values[0]
)

aging_inventory = float(
    df.loc[
        df["KPI"] == "Aging Inventory %",
        "Value"
    ].values[0]
)

shipment_delay = float(
    df.loc[
        df["KPI"] == "Outbound Shipment Delay %",
        "Value"
    ].values[0]
)

wip_buildup = float(
    df.loc[
        df["KPI"] == "WIP Inventory Days",
        "Value"
    ].values[0]
)

# ============================================
# STEP 3 — Business Rules
# ============================================

if warehouse_util > 90:
    alerts.append(
        "Warehouse utilization exceeds safe threshold."
    )

if aging_inventory > 15:
    alerts.append(
        "Inventory aging risk is increasing."
    )

if shipment_delay > 10:
    alerts.append(
        "Outbound shipment delays detected."
    )

if wip_buildup > 10:
    alerts.append(
        "Semi-finished goods accumulation detected."
    )

# ============================================
# STEP 4 — Generate AI-style Insight
# ============================================

summary = f"""
AI Operational Insight Summary

Warehouse utilization is currently at {warehouse_util}%,
indicating elevated warehouse capacity risk.

Inventory aging has reached {aging_inventory}%,
while outbound shipment delay is {shipment_delay}%.

These operational signals suggest increasing
warehouse overflow risk that could potentially
impact production continuity.

Key operational concerns:
{alerts}

Recommended actions:
- Review inbound delivery scheduling
- Reduce slow-moving inventory
- Improve outbound shipment coordination
- Monitor WIP production pacing
"""

# ============================================
# STEP 5 — Output Result
# ============================================

print(summary)

# ============================================
# STEP 6 — Save Report
# ============================================

with open(
    "ai_operational_insight.txt",
    "w"
) as f:
    f.write(summary)

print("AI operational insight report saved.")
