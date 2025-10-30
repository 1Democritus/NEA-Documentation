# ICD-10 X00-X99: External causes of morbidity
# This dataset has been adapted to fit the requested structure.
# - "Disease_type" refers to the *type of external cause* (e.g., Thermal, Mechanical, Chemical).
# - "How_the_disease_transmits" is adapted to "Key_Contributing_Factors".
# - "6_most_common_associated_symptoms" is adapted to "Common_Injuries_Symptoms".
# - "Disease_Name" is the official description of the external cause.

icd_x_data = [
    # X00-X09: Exposure to smoke, fire and flames
    {
        "Geography": "Global (Urban/Residential)",
        "How_the_disease_transmits": ["building", "uncontrolled-fire", "inhalation"],
        "Disease_type": "Thermal/Asphyxiation",
        "6_most_common_associated_symptoms": ["burns", "smoke-inhalation", "respiratory-distress", "blisters", "shock", "carbon-monoxide-poisoning"],
        "Disease_Name": "Exposure to uncontrolled fire in building or structure",
        "ICD_code": "X00"
    },
    {
        "Geography": "Global (Urban/Wildland)",
        "How_the_disease_transmits": ["vehicle", "uncontrolled-fire", "entrapment"],
        "Disease_type": "Thermal/Asphyxiation",
        "6_most_common_associated_symptoms": ["burns", "smoke-inhalation", "traumatic-injury", "blisters", "shock", "respiratory-failure"],
        "Disease_Name": "Exposure to uncontrolled fire in vehicle or vessel",
        "ICD_code": "X01"
    },
    {
        "Geography": "Global (Rural/Wildland)",
        "How_the_disease_transmits": ["wildfire", "vegetation", "uncontrolled-fire"],
        "Disease_type": "Thermal/Asphyxiation",
        "6_most_common_associated_symptoms": ["burns", "smoke-inhalation", "respiratory-distress", "dehydration", "eye-irritation", "exhaustion"],
        "Disease_Name": "Exposure to uncontrolled fire not in building or structure",
        "ICD_code": "X02"
    },
    {
        "Geography": "Global (Residential/Industrial)",
        "How_the_disease_transmits": ["fireplace", "stove", "controlled-fire"],
        "Disease_type": "Thermal",
        "6_most_common_associated_symptoms": ["burns", "blisters", "localized-pain", "skin-redness", "minor-smoke-inhalation", "ember-contact"],
        "Disease_Name": "Exposure to controlled fire in building or structure",
        "ICD_code": "X03"
    },
    {
        "Geography": "Global (Recreational/Rural)",
        "How_the_disease_transmits": ["bonfire", "campfire", "controlled-fire"],
        "Disease_type": "Thermal",
        "6_most_common_associated_symptoms": ["burns", "blisters", "localized-pain", "skin-redness", "ember-contact", "minor-smoke-inhalation"],
        "Disease_Name": "Exposure to controlled fire not in building or structure",
        "ICD_code": "X04"
    },
    {
        "Geography": "Global (Residential/Occupational)",
        "How_the_disease_transmits": ["bed", "chair", "clothing-ignition"],
        "Disease_type": "Thermal",
        "6_most_common_associated_symptoms": ["severe-burns", "clothing-fused-to-skin", "shock", "smoke-inhalation", "localized-pain", "blisters"],
        "Disease_Name": "Exposure to ignition of nightwear",
        "ICD_code": "X05"
    },
    {
        "Geography": "Global (Residential/Occupational)",
        "How_the_disease_transmits": ["clothing-ignition", "flame-contact", "non-nightwear"],
        "Disease_type": "Thermal",
        "6_most_common_associated_symptoms": ["severe-burns", "clothing-fused-to-skin", "shock", "panic", "localized-pain", "blisters"],
        "Disease_Name": "Exposure to ignition or melting of other clothing and apparel",
        "ICD_code": "X06"
    },
    {
        "Geography": "Global (Industrial/Residential)",
        "How_the_disease_transmits": ["plastic", "rubber", "flammable-material"],
        "Disease_type": "Thermal/Chemical",
        "6_most_common_associated_symptoms": ["chemical-burns", "thermal-burns", "toxic-fume-inhalation", "respiratory-distress", "blisters", "skin-adhesion"],
        "Disease_Name": "Exposure to ignition or melting of highly flammable material",
        "ICD_code": "X08"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["smoke", "fire", "unspecified-source"],
        "Disease_type": "Thermal/Asphyxiation",
        "6_most_common_associated_symptoms": ["burns", "smoke-inhalation", "respiratory-distress", "blisters", "shock", "carbon-monoxide-poisoning"],
        "Disease_Name": "Exposure to other or unspecified smoke, fire and flames",
        "ICD_code": "X09"
    },
    # X10-X19: Contact with heat and hot substances
    {
        "Geography": "Global (Residential)",
        "How_the_disease_transmits": ["tap-water", "scald", "bath"],
        "Disease_type": "Thermal (Scald)",
        "6_most_common_associated_symptoms": ["scald-burn", "skin-redness", "blisters", "pain", "peeling-skin", "shock"],
        "Disease_Name": "Contact with hot tap-water",
        "ICD_code": "X10"
    },
    {
        "Geography": "Global (Residential/Occupational)",
        "How_the_disease_transmits": ["boiling-water", "spill", "cooking"],
        "Disease_type": "Thermal (Scald)",
        "6_most_common_associated_symptoms": ["scald-burn", "blisters", "severe-pain", "skin-redness", "peeling-skin", "splash-injury"],
        "Disease_Name": "Contact with other hot fluids",
        "ICD_code": "X11"
    },
    {
        "Geography": "Global (Residential/Occupational)",
        "How_the_disease_transmits": ["steam", "pipe", "inhalation"],
        "Disease_type": "Thermal (Steam)",
        "6_most_common_associated_symptoms": ["steam-burn", "respiratory-burn", "blisters", "severe-pain", "skin-redness", "wheezing"],
        "Disease_Name": "Contact with steam and hot vapours",
        "ICD_code": "X12"
    },
    {
        "Geography": "Global (Industrial/Residential)",
        "How_the_disease_transmits": ["radiator", "pipe", "engine"],
        "Disease_type": "Thermal (Contact)",
        "6_most_common_associated_symptoms": ["contact-burn", "skin-redness", "pain", "blister", "localized-injury", "charring"],
        "Disease_Name": "Contact with hot air and gases",
        "ICD_code": "X13"
    },
    {
        "Geography": "Global (Residential/Occupational)",
        "How_the_disease_transmits": ["radiator", "heater", "appliance"],
        "Disease_type": "Thermal (Contact)",
        "6_most_common_associated_symptoms": ["contact-burn", "skin-redness", "pain", "blister", "localized-injury", "skin-adhesion"],
        "Disease_Name": "Contact with hot household appliances",
        "ICD_code": "X14"
    },
    {
        "Geography": "Global (Industrial/Occupational)",
        "How_the_disease_transmits": ["engine-part", "machinery", "pipe"],
        "Disease_type": "Thermal (Contact)",
        "6_most_common_associated_symptoms": ["contact-burn", "deep-burn", "skin-adhesion", "pain", "blister", "charring"],
        "Disease_Name": "Contact with hot heating appliances, radiators and pipes",
        "ICD_code": "X15"
    },
    {
        "Geography": "Global (Industrial/Occupational)",
        "How_the_disease_transmits": ["tools", "machinery", "metal-parts"],
        "Disease_type": "Thermal (Contact)",
        "6_most_common_associated_symptoms": ["contact-burn", "deep-burn", "skin-adhesion", "pain", "blister", "localized-injury"],
        "Disease_Name": "Contact with hot engines, machinery and tools",
        "ICD_code": "X16"
    },
    {
        "Geography": "Global (Industrial/Foundry)",
        "How_the_disease_transmits": ["molten-metal", "glass", "slag"],
        "Disease_type": "Thermal (Contact/Splash)",
        "6_most_common_associated_symptoms": ["severe-burn", "deep-tissue-damage", "charring", "skin-adhesion", "shock", "amputation-risk"],
        "Disease_Name": "Contact with hot metals",
        "ICD_code": "X17"
    },
    {
        "Geography": "Global (Occupational/Residential)",
        "How_the_disease_transmits": ["grease", "food-oil", "tar"],
        "Disease_type": "Thermal (Scald/Contact)",
        "6_most_common_associated_symptoms": ["deep-burn", "scald-burn", "skin-adhesion", "blisters", "severe-pain", "prolonged-heat-contact"],
        "Disease_Name": "Contact with other hot fats and oils",
        "ICD_code": "X18"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["friction", "unspecified-hot-object", "heat-source"],
        "Disease_type": "Thermal",
        "6_most_common_associated_symptoms": ["burn", "friction-burn", "blister", "skin-redness", "pain", "abraded-skin"],
        "Disease_Name": "Contact with other and unspecified heat and hot substances",
        "ICD_code": "X19"
    },
    # X20-X29: Contact with venomous animals and plants
    {
        "Geography": "Americas/Asia/Africa/Australia",
        "How_the_disease_transmits": ["snake-bite", "envenomation", "puncture-wound"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["fang-marks", "localized-pain", "swelling", "nausea", "paralysis", "necrosis"],
        "Disease_Name": "Contact with venomous snakes",
        "ICD_code": "X20"
    },
    {
        "Geography": "Americas/Australia/Africa",
        "How_the_disease_transmits": ["spider-bite", "envenomation", "puncture-wound"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["fang-marks", "localized-pain", "necrosis", "cramping", "nausea", "headache"],
        "Disease_Name": "Contact with venomous spiders",
        "ICD_code": "X21"
    },
    {
        "Geography": "Americas/Africa/Asia",
        "How_the_disease_transmits": ["scorpion-sting", "envenomation", "sting"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["intense-pain", "swelling", "numbness", "muscle-twitching", "nausea", "respiratory-distress"],
        "Disease_Name": "Contact with scorpions",
        "ICD_code": "X22"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["bee-sting", "wasp-sting", "hornet-sting"],
        "Disease_type": "Toxic (Venom/Allergy)",
        "6_most_common_associated_symptoms": ["sting-site-pain", "swelling", "redness", "itching", "anaphylaxis", "dizziness"],
        "Disease_Name": "Contact with hornets, wasps and bees",
        "ICD_code": "X23"
    },
    {
        "Geography": "Global (Tropical/Americas)",
        "How_the_disease_transmits": ["ant-bite", "ant-sting", "envenomation"],
        "Disease_type": "Toxic (Venom/Allergy)",
        "6_most_common_associated_symptoms": ["multiple-bites", "itching", "pustules", "swelling", "pain", "anaphylaxis"],
        "Disease_Name": "Contact with centipedes and venomous millipedes (tropical)",
        "ICD_code": "X24"
    },
    {
        "Geography": "Global (Marine/Coastal)",
        "How_the_disease_transmits": ["stingray-barb", "jellyfish-sting", "sea-anemone"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["sting-marks", "severe-pain", "laceration", "swelling", "nausea", "paralysis"],
        "Disease_Name": "Contact with other venomous arthropods",
        "ICD_code": "X25"
    },
    {
        "Geography": "Global (Marine/Coastal)",
        "How_the_disease_transmits": ["jellyfish-sting", "stingray-barb", "sea-urchin-spine"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["sting-marks", "severe-pain", "rash", "swelling", "nausea", "muscle-cramps"],
        "Disease_Name": "Contact with venomous marine animals and plants",
        "ICD_code": "X26"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["gila-monster-bite", "lizard-bite", "envenomation"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["bite-mark", "localized-pain", "swelling", "nausea", "dizziness", "lymphangitis"],
        "Disease_Name": "Contact with other specified venomous animals",
        "ICD_code": "X27"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poison-ivy", "poison-oak", "stinging-nettle"],
        "Disease_type": "Toxic (Irritant/Allergy)",
        "6_most_common_associated_symptoms": ["rash", "itching", "blisters", "redness", "swelling", "contact-dermatitis"],
        "Disease_Name": "Contact with venomous plants, thorns and spines",
        "ICD_code": "X28"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["unspecified-bite", "unspecified-sting", "envenomation"],
        "Disease_type": "Toxic (Venom)",
        "6_most_common_associated_symptoms": ["puncture-wound", "pain", "swelling", "redness", "allergic-reaction", "nausea"],
        "Disease_Name": "Contact with unspecified venomous animal or plant",
        "ICD_code": "X29"
    },
    # X30-X39: Exposure to forces of nature
    {
        "Geography": "Global (Sun-exposed)",
        "How_the_disease_transmits": ["sun-exposure", "uv-radiation", "heat"],
        "Disease_type": "Environmental (Heat/Radiation)",
        "6_most_common_associated_symptoms": ["heatstroke", "sunburn", "dehydration", "dizziness", "nausea", "syncope"],
        "Disease_Name": "Exposure to excessive natural heat",
        "ICD_code": "X30"
    },
    {
        "Geography": "Global (Cold/Arctic/Mountainous)",
        "How_the_disease_transmits": ["cold-exposure", "low-temperature", "wind-chill"],
        "Disease_type": "Environmental (Cold)",
        "6_most_common_associated_symptoms": ["hypothermia", "frostbite", "shivering", "confusion", "numbness", "skin-discoloration"],
        "Disease_Name": "Exposure to excessive natural cold",
        "ICD_code": "X31"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["sunlight", "glare", "uv-radiation"],
        "Disease_type": "Environmental (Radiation)",
        "6_most_common_associated_symptoms": ["sunburn", "photokeratitis", "skin-aging", "eye-pain", "headache", "skin-cancer-risk"],
        "Disease_Name": "Exposure to sunlight",
        "ICD_code": "X32"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["lightning-strike", "electrical-discharge", "storm"],
        "Disease_type": "Environmental (Electric)",
        "6_most_common_associated_symptoms": ["cardiac-arrest", "burns", "neurological-damage", "loss-of-consciousness", "tinnitus", "keraunoparalysis"],
        "Disease_Name": "Victim of lightning",
        "ICD_code": "X33"
    },
    {
        "Geography": "Global (Coastal/Seismic)",
        "How_the_disease_transmits": ["earthquake", "seismic-wave", "ground-shaking"],
        "Disease_type": "Environmental (Mechanical)",
        "6_most_common_associated_symptoms": ["crush-injury", "fracture", "laceration", "head-injury", "asphyxiation", "psychological-trauma"],
        "Disease_Name": "Victim of earthquake",
        "ICD_code": "X34"
    },
    {
        "Geography": "Global (Volcanic)",
        "How_the_disease_transmits": ["volcanic-eruption", "ash-inhalation", "lava-flow"],
        "Disease_type": "Environmental (Thermal/Asphyxiation)",
        "6_most_common_associated_symptoms": ["burns", "respiratory-distress", "ash-inhalation", "laceration", "crush-injury", "toxic-gas-poisoning"],
        "Disease_Name": "Victim of volcanic eruption",
        "ICD_code": "X35"
    },
    {
        "Geography": "Global (Coastal/Seismic)",
        "How_the_disease_transmits": ["tsunami", "flood-wave", "drowning"],
        "Disease_type": "Environmental (Drowning/Mechanical)",
        "6_most_common_associated_symptoms": ["drowning", "fracture", "laceration", "crush-injury", "hypothermia", "aspiration-pneumonia"],
        "Disease_Name": "Victim of avalanche, landslide and other earth movements",
        "ICD_code": "X36"
    },
    {
        "Geography": "Global (Coastal/Tropical)",
        "How_the_disease_transmits": ["hurricane", "tornado", "cyclone"],
        "Disease_type": "Environmental (Mechanical)",
        "6_most_common_associated_symptoms": ["fracture", "laceration", "head-injury", "crush-injury", "penetrating-trauma", "drowning"],
        "Disease_Name": "Victim of cataclysmic storm",
        "ICD_code": "X37"
    },
    {
        "Geography": "Global (Riverine/Coastal)",
        "How_the_disease_transmits": ["flood", "rising-water", "drowning"],
        "Disease_type": "Environmental (Drowning/Mechanical)",
        "6_most_common_associated_symptoms": ["drowning", "hypothermia", "laceration", "waterborne-disease", "fracture", "electrocution"],
        "Disease_Name": "Victim of flood",
        "ICD_code": "X38"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["blizzard", "drought", "hailstorm"],
        "Disease_type": "Environmental",
        "6_most_common_associated_symptoms": ["hypothermia", "dehydration", "fracture", "laceration", "frostbite", "head-injury"],
        "Disease_Name": "Exposure to other and unspecified forces of nature",
        "ICD_code": "X39"
    },
    # X40-X49: Accidental poisoning by and exposure to noxious substances
    {
        "Geography": "Global (Residential)",
        "How_the_disease_transmits": ["overdose", "ingestion", "nonopioid-analgesic"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["nausea", "vomiting", "liver-damage", "drowsiness", "stomach-pain", "tinnitus"],
        "Disease_Name": "Accidental poisoning by nonopioid analgesics",
        "ICD_code": "X40"
    },
    {
        "Geography": "Global (Residential)",
        "How_the_disease_transmits": ["overdose", "ingestion", "anticonvulsant"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["drowsiness", "confusion", "ataxia", "nystagmus", "respiratory-depression", "coma"],
        "Disease_Name": "Accidental poisoning by antiepileptic, sedative-hypnotic drugs",
        "ICD_code": "X41"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "narcotics"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["respiratory-depression", "pinpoint-pupils", "unconsciousness", "bradycardia", "cyanosis", "nausea"],
        "Disease_Name": "Accidental poisoning by narcotics and psychodysleptics",
        "ICD_code": "X42"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "psychotropic-drug"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["confusion", "tachycardia", "hallucinations", "seizures", "dry-mouth", "urinary-retention"],
        "Disease_Name": "Accidental poisoning by other drugs acting on autonomic nervous system",
        "ICD_code": "X43"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "unspecified-drug"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["altered-mental-status", "nausea", "vomiting", "respiratory-depression", "seizures", "arrhythmia"],
        "Disease_Name": "Accidental poisoning by other and unspecified drugs",
        "ICD_code": "X44"
    },
    {
        "Geography": "Global (Residential)",
        "How_the_disease_transmits": ["ingestion", "ethanol", "beverage"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["slurred-speech", "ataxia", "stupor", "vomiting", "respiratory-depression", "coma"],
        "Disease_Name": "Accidental poisoning by alcohol",
        "ICD_code": "X45"
    },
    {
        "Geography": "Global (Industrial/Residential)",
        "How_the_disease_transmits": ["ingestion", "inhalation", "solvents"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["dizziness", "headache", "nausea", "confusion", "respiratory-irritation", "unconsciousness"],
        "Disease_Name": "Accidental poisoning by organic solvents and halogenated hydrocarbons",
        "ICD_code": "X46"
    },
    {
        "Geography": "Global (Residential/Industrial)",
        "How_the_disease_transmits": ["inhalation", "carbon-monoxide", "faulty-appliance"],
        "Disease_type": "Toxic (Asphyxiation)",
        "6_most_common_associated_symptoms": ["headache", "dizziness", "nausea", "confusion", "cherry-red-skin", "unconsciousness"],
        "Disease_Name": "Accidental poisoning by carbon monoxide",
        "ICD_code": "X47"
    },
    {
        "Geography": "Global (Agricultural/Residential)",
        "How_the_disease_transmits": ["ingestion", "inhalation", "skin-contact"],
        "Disease_type": "Toxic (Poisoning)",
        "6_most_common_associated_symptoms": ["salivation", "lacrimation", "urination", "defecation", "bradycardia", "muscle-weakness"],
        "Disease_Name": "Accidental poisoning by pesticides",
        "ICD_code": "X48"
    },
    {
        "Geography": "Global (Industrial/Residential)",
        "How_the_disease_transmits": ["ingestion", "inhalation", "bleach"],
        "Disease_type": "Toxic (Poisoning/Chemical)",
        "6_most_common_associated_symptoms": ["chemical-burns", "nausea", "vomiting", "respiratory-distress", "abdominal-pain", "seizures"],
        "Disease_Name": "Accidental poisoning by other and unspecified chemicals",
        "ICD_code": "X49"
    },
    # X50-X59: Overexertion, travel and privation
    {
        "Geography": "Global (Occupational/Recreational)",
        "How_the_disease_transmits": ["heavy-lifting", "strenuous-activity", "repetitive-motion"],
        "Disease_type": "Mechanical (Strain)",
        "6_most_common_associated_symptoms": ["muscle-strain", "back-pain", "joint-pain", "fatigue", "rhabdomyolysis", "sprain"],
        "Disease_Name": "Overexertion and strenuous or repetitive movements",
        "ICD_code": "X50"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["car-sickness", "sea-sickness", "air-travel"],
        "Disease_type": "Environmental (Motion)",
        "6_most_common_associated_symptoms": ["nausea", "vomiting", "dizziness", "vertigo", "pallor", "cold-sweats"],
        "Disease_Name": "Travel and motion",
        "ICD_code": "X51"
    },
    {
        "Geography": "Space (Extra-terrestrial)",
        "How_the_disease_transmits": ["microgravity", "space-flight", "weightlessness"],
        "Disease_type": "Environmental (Gravity)",
        "6_most_common_associated_symptoms": ["space-sickness", "bone-density-loss", "muscle-atrophy", "fluid-shift", "dizziness", "visual-changes"],
        "Disease_Name": "Prolonged stay in weightless environment",
        "ICD_code": "X52"
    },
    {
        "Geography": "Global (Poverty/Conflict/Disaster)",
        "How_the_disease_transmits": ["starvation", "famine", "inadequate-intake"],
        "Disease_type": "Environmental (Privation)",
        "6_most_common_associated_symptoms": ["malnutrition", "weight-loss", "fatigue", "weakness", "vitamin-deficiency", "edema"],
        "Disease_Name": "Lack of food",
        "ICD_code": "X53"
    },
    {
        "Geography": "Global (Arid/Disaster)",
        "How_the_disease_transmits": ["thirst", "no-water-access", "inadequate-intake"],
        "Disease_type": "Environmental (Privation)",
        "6_most_common_associated_symptoms": ["dehydration", "thirst", "dry-mouth", "dizziness", "oliguria", "confusion"],
        "Disease_Name": "Lack of water",
        "ICD_code": "X54"
    },
    {
        "Geography": "Global (Poverty/Conflict/Disaster)",
        "How_the_disease_transmits": ["neglect", "deprivation", "unspecified-lack"],
        "Disease_type": "Environmental (Privation)",
        "6_most_common_associated_symptoms": ["malnutrition", "dehydration", "failure-to-thrive", "hygiene-issues", "weakness", "fatigue"],
        "Disease_Name": "Unspecified privation",
        "ICD_code": "X57"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["high-pressure", "low-pressure", "noise"],
        "Disease_type": "Environmental",
        "6_most_common_associated_symptoms": ["barotrauma", "hearing-loss", "tinnitus", "altitude-sickness", "decompression-sickness", "vertigo"],
        "Disease_Name": "Exposure to other specified factors",
        "ICD_code": "X58"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["unspecified-environment", "unspecified-exposure", "unknown-factor"],
        "Disease_type": "Environmental",
        "6_most_common_associated_symptoms": ["unknown-injury", "unexplained-symptom", "general-malaise", "pain", "dizziness", "fatigue"],
        "Disease_Name": "Exposure to unspecified factor",
        "ICD_code": "X59"
    },
    # X60-X84: Intentional self-harm
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["nausea", "vomiting", "liver-damage", "drowsiness", "stomach-pain", "loss-of-consciousness"],
        "Disease_Name": "Intentional self-poisoning by nonopioid analgesics",
        "ICD_code": "X60"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["drowsiness", "confusion", "ataxia", "respiratory-depression", "coma", "unconsciousness"],
        "Disease_Name": "Intentional self-poisoning by antiepileptic, sedative-hypnotic drugs",
        "ICD_code": "X61"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["respiratory-depression", "pinpoint-pupils", "unconsciousness", "coma", "bradycardia", "cyanosis"],
        "Disease_Name": "Intentional self-poisoning by narcotics and psychodysleptics",
        "ICD_code": "X62"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["confusion", "tachycardia", "hallucinations", "seizures", "dry-mouth", "coma"],
        "Disease_Name": "Intentional self-poisoning by other drugs acting on autonomic nervous system",
        "ICD_code": "X63"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["overdose", "ingestion", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["altered-mental-status", "nausea", "respiratory-depression", "seizures", "arrhythmia", "coma"],
        "Disease_Name": "Intentional self-poisoning by other and unspecified drugs",
        "ICD_code": "X64"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["ingestion", "ethanol", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["slurred-speech", "ataxia", "stupor", "vomiting", "respiratory-depression", "coma"],
        "Disease_Name": "Intentional self-poisoning by alcohol",
        "ICD_code": "X65"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["ingestion", "inhalation", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["dizziness", "headache", "nausea", "confusion", "respiratory-irritation", "unconsciousness"],
        "Disease_Name": "Intentional self-poisoning by organic solvents and halogenated hydrocarbons",
        "ICD_code": "X66"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["inhalation", "carbon-monoxide", "self-harm"],
        "Disease_type": "Toxic (Self-Harm/Asphyxiation)",
        "6_most_common_associated_symptoms": ["headache", "dizziness", "nausea", "confusion", "unconsciousness", "death"],
        "Disease_Name": "Intentional self-poisoning by carbon monoxide",
        "ICD_code": "X67"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["ingestion", "inhalation", "self-harm"],
        "Disease_type": "Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["salivation", "lacrimation", "bradycardia", "muscle-weakness", "seizures", "coma"],
        "Disease_Name": "Intentional self-poisoning by pesticides",
        "ICD_code": "X68"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["ingestion", "inhalation", "self-harm"],
        "Disease_type": "Toxic (Self-Harm/Chemical)",
        "6_most_common_associated_symptoms": ["chemical-burns", "nausea", "vomiting", "respiratory-distress", "seizures", "coma"],
        "Disease_Name": "Intentional self-poisoning by other and unspecified chemicals",
        "ICD_code": "X69"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["hanging", "strangulation", "self-harm"],
        "Disease_type": "Mechanical (Asphyxiation)",
        "6_most_common_associated_symptoms": ["ligature-mark", "neck-pain", "petechiae", "cyanosis", "loss-of-consciousness", "cervical-fracture"],
        "Disease_Name": "Intentional self-harm by hanging, strangulation and suffocation",
        "ICD_code": "X70"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["drowning", "submersion", "self-harm"],
        "Disease_type": "Mechanical (Asphyxiation)",
        "6_most_common_associated_symptoms": ["respiratory-arrest", "cyanosis", "hypothermia", "loss-of-consciousness", "water-in-lungs", "cardiac-arrest"],
        "Disease_Name": "Intentional self-harm by drowning and submersion",
        "ICD_code": "X71"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["handgun", "firearm", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "hemorrhage", "organ-damage", "fracture", "shock", "cardiac-arrest"],
        "Disease_Name": "Intentional self-harm by handgun discharge",
        "ICD_code": "X72"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["rifle", "shotgun", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "severe-hemorrhage", "massive-tissue-damage", "organ-damage", "shock", "cardiac-arrest"],
        "Disease_Name": "Intentional self-harm by rifle, shotgun and larger firearm discharge",
        "ICD_code": "X73"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["firearm", "unspecified-gun", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "hemorrhage", "organ-damage", "fracture", "shock", "cardiac-arrest"],
        "Disease_Name": "Intentional self-harm by other and unspecified firearm discharge",
        "ICD_code": "X74"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["explosive-device", "detonation", "self-harm"],
        "Disease_type": "Mechanical (Traumatic/Blast)",
        "6_most_common_associated_symptoms": ["blast-injury", "amputation", "shrapnel-wounds", "burns", "hemorrhage", "shock"],
        "Disease_Name": "Intentional self-harm by explosive material",
        "ICD_code": "X75"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["fire", "immolation", "self-harm"],
        "Disease_type": "Thermal (Self-Harm)",
        "6_most_common_associated_symptoms": ["severe-burns", "smoke-inhalation", "shock", "respiratory-distress", "disfigurement", "death"],
        "Disease_Name": "Intentional self-harm by smoke, fire and flames",
        "ICD_code": "X76"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["steam", "hot-substance", "self-harm"],
        "Disease_type": "Thermal (Self-Harm)",
        "6_most_common_associated_symptoms": ["scald-burn", "contact-burn", "blisters", "severe-pain", "skin-redness", "shock"],
        "Disease_Name": "Intentional self-harm by steam, hot vapours and hot objects",
        "ICD_code": "X77"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["knife", "blade", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["laceration", "puncture-wound", "hemorrhage", "organ-damage", "shock", "tendon-injury"],
        "Disease_Name": "Intentional self-harm by sharp object",
        "ICD_code": "X78"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["bat", "hammer", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["blunt-force-trauma", "fracture", "hematoma", "head-injury", "internal-bleeding", "crush-injury"],
        "Disease_Name": "Intentional self-harm by blunt object",
        "ICD_code": "X79"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["jump", "height", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["multiple-fractures", "head-injury", "internal-bleeding", "spinal-cord-injury", "shock", "polytrauma"],
        "Disease_Name": "Intentional self-harm by jumping from a high place",
        "ICD_code": "X80"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["jump", "moving-object", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["multiple-fractures", "polytrauma", "amputation", "head-injury", "internal-bleeding", "shock"],
        "Disease_Name": "Intentional self-harm by jumping or lying before moving object",
        "ICD_code": "X81"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["vehicle-crash", "intentional", "self-harm"],
        "Disease_type": "Mechanical (Traumatic)",
        "6_most_common_associated_symptoms": ["multiple-fractures", "head-injury", "internal-bleeding", "polytrauma", "spinal-cord-injury", "shock"],
        "Disease_Name": "Intentional self-harm by crashing of motor vehicle",
        "ICD_code": "X82"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["electrocution", "cold", "self-harm"],
        "Disease_type": "Mechanical/Thermal/Electric (Self-Harm)",
        "6_most_common_associated_symptoms": ["cardiac-arrest", "burns", "hypothermia", "unconsciousness", "frostbite", "arrhythmia"],
        "Disease_Name": "Intentional self-harm by other specified means",
        "ICD_code": "X83"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["unspecified-method", "unknown", "self-harm"],
        "Disease_type": "Mechanical/Toxic (Self-Harm)",
        "6_most_common_associated_symptoms": ["unspecified-injury", "polytrauma", "unconsciousness", "cardiac-arrest", "respiratory-arrest", "hemorrhage"],
        "Disease_Name": "Intentional self-harm by unspecified means",
        "ICD_code": "X84"
    },
    # X85-X99: Assault
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "ingestion", "assault"],
        "Disease_type": "Toxic (Assault)",
        "6_most_common_associated_symptoms": ["nausea", "vomiting", "altered-mental-status", "seizures", "respiratory-depression", "coma"],
        "Disease_Name": "Assault by drugs, medicaments and biological substances",
        "ICD_code": "X85"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "acid", "assault"],
        "Disease_type": "Toxic (Assault/Chemical)",
        "6_most_common_associated_symptoms": ["chemical-burns", "corrosive-injury", "vomiting", "respiratory-distress", "abdominal-pain", "shock"],
        "Disease_Name": "Assault by corrosive substance",
        "ICD_code": "X86"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "pesticide", "assault"],
        "Disease_type": "Toxic (Assault)",
        "6_most_common_associated_symptoms": ["salivation", "lacrimation", "bradycardia", "muscle-weakness", "seizures", "coma"],
        "Disease_Name": "Assault by pesticides",
        "ICD_code": "X87"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "inhalation", "assault"],
        "Disease_type": "Toxic (Assault/Asphyxiation)",
        "6_most_common_associated_symptoms": ["respiratory-distress", "confusion", "headache", "nausea", "unconsciousness", "seizures"],
        "Disease_Name": "Assault by gases and vapours",
        "ICD_code": "X88"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "unspecified-chemical", "assault"],
        "Disease_type": "Toxic (Assault/Chemical)",
        "6_most_common_associated_symptoms": ["nausea", "vomiting", "burns", "altered-mental-status", "respiratory-distress", "coma"],
        "Disease_Name": "Assault by other specified chemicals and noxious substances",
        "ICD_code": "X89"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["poisoning", "unspecified-substance", "assault"],
        "Disease_type": "Toxic (Assault)",
        "6_most_common_associated_symptoms": ["unexplained-illness", "altered-mental-status", "nausea", "vomiting", "seizures", "coma"],
        "Disease_Name": "Assault by unspecified chemical or noxious substance",
        "ICD_code": "X90"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["hanging", "strangulation", "assault"],
        "Disease_type": "Mechanical (Assault/Asphyxiation)",
        "6_most_common_associated_symptoms": ["ligature-mark", "neck-pain", "petechiae", "cyanosis", "loss-of-consciousness", "cervical-fracture"],
        "Disease_Name": "Assault by hanging, strangulation and suffocation",
        "ICD_code": "X91"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["drowning", "submersion", "assault"],
        "Disease_type": "Mechanical (Assault/Asphyxiation)",
        "6_most_common_associated_symptoms": ["respiratory-arrest", "cyanosis", "hypothermia", "loss-of-consciousness", "defensive-wounds", "cardiac-arrest"],
        "Disease_Name": "Assault by drowning and submersion",
        "ICD_code": "X92"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["handgun", "firearm", "assault"],
        "Disease_type": "Mechanical (Assault/Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "hemorrhage", "organ-damage", "fracture", "shock", "cardiac-arrest"],
        "Disease_Name": "Assault by handgun discharge",
        "ICD_code": "X93"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["rifle", "shotgun", "assault"],
        "Disease_type": "Mechanical (Assault/Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "severe-hemorrhage", "massive-tissue-damage", "organ-damage", "shock", "cardiac-arrest"],
        "Disease_Name": "Assault by rifle, shotgun and larger firearm discharge",
        "ICD_code": "X94"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["firearm", "unspecified-gun", "assault"],
        "Disease_type": "Mechanical (Assault/Traumatic)",
        "6_most_common_associated_symptoms": ["gunshot-wound", "hemorrhage", "organ-damage", "fracture", "shock", "cardiac-arrest"],
        "Disease_Name": "Assault by other and unspecified firearm discharge",
        "ICD_code": "X95"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["explosive-device", "detonation", "assault"],
        "Disease_type": "Mechanical (Assault/Traumatic/Blast)",
        "6_most_common_associated_symptoms": ["blast-injury", "amputation", "shrapnel-wounds", "burns", "hemorrhage", "shock"],
        "Disease_Name": "Assault by explosive material",
        "ICD_code": "X96"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["fire", "arson", "assault"],
        "Disease_type": "Thermal (Assault)",
        "6_most_common_associated_symptoms": ["severe-burns", "smoke-inhalation", "shock", "respiratory-distress", "disfigurement", "death"],
        "Disease_Name": "Assault by smoke, fire and flames",
        "ICD_code": "X97"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["steam", "hot-substance", "assault"],
        "Disease_type": "Thermal (Assault)",
        "6_most_common_associated_symptoms": ["scald-burn", "contact-burn", "blisters", "severe-pain", "skin-redness", "shock"],
        "Disease_Name": "Assault by steam, hot vapours and hot objects",
        "ICD_code": "X98"
    },
    {
        "Geography": "Global",
        "How_the_disease_transmits": ["knife", "blade", "assault"],
        "Disease_type": "Mechanical (Assault/Traumatic)",
        "6_most_common_associated_symptoms": ["laceration", "puncture-wound", "hemorrhage", "organ-damage", "shock", "defensive-wounds"],
        "Disease_Name": "Assault by sharp object",
        "ICD_code": "X99"
    }
]

if __name__ == '__main__':
    # This part is just to show you how to access the data.
    # You can delete this and import the 'icd_x_data' list in your main project.
    
    print(f"Total rows generated: {len(icd_x_data)}")
    
    print("\n--- Example Row (X00) ---")
    print(f"ICD Code: {icd_x_data[0]['ICD_code']}")
    print(f"Description: {icd_x_data[0]['Disease_Name']}")
    print(f"Cause Type: {icd_x_data[0]['Disease_type']}")
    print(f"Geography: {icd_x_data[0]['Geography']}")
    print(f"Factors: {icd_x_data[0]['How_the_disease_transmits']}")
    print(f"Injuries/Symptoms: {icd_x_data[0]['6_most_common_associated_symptoms']}")

    print("\n--- Example Row (X60) ---")
    print(f"ICD Code: {icd_x_data[58]['ICD_code']}")
    print(f"Description: {icd_x_data[58]['Disease_Name']}")
    print(f"Cause Type: {icd_x_data[58]['Disease_type']}")
    print(f"Geography: {icd_x_data[58]['Geography']}")
    print(f"Factors: {icd_x_data[58]['How_the_disease_transmits']}")
    print(f"Injuries/Symptoms: {icd_x_data[58]['6_most_common_associated_symptoms']}")

    print("\n--- Example Row (X99) ---")
    print(f"ICD Code: {icd_x_data[-1]['ICD_code']}")
    print(f"Description: {icd_x_data[-1]['Disease_Name']}")
    print(f"Cause Type: {icd_x_data[-1]['Disease_type']}")
    print(f"Geography: {icd_x_data[-1]['Geography']}")
    print(f"Factors: {icd_x_data[-1]['How_the_disease_transmits']}")
    print(f"Injuries/Symptoms: {icd_x_data[-1]['6_most_common_associated_symptoms']}")
