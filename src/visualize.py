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
