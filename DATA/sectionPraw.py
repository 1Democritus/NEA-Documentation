# ICD-10 P-Code Dataset (P00-P96)
# This list contains data rows for AI training.
# Each row follows the structure:
# [Geography, [Transmission_1, Transmission_2, Transmission_3], Condition_Type, [Symptom_1, ..., Symptom_6], Disease_Name, ICD_Code]
#
# Note: "Disease Type" is interpreted as "Condition Type" as P-codes cover perinatal conditions,
# which are often not infectious (e.g., "Maternal", "Birth Injury", "Metabolic").

icd_p_code_data = [
    # P00-P04: Fetus and newborn affected by maternal factors
    ["Worldwide", ["maternal", "placental", "complication"], "Maternal", ["low birth weight", "premature labor", "fetal distress", "small for gestational age", "respiratory distress", "hypoxia"], "Fetus and newborn affected by maternal hypertensive disorders", "P00"],
    ["Worldwide", ["maternal", "placental", "complication"], "Maternal", ["oligohydramnios", "fetal growth restriction", "renal anomalies", "urinary tract abnormalities", "fetal distress", "low birth weight"], "Fetus and newborn affected by maternal renal and urinary tract diseases", "P01"],
    ["Worldwide", ["maternal", "placental", "vertical"], "Maternal", ["fever", "congenital infection", "low birth weight", "hepatosplenomegaly", "jaundice", "rash"], "Fetus and newborn affected by maternal infectious and parasitic diseases", "P02"],
    ["Worldwide", ["maternal", "placental", "complication"], "Maternal", ["fetal growth restriction", "congenital anomalies", "fetal distress", "metabolic disturbance", "endocrine disorder", "autoimmune effects"], "Fetus and newborn affected by other maternal diseases", "P03"],
    ["Worldwide", ["maternal", "placental", "teratogenic"], "Maternal", ["withdrawal symptoms", "low birth weight", "congenital anomalies", "neurobehavioral issues", "SGA", "respiratory depression"], "Fetus and newborn affected by maternal use of drugs and noxious substances", "P04"],

    # P05-P08: Disorders related to length of gestation and fetal growth
    ["Worldwide", ["placental insufficiency", "maternal malnutrition", "genetic"], "Developmental", ["low birth weight", "small for gestational age", "thin/wasted appearance", "hypoglycemia", "polycythemia", "hypothermia"], "Slow fetal growth and fetal malnutrition", "P05"],
    ["Worldwide", ["preterm labor", "maternal factors", "unknown"], "Developmental", ["low birth weight", "immature organs", "respiratory distress", "hypothermia", "feeding difficulties", "apnea"], "Disorders related to short gestation and low birth weight, NEC", "P07"],
    ["Worldwide", ["maternal diabetes", "genetic", "maternal obesity"], "Developmental", ["high birth weight", "macrosomia", "birth injury", "hypoglycemia", "respiratory distress", "polycythemia"], "Disorders related to long gestation and high birth weight", "P08"],

    # P10-P15: Birth trauma
    ["Worldwide", ["birth trauma", "difficult delivery", "instrumental delivery"], "Birth Injury", ["seizures", "apnea", "altered consciousness", "bulging fontanelle", "bradycardia", "hypotonia"], "Intracranial laceration and hemorrhage due to birth injury", "P10"],
    ["Worldwide", ["birth trauma", "fetal malposition", "difficult delivery"], "Birth Injury", ["cranial nerve palsy", "seizures", "visual impairment", "hearing loss", "hemiparesis", "developmental delay"], "Other birth injuries to central nervous system", "P11"],
    ["Worldwide", ["birth trauma", "pressure", "forceps delivery"], "Birth Injury", ["scalp swelling", "cephalohematoma", "bruising", "subgaleal hemorrhage", "caput succedaneum", "calcification (late)"], "Birth injury to scalp", "P12"],
    ["Worldwide", ["birth trauma", "shoulder dystocia", "difficult delivery"], "Birth Injury", ["fractured clavicle", "fractured femur", "fractured humerus", "limited movement", "crepitus", "pain on movement"], "Birth injury to skeleton", "P13"],
    ["Worldwide", ["birth trauma", "shoulder dystocia", "breech delivery"], "Birth Injury", ["brachial plexus palsy", "facial nerve palsy", "phrenic nerve paralysis", "vocal cord paralysis", "asymmetric movement", "hypotonia"], "Birth injury to peripheral nervous system", "P14"],
    ["Worldwide", ["birth trauma", "difficult delivery", "breech delivery"], "Birth Injury", ["liver rupture", "splenic rupture", "adrenal hemorrhage", "abdominal distension", "pallor", "shock"], "Other birth injuries", "P15"],

    # P20-P29: Respiratory and cardiovascular disorders
    ["Worldwide", ["placental insufficiency", "cord compression", "maternal hypotension"], "Respiratory", ["hypoxia", "low Apgar scores", "acidosis", "meconium staining", "fetal bradycardia", "poor perfusion"], "Intrauterine hypoxia", "P20"],
    ["Worldwide", ["intrauterine hypoxia", "difficult delivery", "maternal sedation"], "Respiratory", ["cyanosis", "apnea", "bradycardia", "hypotonia", "poor respiratory effort", "low Apgar scores"], "Birth asphyxia", "P21"],
    ["Worldwide", ["prematurity", "surfactant deficiency", "maternal diabetes"], "Respiratory", ["tachypnea", "nasal flaring", "grunting", "retractions", "cyanosis", "hypoxemia"], "Respiratory distress of newborn", "P22"],
    ["Worldwide", ["vertical transmission", "maternal infection", "aspiration"], "Bacterial", ["respiratory distress", "fever", "tachypnea", "lethargy", "grunting", "poor feeding"], "Congenital pneumonia", "P23"],
    ["Worldwide", ["post-term", "fetal distress", "hypoxia"], "Respiratory", ["meconium-stained fluid", "respiratory distress", "barrel chest", "cyanosis", "rales", "pneumothorax"], "Neonatal aspiration syndromes", "P24"],
    ["Worldwide", ["prematurity", "barotrauma", "aspiration"], "Respiratory", ["respiratory distress", "cyanosis", "mediastinal shift", "hypoxemia", "bradycardia", "air leak"], "Interstitial emphysema and related conditions", "P25"],
    ["Worldwide", ["prematurity", "respiratory distress", "infection"], "Respiratory", ["apnea", "bradycardia", "hypoxemia", "pallor", "sudden respiratory distress", "hypotension"], "Pulmonary hemorrhage originating in the perinatal period", "P26"],
    ["Worldwide", ["prematurity", "prolonged ventilation", "oxygen toxicity"], "Respiratory", ["chronic respiratory distress", "hypoxemia", "tachypnea", "retractions", "wheezing", "CO2 retention"], "Chronic respiratory disease originating in the perinatal period", "P27"],
    ["Worldwide", ["prematurity", "infection", "maternal drug use"], "Respiratory", ["apnea", "bradycardia", "desaturation", "cyanosis", "hypotonia", "irregular breathing"], "Other respiratory conditions originating in the perinatal period", "P28"],
    ["Worldwide", ["congenital heart defect", "birth asphyxia", "persistent fetal circulation"], "Cardiovascular", ["cyanosis", "murmur", "tachycardia", "poor feeding", "respiratory distress", "shock"], "Cardiovascular disorders originating in the perinatal period", "P29"],

    # P35-P39: Infections
    ["Worldwide", ["maternal infection", "vertical", "placental"], "Viral", ["microcephaly", "chorioretinitis", "rash", "hepatosplenomegaly", "jaundice", "hearing loss"], "Congenital viral diseases", "P35"],
    ["Worldwide", ["maternal infection", "vertical", "ascending"], "Bacterial", ["lethargy", "poor feeding", "fever", "respiratory distress", "hypotonia", "seizures"], "Bacterial sepsis of newborn", "P36"],
    ["Worldwide", ["maternal infection", "vertical", "placental"], "Parasitic", ["chorioretinitis", "hydrocephalus", "intracranial calcifications", "hepatosplenomegaly", "fever", "rash"], "Other congenital infectious and parasitic diseases", "P37"],
    ["Worldwide", ["contaminated equipment", "skin colonization", "umbilical stump"], "Bacterial", ["redness at umbilicus", "purulent discharge", "fever", "lethargy", "abdominal distension", "sepsis"], "Omphalitis of newborn", "P38"],
    ["Worldwide", ["maternal", "nosocomial", "environmental"], "Infectious", ["fever", "lethargy", "poor feeding", "skin lesions", "respiratory distress", "conjunctivitis"], "Other infections specific to the perinatal period", "P39"],

    # P50-P61: Hemorrhagic and hematological disorders
    ["Worldwide", ["placental abruption", "cord rupture", "twin-twin transfusion"], "Hematological", ["pallor", "tachycardia", "hypotension", "poor perfusion", "low hemoglobin", "shock"], "Fetal blood loss", "P50"],
    ["Worldwide", ["birth trauma", "prematurity", "vitamin K deficiency"], "Hematological", ["bleeding from cord", "GI bleeding", "oozing from puncture sites", "bruising", "cephalohematoma", "intracranial hemorrhage"], "Umbilical hemorrhage of newborn", "P51"],
    ["Worldwide", ["prematurity", "hypoxia", "birth asphyxia"], "Hematological", ["seizures", "apnea", "bulging fontanelle", "hypotonia", "drop in hematocrit", "bradycardia"], "Intracranial nontraumatic hemorrhage of fetus and newborn", "P52"],
    ["Worldwide", ["vitamin K deficiency", "maternal anticoagulants", "liver disease"], "Hematological", ["GI bleeding", "bruising", "prolonged bleeding", "intracranial hemorrhage", "hematuria", "oozing from cord"], "Hemorrhagic disease of fetus and newborn", "P53"],
    ["Worldwide", ["birth trauma", "prematurity", "sepsis"], "Hematological", ["bruising", "petechiae", "jaundice", "anemia", "organ dysfunction", "thrombocytopenia"], "Other neonatal hemorrhages", "P54"],
    ["Worldwide", ["Rh incompatibility", "ABO incompatibility", "maternal antibodies"], "Hematological", ["jaundice", "anemia", "hepatosplenomegaly", "hydrops fetalis", "positive Coombs test", "pallor"], "Hemolytic disease of fetus and newborn", "P55"],
    ["Worldwide", ["Rh/ABO incompatibility", "twin-twin transfusion", "maternal-fetal hemorrhage"], "Hematological", ["severe anemia", "jaundice", "pallor", "shock", "hepatosplenomegaly", "heart failure"], "Hydrops fetalis due to hemolytic disease", "P56"],
    ["Worldwide", ["Rh/ABO incompatibility", "prematurity", "sepsis"], "Hematological", ["severe hyperbilirubinemia", "lethargy", "hypotonia", "high-pitched cry", "opisthotonos", "seizures"], "Kernicterus", "P57"],
    ["Worldwide", ["sepsis", "prematurity", "birth trauma"], "Hematological", ["jaundice", "bruising", "cephalohematoma", "anemia", "lethargy", "poor feeding"], "Neonatal jaundice due to other excessive hemolysis", "P58"],
    ["Worldwide", ["prematurity", "breast milk", "sepsis"], "Hematological", ["jaundice", "hyperbilirubinemia", "lethargy", "poor feeding", "dark urine", "pale stools"], "Neonatal jaundice from other and unspecified causes", "P59"],
    ["Worldwide", ["sepsis", "hypoxia", "birth asphyxia"], "Hematological", ["bleeding", "thrombosis", "petechiae", "organ failure", "abnormal clotting times", "shock"], "Disseminated intravascular coagulation of fetus and newborn", "P60"],
    ["Worldwide", ["maternal diabetes", "hypoxia", "twin-twin transfusion"], "Hematological", ["plethora", "ruddy skin", "respiratory distress", "hypoglycemia", "seizures", "jaundice"], "Other perinatal hematological disorders", "P61"],

    # P70-P74: Transitory endocrine and metabolic disorders
    ["Worldwide", ["maternal diabetes", "macrosomia", "prematurity"], "Metabolic", ["hypoglycemia", "jitteriness", "seizures", "lethargy", "poor feeding", "apnea"], "Transitory disorders of carbohydrate metabolism", "P70"],
    ["Worldwide", ["prematurity", "birth asphyxia", "maternal hypoparathyroidism"], "Metabolic", ["hypocalcemia", "hypomagnesemia", "jitteriness", "seizures", "apnea", "cardiac arrhythmia"], "Transitory neonatal disorders of calcium and magnesium metabolism", "P71"],
    ["Worldwide", ["prematurity", "birth asphyxia", "sepsis"], "Metabolic", ["thyroid dysfunction", "lethargy", "hypotonia", "poor feeding", "jaundice", "constipation"], "Other transitory neonatal endocrine disorders", "P72"],
    ["Worldwide", ["prematurity", "maternal diet", "genetic"], "Metabolic", ["lethargy", "poor feeding", "vomiting", "seizures", "abnormal odor", "metabolic acidosis"], "Other transitory neonatal electrolyte and metabolic disturbances", "P74"],

    # P75-P78: Digestive system disorders
    ["Worldwide", ["fetal distress", "post-term", "aspiration"], "Digestive", ["meconium-stained ileum", "abdominal distension", "vomiting", "failure to pass meconium", "bowel obstruction", "perforation"], "Meconium ileus", "P75"],
    ["Worldwide", ["prematurity", "hypoxia", "infection"], "Digestive", ["abdominal distension", "bloody stools", "vomiting", "feeding intolerance", "apnea", "lethargy"], "Necrotizing enterocolitis of fetus and newborn", "P77"],
    ["Worldwide", ["prematurity", "sepsis", "hypoxia"], "Digestive", ["vomiting", "feeding intolerance", "jaundice", "abdominal distension", "diarrhea", "dehydration"], "Other perinatal digestive system disorders", "P78"],

    # P80-P83: Conditions involving the integument and temperature
    ["Worldwide", ["prematurity", "low birth weight", "sepsis"], "Systemic", ["cold stress", "low body temperature", "pallor", "bradycardia", "apnea", "lethargy"], "Hypothermia of newborn", "P80"],
    ["Worldwide", ["maternal fever", "infection", "dehydration"], "Systemic", ["high body temperature", "tachycardia", "flushed skin", "irritability", "poor feeding", "seizures"], "Other disturbances of temperature regulation of newborn", "P81"],
    ["Worldwide", ["birth trauma", "infection", "genetic"], "Integument", ["rash", "blisters", "bruising", "edema", "skin peeling", "birthmarks"], "Other conditions of integument specific to fetus and newborn", "P83"],

    # P90-P96: Other disorders
    ["Worldwide", ["hypoxia", "metabolic disturbance", "infection"], "Neurological", ["seizures", "jitteriness", "abnormal cry", "irritability", "lethargy", "apnea"], "Convulsions of newborn", "P90"],
    ["Worldwide", ["hypoxia", "infection", "metabolic"], "Neurological", ["lethargy", "hypotonia", "poor feeding", "abnormal reflexes", "irritability", "coma"], "Other disturbances of cerebral status of newborn", "P91"],
    ["Worldwide", ["prematurity", "neurological issues", "oral aversion"], "Systemic", ["poor suck", "inability to feed", "weight loss", "dehydration", "aspiration", "fatigue during feeding"], "Feeding problems of newborn", "P92"],
    ["Worldwide", ["maternal drug use", "withdrawal", "iatrogenic"], "Systemic", ["high-pitched cry", "irritability", "tremors", "vomiting", "fever", "seizures"], "Reactions and intoxications due to drugs administered to fetus and newborn", "P93"],
    ["Worldwide", ["prematurity", "maternal drug use", "unknown"], "Neurological", ["tremors", "hypertonia", "irritability", "poor sleep", "feeding difficulty", "startles"], "Disorders of muscle tone of newborn", "P94"],
    ["Worldwide", ["unknown", "congenital"], "Systemic", ["fetal death", "maceration", "no signs of life", "stillbirth", "unknown cause", "intrauterine death"], "Fetal death of unspecified cause", "P95"],
    ["Worldwide", ["congenital", "iatrogenic", "unknown"], "Systemic", ["edema", "renal failure", "congenital anomalies", "maternal conditions", "complications", "various signs"], "Other conditions originating in the perinatal period", "P96"]
]

if __name__ == '__main__':
    # This part is just for demonstration, to show how to access the data.
    # You can use this 'icd_p_code_data' list to create your CSV.
    
    print(f"Total rows generated: {len(icd_p_code_data)}")
    
    print("\n--- Example Row (P00) ---")
    print(f"Geography: {icd_p_code_data[0][0]}")
    print(f"Transmission: {icd_p_code_data[0][1]}")
    print(f"Type: {icd_p_code_data[0][2]}")
    print(f"Symptoms: {icd_p_code_data[0][3]}")
    print(f"Label: {icd_p_code_data[0][4]}")
    print(f"ICD Code: {icd_p_code_data[0][5]}")

    print("\n--- Example Row (P36) ---")
    print(f"Geography: {icd_p_code_data[26][0]}")
    print(f"Transmission: {icd_p_code_data[26][1]}")
    print(f"Type: {icd_p_code_data[26][2]}")
    print(f"Symptoms: {icd_p_code_data[26][3]}")
    print(f"Label: {icd_p_code_data[26][4]}")
    print(f"ICD Code: {icd_p_code_data[26][5]}")

    print("\n--- Example Row (P90) ---")
    print(f"Geography: {icd_p_code_data[55][0]}")
    print(f"Transmission: {icd_p_code_data[55][1]}")
    print(f"Type: {icd_p_code_data[55][2]}")
    print(f"Symptoms: {icd_p_code_data[55][3]}")
    print(f"Label: {icd_p_code_data[55][4]}")
    print(f"ICD Code: {icd_p_code_data[55][5]}")
