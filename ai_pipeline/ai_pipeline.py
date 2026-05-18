# ============================================
# AI-Assisted Warehouse Risk Monitoring
# Conceptual Analytics Pipeline
# ============================================

import pandas as pd
from openai import OpenAI

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
# STEP 4 — Dynamic Prompt Engineering
# ============================================

prompt = f"""
You are a senior supply chain analyst.

Analyze the following warehouse operational KPIs.

KPI Summary:
- Warehouse Utilization: {warehouse_util}%
- Aging Inventory: {aging_inventory}%
- Outbound Shipment Delay: {shipment_delay}%
- WIP Inventory Days: {wip_buildup}

Operational Alerts:
{alerts}

Please provide:

1. Executive Summary
2. Root Cause Analysis
3. Operational Risks
4. Recommended Actions

Keep the response concise and professional.
"""

print("Prompt generated successfully")

# ============================================
# STEP 5 — OpenAI API Call
# ============================================

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)

ai_insight = response.choices[0].message.content

# ============================================
# STEP 6 — Output AI Insight
# ============================================

print("\n")
print("===================================")
print(" AI OPERATIONAL INSIGHT REPORT ")
print("===================================")

print(ai_insight)

# ============================================
# STEP 7 — Save AI Report
# ============================================

with open(
    "ai_operational_insight.txt",
    "w"
) as f:
    f.write(ai_insight)

print("\nAI operational insight report saved.")
