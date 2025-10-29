# This file contains a list of dictionaries with data for ICD-10 codes T00-T98.
# The codes T72, T76, T77, T89, and T99 are omitted as they are not valid, billable codes.
#
# The data structure is as follows:
# {
#     "feature_1_category": (Type of injury/condition),
#     "feature_2_common_causes": (List of 3 common external causes),
#     "feature_3_primary_system": (Primary body system affected),
#     "feature_4_common_symptoms_signs": (List of 6 common symptoms or signs),
#     "label_condition_name": (The descriptive name of the ICD-10 code),
#     "icd_code": (The ICD-10 code)
# }

icd_t_code_data = [
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Blunt force", "Fall", "Abrasion"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Scrapes", "Bruising", "Swelling", "Mild pain", "Redness", "Contusion"],
        "label_condition_name": "Superficial injuries involving multiple body regions",
        "icd_code": "T00"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Sharp object", "Laceration", "Puncture"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Bleeding", "Break in skin", "Pain", "Risk of infection", "Visible tissue", "Tissue damage"],
        "label_condition_name": "Open wounds involving multiple body regions",
        "icd_code": "T01"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Vehicle accident", "Severe fall", "Crushing force"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Severe pain", "Deformity", "Loss of function", "Swelling", "Bruising", "Crepitus"],
        "label_condition_name": "Fractures involving multiple body regions",
        "icd_code": "T02"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Sudden twisting", "Sports injury", "Overextension"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Joint pain", "Swelling", "Instability", "Limited range of motion", "Bruising", "Joint deformity"],
        "label_condition_name": "Dislocations, sprains and strains involving multiple body regions",
        "icd_code": "T03"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Heavy machinery", "Building collapse", "Compression"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Severe pain", "Massive swelling", "Compartment syndrome", "Tissue necrosis", "Nerve damage", "Rhabdomyolysis"],
        "label_condition_name": "Crushing injuries involving multiple body regions",
        "icd_code": "T04"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Machinery accident", "Severe trauma", "Explosion"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Limb loss", "Severe bleeding", "Shock", "Phantom limb pain", "Stump wound", "Psychological trauma"],
        "label_condition_name": "Traumatic amputations involving multiple body regions",
        "icd_code": "T05"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Vehicle accident", "Blast injury", "Complex trauma"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Internal bleeding", "Nerve injury", "Vessel damage", "Tendon laceration", "Organ damage", "Varied pain"],
        "label_condition_name": "Other injuries involving multiple body regions",
        "icd_code": "T06"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Major trauma", "Disaster event", "Unspecified accident"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Multiple wounds", "Unconsciousness", "Shock", "Systemic failure", "Respiratory distress", "Severe pain"],
        "label_condition_name": "Unspecified multiple injuries",
        "icd_code": "T07"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Fall from height", "Vehicle accident", "Osteoporosis"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Back pain", "Numbness", "Tingling", "Weakness in limbs", "Paralysis", "Loss of bladder control"],
        "label_condition_name": "Fracture of spine, level unspecified",
        "icd_code": "T08"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Blunt force", "Twisting injury", "Whiplash"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Back pain", "Neck pain", "Stiffness", "Muscle spasm", "Radiating pain", "Limited motion"],
        "label_condition_name": "Other injuries of spine and trunk, level unspecified",
        "icd_code": "T09"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Fall on outstretched hand", "Direct blow", "Sports injury"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Arm pain", "Swelling", "Deformity", "Inability to move arm", "Bruising", "Numbness in hand"],
        "label_condition_name": "Fracture of upper limb, level unspecified",
        "icd_code": "T10"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Laceration", "Overuse", "Sprain"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Arm pain", "Weakness", "Swelling", "Bruising", "Nerve tingling", "Limited range of motion"],
        "label_condition_name": "Other injuries of upper limb, level unspecified",
        "icd_code": "T11"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Fall", "Vehicle accident", "Twisting force"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Leg pain", "Inability to bear weight", "Swelling", "Deformity", "Bruising", "Loss of function"],
        "label_condition_name": "Fracture of lower limb, level unspecified",
        "icd_code": "T12"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Sprain", "Strain", "Laceration"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Leg pain", "Swelling", "Instability", "Bruising", "Difficulty walking", "Stiffness"],
        "label_condition_name": "Other injuries of lower limb, level unspecified",
        "icd_code": "T13"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Accident", "Fall", "Unknown event"],
        "feature_3_primary_system": "Unspecified",
        "feature_4_common_symptoms_signs": ["Pain", "Swelling", "Bruising", "Laceration", "Functional loss", "Tenderness"],
        "label_condition_name": "Injury of unspecified body region",
        "icd_code": "T14"
    },
    {
        "feature_1_category": "Foreign Body",
        "feature_2_common_causes": ["Windblown debris", "Workplace hazard", "Rubbing eye"],
        "feature_3_primary_system": "Sensory",
        "feature_4_common_symptoms_signs": ["Eye pain", "Redness", "Watering", "Gritty sensation", "Blurred vision", "Light sensitivity"],
        "label_condition_name": "Foreign body on external eye",
        "icd_code": "T15"
    },
    {
        "feature_1_category": "Foreign Body",
        "feature_2_common_causes": ["Insect", "Cotton swab tip", "Bead"],
        "feature_3_primary_system": "Sensory",
        "feature_4_common_symptoms_signs": ["Ear pain", "Hearing loss", "Sensation of fullness", "Dizziness", "Ringing in ear", "Discharge"],
        "label_condition_name": "Foreign body in ear",
        "icd_code": "T16"
    },
    {
        "feature_1_category": "Foreign Body",
        "feature_2_common_causes": ["Inhaled food", "Small toy", "Inhaled object"],
        "feature_3_primary_system": "Respiratory",
        "feature_4_common_symptoms_signs": ["Choking", "Coughing", "Wheezing", "Difficulty breathing", "Gasping", "Cyanosis (bluish skin)"],
        "label_condition_name": "Foreign body in respiratory tract",
        "icd_code": "T17"
    },
    {
        "feature_1_category": "Foreign Body",
        "feature_2_common_causes": ["Swallowed object", "Food bolus", "Swallowed coin"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Difficulty swallowing", "Drooling", "Vomiting", "Abdominal pain", "Chest pain", "Sensation of object stuck"],
        "label_condition_name": "Foreign body in alimentary tract",
        "icd_code": "T18"
    },
    {
        "feature_1_category": "Foreign Body",
        "feature_2_common_causes": ["Inserted object", "Retained tampon", "Urinary stone"],
        "feature_3_primary_system": "Genitourinary",
        "feature_4_common_symptoms_signs": ["Pain", "Bleeding", "Urinary retention", "Foul discharge", "Frequent urination", "Discomfort"],
        "label_condition_name": "Foreign body in genitourinary tract",
        "icd_code": "T19"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Scald (hot liquid)", "Fire", "Chemical splash"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Pain", "Swelling", "Peeling skin", "Charred skin"],
        "label_condition_name": "Burn and corrosion of head, face, and neck",
        "icd_code": "T20"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Scald", "Fire", "Chemical exposure"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Pain", "Swelling", "Large area affected", "Shock"],
        "label_condition_name": "Burn and corrosion of trunk",
        "icd_code": "T21"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Scald", "Contact with hot object", "Fire"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Pain", "Swelling", "Peeling skin", "Loss of function"],
        "label_condition_name": "Burn and corrosion of shoulder and upper limb, except wrist and hand",
        "icd_code": "T22"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Touching hot surface", "Scald", "Chemical spill"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Severe pain", "Swelling", "Impaired dexterity", "Skin loss"],
        "label_condition_name": "Burn and corrosion of wrist and hand",
        "icd_code": "T23"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Scald", "Fire", "Chemical exposure"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Pain", "Swelling", "Difficulty walking", "Skin loss"],
        "label_condition_name": "Burn and corrosion of hip and lower limb, except ankle and foot",
        "icd_code": "T24"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Stepping on hot surface", "Scald", "Chemical spill"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Redness", "Blisters", "Pain", "Swelling", "Difficulty bearing weight", "Peeling skin"],
        "label_condition_name": "Burn and corrosion of ankle and foot",
        "icd_code": "T25"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Chemical splash", "UV radiation", "Hot ash"],
        "feature_3_primary_system": "Sensory",
        "feature_4_common_symptoms_signs": ["Severe eye pain", "Blurred vision", "Light sensitivity", "Redness", "Watering", "Blindness"],
        "label_condition_name": "Burn and corrosion confined to eye and adnexa",
        "icd_code": "T26"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Inhaling hot steam", "Inhaling smoke", "Inhaling chemical fumes"],
        "feature_3_primary_system": "Respiratory",
        "feature_4_common_symptoms_signs": ["Difficulty breathing", "Coughing", "Wheezing", "Hoarseness", "Soot in airway", "Facial burns"],
        "label_condition_name": "Burn and corrosion of respiratory tract",
        "icd_code": "T27"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Swallowing corrosive acid", "Swallowing corrosive alkali", "Swallowing hot liquid"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Severe chest pain", "Severe abdominal pain", "Vomiting blood", "Difficulty swallowing", "Drooling", "Shock"],
        "label_condition_name": "Burn and corrosion of other internal organs",
        "icd_code": "T28"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["House fire", "Explosion", "Large chemical spill"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Widespread burns", "Shock", "Hypothermia", "Dehydration", "High infection risk", "Respiratory distress"],
        "label_condition_name": "Burns and corrosions of multiple body regions",
        "icd_code": "T29"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Fire", "Scald", "Chemical exposure"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Pain", "Redness", "Blisters", "Swelling", "Unspecified location", "Skin damage"],
        "label_condition_name": "Burn and corrosion, body region unspecified",
        "icd_code": "T30"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Fire", "Scald", "Explosion"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Percentage TBSA", "Superficial burn", "Partial-thickness burn", "Full-thickness burn", "Shock", "Dehydration"],
        "label_condition_name": "Burns classified according to extent of body surface involved",
        "icd_code": "T31"
    },
    {
        "feature_1_category": "Burn",
        "feature_2_common_causes": ["Acid exposure", "Alkali exposure", "Chemical spill"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Chemical burn", "Tissue necrosis", "Severe pain", "Discoloration", "Percentage TBSA", "Deep tissue damage"],
        "label_condition_name": "Corrosions classified according to extent of body surface involved",
        "icd_code": "T32"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Cold exposure", "Wind chill", "Wet clothing"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Numbness", "Pale skin", "Tingling", "Redness", "Prickling sensation", "Intact skin"],
        "label_condition_name": "Superficial frostbite",
        "icd_code": "T33"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Prolonged cold exposure", "Extreme cold", "Contact with frozen metal"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Hard waxy skin", "White/blue skin", "Blisters (after rewarming)", "Blackened tissue", "Loss of sensation", "Tissue death"],
        "label_condition_name": "Frostbite with tissue necrosis",
        "icd_code": "T34"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Severe cold exposure", "Lost in cold", "Immersion in cold water"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Multiple numb areas", "Waxy skin", "Tissue necrosis", "Hypothermia", "Shivering (or absence)", "Confusion"],
        "label_condition_name": "Frostbite involving multiple body regions and unspecified frostbite",
        "icd_code": "T35"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Incorrect prescription", "Accidental ingestion"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Allergic reaction", "Organ damage", "Dizziness", "Varies by drug"],
        "label_condition_name": "Poisoning by systemic antibiotics",
        "icd_code": "T36"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Drug interaction", "Accidental ingestion"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Kidney damage", "Liver damage", "Allergic reaction", "Varies by drug"],
        "label_condition_name": "Poisoning by other systemic anti-infectives and antiparasitics",
        "icd_code": "T37"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., insulin)", "Incorrect dosage", "Misuse"],
        "feature_3_primary_system": "Endocrine",
        "feature_4_common_symptoms_signs": ["Hypoglycemia", "Hyperglycemia", "Hormonal imbalance", "Mood changes", "Weakness", "Confusion"],
        "label_condition_name": "Poisoning by hormones and their synthetic substitutes and antagonists",
        "icd_code": "T38"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., aspirin)", "Accidental ingestion", "Chronic overuse"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Stomach pain", "Nausea", "Vomiting", "Tinnitus (ringing ears)", "Liver damage", "Bleeding"],
        "label_condition_name": "Poisoning by nonopioid analgesics, antipyretics and antirheumatics",
        "icd_code": "T39"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., heroin)", "Illicit drug use", "Accidental ingestion"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Respiratory depression", "Pinpoint pupils", "Unconsciousness", "Nausea", "Hallucinations", "Agitation"],
        "label_condition_name": "Poisoning by narcotics and psychodysleptics [hallucinogens]",
        "icd_code": "T40"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Anesthesia error", "Overdose", "Inhalation"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Respiratory depression", "Low blood pressure", "Unconsciousness", "Confusion", "Slow heart rate", "Dizziness"],
        "label_condition_name": "Poisoning by anesthetics and therapeutic gases",
        "icd_code": "T41"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Accidental ingestion", "Drug interaction"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Drowsiness", "Confusion", "Unsteady gait", "Slurred speech", "Coma", "Respiratory depression"],
        "label_condition_name": "Poisoning by antiepileptic, sedative-hypnotic and antiparkinsonism drugs",
        "icd_code": "T42"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Drug interaction", "Misuse"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Agitation", "Drowsiness", "Hallucinations", "Seizures", "Arrhythmia", "Dry mouth"],
        "label_condition_name": "Poisoning by psychotropic drugs, not elsewhere classified",
        "icd_code": "T43"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Accidental ingestion", "Misuse"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Blurred vision", "Dry mouth", "Rapid heart rate", "Slow heart rate", "Confusion", "Dizziness"],
        "label_condition_name": "Poisoning by drugs primarily affecting the autonomic nervous system",
        "icd_code": "T44"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., warfarin)", "Chemotherapy side effect", "Drug interaction"],
        "feature_3_primary_system": "Circulatory",
        "feature_4_common_symptoms_signs": ["Bleeding", "Bruising", "Anemia", "Fatigue", "Shortness of breath", "Varies by agent"],
        "label_condition_name": "Poisoning by primarily systemic and hematological agents, not elsewhere classified",
        "icd_code": "T45"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., beta-blocker)", "Accidental ingestion", "Drug interaction"],
        "feature_3_primary_system": "Circulatory",
        "feature_4_common_symptoms_signs": ["Low blood pressure", "Slow heart rate", "Arrhythmia", "Dizziness", "Fainting", "Chest pain"],
        "label_condition_name": "Poisoning by agents primarily affecting the cardiovascular system",
        "icd_code": "T46"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose (e.g., laxative)", "Accidental ingestion", "Misuse"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Diarrhea", "Abdominal cramping", "Dehydration", "Electrolyte imbalance"],
        "label_condition_name": "Poisoning by agents primarily affecting the gastrointestinal system",
        "icd_code": "T47"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overuse of inhaler", "Overdose of cough medicine", "Drug interaction"],
        "feature_3_primary_system": "Respiratory",
        "feature_4_common_symptoms_signs": ["Rapid heart rate", "Tremors", "Drowsiness", "Difficulty breathing", "Dizziness", "Nausea"],
        "label_condition_name": "Poisoning by agents primarily acting on the respiratory system",
        "icd_code": "T48"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Over-application", "Accidental ingestion", "Absorption through skin"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Skin irritation", "Rash", "Nausea (if ingested)", "Dizziness", "Varies by agent", "Systemic effects"],
        "label_condition_name": "Poisoning by topical agents primarily affecting skin and mucous membrane and by ophthalmological, otorhinolaryngological and dental drugs",
        "icd_code": "T49"
    },
    {
        "feature_1_category": "Poisoning",
        "feature_2_common_causes": ["Overdose", "Drug interaction", "Electrolyte imbalance"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Dehydration", "Low blood pressure", "Weakness", "Confusion", "Kidney dysfunction", "Electrolyte imbalance"],
        "label_condition_name": "Poisoning by diuretics and other and unspecified drugs, medicaments and biological substances",
        "icd_code": "T50"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Binge drinking", "Chronic overuse", "Accidental ingestion"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Slurred speech", "Unsteady gait", "Nausea", "Vomiting", "Respiratory depression", "Coma"],
        "label_condition_name": "Toxic effect of alcohol",
        "icd_code": "T51"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Inhalation of fumes", "Ingestion", "Skin absorption"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Dizziness", "Headache", "Nausea", "Confusion", "Unconsciousness", "Organ damage"],
        "label_condition_name": "Toxic effect of organic solvents",
        "icd_code": "T52"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Inhalation", "Ingestion", "Industrial exposure"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Liver damage", "Kidney damage", "Nervous system depression", "Confusion"],
        "label_condition_name": "Toxic effect of halogen derivatives of aliphatic and aromatic hydrocarbons",
        "icd_code": "T53"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion of bleach", "Ingestion of acid", "Ingestion of alkali"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Severe mouth pain", "Severe throat pain", "Drooling", "Vomiting blood", "Difficulty breathing", "Esophageal perforation"],
        "label_condition_name": "Toxic effect of corrosive substances",
        "icd_code": "T54"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion", "Eye contact", "Skin contact"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Skin irritation", "Eye irritation"],
        "label_condition_name": "Toxic effect of soaps and detergents",
        "icd_code": "T55"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion (e.g., lead)", "Inhalation (e.g., mercury)", "Industrial exposure"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Abdominal pain", "Neurological damage", "Kidney damage", "Anemia"],
        "label_condition_name": "Toxic effect of metals",
        "icd_code": "T56"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion (e.g., arsenic)", "Inhalation (e.g., chlorine)", "Industrial exposure"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Diarrhea", "Respiratory distress", "Organ failure", "Varies by substance"],
        "label_condition_name": "Toxic effect of other inorganic substances",
        "icd_code": "T57"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Faulty furnace", "Car exhaust", "Fire smoke inhalation"],
        "feature_3_primary_system": "Circulatory",
        "feature_4_common_symptoms_signs": ["Headache", "Dizziness", "Nausea", "Confusion", "Cherry-red skin", "Unconsciousness"],
        "label_condition_name": "Toxic effect of carbon monoxide",
        "icd_code": "T58"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Industrial leak", "Inhalation", "Chemical exposure"],
        "feature_3_primary_system": "Respiratory",
        "feature_4_common_symptoms_signs": ["Coughing", "Wheezing", "Shortness of breath", "Chest pain", "Dizziness", "Nausea"],
        "label_condition_name": "Toxic effect of other gases, fumes and vapors",
        "icd_code": "T59"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion", "Skin absorption", "Inhalation"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Muscle twitching", "Seizures", "Respiratory failure", "Salivation"],
        "label_condition_name": "Toxic effect of pesticides",
        "icd_code": "T60"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Eating contaminated fish", "Eating contaminated shellfish", "Natural toxins"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Diarrhea", "Numbness", "Tingling", "Paralysis"],
        "label_condition_name": "Toxic effect of noxious substances eaten as seafood",
        "icd_code": "T61"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Eating poisonous mushrooms", "Food poisoning (bacterial toxin)", "Eating spoiled food"],
        "feature_3_primary_system": "Digestive",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Diarrhea", "Abdominal cramps", "Fever", "Dehydration"],
        "label_condition_name": "Toxic effect of other noxious substances eaten as food",
        "icd_code": "T62"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Snake bite", "Spider bite", "Insect sting"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Local pain", "Swelling", "Redness", "Nausea", "Vomiting", "Systemic effects (e.g., paralysis)"],
        "label_condition_name": "Toxic effect of contact with venomous animals",
        "icd_code": "T63"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Eating moldy peanuts", "Eating moldy grains", "Mycotoxin ingestion"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Abdominal pain", "Jaundice", "Liver failure", "Chronic health issues"],
        "label_condition_name": "Toxic effect of aflatoxin and other mycotoxin food contaminants",
        "icd_code": "T64"
    },
    {
        "feature_1_category": "Toxic Effect",
        "feature_2_common_causes": ["Ingestion of unknown substance", "Exposure to unknown toxin", "Plant ingestion"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Altered mental state", "Seizures", "Organ failure", "Varies by substance"],
        "label_condition_name": "Toxic effect of other and unspecified substances",
        "icd_code": "T65"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Radiation therapy", "Nuclear accident", "Prolonged UV exposure"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Fatigue", "Hair loss", "Skin burns", "Radiation sickness"],
        "label_condition_name": "Effects of radiation, unspecified",
        "icd_code": "T66"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Heat wave", "Prolonged sun exposure", "Strenuous exercise in heat"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Heat stroke", "Heat exhaustion", "Fainting", "Dehydration", "Confusion", "High body temperature"],
        "label_condition_name": "Effects of heat and light",
        "icd_code": "T67"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Cold exposure", "Immersion in cold water", "Inadequate clothing"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Shivering", "Confusion", "Drowsiness", "Slow breathing", "Low body temperature", "Loss of coordination"],
        "label_condition_name": "Hypothermia",
        "icd_code": "T68"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Trench foot", "Chilblains", "Prolonged cold/wet exposure"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Numbness", "Tingling", "Pale skin", "Red itchy patches", "Blisters", "Skin breakdown"],
        "label_condition_name": "Other effects of reduced temperature",
        "icd_code": "T69"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Scuba diving", "Rapid ascent (flying)", "Caisson work"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Joint pain (bends)", "Dizziness", "Headache", "Ear pain", "Shortness of breath", "Paralysis"],
        "label_condition_name": "Effects of air pressure and water pressure",
        "icd_code": "T70"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Strangulation", "Suffocation", "Drowning"],
        "feature_3_primary_system": "Respiratory",
        "feature_4_common_symptoms_signs": ["Loss of consciousness", "Cyanosis (bluish skin)", "No breathing", "Weak pulse", "Agitation", "Brain damage"],
        "label_condition_name": "Asphyxiation",
        "icd_code": "T71"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Starvation", "Dehydration", "Neglect"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Extreme weight loss", "Fatigue", "Weakness", "Dizziness", "Organ failure", "Sunken eyes"],
        "label_condition_name": "Effects of other deprivation",
        "icd_code": "T73"
    },
    {
        "feature_1_category": "Trauma",
        "feature_2_common_causes": ["Physical abuse", "Sexual abuse", "Psychological abuse"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Unexplained bruises", "Fear", "Anxiety", "Depression", "Withdrawal", "Physical injuries"],
        "label_condition_name": "Maltreatment syndromes",
        "icd_code": "T74"
    },
    {
        "feature_1_category": "Environmental",
        "feature_2_common_causes": ["Vibration (e.g., power tools)", "Motion sickness", "Lightning strike"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Nausea", "Vomiting", "Dizziness", "Numbness", "Tingling", "Burns (lightning)"],
        "label_condition_name": "Effects of other external causes",
        "icd_code": "T75"
    },
    {
        "feature_1_category": "Adverse Effect",
        "feature_2_common_causes": ["Allergy to food", "Allergy to drug", "Unknown allergen"],
        "feature_3_primary_system": "Immune",
        "feature_4_common_symptoms_signs": ["Anaphylactic shock", "Hives", "Swelling", "Difficulty breathing", "Itching", "Low blood pressure"],
        "label_condition_name": "Adverse effects, not elsewhere classified",
        "icd_code": "T78"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Severe trauma", "Crushing injury", "Major surgery"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Traumatic shock", "Fat embolism", "Wound infection", "Compartment syndrome", "Rhabdomyolysis", "Air embolism"],
        "label_condition_name": "Certain early complications of trauma, not elsewhere classified",
        "icd_code": "T79"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["IV line", "Blood transfusion", "Injection"],
        "feature_3_primary_system": "Circulatory",
        "feature_4_common_symptoms_signs": ["Infection at site", "Phlebitis (vein inflammation)", "Air embolism", "Transfusion reaction", "Fever", "Allergic reaction"],
        "label_condition_name": "Complications following infusion, transfusion and therapeutic injection",
        "icd_code": "T80"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Surgery", "Medical procedure", "Post-operative period"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Hemorrhage", "Shock", "Wound infection", "Sepsis", "Foreign body left in", "Wound dehiscence"],
        "label_condition_name": "Complications of procedures, not elsewhere classified",
        "icd_code": "T81"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Pacemaker", "Heart valve prosthesis", "Vascular graft"],
        "feature_3_primary_system": "Circulatory",
        "feature_4_common_symptoms_signs": ["Infection", "Device failure", "Blood clot", "Device migration", "Leakage", "Erosion"],
        "label_condition_name": "Complications of cardiac and vascular prosthetic devices, implants and grafts",
        "icd_code": "T82"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Urinary catheter", "Ureteral stent", "Penile prosthesis"],
        "feature_3_primary_system": "Genitourinary",
        "feature_4_common_symptoms_signs": ["Infection (UTI)", "Device blockage", "Erosion", "Pain", "Device migration", "Mechanical failure"],
        "label_condition_name": "Complications of genitourinary prosthetic devices, implants and grafts",
        "icd_code": "T83"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Hip replacement", "Knee replacement", "Spinal fusion hardware"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Infection", "Loosening of implant", "Dislocation of joint", "Implant breakage", "Chronic pain", "Reduced mobility"],
        "label_condition_name": "Complications of internal orthopedic prosthetic devices, implants and grafts",
        "icd_code": "T84"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Breast implant", "Neurostimulator", "Surgical mesh"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Infection", "Implant rupture", "Erosion", "Chronic pain", "Device failure", "Migration"],
        "label_condition_name": "Complications of other internal prosthetic devices, implants and grafts",
        "icd_code": "T85"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Kidney transplant", "Liver transplant", "Heart transplant"],
        "feature_3_primary_system": "Immune",
        "feature_4_common_symptoms_signs": ["Organ rejection", "Infection", "Graft-versus-host disease", "Organ dysfunction", "Fever", "Pain at transplant site"],
        "label_condition_name": "Complications of transplanted organs and tissues",
        "icd_code": "T86"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Surgical amputation", "Reattachment surgery", "Traumatic amputation"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Stump infection", "Neuroma (nerve pain)", "Phantom limb pain", "Poor wound healing", "Stump hematoma", "Contracture"],
        "label_condition_name": "Complications peculiar to reattachment and amputation",
        "icd_code": "T87"
    },
    {
        "feature_1_category": "Complication",
        "feature_2_common_causes": ["Adverse drug reaction", "Post-procedural complication", "Surgical care"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Anaphylactic shock (drug)", "Sepsis", "Post-operative confusion", "Respiratory failure", "Kidney failure", "Persistent pain"],
        "label_condition_name": "Other complications of surgical and medical care, not elsewhere classified",
        "icd_code": "T88"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Previous head trauma", "Previous traumatic brain injury", "Old skull fracture"],
        "feature_3_primary_system": "Nervous",
        "feature_4_common_symptoms_signs": ["Chronic headaches", "Cognitive deficits", "Seizure disorder", "Personality changes", "Dizziness", "Chronic pain"],
        "label_condition_name": "Sequelae of injuries of head",
        "icd_code": "T90"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Previous spinal cord injury", "Old neck fracture", "Past trunk injury"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Chronic back pain", "Paralysis", "Numbness", "Chronic nerve pain", "Stiffness", "Muscle weakness"],
        "label_condition_name": "Sequelae of injuries of neck and trunk",
        "icd_code": "T91"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Old arm fracture", "Previous nerve damage", "Past upper limb trauma"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Chronic arm pain", "Reduced range of motion", "Muscle weakness", "Arthritis", "Numbness", "Deformity"],
        "label_condition_name": "Sequelae of injuries of upper limb",
        "icd_code": "T92"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Old leg fracture", "Previous knee injury", "Past lower limb trauma"],
        "feature_3_primary_system": "Musculoskeletal",
        "feature_4_common_symptoms_signs": ["Chronic leg pain", "Limping", "Arthritis", "Joint instability", "Muscle weakness", "Numbness"],
        "label_condition_name": "Sequelae of injuries of lower limb",
        "icd_code": "T93"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Old multiple fractures", "Previous major trauma", "Past multiple injuries"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Chronic widespread pain", "Multiple joint issues", "Cognitive deficits", "Reduced mobility", "Chronic fatigue", "Post-traumatic stress"],
        "label_condition_name": "Sequelae of injuries involving multiple and unspecified body regions",
        "icd_code": "T94"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Old severe burn", "Previous chemical burn", "Old frostbite"],
        "feature_3_primary_system": "Integumentary",
        "feature_4_common_symptoms_signs": ["Scars", "Contractures", "Chronic pain", "Reduced mobility", "Nerve damage", "Disfigurement"],
        "label_condition_name": "Sequelae of burns, corrosions and frostbite",
        "icd_code": "T95"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Past drug overdose", "Previous poisoning", "Old adverse drug reaction"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Chronic cognitive issues", "Organ damage (e.g., kidney)", "Neurological deficits", "Chronic fatigue", "Varies by substance", "Psychological effects"],
        "label_condition_name": "Sequelae of poisoning by drugs, medicaments and biological substances",
        "icd_code": "T96"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Past alcohol poisoning", "Previous lead poisoning", "Old toxic exposure"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Chronic liver disease", "Neuropathy", "Cognitive deficits", "Kidney damage", "Chronic pain", "Varies by substance"],
        "label_condition_name": "Sequelae of toxic effects of substances chiefly nonmedicinal as to source",
        "icd_code": "T97"
    },
    {
        "feature_1_category": "Sequelae",
        "feature_2_common_causes": ["Past radiation exposure", "Old heat stroke", "Previous drowning"],
        "feature_3_primary_system": "Multiple",
        "feature_4_common_symptoms_signs": ["Chronic organ dysfunction", "Neurological deficits", "Chronic pain", "Respiratory issues", "Varies by cause", "Long-term disability"],
        "label_condition_name": "Sequelae of other and unspecified effects of external causes",
        "icd_code": "T98"
    }
]

# You can now use this 'icd_t_code_data' list.
# For example, to convert to a pandas DataFrame and then to a CSV:
#
# import pandas as pd
#
# df = pd.DataFrame(icd_t_code_data)
#
# Re-ordering columns to match the requested structure:
# column_order = [
#     "feature_1_category",
#     "feature_2_common_causes",
#     "feature_3_primary_system",
#     "feature_4_common_symptoms_signs",
#     "label_condition_name",
#     "icd_code"
# ]
# df = df[column_order]
#
# print(df.head())
#
# To save to CSV:
# df.to_csv("icd_t_code_dataset.csv", index=False)
