# This file contains dataset rows for ICD-10 codes C00-C96 (Malignant Neoplasms).
# The data is structured as a list of lists, where each inner list represents a row.
#
# Column Structure:
# 0: Geography (String) - General area of high prevalence.
# 1: Key Risk Factors (List of 3 Strings) - Adapted from "Transmission".
# 2: Disease Type (String) - Adapted to "Neoplastic".
# 3: Common Symptoms (List of 6 Strings)
# 4: Disease Name (String) - The "Label" for AI training.
# 5: ICD-10 Code (String)

disease_data_rows = [
    # C00-C14: Malignant neoplasms of lip, oral cavity and pharynx
    ["Worldwide", ["smoking", "alcohol", "UV radiation"], "Neoplastic", ["sore on lip", "lip lump", "lip bleeding", "lip pain", "neck lump", "numbness"], "Malignant neoplasm of lip", "C00"],
    ["Worldwide", ["smoking", "alcohol", "HPV infection"], "Neoplastic", ["sore throat", "difficulty swallowing", "ear pain", "neck lump", "voice changes", "tongue pain"], "Malignant neoplasm of base of tongue", "C01"],
    ["Worldwide", ["smoking", "alcohol", "genetics"], "Neoplastic", ["tongue ulcer", "mouth pain", "difficulty speaking", "tongue bleeding", "white/red patch", "neck lump"], "Malignant neoplasm of other parts of tongue", "C02"],
    ["Worldwide", ["smoking", "alcohol", "poor oral hygiene"], "Neoplastic", ["gum swelling", "gum bleeding", "loose teeth", "mouth ulcer", "denture fit change", "jaw pain"], "Malignant neoplasm of gum", "C03"],
    ["Worldwide", ["smoking", "alcohol", "betel quid"], "Neoplastic", ["mouth ulcer", "white/red patch", "mouth pain", "difficulty swallowing", "neck lump", "ear pain"], "Malignant neoplasm of floor of mouth", "C04"],
    ["Worldwide", ["smoking", "alcohol", "ill-fitting dentures"], "Neoplastic", ["palate sore", "palate lump", "mouth pain", "difficulty swallowing", "denture fit change", "bleeding"], "Malignant neoplasm of palate", "C05"],
    ["Worldwide", ["smoking", "alcohol", "betel quid"], "Neoplastic", ["cheek lump", "mouth ulcer", "white/red patch", "mouth pain", "trismus", "numbness"], "Malignant neoplasm of other parts of mouth", "C06"],
    ["East Asia", ["radiation", "genetics", "smoking"], "Neoplastic", ["painless cheek swelling", "facial numbness", "facial weakness", "difficulty opening mouth", "ear pain", "gland lump"], "Malignant neoplasm of parotid gland", "C07"],
    ["Worldwide", ["radiation", "genetics", "Sjögren syndrome"], "Neoplastic", ["lump under jaw", "mouth pain", "facial numbness", "difficulty swallowing", "facial weakness", "persistent swelling"], "Malignant neoplasm of other major salivary glands", "C08"],
    ["Worldwide", ["HPV infection", "smoking", "alcohol"], "Neoplastic", ["sore throat", "neck lump", "ear pain", "difficulty swallowing", "tonsil swelling", "blood in saliva"], "Malignant neoplasm of tonsil", "C09"],
    ["Worldwide", ["HPV infection", "smoking", "alcohol"], "Neoplastic", ["persistent sore throat", "voice changes", "ear pain", "neck lump", "painful swallowing", "unexplained weight loss"], "Malignant neoplasm of oropharynx", "C10"],
    ["East Asia", ["EBV infection", "genetics", "salted fish diet"], "Neoplastic", ["neck lump", "nasal congestion", "hearing loss", "tinnitus", "headaches", "nosebleeds"], "Malignant neoplasm of nasopharynx", "C11"],
    ["Worldwide", ["smoking", "alcohol", "genetics"], "Neoplastic", ["difficulty swallowing", "ear pain", "hoarseness", "sore throat", "neck lump", "chronic cough"], "Malignant neoplasm of pyriform sinus", "C12"],
    ["Worldwide", ["smoking", "alcohol", "Plummer-Vinson"], "Neoplastic", ["sore throat", "difficulty swallowing", "neck lump", "ear pain", "voice changes", "persistent cough"], "Malignant neoplasm of hypopharynx", "C13"],
    ["Worldwide", ["smoking", "alcohol", "genetics"], "Neoplastic", ["sore throat", "swallowing difficulty", "voice changes", "neck mass", "ear pain", "unexplained weight loss"], "Malignant neoplasm of other pharynx sites", "C14"],

    # C15-C26: Malignant neoplasms of digestive organs
    ["Worldwide", ["smoking", "alcohol", "GERD"], "Neoplastic", ["difficulty swallowing", "weight loss", "chest pain", "indigestion", "hoarseness", "chronic cough"], "Malignant neoplasm of esophagus", "C15"],
    ["East Asia", ["H. pylori", "smoking", "salted food diet"], "Neoplastic", ["indigestion", "abdominal pain", "nausea", "loss of appetite", "bloating after eating", "unexplained weight loss"], "Malignant neoplasm of stomach", "C16"],
    ["Worldwide", ["Crohn's disease", "genetics", "celiac disease"], "Neoplastic", ["abdominal pain", "weight loss", "nausea", "vomiting", "anemia", "fatigue"], "Malignant neoplasm of small intestine", "C17"],
    ["Developed nations", ["diet", "obesity", "genetics"], "Neoplastic", ["change in bowel habits", "rectal bleeding", "abdominal discomfort", "unexplained weight loss", "fatigue", "anemia"], "Malignant neoplasm of colon", "C18"],
    ["Developed nations", ["diet", "obesity", "genetics"], "Neoplastic", ["change in bowel habits", "rectal bleeding", "abdominal pain", "bloating", "fatigue", "unexplained weight loss"], "Malignant neoplasm of rectosigmoid junction", "C19"],
    ["Developed nations", ["diet", "obesity", "IBD"], "Neoplastic", ["rectal bleeding", "change in bowel habits", "tenesmus", "abdominal pain", "anemia", "unexplained weight loss"], "Malignant neoplasm of rectum", "C20"],
    ["Worldwide", ["HPV infection", "smoking", "immunosuppression"], "Neoplastic", ["anal bleeding", "anal pain", "anal lump", "anal itching", "change in bowel habits", "fecal incontinence"], "Malignant neoplasm of anus and anal canal", "C21"],
    ["East Asia", ["Hepatitis B", "Hepatitis C", "alcohol"], "Neoplastic", ["jaundice", "abdominal pain", "ascites", "unexplained weight loss", "loss of appetite", "fatigue"], "Malignant neoplasm of liver", "C22"],
    ["Worldwide", ["gallstones", "obesity", "genetics"], "Neoplastic", ["jaundice", "abdominal pain", "nausea", "vomiting", "bloating", "unexplained weight loss"], "Malignant neoplasm of gallbladder", "C23"],
    ["Worldwide", ["PSC", "liver flukes", "choledochal cysts"], "Neoplastic", ["jaundice", "abdominal pain", "itching", "clay-colored stools", "dark urine", "unexplained weight loss"], "Malignant neoplasm of other biliary tract", "C24"],
    ["Worldwide", ["smoking", "genetics", "chronic pancreatitis"], "Neoplastic", ["jaundice", "abdominal pain", "back pain", "unexplained weight loss", "loss of appetite", "new-onset diabetes"], "Malignant neoplasm of pancreas", "C25"],
    ["Worldwide", ["genetics", "IBD", "obesity"], "Neoplastic", ["abdominal pain", "weight loss", "nausea", "vomiting", "fatigue", "change in bowel habits"], "Malignant neoplasm of other digestive organs", "C26"],

    # C30-C39: Malignant neoplasms of respiratory and intrathoracic organs
    ["Worldwide", ["wood dust", "smoking", "industrial chemicals"], "Neoplastic", ["nasal congestion", "nosebleeds", "facial pain", "headache", "hearing loss", "vision problems"], "Malignant neoplasm of nasal cavity and middle ear", "C30"],
    ["Worldwide", ["smoking", "wood dust", "nickel exposure"], "Neoplastic", ["chronic sinusitis", "nasal obstruction", "facial swelling", "headache", "vision changes", "nosebleeds"], "Malignant neoplasm of accessory sinuses", "C31"],
    ["Worldwide", ["smoking", "alcohol", "genetics"], "Neoplastic", ["hoarseness", "persistent cough", "sore throat", "difficulty swallowing", "ear pain", "neck lump"], "Malignant neoplasm of larynx", "C32"],
    ["Worldwide", ["smoking", "radon", "genetics"], "Neoplastic", ["persistent cough", "shortness of breath", "hoarseness", "wheezing", "chest pain", "coughing up blood"], "Malignant neoplasm of trachea", "C33"],
    ["Worldwide", ["smoking", "radon", "asbestos"], "Neoplastic", ["persistent cough", "chest pain", "shortness of breath", "coughing up blood", "unexplained weight loss", "fatigue"], "Malignant neoplasm of bronchus and lung", "C34"],
    ["Worldwide", ["genetics", "radiation", "autoimmune disorders"], "Neoplastic", ["cough", "chest pain", "shortness of breath", "Myasthenia Gravis", "facial swelling", "hoarseness"], "Malignant neoplasm of thymus", "C37"],
    ["Worldwide", ["asbestos", "radiation", "genetics"], "Neoplastic", ["chest pain", "shortness of breath", "persistent cough", "fatigue", "unexplained weight loss", "pleural effusion"], "Malignant neoplasm of heart, mediastinum, and pleura", "C38"],
    ["Worldwide", ["smoking", "asbestos", "genetics"], "Neoplastic", ["cough", "chest pain", "shortness of breath", "fatigue", "weight loss", "hoarseness"], "Malignant neoplasm of other respiratory organs", "C39"],

    # C40-C41: Malignant neoplasms of bone and articular cartilage
    ["Worldwide", ["genetics", "radiation", "Paget's disease"], "Neoplastic", ["bone pain", "swelling near bone", "pathologic fracture", "fatigue", "unexplained weight loss", "limited range of motion"], "Malignant neoplasm of bone and articular cartilage of limbs", "C40"],
    ["Worldwide", ["genetics", "radiation", "Paget's disease"], "Neoplastic", ["jaw pain", "pelvic pain", "back pain", "swelling", "pathologic fracture", "fatigue"], "Malignant neoplasm of bone and articular cartilage of other sites", "C41"],

    # C43-C44: Melanoma and other malignant neoplasms of skin
    ["Australasia", ["UV radiation", "genetics", "many moles"], "Neoplastic", ["new mole", "changing mole", "irregular border", "asymmetric shape", "multiple colors", "diameter >6mm"], "Malignant melanoma of skin", "C43"],
    ["Australasia", ["UV radiation", "fair skin", "immunosuppression"], "Neoplastic", ["pearly/waxy bump", "flat, flesh-colored lesion", "firm, red nodule", "crusting/bleeding sore", "scaly patch", "non-healing sore"], "Other malignant neoplasms of skin", "C44"],

    # C45-C49: Malignant neoplasms of mesothelial and soft tissue
    ["Worldwide", ["asbestos", "radiation", "genetics"], "Neoplastic", ["shortness of breath", "chest pain", "dry cough", "unexplained weight loss", "abdominal swelling", "abdominal pain"], "Mesothelioma", "C45"],
    ["Sub-Saharan Africa", ["HHV-8 infection", "HIV/AIDS", "immunosuppression"], "Neoplastic", ["purple/red skin lesions", "leg swelling", "internal lesions", "cough", "abdominal pain", "bleeding"], "Kaposi sarcoma", "C46"],
    ["Worldwide", ["genetics", "radiation", "neurofibromatosis"], "Neoplastic", ["persistent pain", "lump under skin", "numbness", "tingling", "weakness in limb", "dizziness"], "Malignant neoplasm of peripheral nerves", "C47"],
    ["Worldwide", ["genetics", "radiation", "chemical exposure"], "Neoplastic", ["abdominal pain", "abdominal mass", "feeling of fullness", "back pain", "unexplained weight loss", "bowel obstruction"], "Malignant neoplasm of retroperitoneum and peritoneum", "C48"],
    ["Worldwide", ["genetics", "radiation", "chemical exposure"], "Neoplastic", ["painless lump", "swelling in limb", "pain if nerve compressed", "limited mobility", "fatigue", "unexplained weight loss"], "Malignant neoplasm of other connective and soft tissue", "C49"],

    # C50: Malignant neoplasm of breast
    ["Developed nations", ["genetics", "female gender", "age"], "Neoplastic", ["breast lump", "nipple discharge", "skin dimpling", "nipple retraction", "breast pain", "skin redness/thickening"], "Malignant neoplasm of breast", "C50"],

    # C51-C58: Malignant neoplasms of female genital organs
    ["Worldwide", ["HPV infection", "smoking", "immunosuppression"], "Neoplastic", ["vulvar itching", "vulvar pain", "skin changes", "lump or sore", "bleeding", "abnormal discharge"], "Malignant neoplasm of vulva", "C51"],
    ["Worldwide", ["age", "DES exposure", "HPV infection"], "Neoplastic", ["abnormal vaginal bleeding", "pain during intercourse", "vaginal lump", "watery discharge", "pelvic pain", "painful urination"], "Malignant neoplasm of vagina", "C52"],
    ["Developing nations", ["HPV infection", "smoking", "immunosuppression"], "Neoplastic", ["abnormal vaginal bleeding", "bleeding after intercourse", "pelvic pain", "pain during intercourse", "watery/bloody discharge", "leg swelling"], "Malignant neoplasm of cervix uteri", "C53"],
    ["Developed nations", ["obesity", "estrogen therapy", "genetics"], "Neoplastic", ["abnormal uterine bleeding", "postmenopausal bleeding", "pelvic pain", "abdominal bloating", "pain during intercourse", "unexplained weight loss"], "Malignant neoplasm of corpus uteri", "C54"],
    ["Worldwide", ["obesity", "genetics", "estrogen"], "Neoplastic", ["abnormal bleeding", "pelvic pain", "abdominal mass", "frequent urination", "bloating", "painful intercourse"], "Malignant neoplasm of uterus, part unspecified", "C55"],
    ["Worldwide", ["genetics", "age", "obesity"], "Neoplastic", ["abdominal bloating", "pelvic pain", "feeling full quickly", "frequent urination", "fatigue", "unexplained weight loss"], "Malignant neoplasm of ovary", "C56"],
    ["Worldwide", ["genetics", "age", "HPV infection"], "Neoplastic", ["pelvic pain", "abdominal swelling", "abnormal bleeding", "vaginal discharge", "urinary symptoms", "bowel symptoms"], "Malignant neoplasm of other female genital organs", "C57"],
    ["Worldwide", ["age", "previous molar pregnancy", "genetics"], "Neoplastic", ["abnormal vaginal bleeding", "high hCG levels", "severe nausea", "vomiting", "pelvic pressure", "uterine enlargement"], "Malignant neoplasm of placenta", "C58"],

    # C60-C63: Malignant neoplasms of male genital organs
    ["Worldwide", ["HPV infection", "smoking", "phimosis"], "Neoplastic", ["penile lump", "sore on penis", "bleeding from penis", "foul-smelling discharge", "skin thickening", "groin lump"], "Malignant neoplasm of penis", "C60"],
    ["Developed nations", ["age", "genetics", "African ancestry"], "Neoplastic", ["frequent urination", "weak urine stream", "nocturia", "blood in urine", "erectile dysfunction", "bone pain"], "Malignant neoplasm of prostate", "C61"],
    ["Developed nations", ["cryptorchidism", "genetics", "age"], "Neoplastic", ["painless testicular lump", "scrotal swelling", "scrotal heaviness", "dull ache in groin", "back pain", "breast tenderness"], "Malignant neoplasm of testis", "C62"],
    ["Worldwide", ["cryptorchidism", "genetics", "mumps"], "Neoplastic", ["scrotal mass", "groin pain", "lower abdominal pain", "blood in semen", "urethral discharge", "swelling"], "Malignant neoplasm of other male genital organs", "C63"],

    # C64-C68: Malignant neoplasms of urinary tract
    ["Worldwide", ["smoking", "obesity", "genetics"], "Neoplastic", ["blood in urine", "flank pain", "abdominal mass", "unexplained weight loss", "fatigue", "fever"], "Malignant neoplasm of kidney", "C64"],
    ["Worldwide", ["smoking", "Aristolochic acid", "genetics"], "Neoplastic", ["blood in urine", "flank pain", "frequent urination", "painful urination", "urinary tract infections", "fatigue"], "Malignant neoplasm of renal pelvis", "C65"],
    ["Worldwide", ["smoking", "Aristolochic acid", "genetics"], "Neoplastic", ["blood in urine", "flank pain", "back pain", "change in urination", "fatigue", "unexplained weight loss"], "Malignant neoplasm of ureter", "C66"],
    ["Worldwide", ["smoking", "chemical exposure", "chronic infections"], "Neoplastic", ["blood in urine", "frequent urination", "painful urination", "urgency to urinate", "pelvic pain", "back pain"], "Malignant neoplasm of bladder", "C67"],
    ["Worldwide", ["smoking", "chronic infections", "genetics"], "Neoplastic", ["blood in urine", "painful urination", "frequent urination", "abdominal pain", "pelvic mass", "difficulty urinating"], "Malignant neoplasm of other urinary organs", "C68"],

    # C69-C72: Malignant neoplasms of eye, brain and other parts of central nervous system
    ["Worldwide", ["UV radiation", "genetics", "fair skin"], "Neoplastic", ["vision changes", "dark spot on iris", "flashing lights", "floaters", "eye bulge", "eye pain"], "Malignant neoplasm of eye and adnexa", "C69"],
    ["Worldwide", ["radiation", "genetics", "age"], "Neoplastic", ["headaches", "seizures", "vision problems", "hearing loss", "weakness in limbs", "cognitive changes"], "Malignant neoplasm of meninges", "C70"],
    ["Worldwide", ["radiation", "genetics", "chemical exposure"], "Neoplastic", ["headaches", "seizures", "nausea", "vomiting", "personality changes", "weakness/numbness"], "Malignant neoplasm of brain", "C71"],
    ["Worldwide", ["radiation", "genetics", "neurofibromatosis"], "Neoplastic", ["back pain", "limb weakness", "loss of sensation", "bowel/bladder dysfunction", "paralysis", "muscle spasms"], "Malignant neoplasm of spinal cord and other CNS", "C72"],

    # C73-C75: Malignant neoplasms of thyroid and other endocrine glands
    ["Worldwide", ["radiation", "genetics", "female gender"], "Neoplastic", ["neck lump", "hoarseness", "difficulty swallowing", "neck pain", "swollen lymph nodes", "cough"], "Malignant neoplasm of thyroid gland", "C73"],
    ["Worldwide", ["genetics", "smoking", "radiation"], "Neoplastic", ["high blood pressure", "weight gain", "weakness", "abdominal pain", "anxiety", "excessive sweating"], "Malignant neoplasm of adrenal gland", "C74"],
    ["Worldwide", ["genetics", "radiation", "MEN1 syndrome"], "Neoplastic", ["hormone imbalance", "headaches", "vision problems", "weight changes", "fatigue", "dizziness"], "Malignant neoplasm of other endocrine glands", "C75"],

    # C76-C80: Malignant neoplasms of ill-defined, other secondary and unspecified sites
    ["Worldwide", ["genetics", "radiation", "unknown"], "Neoplastic", ["pain", "lump", "fatigue", "unexplained weight loss", "fever", "variable by site"], "Malignant neoplasm of other and ill-defined sites", "C76"],
    ["Worldwide", ["primary cancer", "unknown", "unknown"], "Neoplastic", ["swollen lymph nodes", "pain", "fever", "night sweats", "unexplained weight loss", "fatigue"], "Secondary malignant neoplasm of lymph nodes", "C77"],
    ["Worldwide", ["primary cancer", "unknown", "unknown"], "Neoplastic", ["cough", "shortness of breath", "jaundice", "abdominal pain", "difficulty swallowing", "unexplained weight loss"], "Secondary malignant neoplasm of respiratory/digestive organs", "C78"],
    ["Worldwide", ["primary cancer", "unknown", "unknown"], "Neoplastic", ["bone pain", "headaches", "seizures", "skin lesions", "abdominal pain", "unexplained weight loss"], "Secondary malignant neoplasm of other and unspecified sites", "C79"],
    ["Worldwide", ["unknown", "unknown", "unknown"], "Neoplastic", ["unexplained weight loss", "fatigue", "pain", "fever", "loss of appetite", "site-specific symptoms"], "Malignant neoplasm, unspecified site (CUP)", "C80"],

    # C81-C96: Malignant neoplasms of lymphoid, hematopoietic and related tissue
    ["Developed nations", ["EBV infection", "genetics", "immunosuppression"], "Neoplastic", ["painless swollen lymph nodes", "fever", "night sweats", "unexplained weight loss", "itching", "fatigue"], "Hodgkin lymphoma", "C81"],
    ["Worldwide", ["genetics", "chemical exposure", "autoimmune disease"], "Neoplastic", ["swollen lymph nodes", "fatigue", "fever", "night sweats", "unexplained weight loss", "abdominal swelling"], "Follicular lymphoma", "C82"],
    ["Worldwide", ["genetics", "chemical exposure", "immunosuppression"], "Neoplastic", ["swollen lymph nodes", "fever", "night sweats", "unexplained weight loss", "fatigue", "abdominal pain"], "Diffuse non-Hodgkin lymphoma", "C83"],
    ["East Asia", ["HTLV-1", "EBV infection", "genetics"], "Neoplastic", ["swollen lymph nodes", "skin rash", "fever", "unexplained weight loss", "fatigue", "bone lesions"], "Mature T/NK-cell lymphomas", "C84"],
    ["Worldwide", ["genetics", "immunosuppression", "EBV infection"], "Neoplastic", ["swollen lymph nodes", "fever", "night sweats", "skin lesions", "fatigue", "unexplained weight loss"], "Other specified T/NK-cell lymphomas", "C85"],
    ["Worldwide", ["genetics", "HTLV-1", "autoimmune disease"], "Neoplastic", ["skin rash/lesions", "swollen lymph nodes", "fever", "night sweats", "unexplained weight loss", "itching"], "Other specified types of T/NK-cell lymphoma", "C86"],
    ["Worldwide", ["Hepatitis C", "HIV/AIDS", "genetics"], "Neoplastic", ["fatigue", "weakness", "fever", "swollen lymph nodes", "easy bleeding", "unexplained weight loss"], "Malignant immunoproliferative diseases", "C88"],
    ["Worldwide", ["genetics", "radiation", "chemical exposure"], "Neoplastic", ["bone pain", "fatigue", "recurrent infections", "kidney problems", "anemia", "easy bruising"], "Multiple myeloma", "C90"],
    ["Developed nations", ["genetics", "chemical exposure", "radiation"], "Neoplastic", ["fatigue", "recurrent infections", "easy bruising", "swollen lymph nodes", "fever", "unexplained weight loss"], "Lymphoid leukemia", "C91"],
    ["Worldwide", ["genetics", "chemical exposure", "radiation"], "Neoplastic", ["fatigue", "fever", "easy bruising", "recurrent infections", "shortness of breath", "unexplained weight loss"], "Myeloid leukemia", "C92"],
    ["Worldwide", ["genetics", "chemical exposure", "radiation"], "Neoplastic", ["fatigue", "fever", "gum swelling", "easy bruising", "recurrent infections", "skin rash"], "Monocytic leukemia", "C93"],
    ["Worldwide", ["genetics", "chemical exposure", "radiation"], "Neoplastic", ["fatigue", "fever", "easy bruising", "recurrent infections", "weakness", "shortness of breath"], "Other leukemias of specified cell type", "C94"],
    ["Worldwide", ["genetics", "chemical exposure", "radiation"], "Neoplastic", ["fatigue", "fever", "easy bruising", "recurrent infections", "unexplained weight loss", "bone pain"], "Leukemia of unspecified cell type", "C95"],
    ["Worldwide", ["genetics", "radiation", "chemical exposure"], "Neoplastic", ["fever", "fatigue", "recurrent infections", "easy bruising", "swollen lymph nodes", "unexplained weight loss"], "Other specified malignant neoplasms of lymphoid tissue", "C96"]
]
