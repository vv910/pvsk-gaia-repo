"""
Section 3 (Results) formalization covering:
- Hysteresis behavior in planar vs bilayer cells
- Thickness optimization of mp-TiO2
- Best cell performance
- IPCE characterization
- Reproducibility histogram
"""

from gaia.lang import (
    claim,
    setting,
)

# --- Cell without mp-TiO2: large hysteresis ---

no_mp_tio2_forward_scan = claim(
    "For a flat cell without mp-TiO2 (FTO/bl-TiO2/350-nm-thick perovskite layer/PTAA/Au), the forward scan (short circuit to open circuit) at 40 ms delay yielded Jsc = 19.2 mA cm^-2, Voc = 1.07 V, FF = 0.44, and PCE = 9.1% under AM 1.5 G illumination [@Jeon2014].",
    title="Flat cell without mp-TiO2: forward scan performance"
)

no_mp_tio2_reverse_scan = claim(
    "For a flat cell without mp-TiO2 (FTO/bl-TiO2/350-nm-thick perovskite layer/PTAA/Au), the reverse scan (open circuit to short circuit) at 40 ms delay yielded Jsc = 19.2 mA cm^-2, Voc = 1.09 V, FF = 0.69, and PCE = 14.4% under AM 1.5 G illumination [@Jeon2014].",
    title="Flat cell without mp-TiO2: reverse scan performance"
)

large_hysteresis_without_mp = claim(
    "A flat cell without mp-TiO2 exhibits large hysteresis and distortion between forward and reverse scans, with a discrepancy of 9.1% in overall efficiency (reverse scan PCE = 14.4% vs forward scan PCE = 9.1%) [@Jeon2014].",
    title="Large hysteresis in cells without mp-TiO2"
)

delay_time_effect = claim(
    "For cells without mp-TiO2, as the delay time increased from 10 to 300 ms, efficiency decreased from 11.0% to 7.0% in the forward scan and from 16.5% to 8.5% in the reverse scan; efficiencies did not approach similar values even with long scan time [@Jeon2014].",
    title="Efficiency declines with longer delay time without mp-TiO2"
)

# --- Bilayer cell: no hysteresis ---

bilayer_forward_scan = claim(
    "For a bilayered cell (FTO/bl-TiO2/200-nm-thick mp-TiO2-perovskite nanocomposite layer/perovskite upper layer/PTAA/Au), the forward scan yielded Jsc = 20.1 mA cm^-2, Voc = 1.08 V, FF = 0.73, and PCE = 15.8% under AM 1.5 G illumination [@Jeon2014].",
    title="Bilayer cell: forward scan performance"
)

bilayer_reverse_scan = claim(
    "For a bilayered cell (FTO/bl-TiO2/200-nm-thick mp-TiO2-perovskite nanocomposite layer/perovskite upper layer/PTAA/Au), the reverse scan yielded Jsc = 19.9 mA cm^-2, Voc = 1.06 V, FF = 0.75, and PCE = 15.9% under AM 1.5 G illumination [@Jeon2014].",
    title="Bilayer cell: reverse scan performance"
)

negligible_hysteresis_bilayer = claim(
    "The J-V curves of the forward and reverse scans of the bilayered cell are well coincident; efficiency and average efficiency from both scan directions are symmetrical and identical regardless of scanning direction [@Jeon2014].",
    title="Bilayer cell exhibits negligible hysteresis"
)

average_bilayer_efficiency = claim(
    "The overall efficiencies for bilayer cell from both scan directions under the standard method (40 ms delay) are 15.8% and 15.9%, with an average of 15.85% [@Jeon2014].",
    title="Bilayer cell average efficiency 15.85%"
)

# --- Thickness optimization ---

thickness_vs_efficiency = claim(
    "As the mp-TiO2 layer thickness increases to approximately 200 nm, the difference in efficiency between forward and reverse scans reaches a minimum; the reverse scan efficiency does not vary greatly with mp-TiO2 thickness, whereas the forward scan shows pronounced variation [@Jeon2014].",
    title="Optimal mp-TiO2 thickness minimizes hysteresis"
)

hysteresis_origin = claim(
    "The large diffusion capacitance in perovskite cells operating under reverse or forward biases causes charge redistribution delay, leading to underestimation in forward scan and overestimation in reverse scan; slow charge collection via the perovskite material itself must be improved by an optimally thick mp-TiO2 layer for efficient charge collection [@Jeon2014].",
    title="Hysteresis originates from large diffusion capacitance"
)

# --- Best cell performance ---

best_cell_average = claim(
    "The best performing cell (with 200-nm-thick mp-TiO2) showed average values from J-V curves: Jsc = 19.58 mA cm^-2, Voc = 1.105 V, FF = 76.2%, corresponding to a PCE of 16.5% under standard AM 1.5 G conditions [@Jeon2014].",
    title="Best cell average performance is 16.5% PCE"
)

ipce_plateau = claim(
    "The best cell showed a very broad IPCE plateau of over 80% between 420 and 700 nm wavelength range [@Jeon2014].",
    title="IPCE plateau exceeds 80% between 420-700 nm"
)

jsc_from_ipce = claim(
    "The Jsc value integrated from the IPCE spectrum agreed well with that measured by J-V curve for the best cell [@Jeon2014].",
    title="IPCE-integrated Jsc matches J-V measurement"
)

# --- Reproducibility ---

reproducibility_histogram = claim(
    "A histogram of average PCEs for 108 independently fabricated devices shows that approximately 80% of the cells made using the solvent-engineering process exhibited overall efficiency exceeding 15% under 1 sun conditions [@Jeon2014].",
    title="80% of 108 devices exceed 15% PCE"
)

certified_efficiency_162 = claim(
    "A device fabricated by solvent engineering was certified by a standardized method in a photovoltaics calibration laboratory, confirming a PCE of 16.2% under AM 1.5 G full sun conditions [@Jeon2014].",
    title="Certified PCE of 16.2% under AM 1.5 G full sun"
)

# --- Key finding: balanced thickness ---

balanced_thickness_concept = claim(
    "A balanced ratio between the perovskite-infiltrated mp-TiO2 layer and the thin upper perovskite layer is critical for achieving coincident reverse and forward scans and high efficiency [@Jeon2014].",
    title="Balanced mp-TiO2/perovskite layer ratio is critical"
)