from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

df = pd.read_csv(DATA / "dice_temperature_scenarios_long.csv")

def plot_metric(metric, title, ylabel, filename, yref=None):
    x = df[df["metric"] == metric]
    fig, ax = plt.subplots(figsize=(11, 6))
    for scenario in sorted(x["temperature_limit_C"].unique()):
        s = x[x["temperature_limit_C"] == scenario]
        ax.plot(s["year"], s["value"], linewidth=2, label=f"{scenario:.1f} °C")
    if yref is not None:
        ax.axhline(yref, linestyle=":", linewidth=1.5)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    ax.legend(ncol=4, frameon=False)
    fig.tight_layout()
    fig.savefig(FIG / filename, dpi=220, bbox_inches="tight")
    plt.close(fig)

plot_metric("atmospheric_temperature_increase_C",
            "Atmospheric Temperature Response under DICE 2023 Temperature Limits",
            "Temperature increase (°C)", "01_atmospheric_temperature.png")

plot_metric("emissions_control_rate",
            "Emissions Control Rate by Temperature Limit",
            "Emissions control rate", "02_emissions_control_rate.png", 1.0)

plot_metric("total_CO2_emissions_GtCO2_per_year",
            "Total CO₂ Emissions Pathways",
            "CO₂ emissions (GtCO₂ per year)", "03_total_co2_emissions.png", 0.0)

plot_metric("social_cost_of_carbon_usd_per_tCO2",
            "Social Cost of Carbon across Temperature Limit Scenarios",
            "SCC (USD per tCO₂)", "04_social_cost_of_carbon.png")

plot_metric("carbon_price_usd_per_tCO2",
            "Carbon Price Pathways",
            "Carbon price (USD per tCO₂)", "05_carbon_price.png")

plot_metric("atmospheric_concentration_ppm",
            "Atmospheric Carbon Concentration",
            "Atmospheric concentration (ppm)", "06_atmospheric_concentration.png")

plot_metric("gross_output", "Gross Economic Output",
            "Model output", "07_gross_output.png")

plot_metric("consumption_per_capita_2019USD", "Consumption per Capita",
            "Consumption per capita (2019 USD)", "08_consumption_per_capita.png")

plot_metric("gross_investment", "Gross Investment",
            "Model investment", "09_gross_investment.png")

print("Figures regenerated in:", FIG)


# Scenario workflow
fig, ax = plt.subplots(figsize=(12, 6.5))
ax.axis("off")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

stages = [
    (0.12, 0.70, "Temperature\nconstraint"),
    (0.38, 0.70, "DICE 2023\noptimization"),
    (0.64, 0.70, "Climate\nresponse"),
    (0.88, 0.70, "Economic\nresponse"),
]

for x, y, label in stages:
    ax.text(
        x, y, label,
        ha="center", va="center",
        fontsize=14,
        bbox=dict(boxstyle="round,pad=0.65", fc="white", ec="black", lw=1.5)
    )

for x1, x2 in [(0.20, 0.29), (0.46, 0.55), (0.72, 0.79)]:
    ax.annotate(
        "", xy=(x2, 0.70), xytext=(x1, 0.70),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

ax.text(
    0.64, 0.31,
    "Temperature\nCO₂ emissions\nAtmospheric concentration\nEmissions control rate",
    ha="center", va="center", fontsize=11,
    bbox=dict(boxstyle="round,pad=0.55", fc="white", ec="0.55")
)

ax.text(
    0.88, 0.31,
    "Social cost of carbon\nCarbon price\nGross output\nConsumption\nInvestment",
    ha="center", va="center", fontsize=11,
    bbox=dict(boxstyle="round,pad=0.55", fc="white", ec="0.55")
)

ax.annotate("", xy=(0.64, 0.43), xytext=(0.64, 0.60),
            arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.88, 0.43), xytext=(0.88, 0.60),
            arrowprops=dict(arrowstyle="->", lw=1.5))

ax.set_title("DICE 2023 Temperature Limit Scenario Analysis Workflow", fontsize=18, pad=22)
fig.tight_layout()
fig.savefig(FIG / "00_scenario_workflow.png", dpi=240, bbox_inches="tight")
plt.close(fig)
