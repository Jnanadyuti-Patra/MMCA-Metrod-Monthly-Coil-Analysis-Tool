# MMCA (Metrod-Monthly-Coil-Analysis-Tool)
Metrod Monthly Coil Analysis (MMCA) is a data tracking tool that I developed during my internship at Metrod Holdings Berhad in Malaysia. It monitors 48+ process and product parameters in CCR copper rod fabrication to identify and quantify causes behind grade fluctuations, aiding in process optimization and consistency.
# 🛠️ Why MMCA Was Needed
In Continuous Casting and Rolling (CCR) operations at copper fabrication facilities like Metrod Holdings Berhad (MHB), copper rod grade changes—both upgrades and downgrades—can significantly affect:
- Product quality
- Customer satisfaction
- Operational costs
- Scrap and rework volume

Despite rigorous standard operating procedures (SOPs), process variability across shifts, equipment aging, raw material inconsistencies, and human error can lead to undesired grade shifts. Traditionally, these are detected late—either during QC at the end of the line or post-delivery complaints—making root cause analysis reactive and unreliable.

There was no systematic, data-driven tool that tracked all relevant process and product parameters in tandem to pinpoint what changed and when, making grade shift analysis largely manual and prone to error.
# 📊 What MMCA Does (Detailed Tool Explanation)
MMCA—developed in Excel with support for advanced filtering, calculations—systematically tracks 48+ parameters across each CCR copper rod coil for a selected time frame (typically monthly).
- **Input Structure:**
   - **Monthly coil-wise raw data from:**
      - CCR plant logs
      - Quality control lab reports
- **Parameters tracked include:**
   - **Process parameters:** _SV Temp, HF Temp, Tundish Temp, SCU1_CO_Red, SCU1_CO_Blue, SCU1_CO_Orange, SCU1_CO_Yellow, SCU1_CO_White, SCU1_CO_Green, SCU1_CO_UL, SCU1_CO_SV, SCU1_CO_HF, SCU1_CO_LL, SCU1_CO_TUN, SCU2_CO_Red, SCU2_CO_Blue, SCU2_CO_Orange, 
     SCU2_CO_Yellow, SCU2_CO_White, SCU2_CO_Green, SCU2_CO_UL, SCU2_CO_SV, SCU2_CO_HF, SCU2_CO_LL, SCU2_CO_TUN, WEIGHT_HF, WHEEL_TEMP, ROD_SPEED, BAR_ENTRY_TEMP, BAR_RM_ENTRY_TEMP, SOLUBLE_OIL_TEMP, SOLUBLE_OIL_CONC, SOLUBLE_IPA_CONC,
     NAPS_FLOW_ZONE1, NAPS_CONC, NAPS_IPA_CONC, WAX_CONC, DA_WHEEL_BOTTOM_FLOW, O2_WHEEL_BOTTOM_FLOW, DA_WHEEL_SIDE_FLOW, O2_WHEEL_SIDE_FLOW, DA_BAND_FLOW, O2_BAND_FLOW, NIP_NOZZLE_FLOW, BAND1_FLOW, BAND2_FLOW, BAND3_FLOW, WHEEL1_FLOW, 
     WHEEL2_FLOW, WHEEL3_FLOW, WHEEL_MACHINE_SIDE_FLOW, WHEEL_OPERATOR_SIDE_FLOW, AFTER_COOLER1_FLOW, AFTER_COOLER2_FLOW, AFTER_COOLER3_FLOW, SRIPPER_SHOE_FLOW_
   - **Product parameters:** _Grade, 15 X 15 Twist Test (Index), Oxygen (ppm), 25 RTF Twist Test (Number), Oxide Content (Å), Aluminium (Al), Antimony (Sb), Arsenic (As), Bismuth (Bi), Cadmium (Cd), Iron (Fe) (ppm), Lead (Pb), Nickel (Ni), Phosphorus (P), Selenium
     (Se), Sulphur (S), Tellurium (Te), Tin (Sn), Zinc (Zn), Large Defect in Defectomat, Medium Defect in Defectomat, Small Defect in Defectomat, Rolling mill roll - 1, Rolling mill roll - 2, Rolling mill roll - 3, Rolling mill roll - 4, Rolling mill roll - 
     5, Rolling mill roll - 6, Rolling mill roll - 7, Rolling mill roll - 8, Rolling mill roll - 9, Rolling mill roll - 10, Chromium (Cr), Manganese (Mn), Silicon (Si), Cobalt (Co) (ppm), Silver (Ag)_
# 📈 Results
The Metrod Monthly Coil Analysis (MMCA) tool generates two key outputs based on the data provided by the user:
- **Process Parameter Summary:** _MMCA calculates the average values of all tracked process parameters (e.g., temperatures, flow rates, speeds, concentrations) over a selected date or coil range. This enables the engineer to observe overall trends, detect anomalies, and compare operational behavior between high-grade and downgraded coils._
- **Product Parameter Root Cause Mapping:** _The tool identifies which specific product parameters (e.g., Oxygen ppm, Twist Test Index, elemental impurities, surface defects) have directly contributed to how many exact grade changes across the dataset. This correlation enables precise, data-driven root cause identification._

By examining these results together, the engineer gains a holistic understanding of the system, allowing them to determine whether grade drops were caused by:
- Raw material inconsistency (e.g., elevated impurity levels)
- Equipment or rolling mill performance issues
- Thermal or pressure variations in casting/cooling zones

This insight empowers engineers to take targeted corrective actions, reducing grade variability, improving process stability, and enhancing product quality over time.
