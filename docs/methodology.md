# Methodology Notes

## Scenario design

The source workbook evaluates seven upper atmospheric temperature constraints:

1.5 °C  
2.0 °C  
2.5 °C  
3.0 °C  
3.5 °C  
4.0 °C  
4.5 °C

The model horizon runs from 2020 to 2195 in five year steps.

## Variables visualized

Climate variables

Atmospheric temperature increase  
Atmospheric carbon concentration  
Emissions control rate  
Total CO₂ emissions

Economic variables

Social cost of carbon  
Carbon price  
Gross output  
Consumption per capita  
Gross investment

## Model equations highlighted in the source report

Damage function

Ω(t) = ψ₁ T_AT(t) + ψ₂ [T_AT(t)]²

with the source report using ψ₁ = 0 and ψ₂ = 0.003467.

Emissions equation

E_CO2e(t) = E_CO2e_base(t) [1 − μ(t)]

where μ(t) is the emissions control rate.

## Interpretation caution

This repository reproduces and visualizes the results contained in the supplied academic workbook. It does not claim that a particular temperature target is an externally validated policy optimum.

The source term paper interpreted 3 to 3.5 °C as a pragmatic tradeoff in its classroom exercise. That conclusion is presented as a result of the submitted model analysis, not as a general climate policy recommendation.
