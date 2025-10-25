# ICD-10 J-Chapter (J00-J99) Disease Data
#
# This list contains data rows for diseases in the ICD-10 J chapter (J00-J99).
#
# Note: The ICD-10 classification does not use every code from J00 to J99
# at the three-character category level. Many codes (e.g., J07, J08, J19, J23-J29,
# J48-J59, etc.) are not valid primary diagnostic codes. This dataset includes
# *only* the valid 3-character categories, as per the instruction
# to "omit those unused codes". This results in 64 rows.

# Header for the CSV file
csv_header = [
    "Geography",
    "Transmission",
    "Disease_Type",
    "Symptoms",
    "Disease_Name",
    "ICD_Code"
]

# Data rows
disease_data = [
    # --- J00-J06: Acute upper respiratory infections ---
    [
        "Worldwide",  # Geography
        ["droplet", "airborne", "contact"],  # Transmission
        "viral",  # Disease_Type
        ["runny nose", "sore throat", "cough", "congestion", "sneezing", "mild fever"],  # Symptoms
        "Acute nasopharyngitis (common cold)",  # Disease_Name
        "J00"  # ICD_Code
    ],
    [
        "Worldwide",
        ["complication", "droplet", "biofilm"],
        "viral",
        ["facial pain", "headache", "nasal congestion", "thick nasal discharge", "fever", "loss of smell"],
        "Acute sinusitis",
        "J01"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["sore throat", "painful swallowing", "fever", "red pharynx", "swollen tonsils", "headache"],
        "Acute pharyngitis",
        "J02"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["sore throat", "swollen tonsils", "white/yellow patches", "painful swallowing", "fever", "swollen lymph nodes"],
        "Acute tonsillitis",
        "J03"
    ],
    [
        "Worldwide",
        ["droplet", "vocal strain", "irritants"],
        "viral",
        ["hoarseness", "voice loss", "sore throat", "dry cough", "fever", "throat irritation"],
        "Acute laryngitis and tracheitis",
        "J04"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["barking cough", "stridor", "hoarseness", "difficulty breathing", "fever", "drooling"],
        "Acute obstructive laryngitis (croup) and epiglottitis",
        "J05"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["cough", "sore throat", "runny nose", "fever", "headache", "malaise"],
        "Acute upper respiratory infection, unspecified",
        "J06"
    ],
    # --- J09-J18: Influenza and pneumonia ---
    [
        "Worldwide (pandemic potential)",
        ["droplet", "airborne", "zoonotic"],
        "viral",
        ["high fever", "severe body aches", "cough", "headache", "fatigue", "shortness of breath"],
        "Influenza due to identified zoonotic/pandemic virus",
        "J09"
    ],
    [
        "Worldwide (seasonal)",
        ["droplet", "airborne", "contact"],
        "viral",
        ["fever", "cough", "sore throat", "body aches", "headache", "fatigue"],
        "Influenza due to identified seasonal influenza virus",
        "J10"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["fever", "cough", "sore throat", "body aches", "headache", "fatigue"],
        "Influenza, virus not identified (Flu-like illness)",
        "J11"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "complication"],
        "viral",
        ["cough", "fever", "chills", "shortness of breath", "fatigue", "chest pain"],
        "Viral pneumonia, not elsewhere classified",
        "J12"
    ],
    [
        "Worldwide",
        ["droplet", "aspiration", "complication"],
        "bacterial",
        ["sudden high fever", "productive cough", "rust-colored sputum", "chest pain", "shortness of breath", "chills"],
        "Pneumonia due to Streptococcus pneumoniae",
        "J13"
    ],
    [
        "Worldwide",
        ["droplet", "aspiration", "complication"],
        "bacterial",
        ["fever", "cough", "shortness of breath", "chest pain", "chills", "purulent sputum"],
        "Pneumonia due to Haemophilus influenzae",
        "J14"
    ],
    [
        "Worldwide",
        ["droplet", "aspiration", "nosocomial"],
        "bacterial",
        ["fever", "productive cough", "purulent sputum", "shortness of breath", "chest pain", "chills"],
        "Bacterial pneumonia, not elsewhere classified",
        "J15"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "inhalation"],
        "bacterial",
        ["low-grade fever", "dry cough", "headache", "malaise", "chest soreness", "fatigue"],
        "Pneumonia due to other infectious organisms (e.g., Atypical)",
        "J16"
    ],
    [
        "Worldwide",
        ["complication", "systemic", "opportunistic"],
        "bacterial",
        ["fever", "cough", "dyspnea", "underlying disease symptoms", "chest pain", "weakness"],
        "Pneumonia in diseases classified elsewhere",
        "J17"
    ],
    [
        "Worldwide",
        ["droplet", "aspiration", "community-acquired"],
        "bacterial",
        ["fever", "cough", "shortness of breath", "chest pain", "chills", "malaise"],
        "Pneumonia, organism unspecified",
        "J18"
    ],
    # --- J20-J22: Other acute lower respiratory infections ---
    [
        "Worldwide",
        ["droplet", "airborne", "irritants"],
        "viral",
        ["persistent cough", "mucus production", "chest discomfort", "wheezing", "low-grade fever", "fatigue"],
        "Acute bronchitis",
        "J20"
    ],
    [
        "Worldwide (common in infants)",
        ["droplet", "contact", "fomites"],
        "viral",
        ["wheezing", "rapid breathing", "cough", "fever", "nasal flaring", "retractions"],
        "Acute bronchiolitis (RSV)",
        "J21"
    ],
    [
        "Worldwide",
        ["droplet", "airborne", "contact"],
        "viral",
        ["cough", "fever", "shortness of breath", "chest congestion", "wheezing", "malaise"],
        "Unspecified acute lower respiratory infection",
        "J22"
    ],
    # --- J30-J39: Other diseases of upper respiratory tract ---
    [
        "Worldwide",
        ["allergen", "environmental", "genetic"],
        "fungal",
        ["sneezing", "itchy nose", "runny nose", "nasal congestion", "watery eyes", "post-nasal drip"],
        "Allergic rhinitis and vasomotor rhinitis",
        "J30"
    ],
    [
        "Worldwide",
        ["irritants", "environmental", "complication"],
        "bacterial",
        ["persistent congestion", "post-nasal drip", "chronic cough", "sore throat", "bad breath", "facial pressure"],
        "Chronic rhinitis, nasopharyngitis and pharyngitis",
        "J31"
    ],
    [
        "Worldwide",
        ["biofilm", "complication", "inflammation"],
        "bacterial",
        ["nasal congestion", "facial pain/pressure", "thick nasal discharge", "loss of smell", "cough", "fatigue"],
        "Chronic sinusitis",
        "J32"
    ],
    [
        "Worldwide",
        ["inflammation", "complication", "allergy"],
        "fungal",
        ["nasal obstruction", "runny nose", "loss of smell", "facial pressure", "snoring", "post-nasal drip"],
        "Nasal polyps",
        "J33"
    ],
    [
        "Worldwide",
        ["trauma", "complication", "congenital"],
        "bacterial",
        ["nasal obstruction", "nosebleeds", "facial pain", "headache", "runny nose", "difficulty breathing"],
        "Other disorders of nose (e.g., Deviated septum)",
        "J34"
    ],
    [
        "Worldwide",
        ["complication", "biofilm", "recurrent infection"],
        "bacterial",
        ["recurrent sore throat", "enlarged tonsils", "snoring", "sleep apnea", "bad breath", "difficulty swallowing"],
        "Chronic diseases of tonsils and adenoids",
        "J35"
    ],
    [
        "Worldwide",
        ["complication", "bacterial spread", "local infection"],
        "bacterial",
        ["severe sore throat", "unilateral swelling", "trismus (lockjaw)", "muffled voice", "fever", "drooling"],
        "Peritonsillar abscess (Quinsy)",
        "J36"
    ],
    [
        "Worldwide",
        ["irritants", "vocal strain", "acid reflux"],
        "bacterial",
        ["chronic hoarseness", "voice change", "throat clearing", "dry cough", "globus sensation", "sore throat"],
        "Chronic laryngitis and laryngotracheitis",
        "J37"
    ],
    [
        "Worldwide",
        ["vocal strain", "irritants", "trauma"],
        "bacterial",
        ["hoarseness", "voice changes", "voice fatigue", "aphonia", "breathy voice", "throat pain"],
        "Diseases of vocal cords (e.g., Nodules, Polyps)",
        "J38"
    ],
    [
        "Worldwide",
        ["complication", "inflammation", "trauma"],
        "bacterial",
        ["varied UR symptoms", "obstruction", "pain", "discharge", "hoarseness", "unspecified UR issue"],
        "Other diseases of upper respiratory tract, NEC",
        "J39"
    ],
    # --- J40-J47: Chronic lower respiratory diseases ---
    [
        "Worldwide",
        ["irritants", "smoking", "pollution"],
        "viral",
        ["cough", "mucus production", "chest tightness", "wheezing", "shortness of breath", "fatigue"],
        "Bronchitis, not specified as acute or chronic",
        "J40"
    ],
    [
        "Worldwide (assoc. with smoking)",
        ["smoking", "irritants", "pollution"],
        "bacterial",
        ["chronic productive cough", "excess sputum", "wheezing", "shortness of breath", "frequent infections", "chest tightness"],
        "Simple and mucopurulent chronic bronchitis",
        "J41"
    ],
    [
        "Worldwide",
        ["smoking", "pollution", "genetic"],
        "bacterial",
        ["chronic cough", "sputum production", "dyspnea", "wheezing", "chest tightness", "fatigue"],
        "Unspecified chronic bronchitis (COPD component)",
        "J42"
    ],
    [
        "Worldwide",
        ["smoking", "genetic", "pollution"],
        "bacterial",
        ["shortness of breath", "dyspnea on exertion", "chronic cough", "wheezing", "barrel chest", "weight loss"],
        "Emphysema (COPD component)",
        "J43"
    ],
    [
        "Worldwide",
        ["smoking", "pollution", "occupational"],
        "bacterial",
        ["chronic cough", "sputum production", "dyspnea", "wheezing", "frequent infections", "fatigue"],
        "Other chronic obstructive pulmonary disease (COPD)",
        "J44"
    ],
    [
        "Worldwide",
        ["genetic", "allergen", "environmental"],
        "fungal",
        ["wheezing", "shortness of breath", "chest tightness", "cough", "nighttime symptoms", "exercise-induced cough"],
        "Asthma",
        "J45"
    ],
    [
        "Worldwide",
        ["complication", "allergen", "trigger"],
        "fungal",
        ["severe dyspnea", "unresponsive wheezing", "chest tightness", "cyanosis", "anxiety", "inability to speak"],
        "Status asthmaticus (Severe asthma attack)",
        "J46"
    ],
    [
        "Worldwide",
        ["complication", "recurrent infection", "genetic"],
        "bacterial",
        ["chronic productive cough", "copious purulent sputum", "hemoptysis", "recurrent infections", "shortness of breath", "clubbing"],
        "Bronchiectasis",
        "J47"
    ],
    # --- J60-J70: Lung diseases due to external agents ---
    [
        "Worldwide (coal mining regions)",
        ["inhalation", "occupational", "dust"],
        "bacterial",
        ["cough", "black sputum", "shortness of breath", "dyspnea", "chest tightness", "progressive fibrosis"],
        "Coalworker's pneumoconiosis (Black Lung)",
        "J60"
    ],
    [
        "Worldwide (industrial areas)",
        ["inhalation", "occupational", "asbestos"],
        "fungal",
        ["shortness of breath", "dry cough", "chest pain", "clubbing of fingers", "crackles in lungs", "fatigue"],
        "Pneumoconiosis due to asbestos (Asbestosis)",
        "J61"
    ],
    [
        "Worldwide (mining, construction)",
        ["inhalation", "occupational", "silica"],
        "bacterial",
        ["shortness of breath", "severe cough", "fatigue", "chest pain", "fever", "weight loss"],
        "Pneumoconiosis due to silica (Silicosis)",
        "J62"
    ],
    [
        "Worldwide (industrial)",
        ["inhalation", "occupational", "metal dust"],
        "fungal",
        ["cough", "dyspnea", "chest tightness", "wheezing", "fibrosis", "reduced lung function"],
        "Pneumoconiosis due to other inorganic dusts",
        "J63"
    ],
    [
        "Worldwide (industrial)",
        ["inhalation", "occupational", "dust"],
        "fungal",
        ["cough", "shortness of breath", "chest pain", "fibrosis", "fatigue", "weight loss"],
        "Pneumoconiosis, unspecified",
        "J64"
    ],
    [
        "Worldwide (high TB/silica areas)",
        ["inhalation", "occupational", "complication"],
        "bacterial",
        ["cough", "hemoptysis", "fever", "night sweats", "weight loss", "shortness of breath"],
        "Pneumoconiosis associated with tuberculosis",
        "J65"
    ],
    [
        "Worldwide (agricultural)",
        ["inhalation", "occupational", "organic dust"],
        "fungal",
        ["cough", "fever", "chills", "shortness of breath", "malaise", "chest tightness"],
        "Airway disease due to specific organic dust",
        "J66"
    ],
    [
        "Worldwide (various)",
        ["inhalation", "occupational", "allergen"],
        "fungal",
        ["fever", "chills", "cough", "dyspnea", "malaise", "headache"],
        "Hypersensitivity pneumonitis (e.g., Farmer's Lung)",
        "J67"
    ],
    [
        "Worldwide (industrial)",
        ["inhalation", "occupational", "chemical"],
        "viral",
        ["cough", "wheezing", "shortness of breath", "chest pain", "pulmonary edema", "throat irritation"],
        "Respiratory conditions due to inhalation of chemicals",
        "J68"
    ],
    [
        "Worldwide",
        ["aspiration", "inhalation", "complication"],
        "bacterial",
        ["cough", "choking", "fever", "shortness of breath", "chest pain", "putrid sputum"],
        "Pneumonitis due to solids and liquids (Aspiration)",
        "J69"
    ],
    [
        "Worldwide",
        ["radiation", "drug-induced", "complication"],
        "fungal",
        ["dry cough", "dyspnea", "fever", "chest pain", "fibrosis", "fatigue"],
        "Respiratory conditions due to other external agents",
        "J70"
    ],
    # --- J80-J84: Other respiratory diseases (interstitium) ---
    [
        "Worldwide",
        ["complication", "sepsis", "trauma"],
        "bacterial",
        ["severe dyspnea", "hypoxemia", "tachypnea", "cyanosis", "diffuse lung infiltrates", "organ failure"],
        "Acute respiratory distress syndrome (ARDS)",
        "J80"
    ],
    [
        "Worldwide",
        ["cardiac", "non-cardiac", "complication"],
        "bacterial",
        ["shortness of breath", "orthopnea", "pink frothy sputum", "cough", "wheezing", "paroxysmal nocturnal dyspnea"],
        "Pulmonary edema",
        "J81"
    ],
    [
        "Worldwide",
        ["parasitic", "drug-reaction", "idiopathic"],
        "parasitic",
        ["cough", "fever", "wheezing", "dyspnea", "malaise", "high eosinophil count"],
        "Pulmonary eosinophilia, not elsewhere classified",
        "J82"
    ],
    # J83 is not a valid 3-character code
    [
        "Worldwide",
        ["idiopathic", "autoimmune", "environmental"],
        "fungal",
        ["progressive dyspnea", "dry cough", "fatigue", "clubbing of fingers", "weight loss", "crackles in lungs"],
        "Other interstitial pulmonary diseases (e.g., IPF)",
        "J84"
    ],
    # --- J85-J86: Suppurative and necrotic conditions ---
    [
        "Worldwide",
        ["aspiration", "complication", "bacterial"],
        "bacterial",
        ["fever", "productive cough", "foul-smelling sputum", "chest pain", "night sweats", "weight loss"],
        "Abscess of lung and mediastinum",
        "J85"
    ],
    [
        "Worldwide",
        ["complication", "bacterial spread", "pneumonia"],
        "bacterial",
        ["fever", "chest pain", "cough", "shortness of breath", "malaise", "weight loss"],
        "Pyothorax (Empyema)",
        "J86"
    ],
    # --- J90-J94: Other diseases of pleura ---
    [
        "Worldwide",
        ["complication", "cardiac", "inflammatory"],
        "bacterial",
        ["shortness of breath", "pleuritic chest pain", "dry cough", "fever", "dullness to percussion", "decreased breath sounds"],
        "Pleural effusion, not elsewhere classified",
        "J90"
    ],
    [
        "Worldwide",
        ["complication", "systemic", "inflammatory"],
        "bacterial",
        ["dyspnea", "chest pain", "cough", "underlying disease symptoms", "fever", "malaise"],
        "Pleural effusion in conditions classified elsewhere",
        "J91"
    ],
    [
        "Worldwide (industrial)",
        ["asbestos", "inhalation", "occupational"],
        "fungal",
        ["asymptomatic", "shortness of breath", "chest pain", "reduced lung function", "history of asbestos", "cough"],
        "Pleural plaque",
        "J92"
    ],
    [
        "Worldwide",
        ["trauma", "spontaneous", "complication"],
        "bacterial",
        ["sudden chest pain", "shortness of breath", "tachycardia", "cyanosis", "hyperresonance", "absent breath sounds"],
        "Pneumothorax (Collapsed lung)",
        "J93"
    ],
    [
        "Worldwide",
        ["complication", "trauma", "inflammatory"],
        "bacterial",
        ["chest pain", "dyspnea", "cough", "fever", "pleural friction rub", "hemoptysis"],
        "Other pleural conditions (e.g., Hemothorax)",
        "J94"
    ],
    # --- J95-J99: Other diseases of the respiratory system ---
    [
        "Worldwide (healthcare settings)",
        ["complication", "nosocomial", "iatrogenic"],
        "bacterial",
        ["fever", "dyspnea", "cough", "hypoxemia", "purulent sputum", "chest infiltrates"],
        "Postprocedural respiratory disorders, NEC",
        "J95"
    ],
    [
        "Worldwide",
        ["complication", "multi-organ", "systemic"],
        "viral",
        ["severe dyspnea", "hypoxemia", "hypercapnia", "confusion", "cyanosis", "rapid breathing"],
        "Respiratory failure, not elsewhere classified",
        "J96"
    ],
    # J97 is not a valid 3-character code
    [
        "Worldwide",
        ["complication", "idiopathic", "congenital"],
        "bacterial",
        ["cough", "dyspnea", "wheezing", "chest pain", "abnormal breathing", "unspecified symptom"],
        "Other respiratory disorders, NEC",
        "J98"
    ],
    [
        "Worldwide",
        ["complication", "systemic", "autoimmune"],
        "viral",
        ["dyspnea", "cough", "underlying disease symptoms", "chest pain", "fibrosis", "hypoxemia"],
        "Respiratory disorders in diseases classified elsewhere",
        "J99"
    ]
]

# Example: How to use this data with the csv module
#
# import csv
#
# # Get the header and the data rows
# header = csv_header
# data = disease_data
#
# # Write to a CSV file
# with open('icd_j_disease_dataset.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     # Write the header
#     writer.writerow(header)
#     # Write the data rows
#     writer.writerows(data)
#
# print("CSV file 'icd_j_disease_dataset.csv' created successfully.")
#
