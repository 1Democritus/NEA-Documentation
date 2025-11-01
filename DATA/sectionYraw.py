# ICD-10 Y00-Y99: External causes of morbidity
# This data is structured for AI training as requested.
# The features have been adapted from "disease" features to "external cause" features
# to accurately reflect the nature of the Y-code block.

icd_y_code_data = [
    # Y00-Y09: Assault
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Blunt force", "Weapon"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Contusion", "Fracture", "Laceration", "Head trauma", "Internal bleeding", "Pain"],
        "Label": "Assault by blunt object",
        "ICD_Code": "Y00"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Push", "Fall"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Fracture", "Head trauma", "Sprain", "Contusion", "Internal injury", "Death"],
        "Label": "Assault by pushing from high place",
        "ICD_Code": "Y01"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Push", "Surface-level"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Contusion", "Sprain", "Fracture", "Laceration", "Minor head injury", "Abrasion"],
        "Label": "Assault by pushing or placing victim before moving object",
        "ICD_Code": "Y02"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Vehicle", "Impact"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Polytrauma", "Fracture", "Head trauma", "Internal bleeding", "Crush injury", "Death"],
        "Label": "Assault by crashing of motor vehicle",
        "ICD_Code": "Y03"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Physical", "No weapon"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Contusion", "Abrasion", "Laceration", "Minor fracture", "Sprain", "Black eye"],
        "Label": "Assault by bodily force",
        "ICD_Code": "Y04"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Sexual", "Physical force"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Genital trauma", "Laceration", "Contusion", "Psychological trauma", "STD transmission", "Pregnancy"],
        "Label": "Assault by sexual intercourse",
        "ICD_Code": "Y05"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Neglect", "Abandonment"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Malnutrition", "Dehydration", "Hypothermia", "Developmental delay", "Psychological trauma", "Infection"],
        "Label": "Neglect and abandonment",
        "ICD_Code": "Y06"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Maltreatment", "Various methods"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Varies (see other codes)", "Psychological trauma", "Chronic pain", "Physical injury", "Malnutrition", "Death"],
        "Label": "Other maltreatment",
        "ICD_Code": "Y07"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Specified", "Not listed"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Varies", "Injury", "Trauma", "Pain", "Laceration", "Contusion"],
        "Label": "Assault by other specified means",
        "ICD_Code": "Y08"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Assault", "Unspecified", "Unknown"],
        "Cause_Type": "Assault",
        "Associated_Outcomes": ["Varies", "Injury", "Trauma", "Pain", "Laceration", "Contusion"],
        "Label": "Assault by unspecified means",
        "ICD_Code": "Y09"
    },

    # Y10-Y19: Intentional self-harm
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Nausea", "Vomiting", "Altered mental status", "Organ failure", "Coma", "Death"],
        "Label": "Poisoning by nonopioid analgesics, self-harm",
        "ICD_Code": "Y10"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Sedation", "Respiratory depression", "Altered mental status", "Seizure", "Coma", "Death"],
        "Label": "Poisoning by antiepileptic/sedative-hypnotic drugs, self-harm",
        "ICD_Code": "Y11"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Respiratory depression", "Miosis (pinpoint pupils)", "Sedation", "Hypotension", "Coma", "Death"],
        "Label": "Poisoning by narcotics and psychodysleptics, self-harm",
        "ICD_Code": "Y12"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Arrhythmia", "Hypotension", "Altered mental status", "Seizure", "Varies by drug", "Death"],
        "Label": "Poisoning by other psychotropic drugs, self-harm",
        "ICD_Code": "Y13"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Arrhythmia", "Hypotension/Hypertension", "Varies by drug", "Altered mental status", "Organ failure", "Death"],
        "Label": "Poisoning by other autonomic nervous system drugs, self-harm",
        "ICD_Code": "Y14"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Varies by drug", "Altered mental status", "Nausea", "Vomiting", "Organ failure", "Death"],
        "Label": "Poisoning by other and unspecified drugs, self-harm",
        "ICD_Code": "Y15"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Altered mental status", "Nausea", "Vomiting", "Respiratory depression", "Metabolic acidosis", "Death"],
        "Label": "Poisoning by alcohol, self-harm",
        "ICD_Code": "Y16"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Overdose"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Caustic injury", "Nausea", "Vomiting", "Metabolic acidosis", "Organ failure", "Death"],
        "Label": "Poisoning by organic solvents/halogenated hydrocarbons, self-harm",
        "ICD_Code": "Y17"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Inhalation", "Gas"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Hypoxia", "Headache", "Altered mental status", "Nausea", "Coma", "Death"],
        "Label": "Poisoning by other gases and vapors, self-harm",
        "ICD_Code": "Y18"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Self-harm", "Ingestion", "Exposure"],
        "Cause_Type": "Intentional Self-Harm",
        "Associated_Outcomes": ["Varies by substance", "Nausea", "Vomiting", "Chemical burn", "Organ failure", "Death"],
        "Label": "Poisoning by other and unspecified chemicals, self-harm",
        "ICD_Code": "Y19"
    },

    # Y20-Y34: Event of undetermined intent
    # Note: These are often parallel to Y10-Y19 but with "undetermined intent"
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Hanging", "Strangulation", "Suffocation"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Hypoxia", "Neck injury", "Cerebral edema", "Loss of consciousness", "Petechiae", "Death"],
        "Label": "Hanging, strangulation and suffocation, undetermined intent",
        "ICD_Code": "Y20"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Firearm", "Discharge", "Gunshot"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Gunshot wound", "Hemorrhage", "Penetrating trauma", "Organ damage", "Fracture", "Death"],
        "Label": "Handgun discharge, undetermined intent",
        "ICD_Code": "Y22"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Firearm", "Discharge", "Gunshot"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Gunshot wound", "Hemorrhage", "Penetrating trauma", "Organ damage", "Fracture", "Death"],
        "Label": "Rifle, shotgun and larger firearm discharge, undetermined intent",
        "ICD_Code": "Y23"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Firearm", "Discharge", "Gunshot"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Gunshot wound", "Hemorrhage", "Penetrating trauma", "Organ damage", "Fracture", "Death"],
        "Label": "Other and unspecified firearm discharge, undetermined intent",
        "ICD_Code": "Y24"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Explosive", "Detonation", "Blast"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Blast injury", "Burn", "Fracture", "Tympanic membrane rupture", "Penetrating trauma", "Death"],
        "Label": "Contact with explosive material, undetermined intent",
        "ICD_Code": "Y25"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Smoke", "Fire", "Inhalation"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Burn", "Smoke inhalation", "Hypoxia", "Respiratory distress", "Carbon monoxide poisoning", "Death"],
        "Label": "Exposure to smoke, fire and flames, undetermined intent",
        "ICD_Code": "Y26"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Heat", "Vapor", "Liquid"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Burn (scald)", "Blistering", "Erythema", "Pain", "Infection", "Shock"],
        "Label": "Contact with hot objects, undetermined intent",
        "ICD_Code": "Y27"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Cutting", "Piercing", "Tool"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Laceration", "Hemorrhage", "Penetrating trauma", "Organ damage", "Nerve damage", "Infection"],
        "Label": "Contact with sharp object, undetermined intent",
        "ICD_Code": "Y28"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Impact", "Blunt force", "Object"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Contusion", "Fracture", "Laceration", "Head trauma", "Internal bleeding", "Pain"],
        "Label": "Contact with blunt object, undetermined intent",
        "ICD_Code": "Y29"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Fall", "Push", "Jump"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Fracture", "Head trauma", "Sprain", "Contusion", "Internal injury", "Death"],
        "Label": "Falling, jumping or pushed from a high place, undetermined intent",
        "ICD_Code": "Y30"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Fall", "Slip", "Trip"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Fracture", "Sprain", "Contusion", "Laceration", "Head injury", "Abrasion"],
        "Label": "Falling, lying or running before or into moving object, undetermined intent",
        "ICD_Code": "Y31"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Vehicle", "Impact", "Crash"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Polytrauma", "Fracture", "Head trauma", "Internal bleeding", "Crush injury", "Death"],
        "Label": "Crashing of motor vehicle, undetermined intent",
        "ICD_Code": "Y32"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Specified", "Not listed", "Various"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Varies", "Injury", "Trauma", "Pain", "Laceration", "Contusion"],
        "Label": "Other specified events, undetermined intent",
        "ICD_Code": "Y33"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Unspecified", "Unknown", "Various"],
        "Cause_Type": "Undetermined Intent",
        "Associated_Outcomes": ["Varies", "Injury", "Trauma", "Pain", "Laceration", "Contusion"],
        "Label": "Unspecified event, undetermined intent",
        "ICD_Code": "Y34"
    },

    # Y35-Y38: Legal intervention, operations of war...
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Legal intervention", "Firearm", "Law enforcement"],
        "Cause_Type": "Legal Intervention/War",
        "Associated_Outcomes": ["Gunshot wound", "Hemorrhage", "Penetrating trauma", "Organ damage", "Fracture", "Death"],
        "Label": "Legal intervention",
        "ICD_Code": "Y35"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["War", "Military", "Various weapons"],
        "Cause_Type": "Legal Intervention/War",
        "Associated_Outcomes": ["Polytrauma", "Burn", "Blast injury", "Gunshot wound", "Fracture", "Death"],
        "Label": "Operations of war",
        "ICD_Code": "Y36"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Military", "Non-hostile", "Accident"],
        "Cause_Type": "Legal Intervention/War",
        "Associated_Outcomes": ["Varies", "Injury", "Fracture", "Trauma", "Burn", "Death"],
        "Label": "Military operations",
        "ICD_Code": "Y37"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Terrorism", "Various", "Intentional"],
        "Cause_Type": "Legal Intervention/War",
        "Associated_Outcomes": ["Varies", "Blast injury", "Burn", "Gunshot wound", "Polytrauma", "Death"],
        "Label": "Terrorism",
        "ICD_Code": "Y38"
    },

    # Y40-Y59: Drugs, medicaments and biological substances causing adverse effects in therapeutic use
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Antibiotic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Rash", "Anaphylaxis", "Diarrhea", "Nausea", "Urticaria", "Fever"],
        "Label": "Adverse effect of penicillins",
        "ICD_Code": "Y40"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Antibiotic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Ototoxicity", "Nephrotoxicity", "Rash", "Nausea", "Allergic reaction", "Vomiting"],
        "Label": "Adverse effect of other systemic antibiotics",
        "ICD_Code": "Y41"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Anti-infective"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Rash", "Nausea", "Hepatotoxicity", "Neuropathy", "Allergic reaction", "Vomiting"],
        "Label": "Adverse effect of other systemic anti-infectives and antiparasitics",
        "ICD_Code": "Y42"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Hormone"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Weight gain", "Mood change", "Thrombosis", "Hirsutism", "Electrolyte imbalance", "Hyperglycemia"],
        "Label": "Adverse effect of hormones and their synthetic substitutes and antagonists",
        "ICD_Code": "Y43"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Analgesic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["GI bleeding", "Rash", "Nausea", "Nephrotoxicity", "Allergic reaction", "Tinnitus"],
        "Label": "Adverse effect of nonopioid analgesics",
        "ICD_Code": "Y44"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Sedative"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Drowsiness", "Dizziness", "Cognitive impairment", "Ataxia", "Respiratory depression", "Dependence"],
        "Label": "Adverse effect of antiepileptics and sedative-hypnotics",
        "ICD_Code": "Y45"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Psychotropic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Sedation", "Extrapyramidal symptoms", "Weight gain", "Sexual dysfunction", "Serotonin syndrome", "Dizziness"],
        "Label": "Adverse effect of psychotropic drugs",
        "ICD_Code": "Y46"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Anesthetic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Hypotension", "Nausea", "Vomiting", "Respiratory depression", "Allergic reaction", "Malignant hyperthermia"],
        "Label": "Adverse effect of anesthetics and therapeutic gases",
        "ICD_Code": "Y47"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Opioid"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Constipation", "Nausea", "Sedation", "Respiratory depression", "Pruritus (itching)", "Dependence"],
        "Label": "Adverse effect of narcotics and psychodysleptics [hallucinogens]",
        "ICD_Code": "Y48"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Autonomic"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Dry mouth", "Blurred vision", "Urinary retention", "Tachycardia", "Hypotension", "Dizziness"],
        "Label": "Adverse effect of drugs affecting autonomic nervous system",
        "ICD_Code": "Y49"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Cardiovascular"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Hypotension", "Bradycardia", "Cough", "Dizziness", "Electrolyte imbalance", "Arrhythmia"],
        "Label": "Adverse effect of cardiovascular drugs",
        "ICD_Code": "Y50"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Cardiovascular"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Hypotension", "Bradycardia", "Cough", "Dizziness", "Electrolyte imbalance", "Arrhythmia"],
        "Label": "Adverse effect of cardiovascular drugs (duplicate, distinct code)",
        "ICD_Code": "Y51"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Gastrointestinal"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Diarrhea", "Constipation", "Nausea", "Vomiting", "Abdominal pain", "Headache"],
        "Label": "Adverse effect of gastrointestinal drugs",
        "ICD_Code": "Y53"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Various"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Varies", "Rash", "Nausea", "Headache", "Dizziness", "Vomiting"],
        "Label": "Adverse effect of water-balance, mineral and uric acid metabolism drugs",
        "ICD_Code": "Y54"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Various"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Varies", "Rash", "Nausea", "Headache", "Dizziness", "Vomiting"],
        "Label": "Adverse effect of other and unspecified drugs and medicaments",
        "ICD_Code": "Y55"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Topical"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Contact dermatitis", "Rash", "Pruritus (itching)", "Dryness", "Erythema", "Burning sensation"],
        "Label": "Adverse effect of topical agents",
        "ICD_Code": "Y56"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Bacterial vaccine"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Fever", "Myalgia", "Headache", "Local injection site reaction", "Fatigue", "Allergic reaction"],
        "Label": "Adverse effect of bacterial vaccines",
        "ICD_Code": "Y58"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Vaccine/Biological"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Fever", "Myalgia", "Headache", "Local injection site reaction", "Fatigue", "Allergic reaction"],
        "Label": "Adverse effect of other and unspecified vaccines and biological substances",
        "ICD_Code": "Y59"
    },

    # Y60-Y69: Misadventures to patients during surgical and medical care
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Surgical error", "Unintentional cut"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Hemorrhage", "Infection", "Nerve damage", "Organ damage", "Pain", "Delayed healing"],
        "Label": "Unintentional cut, puncture, perforation or hemorrhage during surgical and medical care",
        "ICD_Code": "Y60"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Surgical error", "Retained object"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Infection", "Pain", "Abscess", "Obstruction", "Fistula", "Need for reoperation"],
        "Label": "Foreign object left in body during surgical and medical care",
        "ICD_Code": "Y61"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Surgical error", "Asepsis failure"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Surgical site infection", "Sepsis", "Abscess", "Delayed healing", "Fever", "Pain"],
        "Label": "Failure of sterile precautions during surgical and medical care",
        "ICD_Code": "Y62"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Error", "Dosing/Administration"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Adverse drug reaction", "Overdose", "Underdose", "Toxicity", "Ineffective treatment", "Death"],
        "Label": "Failure in dosage or administration of drug or biological substance",
        "ICD_Code": "Y63"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Transfusion", "Contamination"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Infection (e.g., Hepatitis, HIV)", "Sepsis", "Fever", "Shock", "Organ failure", "Death"],
        "Label": "Contaminated medical or biological substance",
        "ICD_Code": "Y64"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Error", "Various"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Varies", "Injury", "Adverse reaction", "Ineffective treatment", "Pain", "Complication"],
        "Label": "Other misadventures during surgical and medical care",
        "ICD_Code": "Y65"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Procedure", "Nonadministration"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Untreated condition", "Progression of disease", "Worsening symptoms", "Complication", "Pain", "Death"],
        "Label": "Nonadministration of surgical and medical care",
        "ICD_Code": "Y66"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Medical misadventure", "Error", "Unspecified"],
        "Cause_Type": "Medical Misadventure",
        "Associated_Outcomes": ["Varies", "Injury", "Complication", "Adverse event", "Pain", "Ineffective treatment"],
        "Label": "Unspecified misadventures during surgical and medical care",
        "ICD_Code": "Y69"
    },

    # Y70-Y82: Medical devices associated with adverse incidents...
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Anesthesiology"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Hypoxia", "Barotrauma", "Anesthetic complication", "Arrhythmia", "Hypotension", "Aspiration"],
        "Label": "Anesthesiology devices associated with adverse incidents",
        "ICD_Code": "Y70"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Cardiovascular"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Thrombosis", "Hemorrhage", "Arrhythmia", "Device failure", "Infection", "Perforation"],
        "Label": "Cardiovascular devices associated with adverse incidents",
        "ICD_Code": "Y71"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "ENT"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Perforation", "Bleeding", "Infection", "Hearing loss", "Device migration", "Pain"],
        "Label": "Otorhinolaryngological devices associated with adverse incidents",
        "ICD_Code": "Y72"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Gastroenterology"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Perforation", "Bleeding", "Infection", "Obstruction", "Device migration", "Pain"],
        "Label": "Gastroenterology and urology devices associated with adverse incidents",
        "ICD_Code": "Y73"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Hospital furniture"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Fall", "Fracture", "Contusion", "Entrapment", "Laceration", "Pain"],
        "Label": "General hospital and personal use devices associated with adverse incidents",
        "ICD_Code": "Y74"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Neurological"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Device failure", "Infection", "Nerve damage", "CSF leak", "Over/under stimulation", "Pain"],
        "Label": "Neurological devices associated with adverse incidents",
        "ICD_Code": "Y75"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Obstetric/Gynecological"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Perforation", "Bleeding", "Infection", "Device migration", "Pain", "Infertility"],
        "Label": "Obstetric and gynecological devices associated with adverse incidents",
        "ICD_Code": "Y76"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Ophthalmic"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Vision loss", "Infection", "Corneal abrasion", "Increased intraocular pressure", "Device dislocation", "Pain"],
        "Label": "Ophthalmic devices associated with adverse incidents",
        "ICD_Code": "Y77"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Radiological"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Radiation burn", "Overexposure", "Device failure", "Contrast reaction", "Inaccurate imaging", "Delayed diagnosis"],
        "Label": "Radiological devices associated with adverse incidents",
        "ICD_Code": "Y78"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Orthopedic"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_outcomes": ["Prosthesis loosening", "Infection", "Fracture", "Device breakage", "Nerve damage", "Chronic pain"],
        "Label": "Orthopedic devices associated with adverse incidents",
        "ICD_Code": "Y79"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Physical medicine"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Burn", "Muscle strain", "Pain", "Device failure", "Skin irritation", "Fall"],
        "Label": "Physical medicine devices associated with adverse incidents",
        "ICD_Code": "Y80"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "General/Plastic surgery"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Infection", "Bleeding", "Device failure", "Poor cosmetic result", "Suture dehiscence", "Pain"],
        "Label": "General- and plastic-surgery devices associated with adverse incidents",
        "ICD_Code": "Y81"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse incident", "Medical device", "Other/Unspecified"],
        "Cause_Type": "Adverse Medical Device Incident",
        "Associated_Outcomes": ["Varies", "Infection", "Device failure", "Pain", "Bleeding", "Injury"],
        "Label": "Other and unspecified medical devices associated with adverse incidents",
        "ICD_Code": "Y82"
    },

    # Y83-Y84: Surgical and other medical procedures as the cause of abnormal reaction...
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse procedure outcome", "Surgery", "No misadventure"],
        "Cause_Type": "Adverse Procedure Outcome (No Misadventure)",
        "Associated_Outcomes": ["Postoperative infection", "Hemorrhage", "Chronic pain", "Scarring", "Functional impairment", "Anesthetic reaction"],
        "Label": "Surgical operation and other surgical procedures as the cause of abnormal reaction",
        "ICD_Code": "Y83"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Adverse procedure outcome", "Medical procedure", "No misadventure"],
        "Cause_Type": "Adverse Procedure Outcome (No Misadventure)",
        "Associated_Outcomes": ["Adverse reaction", "Complication", "Pain", "Infection", "Bleeding", "Functional impairment"],
        "Label": "Other medical procedures as the cause of abnormal reaction",
        "ICD_Code": "Y84"
    },

    # Y85-Y89: Sequelae of external causes... (Late effects)
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Sequela", "Late effect", "Transport accident"],
        "Cause_Type": "Sequelae of External Cause",
        "Associated_Outcomes": ["Chronic pain", "Disability", "Cognitive impairment", "Scarring", "Arthritis", "Neuropathy"],
        "Label": "Sequelae of transport accident",
        "ICD_Code": "Y85"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Sequela", "Late effect", "Other accident"],
        "Cause_Type": "Sequelae of External Cause",
        "Associated_Outcomes": ["Chronic pain", "Disability", "Cognitive impairment", "Scarring", "Arthritis", "Neuropathy"],
        "Label": "Sequelae of other accidents",
        "ICD_Code": "Y86"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Sequela", "Late effect", "Intentional harm"],
        "Cause_Type": "Sequelae of External Cause",
        "Associated_Outcomes": ["Chronic pain", "PTSD", "Disability", "Depression", "Anxiety", "Scarring"],
        "Label": "Sequelae of intentional self-harm, assault and events of undetermined intent",
        "ICD_Code": "Y87"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Sequela", "Late effect", "Medical/Surgical care"],
        "Cause_Type": "Sequelae of External Cause",
        "Associated_Outcomes": ["Chronic pain", "Adhesion", "Disability", "Organ dysfunction", "Scarring", "Infection"],
        "Label": "Sequelae of surgical and medical care as external cause",
        "ICD_Code": "Y88"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Sequela", "Late effect", "Other external cause"],
        "Cause_Type": "Sequelae of External Cause",
        "Associated_Outcomes": ["Chronic pain", "Disability", "Cognitive impairment", "Scarring", "PTSD", "Varies"],
        "Label": "Sequelae of other external causes",
        "ICD_Code": "Y89"
    },

    # Y90-Y98: Supplementary factors...
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Alcohol", "Blood test"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Intoxication", "Impaired judgment", "Ataxia", "Altered mental status", "Injury (see other codes)", "Accident (see other codes)"],
        "Label": "Evidence of alcohol involvement determined by blood alcohol level",
        "ICD_Code": "Y90"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Alcohol", "Clinical observation"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Intoxication", "Impaired judgment", "Slurred speech", "Ataxia", "Altered mental status", "Injury (see other codes)"],
        "Label": "Evidence of alcohol involvement determined by level of intoxication",
        "ICD_Code": "Y91"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Acquired", "Hospital"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Infection", "Pneumonia", "UTI", "Surgical site infection", "C. difficile", "Bacteremia"],
        "Label": "Nosocomial condition (Hospital-acquired)",
        "ICD_Code": "Y95"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Acquired", "Workplace"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Repetitive strain injury", "Laceration", "Fracture", "Exposure", "Burn", "Hearing loss"],
        "Label": "Work-related condition",
        "ICD_Code": "Y96"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Exposure", "Environment"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Asthma exacerbation", "Lead poisoning", "Respiratory irritation", "Skin rash", "Cancer (long-term)", "Allergic reaction"],
        "Label": "Environmental-pollution-related condition",
        "ICD_Code": "Y97"
    },
    {
        "Geography": "Global",
        "Transmission_Mechanism": ["Supplementary factor", "Behavior", "Lifestyle"],
        "Cause_Type": "Supplementary Factor",
        "Associated_Outcomes": ["Obesity", "Type 2 Diabetes", "Hypertension", "Heart disease", "Lung cancer (smoking)", "Cirrhosis (alcohol)"],
        "Label": "Lifestyle-related condition",
        "ICD_Code": "Y98"
    }
]
