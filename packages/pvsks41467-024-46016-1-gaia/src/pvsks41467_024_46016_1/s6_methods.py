"""Methods section: Materials and fabrication procedures."""

from gaia.lang import (
    claim,
    setting,
)

# Materials settings
materials_setting = setting(
    "Materials used include: lead(II) iodide (PbI₂, 99.9985%), tin(IV) oxide (SnO₂, 15 wt% in H₂O colloidal dispersion), methylammonium iodide (MAI, 99.99%), formamidinium iodide (FAI, 99.99%), n-hexyl trimethyl ammonium bromide (HTAB) from Greatcell Solar Materials; PPDT2FBT, P3HT (Lisicon SP001), Spiro-MeOTAD from various suppliers; silver paste (PV416) from DuPont; and various solvents and chemicals from Sigma-Aldrich [@Weerasinghe2024].",
    title="Materials list for R2R PeSC fabrication",
)

tce_specification = setting(
    "Commercially available TCE substrates with a sheet resistance of 8 Ω sq⁻¹ (OPV8) were sourced from MekoPrint [@Weerasinghe2024].",
    title="TCE substrate specification",
)

# Ink preparation
ec_binder = setting(
    "Ethyl cellulose (EC, Sigma-Aldrich, viscosity 4 cP, 5% in toluene/ethanol) was used as the binder for carbon ink formulation [@Weerasinghe2024].",
    title="Ethyl cellulose binder for carbon ink",
)

carbon_pigment = setting(
    "A 1:1 mixture of carbon black (Vulcan XC72, Cabot) and graphene nanoplatelet powder (CamGraph G3, Cambridge Nanosystems) was used as the conductive carbon pigment [@Weerasinghe2024].",
    title="Carbon pigment mixture for conductive ink",
)

pgmesa_solver = setting(
    "Propylene glycol methyl ether acetate (PGMEA) was used as the solvent for the carbon ink [@Weerasinghe2024].",
    title="PGMEA solvent for carbon ink",
)

two_stage_ink_prep = claim(
    "The carbon ink preparation was separated into two stages: (1) a high-viscosity ink produced by mixing 40 g EC in 330 g PGMEA, then adding 130 g of conductive carbon pigment and processing through a three-roll mill; (2) dilution of the high-viscosity ink with additional EC/PGMEA solution to achieve SD-coating viscosity [@Weerasinghe2024].",
    title="Two-stage carbon ink preparation process",
)

# Perovskite solution preparation
pbi2_fai_solution = setting(
    "The PbI₂:FAI solution was prepared by dissolving 1.1 mmol (507 mg) PbI₂ and 0.45 mol% (0.5 mmol, 0.85 mg) FAI per 1 ml of anhydrous N,N-dimethylformamide in a nitrogen-filled glove box, and stirred at 70°C for approximately 1 h [@Weerasinghe2024].",
    title="PbI₂:FAI perovskite precursor solution",
)

mai_solution = setting(
    "The MAI solution for the second step of the deposition was made by stirring 40 mg of MAI per 1 ml of anhydrous 2-propanol for 10 min at ambient temperature [@Weerasinghe2024].",
    title="MAI solution for second-step deposition",
)

htab_solution = setting(
    "1.0 mM HTAB solution was prepared in a mixed solvent (chlorobenzene:isopropanol τ = 93·1 v/v%) [@Weerasinghe2024].",
    title="HTAB solution preparation",
)

htm_solutions = setting(
    "The PPDT2FBT HTM solution was prepared by dissolving 10 mg of PPDT2FBT per 1 ml of dichlorobenzene. The P3HT solution was prepared by dissolving 5 mg of P3HT in 1 mL of dichlorobenzene, with polymers dissolved by stirring at 70°C for more than 1 h [@Weerasinghe2024].",
    title="HTM solutions preparation",
)

spiro_meotad_solution = setting(
    "The Spiro-OMeTAD solution was prepared by mixing 6.0×10⁻⁵ mol Spiro-OMeTAD (73 mg), 2.0×10⁻⁴ mol t-BP (28.8 μL), 2.0×10⁻⁴ mol LiNTf₂ (17 μL of 520 mg mL⁻¹ solution in CH₃CN), and 1.6×10⁻⁶ mol FK209 (8 μL of 300 mg mL⁻¹ solution in CH₃CN) in 1 mL chlorobenzene [@Weerasinghe2024].",
    title="Spiro-OMeTAD solution for reference devices",
)

# Fabrication methods
rg_coating_etl = setting(
    "The SnO₂ ETL layer was coated using RG coating method at 4 rpm RG roll (200 R roll) speed, 0.25 m min⁻¹ line speed and 13 mm coating width on flexible TCE substrate under ambient conditions [@Weerasinghe2024].",
    title="RG coating of SnO₂ ETL",
)

ir_treatment = setting(
    "The PET/TCE/SnO₂ film underwent R2R IR treatment (2–3 W cm⁻²) for about 5 min using an industrial R2R screen printer (Orthotec SRN3030), followed by hot plate treatment at greater than 135°C for about 30 s with hot air blowing at 120°C for about 30 s [@Weerasinghe2024].",
    title="IR treatment of SnO₂ layer",
)

perovskite_sd_coating = setting(
    "The PbI₂:FAI solution was SD coated at 20 μL min⁻¹ flow rate, 0.3 m min⁻¹ web speed, 13 mm coating width. The wet film was subjected to nitrogen flow using a 10 cm-wide air blade at the edge of supporting roller (about 10 cm behind coating head and 1–2 cm above substrate) with N₂ flow rate of 50–100 L min⁻¹. The MAI solution was then SD coated at 60 μL min⁻¹, followed by solvent evaporation with gentle air blowing and hot plate at 135°C for about 10 s [@Weerasinghe2024].",
    title="SD coating of perovskite layers",
)

htab_p3ht_deposition = setting(
    "The HTAB and P3HT solutions were deposited sequentially via SD coating at 0.3 m min⁻¹ line speed: HTAB layer at 15 μL min⁻¹ flow rate, 7 mm coating width, followed by annealing on curved hotplate at 100°C for 30 s; then P3HT layer at 10 μL min⁻¹ flow rate, 6 mm coating width, with the SD head immediately above the second curved hotplate at 45±5°C [@Weerasinghe2024].",
    title="HTAB and P3HT sequential SD coating",
)

carbon_electrode_sd = setting(
    "The carbon electrode was SD coated onto the P3HT layer using the PGMEA-based carbon ink by placing the SD head immediately above the curved hotplate at 70°C (120 μL min⁻¹ flow rate, 5 mm coating width) to remove solvents, before an additional annealing step on the second curved hotplate at 130°C [@Weerasinghe2024].",
    title="Carbon electrode SD coating",
)

silver_grid_printing = setting(
    "Silver grid was screen printed using a semi-auto screen printer (Keywell KY-600FH) with 180 mesh screen onto the top carbon electrode and annealed at 130°C for 30 s on a hot plate [@Weerasinghe2024].",
    title="Silver grid screen printing",
)

# Module fabrication
stripe_pattern = setting(
    "All R2R-processed PeSC modules comprising five series-connected strip cells were fabricated on a stripe-patterned (13 mm stripes with 2 mm gap between stripes) commercial TCE. The module has the configuration: PET/TCE/SnO₂/FA₀.₄₅MA₀.₅₅PbI₃/HTAB/P3HT/Carbon/Ag [@Weerasinghe2024].",
    title="Module stripe pattern configuration",
)

five_stripe_flow_rates = claim(
    "For five-stripe module coating, flow rates were: PbI₂:FAI at 100, MAI at 300, HTAB at 140, P3HT at 92, and carbon inks at 600 μL min⁻¹. The P3HT layer was deposited on a custom-built curved hot plate fitted with a heating tape at 45±5°C [@Weerasinghe2024].",
    title="Module flow rates for five-stripe coating",
)

# Characterisation methods
jv_measurement = setting(
    "Manual J-V measurements were undertaken using a solar simulator (Newport Oriel) in air without encapsulation, calibrated to 1-sun (1000 W m⁻²) AM 1.5 G illumination using a certified Si reference cell with KG-1 filter (spectral mismatch factor with carbon-based cells: 0.92) and a Keithley 2400 source metre. Cells used a shadow mask defining 0.08 cm² active area; modules were tested without a shadow mask [@Weerasinghe2024].",
    title="J-V measurement conditions",
)

scan_parameters = setting(
    "J-V measurements were carried out in forward (increasing forward bias) and reverse (decreasing forward bias) scan directions over the voltage range from -0.2 V to 1.2 V with 20 mV step (250 mV s⁻¹) for cells, and -0.2 V to 5 V with 200 mV step (1 V s⁻¹) for modules [@Weerasinghe2024].",
    title="J-V scan parameters",
)

__all__ = [
    "materials_setting",
    "tce_specification",
    "ec_binder",
    "carbon_pigment",
    "pgmesa_solver",
    "two_stage_ink_prep",
    "pbi2_fai_solution",
    "mai_solution",
    "htab_solution",
    "htm_solutions",
    "spiro_meotad_solution",
    "rg_coating_etl",
    "ir_treatment",
    "perovskite_sd_coating",
    "htab_p3ht_deposition",
    "carbon_electrode_sd",
    "silver_grid_printing",
    "stripe_pattern",
    "five_stripe_flow_rates",
    "jv_measurement",
    "scan_parameters",
]