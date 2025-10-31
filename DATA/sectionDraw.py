# This file contains a list of synthetic data for ICD-10 codes D00-D89.
# Each item is a dictionary structured for analysis or conversion to CSV.

disease_data = [
    # D00-D09: In situ neoplasms
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "genetic", "lifestyle"],
        "disease_type": "neoplastic",
        "symptoms": ["oral lesion", "white patch", "red patch", "difficulty swallowing", "pain", "bleeding"],
        "disease_name": "Carcinoma in situ of oral cavity, esophagus and stomach",
        "icd_code": "D00"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "lifestyle", "idiopathic"],
        "disease_type": "neoplastic",
        "symptoms": ["abdominal pain", "change in bowel habits", "rectal bleeding", "fatigue", "weight loss", "anemia"],
        "disease_name": "Carcinoma in situ of other and unspecified digestive organs",
        "icd_code": "D01"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "lifestyle", "genetic"],
        "disease_type": "neoplastic",
        "symptoms": ["persistent cough", "chest pain", "wheezing", "shortness of breath", "coughing up blood", "hoarseness"],
        "disease_name": "Carcinoma in situ of middle ear and respiratory system",
        "icd_code": "D02"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "UV radiation", "genetic"],
        "disease_type": "neoplastic",
        "symptoms": ["new mole", "changing mole", "irregular border", "varied color", "diameter increase", "itchy skin lesion"],
        "disease_name": "Melanoma in situ",
        "icd_code": "D03"
    },
    {
        "geography": "Worldwide",
        "transmission": ["UV radiation", "environmental", "genetic"],
        "disease_type": "neoplastic",
        "symptoms": ["scaly patch", "raised lesion", "non-healing sore", "wart-like growth", "crusting", "bleeding lesion"],
        "disease_name": "Carcinoma in situ of skin",
        "icd_code": "D04"
    },
    {
        "geography": "Worldwide",
        "transmission": ["genetic", "hormonal", "lifestyle"],
        "disease_type": "neoplastic",
        "symptoms": ["breast lump", "skin dimpling", "nipple discharge", "nipple retraction", "breast pain", "no symptoms (screening)"],
        "disease_name": "Carcinoma in situ of breast",
        "icd_code": "D05"
    },
    {
        "geography": "Worldwide",
        "transmission": ["viral (HPV)", "lifestyle", "immunodeficiency"],
        "disease_type": "neoplastic",
        "symptoms": ["abnormal vaginal bleeding", "pelvic pain", "pain during intercourse", "abnormal discharge", "no symptoms (screening)", "post-menopausal bleeding"],
        "disease_name": "Carcinoma in situ of cervix uteri",
        "icd_code": "D06"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "genetic", "lifestyle"],
        "disease_type": "neoplastic",
        "symptoms": ["abnormal uterine bleeding", "pelvic pain", "abdominal bloating", "abnormal discharge", "painful intercourse", "no symptoms"],
        "disease_name": "Carcinoma in situ of other and unspecified genital organs",
        "icd_code": "D07"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "chronic irritation", "idiopathic"],
        "disease_type": "neoplastic",
        "symptoms": ["painless hematuria", "urinary frequency", "urinary urgency", "pelvic pain", "flank pain", "no symptoms"],
        "disease_name": "Carcinoma in situ of other and unspecified urinary organs",
        "icd_code": "D09" # D08 is often not used; skipping to D09.
    },
    
    # D10-D36: Benign neoplasms
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "difficulty swallowing", "hoarseness", "oral growth", "sore throat", "no symptoms"],
        "disease_name": "Benign neoplasm of mouth and pharynx",
        "icd_code": "D10"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "swelling in neck", "dry mouth", "difficulty swallowing", "facial numbness", "no symptoms"],
        "disease_name": "Benign neoplasm of major salivary glands",
        "icd_code": "D11"
    },
    {
        "geography": "Worldwide",
        "transmission": ["genetic", "lifestyle", "idiopathic"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["rectal bleeding", "change in bowel habits", "abdominal pain", "anemia", "fatigue", "no symptoms (screening)"],
        "disease_name": "Benign neoplasm of colon, rectum, anus and anal canal",
        "icd_code": "D12"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["abdominal pain", "indigestion", "bloating", "nausea", "weight loss", "no symptoms"],
        "disease_name": "Benign neoplasm of other and ill-defined digestive organs",
        "icd_code": "D13"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["hoarseness", "difficulty breathing", "persistent cough", "wheezing", "stridor", "no symptoms"],
        "disease_name": "Benign neoplasm of middle ear and respiratory system",
        "icd_code": "D14"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["chest pain", "shortness of breath", "cough", "palpitations", "fatigue", "no symptoms"],
        "disease_name": "Benign neoplasm of other and unspecified intrathoracic organs",
        "icd_code": "D15"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["bone pain", "painless lump", "swelling", "pathologic fracture", "limited joint motion", "no symptoms"],
        "disease_name": "Benign neoplasm of bone and articular cartilage",
        "icd_code": "D16"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless soft lump", "slow-growing mass", "dull ache", "cosmetic deformity", "pressure on nerves", "no symptoms"],
        "disease_name": "Benign lipomatous neoplasm",
        "icd_code": "D17"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["red/blue skin lesion", "birthmark", "swelling", "pain", "bleeding", "no symptoms"],
        "disease_name": "Hemangioma and lymphangioma, any site",
        "icd_code": "D18"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "nerve pain", "numbness", "tingling", "muscle weakness", "no symptoms"],
        "disease_name": "Benign neoplasm of mesothelial tissue",
        "icd_code": "D19"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "swelling", "pain if pressing nerve", "cosmetic issue", "restricted movement", "no symptoms"],
        "disease_name": "Benign neoplasm of soft tissue of retroperitoneum and peritoneum",
        "icd_code": "D20"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "slow-growing mass", "pain", "numbness", "tingling", "no symptoms"],
        "disease_name": "Other benign neoplasms of connective and other soft tissue",
        "icd_code": "D21"
    },
    {
        "geography": "Worldwide",
        "transmission": ["UV radiation", "genetic", "idiopathic"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["mole", "skin tag", "wart-like growth", "pigmented lesion", "slow-growing", "no symptoms"],
        "disease_name": "Melanocytic nevi",
        "icd_code": "D22"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "UV radiation", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["skin lump", "cyst", "non-healing sore", "wart", "scaly patch", "no symptoms"],
        "disease_name": "Other benign neoplasms of skin",
        "icd_code": "D23"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "idiopathic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless breast lump", "rubbery mass", "movable lump", "breast pain", "nipple discharge", "no symptoms"],
        "disease_name": "Benign neoplasm of breast",
        "icd_code": "D24"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "genetic", "idiopathic"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["heavy menstrual bleeding", "pelvic pain", "frequent urination", "constipation", "infertility", "no symptoms"],
        "disease_name": "Leiomyoma of uterus (fibroids)",
        "icd_code": "D25"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["abnormal uterine bleeding", "pelvic pain", "infertility", "abdominal bloating", "painful intercourse", "no symptoms"],
        "disease_name": "Other benign neoplasms of uterus",
        "icd_code": "D26"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "idiopathic", "genetic"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["pelvic pain", "abdominal bloating", "urinary frequency", "feeling full quickly", "painful intercourse", "no symptoms"],
        "disease_name": "Benign neoplasm of ovary",
        "icd_code": "D27"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["abnormal vaginal bleeding", "pelvic pain", "vaginal mass", "painful intercourse", "abnormal discharge", "no symptoms"],
        "disease_name": "Benign neoplasm of other and unspecified female genital organs",
        "icd_code": "D28"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless testicular lump", "scrotal swelling", "penile lesion", "urinary difficulty", "pain", "no symptoms"],
        "disease_name": "Benign neoplasm of male genital organs",
        "icd_code": "D29"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless hematuria", "urinary frequency", "urinary urgency", "flank pain", "pelvic mass", "no symptoms"],
        "disease_name": "Benign neoplasm of urinary organs",
        "icd_code": "D30"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["vision changes", "eye pain", "protruding eye", "visual field loss", "lump on eyelid", "no symptoms"],
        "disease_name": "Benign neoplasm of eye and adnexa",
        "icd_code": "D31"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["hearing loss", "headache", "seizures", "vision problems", "balance issues", "no symptoms"],
        "disease_name": "Benign neoplasm of meninges",
        "icd_code": "D32"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["headache", "seizures", "nausea", "vomiting", "vision changes", "cognitive changes"],
        "disease_name": "Benign neoplasm of brain and other parts of central nervous system",
        "icd_code": "D33"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["neck swelling", "hoarseness", "difficulty swallowing", "hyperthyroidism symptoms", "hypothyroidism symptoms", "no symptoms"],
        "disease_name": "Benign neoplasm of thyroid gland",
        "icd_code": "D34"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["hormonal imbalance", "weight gain", "high blood pressure", "headache", "fatigue", "no symptoms"],
        "disease_name": "Benign neoplasm of other and unspecified endocrine glands",
        "icd_code": "D35"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "neoplastic (benign)",
        "symptoms": ["painless lump", "swelling", "pain", "depends on location", "incidental finding", "no symptoms"],
        "disease_name": "Benign neoplasm of other and unspecified sites",
        "icd_code": "D36"
    },

    # D37-D48: Neoplasms of uncertain or unknown behavior
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "lifestyle", "genetic"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["oral lesion", "dysphagia", "indigestion", "abdominal pain", "weight loss", "bleeding"],
        "disease_name": "Neoplasm of uncertain behavior of oral cavity and digestive organs",
        "icd_code": "D37"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "lifestyle", "genetic"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["persistent cough", "hoarseness", "wheezing", "chest pain", "shortness of breath", "hemoptysis"],
        "disease_name": "Neoplasm of uncertain behavior of middle ear and respiratory system",
        "icd_code": "D38"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "genetic", "idiopathic"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["abnormal uterine bleeding", "pelvic pain", "ovarian mass", "bloating", "urinary symptoms", "no symptoms"],
        "disease_name": "Neoplasm of uncertain behavior of female genital organs",
        "icd_code": "D39"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hormonal", "genetic", "idiopathic"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["testicular lump", "prostate enlargement", "urinary difficulty", "elevated PSA", "pain", "no symptoms"],
        "disease_name": "Neoplasm of uncertain behavior of male genital organs",
        "icd_code": "D40"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "chronic irritation", "idiopathic"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["painless hematuria", "urinary frequency", "urinary urgency", "flank pain", "pelvic mass", "no symptoms"],
        "disease_name": "Neoplasm of uncertain behavior of urinary organs",
        "icd_code": "D41"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["headache", "seizures", "vision changes", "hearing loss", "balance issues", "focal neurological deficit"],
        "disease_name": "Neoplasm of uncertain behavior of meninges",
        "icd_code": "D42"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "radiation"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["headache", "seizures", "nausea", "vomiting", "cognitive changes", "focal neurological deficit"],
        "disease_name": "Neoplasm of uncertain behavior of brain and central nervous system",
        "icd_code": "D43"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["hormonal imbalance", "thyroid nodule", "pituitary symptoms", "adrenal symptoms", "weight changes", "no symptoms"],
        "disease_name": "Neoplasm of uncertain behavior of endocrine glands",
        "icd_code": "D44"
    },
    {
        "geography": "Worldwide",
        "transmission": ["genetic", "idiopathic", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "headache", "dizziness", "itchiness", "enlarged spleen", "flushing"],
        "disease_name": "Polycythemia vera",
        "icd_code": "D45"
    },
    {
        "geography": "Worldwide",
        "transmission": ["environmental", "genetic", "idiopathic"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "shortness of breath", "easy bruising", "frequent infections", "pale skin", "fever"],
        "disease_name": "Myelodysplastic syndromes",
        "icd_code": "D46"
    },
    {
        "geography": "Worldwide",
        "transmission": ["genetic", "idiopathic", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "weight loss", "night sweats", "enlarged spleen", "fever", "frequent infections"],
        "disease_name": "Other neoplasms of uncertain behavior of lymphoid, hematopoietic and related tissue",
        "icd_code": "D47"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "environmental", "N/A"],
        "disease_type": "neoplastic (uncertain)",
        "symptoms": ["painless lump", "swelling", "pain", "depends on location", "incidental finding", "no symptoms"],
        "disease_name": "Neoplasm of uncertain behavior of other and unspecified sites",
        "icd_code": "D48"
    },

    # D50-D53: Nutritional anaemias
    {
        "geography": "Worldwide",
        "transmission": ["dietary", "malabsorption", "blood loss"],
        "disease_type": "nutritional",
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness", "pica"],
        "disease_name": "Iron deficiency anemia",
        "icd_code": "D50"
    },
    {
        "geography": "Worldwide",
        "transmission": ["dietary", "malabsorption", "autoimmune"],
        "disease_type": "nutritional",
        "symptoms": ["fatigue", "weakness", "numbness", "tingling", "balance problems", "sore tongue"],
        "disease_name": "Vitamin B12 deficiency anemia",
        "icd_code": "D51"
    },
    {
        "geography": "Worldwide",
        "transmission": ["dietary", "malabsorption", "alcoholism"],
        "disease_type": "nutritional",
        "symptoms": ["fatigue", "weakness", "sore mouth", "sore tongue", "pale skin", "irritability"],
        "disease_name": "Folate deficiency anemia",
        "icd_code": "D52"
    },
    {
        "geography": "Worldwide",
        "transmission": ["dietary", "malnutrition", "N/A"],
        "disease_type": "nutritional",
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness", "headache"],
        "disease_name": "Other nutritional anemias",
        "icd_code": "D53"
    },

    # D55-D59: Haemolytic anaemias
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["fatigue", "jaundice", "dark urine", "enlarged spleen", "weakness", "shortness of breath"],
        "disease_name": "Anemia due to enzyme disorders",
        "icd_code": "D55"
    },
    {
        "geography": "Africa, Mediterranean, Asia",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["fatigue", "weakness", "pale skin", "jaundice", "dark urine", "enlarged spleen"],
        "disease_name": "Thalassemia",
        "icd_code": "D56"
    },
    {
        "geography": "Sub-Saharan Africa, Americas",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["pain crises", "fatigue", "swelling of hands/feet", "frequent infections", "jaundice", "delayed growth"],
        "disease_name": "Sickle-cell disorders",
        "icd_code": "D57"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["jaundice", "anemia", "enlarged spleen", "gallstones", "fatigue", "weakness"],
        "disease_name": "Other hereditary hemolytic anemias",
        "icd_code": "D58"
    },
    {
        "geography": "Worldwide",
        "transmission": ["autoimmune", "idiopathic", "drug-induced"],
        "disease_type": "autoimmune",
        "symptoms": ["fatigue", "jaundice", "dark urine", "enlarged spleen", "weakness", "shortness of breath"],
        "disease_name": "Acquired hemolytic anemia",
        "icd_code": "D59"
    },

    # D60-D64: Aplastic and other anaemias
    {
        "geography": "Worldwide",
        "transmission": ["autoimmune", "idiopathic", "N/A"],
        "disease_type": "autoimmune",
        "symptoms": ["fatigue", "pale skin", "weakness", "shortness of breath", "dizziness", "no reticulocytes"],
        "disease_name": "Acquired pure red cell aplasia",
        "icd_code": "D60"
    },
    {
        "geography": "Worldwide",
        "transmission": ["autoimmune", "toxins", "radiation"],
        "disease_type": "autoimmune",
        "symptoms": ["fatigue", "frequent infections", "easy bruising", "bleeding gums", "pale skin", "shortness of breath"],
        "disease_name": "Other aplastic anemias",
        "icd_code": "D61"
    },
    {
        "geography": "Worldwide",
        "transmission": ["blood loss", "hemorrhage", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "dizziness", "pale skin", "shortness of breath", "low blood pressure", "rapid heart rate"],
        "disease_name": "Acute posthemorrhagic anemia",
        "icd_code": "D62"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "headache", "dizziness"],
        "disease_name": "Anemia in chronic diseases",
        "icd_code": "D63"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "headache", "dizziness"],
        "disease_name": "Other anemias",
        "icd_code": "D64"
    },

    # D65-D69: Coagulation defects, purpura and other haemorrhagic conditions
    {
        "geography": "Worldwide",
        "transmission": ["sepsis", "trauma", "cancer"],
        "disease_type": "haematological",
        "symptoms": ["bleeding", "bruising", "blood clots", "low blood pressure", "organ failure", "shortness of breath"],
        "disease_name": "Disseminated intravascular coagulation (DIC)",
        "icd_code": "D65"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["prolonged bleeding", "swollen joints", "deep bruises", "nosebleeds", "blood in urine", "pain"],
        "disease_name": "Hereditary factor VIII deficiency (Hemophilia A)",
        "icd_code": "D66"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["prolonged bleeding", "swollen joints", "deep bruises", "nosebleeds", "blood in urine", "pain"],
        "disease_name": "Hereditary factor IX deficiency (Hemophilia B)",
        "icd_code": "D67"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["easy bruising", "nosebleeds", "bleeding gums", "heavy menstruation", "prolonged bleeding", "N/A"],
        "disease_name": "Other coagulation defects (incl. von Willebrand)",
        "icd_code": "D68"
    },
    {
        "geography": "Worldwide",
        "transmission": ["autoimmune", "viral", "idiopathic"],
        "disease_type": "autoimmune",
        "symptoms": ["easy bruising", "petechiae", "bleeding gums", "nosebleeds", "blood in urine", "heavy menstruation"],
        "disease_name": "Purpura and other hemorrhagic conditions (incl. ITP)",
        "icd_code": "D69"
    },

    # D70-D77: Other diseases of blood and blood-forming organs
    {
        "geography": "Worldwide",
        "transmission": ["drug-induced", "autoimmune", "idiopathic"],
        "disease_type": "haematological",
        "symptoms": ["fever", "chills", "sore throat", "frequent infections", "mouth sores", "fatigue"],
        "disease_name": "Agranulocytosis",
        "icd_code": "D70"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["recurrent infections", "abscesses", "pneumonia", "granulomas", "diarrhea", "lymphadenopathy"],
        "disease_name": "Functional disorders of polymorphonuclear neutrophils",
        "icd_code": "D71"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "allergic", "parasitic"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "fever", "cough", "wheezing", "abdominal pain", "skin rash"],
        "disease_name": "Eosinophilia",
        "icd_code": "D72"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "autoimmune", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["enlarged spleen", "abdominal pain", "fatigue", "anemia", "thrombocytopenia", "portal hypertension"],
        "disease_name": "Diseases of spleen",
        "icd_code": "D73"
    },
    {
        "geography": "Worldwide",
        "transmission": ["genetic", "idiopathic", "N/A"],
        "disease_type": "genetic",
        "symptoms": ["cyanosis (blue skin)", "shortness of breath", "fatigue", "headache", "dizziness", "seizures"],
        "disease_name": "Methemoglobinemia",
        "icd_code": "D74"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "weakness", "fever", "weight loss", "depends on specific disease", "abnormal blood count"],
        "disease_name": "Other diseases of blood and blood-forming organs",
        "icd_code": "D75"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "autoimmune", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fever", "rash", "lymphadenopathy", "enlarged spleen", "enlarged liver", "fatigue"],
        "disease_name": "Certain diseases involving lymphoreticular tissue and reticulohistiocytic system",
        "icd_code": "D76"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["depends on disorder", "abnormal blood count", "bleeding", "clotting", "anemia", "infection"],
        "disease_name": "Other specified diseases of blood and blood-forming organs",
        "icd_code": "D77"
    },

    # D80-D89: Certain disorders involving the immune mechanism
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["recurrent infections", "pneumonia", "sinusitis", "diarrhea", "autoimmune disorders", "poor growth"],
        "disease_name": "Immunodeficiency with predominantly antibody defects",
        "icd_code": "D80"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["severe recurrent infections", "failure to thrive", "chronic diarrhea", "skin rashes", "oral thrush", "pneumonia"],
        "disease_name": "Combined immunodeficiencies",
        "icd_code": "D81"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["recurrent infections", "eczema", "thrombocytopenia", "easy bruising", "bloody diarrhea", "autoimmune disorders"],
        "disease_name": "Immunodeficiency associated with other major defects",
        "icd_code": "D82"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["recurrent infections", "pneumonia", "sinusitis", "autoimmune disorders", "enlarged lymph nodes", "enlarged spleen"],
        "disease_name": "Common variable immunodeficiency (CVID)",
        "icd_code": "D83"
    },
    {
        "geography": "Worldwide",
        "transmission": ["hereditary", "genetic", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["recurrent infections", "depends on specific defect", "autoimmune symptoms", "poor vaccine response", "recurrent fungal infections", "recurrent viral infections"],
        "disease_name": "Other immunodeficiencies",
        "icd_code": "D84"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "autoimmune", "N/A"],
        "disease_type": "autoimmune",
        "symptoms": ["granulomas", "cough", "shortness of breath", "fatigue", "weight loss", "swollen lymph nodes"],
        "disease_name": "Sarcoidosis",
        "icd_code": "D86"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["depends on disorder", "abnormal immune function", "inflammation", "autoimmunity", "recurrent infections", "fatigue"],
        "disease_name": "Other specified disorders involving the immune mechanism",
        "icd_code": "D87"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "genetic", "N/A"],
        "disease_type": "haematological",
        "symptoms": ["fatigue", "weakness", "weight loss", "anemia", "bone pain", "kidney problems"],
        "disease_name": "Other immunoproliferative diseases",
        "icd_code": "D88"
    },
    {
        "geography": "Worldwide",
        "transmission": ["idiopathic", "N/A", "N/A"],
        "disease_type": "immunodeficiency",
        "symptoms": ["depends on disorder", "abnormal immune function", "inflammation", "autoimmunity", "recurrent infections", "fatigue"],
        "disease_name": "Other disorders involving the immune mechanism, not elsewhere classified",
        "icd_code": "D89"
    }
]
