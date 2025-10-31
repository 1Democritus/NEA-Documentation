import pandas as pd

columns = ['Geography', 'Transmission', 'Disease Type', 'Symptoms', 'Disease Name', 'ICD Code']

sectionA = [
    # Header Row
    

    # A00-A09: Intestinal infectious diseases
    ['South Asia', 'waterborne, fecal-oral, poor sanitation', 'bacterial', 'profuse diarrhea, dehydration, shock, vomiting, rapid heart rate, low blood pressure', 'Cholera', 'A00'],
    ['Global/Developing Nations', 'contaminated food, poor hygiene, fecal-oral', 'bacterial', 'sustained high fever, headache, abdominal pain, rose spots, malaise, constipation', 'Typhoid Fever', 'A01'],
    ['Americas', 'contaminated food, poultry, pet reptiles', 'bacterial', 'diarrhea, abdominal cramps, fever, vomiting, nausea, bloody stool', 'Other salmonella infections', 'A02'],
    ['Sub-Saharan Africa', 'fecal-oral, direct contact, waterborne', 'bacterial', 'bloody diarrhea, abdominal cramps, fever, tenesmus, dehydration, vomiting', 'Shigellosis', 'A03'],
    ['Global', 'ingestion, contaminated food, poor cooking', 'bacterial', 'diarrhea, cramping, nausea, vomiting, fever, abdominal tenderness', 'Other bacterial intestinal infections', 'A04'],
    ['Global', 'toxins, improper storage, raw foods', 'bacterial', 'rapid onset, nausea, vomiting, abdominal pain, dizziness, weakness', 'Other bacterial food poisoning', 'A05'],
    ['Indian Subcontinent', 'contaminated water, fecal-oral, poor sanitation', 'parasitic', 'bloody diarrhea, stomach pain, fever, fatigue, weight loss, liver abscess', 'Amoebiasis', 'A06'],
    ['Americas/Europe', 'waterborne, direct contact, host-to-host', 'parasitic', 'watery diarrhea, bloating, gas, cramps, greasy stools, weight loss', 'Other protozoal intestinal diseases', 'A07'],
    ['Global', 'airborne droplets, fecal-oral, fomites', 'viral', 'vomiting, watery diarrhea, low-grade fever, abdominal cramps, nausea, muscle aches', 'Viral and other specified intestinal infections', 'A08'],
    ['Global', 'fecal-oral, contact, contaminated food', 'viral', 'diarrhea, vomiting, dehydration, abdominal discomfort, fever, loss of appetite', 'Infectious gastroenteritis and colitis, unspecified', 'A09'],

    # A15-A19: Tuberculosis
    ['Southeast Asia', 'airborne droplets, prolonged contact, coughing', 'bacterial', 'chronic cough, chest pain, fever, night sweats, weight loss, fatigue', 'Respiratory tuberculosis confirmed', 'A15'],
    ['Southeast Asia', 'airborne droplets, prolonged contact, coughing', 'bacterial', 'chronic cough, chest pain, fever, night sweats, weight loss, fatigue', 'Respiratory tuberculosis not confirmed', 'A16'],
    ['Global/Immunocompromised', 'airborne droplets, prolonged contact, coughing', 'bacterial', 'severe headache, neck stiffness, confusion, vision changes, fever, seizures', 'Tuberculosis of nervous system', 'A17'],
    ['Global/Immunocompromised', 'airborne droplets, prolonged contact, coughing', 'bacterial', 'local pain, fever, organ dysfunction, weight loss, fatigue, swollen glands', 'Tuberculosis of other organs', 'A18'],
    ['Global/Immunocompromised', 'airborne droplets, prolonged contact, coughing', 'bacterial', 'high fever, chills, weakness, breathing issues, enlarged spleen, skin lesions', 'Miliary tuberculosis', 'A19'],

    # A20-A28: Certain zoonotic bacterial diseases
    ['Central Asia', 'flea bites, rodent contact, airborne', 'bacterial', 'sudden fever, chills, headache, painful lymph nodes (buboes), weakness, coughing', 'Plague', 'A20'],
    ['North America', 'insect bites, handling animals, inhalation', 'bacterial', 'fever, skin ulcer, swollen lymph nodes, headache, joint pain, nausea', 'Tularemia', 'A21'],
    ['Global/Agricultural', 'spores, contact with animals, contaminated products', 'bacterial', 'skin sore, fever, chills, nausea, headache, difficulty breathing', 'Anthrax', 'A22'],
    ['Mediterranean/Middle East', 'unpasteurized dairy, animal contact, inhalation', 'bacterial', 'undulating fever, joint pain, sweating, fatigue, back pain, loss of appetite', 'Brucellosis', 'A23'],
    ['Southeast Asia', 'contaminated water, soil contact, inhalation', 'bacterial', 'fever, muscle aches, chest pain, coughing, lung nodules, abscesses', 'Glanders and melioidosis', 'A24'],
    ['Asia', 'rat bite, rodent urine, contaminated food', 'bacterial', 'fever, chills, vomiting, joint pain, rash, muscle aches', 'Rat-bite fever', 'A25'],
    ['Global/Occupational', 'handling infected meat, skin puncture, cuts', 'bacterial', 'purple skin lesion, fever, joint pain, swollen lymph nodes, general illness, headache', 'Erysipeloid', 'A26'],
    ['Southeast Asia', 'contaminated water, animal urine, skin contact', 'bacterial', 'high fever, headache, muscle aches, jaundice, vomiting, red eyes', 'Leptospirosis', 'A27'],
    ['Global', 'animal contact, bites, environmental', 'bacterial', 'fever, localized swelling, headache, general weakness, nausea, joint pain', 'Other zoonotic bacterial diseases', 'A28'],

    # A30-A49: Other bacterial diseases
    ['South America', 'airborne droplets, close contact, prolonged exposure', 'bacterial', 'skin lesions, nerve damage, muscle weakness, sensory loss, eye problems, nosebleeds', 'Leprosy [Hansen\'s disease]', 'A30'],
    ['Global/Immunocompromised', 'environmental, soil contact, aerosols', 'bacterial', 'lung disease, swollen lymph nodes, skin ulcers, fever, weight loss, fatigue', 'Infection due to other mycobacteria', 'A31'],
    ['Global', 'contaminated food, raw dairy, soil', 'bacterial', 'fever, muscle aches, diarrhea, stiff neck, confusion, convulsions', 'Listeriosis', 'A32'],
    ['Developing Nations', 'non-sterile delivery, umbilical cord infection', 'bacterial', 'muscle spasms, difficulty feeding, irritability, lockjaw, arching of back, seizures', 'Tetanus neonatorum', 'A33'],
    ['Developing Nations', 'non-sterile birth, wound infection', 'bacterial', 'muscle spasms, lockjaw, stiff neck, fever, irritability, sweating', 'Obstetrical tetanus', 'A34'],
    ['Global/Unvaccinated', 'deep puncture wound, soil contamination', 'bacterial', 'muscle spasms, lockjaw, stiff neck, headache, fever, excessive sweating', 'Other tetanus', 'A35'],
    ['Global/Unvaccinated', 'airborne droplets, direct contact, fomites', 'bacterial', 'sore throat, fever, swollen neck glands, difficulty breathing, bluish skin, nasal discharge', 'Diphtheria', 'A36'],
    ['Global/Infants', 'airborne droplets, direct contact, coughing', 'bacterial', 'severe coughing fits, vomiting after cough, "whoop" sound, runny nose, fatigue, apnea', 'Whooping cough', 'A37'],
    ['Global', 'airborne droplets, direct contact, saliva', 'bacterial', 'sore throat, high fever, bright red rash, strawberry tongue, headache, chills', 'Scarlet fever', 'A38'],
    ['Sub-Saharan Africa', 'airborne droplets, saliva, close contact', 'bacterial', 'sudden fever, stiff neck, severe headache, photophobia, rash, confusion', 'Meningococcal infection', 'A39'],
    ['Global', 'contact, wounds, bloodstream', 'bacterial', 'high fever, shaking chills, rapid heart rate, confusion, low blood pressure, rapid breathing', 'Streptococcal septicaemia', 'A40'],
    ['Global', 'contact, wounds, bloodstream', 'bacterial', 'high fever, shaking chills, rapid heart rate, confusion, low blood pressure, rapid breathing', 'Other septicaemia', 'A41'],
    ['Global', 'normal flora, dental procedure, trauma', 'bacterial', 'painful swelling, abscesses, draining sinus tracts, fever, weight loss, fatigue', 'Actinomycosis', 'A42'],
    ['Global/Immunocompromised', 'inhalation, soil contact, skin trauma', 'bacterial', 'persistent cough, chest pain, fever, shortness of breath, skin lesions, weight loss', 'Nocardiosis', 'A43'],
    ['South America', 'sandfly bite, cat scratch, lice', 'bacterial', 'fever, headache, fatigue, swollen glands, skin lesions, body aches', 'Bartonellosis', 'A44'],
    ['Global', 'skin break, open wound, direct contact', 'bacterial', 'bright red skin rash, raised border, fever, chills, headache, general malaise', 'Erysipelas', 'A46'],
    ['Global', 'various, contact, inhalation', 'bacterial', 'fever, localized symptoms, headache, fatigue, inflammation, body aches', 'Other bacterial diseases, not elsewhere classified', 'A48'],
    ['Global', 'various, unknown source', 'bacterial', 'fever, inflammation, fatigue, chills, body aches, localized pain', 'Bacterial infection of unspecified site', 'A49'],

    # A50-A64: Infections with a predominantly sexual mode of transmission
    ['Global', 'mother-to-child, vertical transmission', 'bacterial', 'rash, runny nose, hepatosplenomegaly, bone deformities, anemia, jaundice', 'Congenital syphilis', 'A50'],
    ['Global', 'sexual contact, direct contact', 'bacterial', 'painless chancre, rash, swollen lymph nodes, fever, sore throat, hair loss', 'Early syphilis', 'A51'],
    ['Global', 'sexual contact, direct contact', 'bacterial', 'neurological damage, heart problems, gummas, blindness, dementia, paralysis', 'Late syphilis', 'A52'],
    ['Global', 'sexual contact, direct contact', 'bacterial', 'varied, non-specific symptoms, fever, malaise, rash, headache, muscle pain', 'Other and unspecified syphilis', 'A53'],
    ['Global', 'sexual contact, mother-to-child', 'bacterial', 'painful urination, discharge, abdominal pain, fever, joint swelling, sore throat', 'Gonococcal infection', 'A54'],
    ['Africa, Asia, S America', 'sexual contact, direct contact', 'bacterial', 'swollen lymph nodes, fever, joint pain, headache, rectal pain, genital ulcers', 'Chlamydial lymphogranuloma (venereum)', 'A55'],
    ['Global', 'sexual contact, mother-to-child', 'bacterial', 'painful urination, discharge, abdominal pain, testicular pain, rectal pain, sore throat', 'Other sexually transmitted chlamydial diseases', 'A56'],
    ['Africa, Asia', 'sexual contact, direct contact', 'bacterial', 'painful genital ulcer, swollen lymph nodes, fever, pus discharge, burning sensation, headache', 'Chancroid', 'A57'],
    ['Developing Countries', 'sexual contact, direct contact', 'bacterial', 'progressive genital ulcers, bleeding, swelling, pain, lack of lymph node involvement', 'Granuloma inguinale', 'A58'],
    ['Global', 'sexual contact, direct contact, fomites', 'parasitic', 'discharge, itching, painful urination, abdominal pain, foul odor, spotting', 'Trichomoniasis', 'A59'],
    ['Global', 'sexual contact, direct contact, skin-to-skin', 'viral', 'painful blisters, ulcers, itching, flu-like symptoms, lymph node swelling, painful urination', 'Anogenital herpesviral infection', 'A60'],
    ['Global', 'sexual contact, direct contact', 'bacterial', 'genital lesions, discharge, pain, itching, swelling, fever', 'Other predominantly sexually transmitted diseases, NEC', 'A63'],
    ['Global', 'sexual contact, unknown', 'viral', 'discharge, pain, itching, rash, fever, malaise', 'Unspecified sexually transmitted disease', 'A64'],

    # A65-A69: Other spirochaetal diseases
    ['Africa, Middle East', 'non-sexual contact, oral contact, direct contact', 'bacterial', 'skin lesions, bone damage, gummas, painless ulcers, nerve deafness, eye inflammation', 'Nonvenereal syphilis', 'A65'],
    ['Africa, Southeast Asia', 'skin contact, direct contact, non-sexual contact', 'bacterial', 'painless skin nodules, bone pain, joint swelling, skin ulcers, fever, rash', 'Yaws', 'A66'],
    ['Latin America', 'skin contact, direct contact', 'bacterial', 'initial skin lesion, white skin patches, hyperpigmentation, itching, rash, scaling', 'Pinta (carate)', 'A67'],
    ['Africa, Asia', 'tick vector, louse vector, direct contact', 'bacterial', 'recurring high fever, headache, muscle aches, nausea, rash, vomiting', 'Relapsing fevers', 'A68'],
    ['Global', 'tick bite, animal contact, direct contact', 'bacterial', 'fever, rash, joint pain, headache, fatigue, neurological symptoms', 'Other spirochaetal infections', 'A69'],

    # A70-A74: Other diseases caused by Chlamydiae
    ['Global/Birds', 'avian aerosols, bird droppings, inhalation', 'bacterial', 'fever, headache, dry cough, chest pain, muscle aches, chills', 'Infection due to Chlamydia psittaci', 'A70'],
    ['Africa, Middle East', 'eye discharge, direct contact, flies', 'bacterial', 'painful eyes, inflammation, discharge, in-turned eyelashes, blurred vision, scarring', 'Trachoma', 'A71'],
    ['Global', 'various, contact, aerosols', 'bacterial', 'fever, localized inflammation, headache, body aches, joint pain, fatigue', 'Other diseases caused by Chlamydiae', 'A74'],

    # A75-A79: Rickettsioses
    ['Global/Poverty Areas', 'louse vector, flea vector, body fluids', 'bacterial', 'high fever, severe headache, rash, muscle aches, chills, confusion', 'Typhus fever', 'A75'],
    ['Global/Americas', 'tick vector, animal contact, insect bites', 'bacterial', 'fever, headache, rash, muscle pain, nausea, vomiting', 'Spotted fever [rickettsioses]', 'A77'],
    ['Global/Livestock', 'inhalation, contaminated milk, animal contact', 'bacterial', 'high fever, severe headache, dry cough, chest pain, fatigue, night sweats', 'Q fever', 'A78'],
    ['Global', 'insect vector, animal contact', 'bacterial', 'fever, rash, headache, muscle aches, malaise, chills', 'Other rickettsioses', 'A79'],

    # A80-A89: Viral infections of the central nervous system
    ['Asia, Africa', 'fecal-oral, direct contact, waterborne', 'viral', 'fever, fatigue, vomiting, stiff neck, muscle weakness, paralysis', 'Acute poliomyelitis', 'A80'],
    ['Global', 'unknown, direct contact, droplet', 'viral', 'slow onset, neurological changes, cognitive decline, ataxia, vision loss, seizure', 'Atypical virus infections of central nervous system', 'A81'],
    ['Global/Zoonotic', 'animal bite, saliva contact, direct contact', 'viral', 'fever, headache, confusion, hydrophobia, muscle spasms, paralysis', 'Rabies', 'A82'],
    ['Global/Tropical', 'mosquito vector, insect bite', 'viral', 'fever, headache, vomiting, stiff neck, confusion, seizures', 'Mosquito-borne viral encephalitis', 'A83'],
    ['Europe, Asia', 'tick vector, unpasteurized milk, blood transfusion', 'viral', 'fever, headache, vomiting, stiff neck, confusion, dizziness', 'Tick-borne viral encephalitis', 'A84'],
    ['Global', 'various, direct contact, airborne', 'viral', 'fever, headache, confusion, seizures, stiff neck, nausea', 'Other viral encephalitis, not elsewhere classified', 'A85'],
    ['Global', 'unknown, vector-borne', 'viral', 'fever, headache, confusion, seizures, stiff neck, nausea', 'Unspecified viral encephalitis', 'A86'],
    ['Global', 'airborne droplets, direct contact, fecal-oral', 'viral', 'sudden fever, severe headache, stiff neck, nausea, vomiting, photophobia', 'Viral meningitis', 'A87'],
    ['Global', 'direct contact, unknown', 'viral', 'fever, headache, vomiting, rash, malaise, body aches', 'Other viral infections of central nervous system, NEC', 'A88'],
    ['Global', 'unknown', 'viral', 'fever, headache, fatigue, stiff neck, confusion, vomiting', 'Unspecified viral infection of central nervous system', 'A89'],

    # A90-A99: Arthropod-borne viral fevers and viral haemorrhagic fevers
    ['Southeast Asia', 'mosquito vector (Aedes), insect bite', 'viral', 'high fever, severe headache, joint pain, muscle pain, rash, eye pain', 'Dengue fever', 'A90'],
    ['Southeast Asia', 'mosquito vector (Aedes), insect bite', 'viral', 'high fever, internal bleeding, shock, abdominal pain, persistent vomiting, severe fatigue', 'Dengue haemorrhagic fever', 'A91'],
    ['Americas, Africa', 'mosquito vector, insect bite', 'viral', 'fever, headache, joint pain, rash, muscle aches, eye pain', 'Other mosquito-borne viral fevers', 'A92'],
    ['Global', 'tick vector, flea vector, insect bite', 'viral', 'fever, headache, muscle aches, rash, nausea, chills', 'Other arthropod-borne viral fevers, NEC', 'A93'],
    ['Global', 'insect vector, unknown', 'viral', 'fever, headache, muscle aches, rash, malaise, chills', 'Unspecified arthropod-borne viral fever', 'A94'],
    ['Sub-Saharan Africa', 'mosquito vector (Aedes), insect bite', 'viral', 'fever, jaundice, bleeding, shock, vomiting blood, headache', 'Yellow fever', 'A95'],
    ['South America', 'rodent urine/faeces, inhalation, direct contact', 'viral', 'fever, muscle aches, headache, malaise, bleeding gums, neurological signs', 'Arenaviral haemorrhagic fever', 'A96'],
    ['Southeast Asia', 'mosquito vector (Aedes), insect bite', 'viral', 'abnormal liver function, abdominal tenderness, circulatory failure, mucosal bleeding, low platelet count, persistent vomiting', 'Severe Dengue (Dengue haemorrhagic fever/shock syndrome)', 'A97'],
    ['Africa', 'vector, animal contact, bodily fluids', 'viral', 'high fever, severe headache, bleeding, shock, muscle aches, fatigue', 'Other viral haemorrhagic fevers, not elsewhere classified', 'A98'],
    ['Global', 'unknown, vector', 'viral', 'high fever, headache, fatigue, bleeding, shock, muscle aches', 'Unspecified viral haemorrhagic fever', 'A99'],
]

sectionB = [
    ["Worldwide", ["contact", "saliva", "sexual"], "viral", ["cold sores", "genital ulcers", "fever", "blisters", "body aches", "swollen lymph nodes"], "Herpesviral infections", "B00"],
    ["Worldwide", ["airborne", "droplet", "contact"], "viral", ["rash", "fever", "itching", "fatigue", "headache", "loss of appetite"], "Varicella (chickenpox)", "B01"],
    ["Worldwide", ["contact", "reactivation", "droplet"], "viral", ["painful rash", "blisters", "burning sensation", "numbness", "itching", "fever"], "Zoster (shingles)", "B02"],
    ["Worldwide (Eradicated)", ["airborne", "droplet", "contact"], "viral", ["high fever", "rash", "pustules", "headache", "back pain", "vomiting"], "Smallpox", "B03"],
    ["Central and West Africa", ["animal bite", "contact", "droplet"], "viral", ["fever", "rash", "swollen lymph nodes", "headache", "muscle aches", "exhaustion"], "Monkeypox", "B04"],
    ["Worldwide", ["airborne", "droplet", "contact"], "viral", ["fever", "cough", "runny nose", "red eyes", "Koplik spots", "full-body rash"], "Measles", "B05"],
    ["Worldwide", ["airborne", "droplet", "contact"], "viral", ["mild fever", "rash", "swollen lymph nodes", "headache", "joint pain", "runny nose"], "Rubella (German measles)", "B06"],
    ["Worldwide", ["contact", "autoinoculation", "fomites"], "viral", ["flesh-colored growths", "rough texture", "small black dots", "itching", "discomfort", "painless lumps"], "Viral warts", "B07"],
    ["Worldwide", ["contact", "droplet", "sexual"], "viral", ["blisters", "ulcers", "rash", "fever", "sore throat", "swollen lymph nodes"], "Other viral infections with skin/mucous membrane lesions", "B08"],
    ["Worldwide", ["contact", "droplet", "airborne"], "viral", ["rash", "fever", "blisters", "lesions", "malaise", "itching"], "Unspecified viral infection with skin/mucous membrane lesions", "B09"],
    ["Worldwide", ["fecal-oral", "contaminated food", "contaminated water"], "viral", ["fatigue", "nausea", "jaundice", "abdominal pain", "dark urine", "loss of appetite"], "Acute hepatitis A", "B15"],
    ["Worldwide", ["bloodborne", "sexual", "perinatal"], "viral", ["jaundice", "fatigue", "abdominal pain", "dark urine", "joint pain", "nausea"], "Acute hepatitis B", "B16"],
    ["Worldwide", ["bloodborne", "sexual", "fecal-oral"], "viral", ["jaundice", "fatigue", "nausea", "abdominal pain", "fever", "dark urine"], "Other acute viral hepatitis", "B17"],
    ["Worldwide", ["bloodborne", "sexual", "perinatal"], "viral", ["fatigue", "jaundice", "abdominal swelling", "leg swelling", "bruising easily", "confusion"], "Chronic viral hepatitis", "B18"],
    ["Worldwide", ["bloodborne", "sexual", "fecal-oral"], "viral", ["fatigue", "mild fever", "nausea", "jaundice", "abdominal discomfort", "muscle aches"], "Unspecified viral hepatitis", "B19"],
    ["Worldwide", ["sexual", "bloodborne", "perinatal"], "viral", ["fever", "fatigue", "swollen lymph nodes", "weight loss", "night sweats", "recurrent infections"], "Human immunodeficiency virus [HIV] disease", "B20-B24"],
    ["Worldwide", ["saliva", "blood", "sexual"], "viral", ["prolonged fever", "fatigue", "pneumonia", "vision problems", "diarrhea", "weight loss"], "Cytomegaloviral disease", "B25"],
    ["Worldwide", ["droplet", "saliva", "contact"], "viral", ["swollen salivary glands", "fever", "headache", "muscle aches", "fatigue", "pain while chewing"], "Mumps", "B26"],
    ["Worldwide", ["saliva", "droplet", "contact"], "viral", ["fatigue", "fever", "sore throat", "swollen lymph nodes", "headache", "rash"], "Infectious mononucleosis", "B27"],
    ["Worldwide", ["contact", "fomites", "droplet"], "viral", ["red eyes", "watery discharge", "itching", "gritty feeling", "light sensitivity", "crusting of eyelids"], "Viral conjunctivitis", "B30"],
    ["Worldwide", ["vector-borne", "droplet", "contact"], "viral", ["fever", "rash", "headache", "joint pain", "malaise", "hemorrhage"], "Other viral diseases, not elsewhere classified", "B33"],
    ["Worldwide", ["airborne", "contact", "vector-borne"], "viral", ["fever", "cough", "sore throat", "runny nose", "body aches", "fatigue"], "Viral infection of unspecified site", "B34"],
    ["Worldwide", ["contact", "fomites", "soil"], "fungal", ["itching rash", "ring-shaped rash", "scaly skin", "hair loss", "cracked skin", "blisters"], "Dermatophytosis (Ringworm)", "B35"],
    ["Worldwide", ["contact", "environment", "overgrowth"], "fungal", ["discolored skin patches", "scaly skin", "mild itching", "powdery skin texture", "skin discoloration", "folliculitis"], "Other superficial mycoses", "B36"],
    ["Worldwide", ["overgrowth", "contact", "immunosuppression"], "fungal", ["white patches", "soreness", "redness", "itching", "cottage cheese discharge", "pain during swallowing"], "Candidiasis", "B37"],
    ["Americas (Southwest US)", ["inhalation", "soil", "dust"], "fungal", ["fever", "cough", "chest pain", "fatigue", "headache", "night sweats"], "Coccidioidomycosis", "B38"],
    ["Americas (Ohio/Mississippi River valleys)", ["inhalation", "bird droppings", "bat guano"], "fungal", ["fever", "cough", "fatigue", "chills", "headache", "chest pain"], "Histoplasmosis", "B39"],
    ["North America", ["inhalation", "soil", "wood"], "fungal", ["fever", "cough", "night sweats", "muscle aches", "weight loss", "chest pain"], "Blastomycosis", "B40"],
    ["Central and South America", ["inhalation", "soil", "trauma"], "fungal", ["mouth ulcers", "skin lesions", "cough", "fever", "weight loss", "swollen lymph nodes"], "Paracoccidioidomycosis", "B41"],
    ["Worldwide (Tropical/Subtropical)", ["thorn prick", "soil", "plant matter"], "fungal", ["painless skin nodules", "ulcers", "lesions along lymphatics", "joint pain", "cough", "shortness of breath"], "Sporotrichosis", "B42"],
    ["Worldwide (Tropical/Subtropical)", ["trauma", "soil", "wood"], "fungal", ["warty skin lesions", "cauliflower-like nodules", "slow-growing bumps", "itching", "pus drainage", "abscess"], "Chromomycosis and phaeomycotic abscess", "B43"],
    ["Worldwide", ["inhalation", "environment", "compost"], "fungal", ["cough", "wheezing", "fever", "shortness of breath", "chest pain", "coughing up blood"], "Aspergillosis", "B44"],
    ["Worldwide", ["inhalation", "bird droppings", "soil"], "fungal", ["headache", "fever", "neck stiffness", "nausea", "confusion", "light sensitivity"], "Cryptococcosis", "B45"],
    ["Worldwide", ["inhalation", "trauma", "ingestion"], "fungal", ["facial swelling", "nasal congestion", "black lesions on nose", "fever", "headache", "cough"], "Zygomycosis (Mucormycosis)", "B46"],
    ["Africa, Americas, Asia (Tropical)", ["trauma", "soil", "water"], "fungal", ["painless swelling", "nodules", "draining sinuses", "grainy discharge", "foot deformity", "abscess"], "Mycetoma", "B47"],
    ["Worldwide", ["inhalation", "trauma", "environment"], "fungal", ["fever", "cough", "skin lesions", "weight loss", "fatigue", "organ-specific symptoms"], "Other mycoses, not elsewhere classified", "B48"],
    ["Worldwide", ["inhalation", "contact", "immunosuppression"], "fungal", ["fever", "cough", "shortness of breath", "skin rash", "fatigue", "headache"], "Unspecified mycosis", "B49"],
    ["Sub-Saharan Africa, Asia, South America", ["mosquito bite", "vector-borne", "blood transfusion"], "parasitic", ["high fever", "chills", "headache", "sweats", "nausea", "severe anemia"], "Plasmodium falciparum malaria", "B50"],
    ["Asia, Latin America, some Africa", ["mosquito bite", "vector-borne", "blood transfusion"], "parasitic", ["fever", "chills", "sweats", "headache", "fatigue", "relapsing fever"], "Plasmodium vivax malaria", "B51"],
    ["Worldwide (Tropical/Subtropical)", ["mosquito bite", "vector-borne", "blood transfusion"], "parasitic", ["fever", "chills", "headache", "muscle pain", "fatigue", "fever every 72 hours"], "Plasmodium malariae malaria", "B52"],
    ["Worldwide (Tropical/Subtropical)", ["mosquito bite", "vector-borne", "blood transfusion"], "parasitic", ["fever", "chills", "headache", "nausea", "vomiting", "fatigue"], "Other specified malaria", "B53"],
    ["Worldwide (Tropical/Subtropical)", ["mosquito bite", "vector-borne", "blood transfusion"], "parasitic", ["fever", "chills", "sweating", "headache", "malaise", "body aches"], "Unspecified malaria", "B54"],
    ["Asia, Africa, Americas (Tropical/Subtropical)", ["sandfly bite", "vector-borne", "blood transfusion"], "parasitic", ["skin sores", "fever", "weight loss", "enlarged spleen", "enlarged liver", "anemia"], "Leishmaniasis", "B55"],
    ["Sub-Saharan Africa", ["tsetse fly bite", "vector-borne", "maternal-fetal"], "parasitic", ["fever", "headaches", "joint pains", "itching", "confusion", "sleep disturbances"], "African trypanosomiasis (sleeping sickness)", "B56"],
    ["Americas", ["triatomine bug bite", "vector-borne", "blood transfusion"], "parasitic", ["fever", "swelling at bite", "fatigue", "rash", "body aches", "enlarged heart"], "Chagas disease", "B57"],
    ["Worldwide", ["undercooked meat", "cat feces", "contaminated water"], "parasitic", ["flu-like symptoms", "swollen lymph nodes", "muscle aches", "headache", "fever", "blurred vision"], "Toxoplasmosis", "B58"],
    ["Worldwide", ["inhalation", "immunosuppression", "reactivation"], "fungal", ["fever", "cough", "shortness of breath", "chest pain", "fatigue", "weight loss"], "Pneumocystosis", "B59"],
    ["Worldwide", ["fecal-oral", "contaminated water", "vector-borne"], "parasitic", ["diarrhea", "abdominal cramps", "fever", "nausea", "headache", "fatigue"], "Other protozoal diseases, not elsewhere classified", "B60"],
    ["Africa, South America, Asia", ["freshwater snail contact", "waterborne", "skin penetration"], "parasitic", ["rash", "fever", "chills", "cough", "muscle aches", "abdominal pain"], "Schistosomiasis", "B65"],
    ["Worldwide", ["ingesting aquatic plants", "undercooked fish", "contaminated water"], "parasitic", ["abdominal pain", "diarrhea", "fever", "jaundice", "cough", "fatigue"], "Other fluke infections", "B66"],
    ["Worldwide", ["ingesting parasite eggs", "dog feces", "livestock contact"], "parasitic", ["cysts in organs", "abdominal pain", "nausea", "jaundice", "chest pain", "cough"], "Echinococcosis (Hydatid disease)", "B67"],
    ["Worldwide", ["undercooked meat", "fecal-oral", "ingestion"], "parasitic", ["abdominal pain", "nausea", "weight loss", "passing tapeworm segments", "loss of appetite", "dizziness"], "Taeniasis", "B68"],
    ["Worldwide", ["fecal-oral", "ingesting parasite eggs", "contaminated water"], "parasitic", ["seizures", "headaches", "cysts in muscle", "vision problems", "confusion", "swelling under skin"], "Cysticercosis", "B69"],
    ["Worldwide", ["undercooked freshwater fish", "ingestion", "contaminated water"], "parasitic", ["abdominal discomfort", "diarrhea", "vomiting", "weight loss", "vitamin B12 deficiency", "fatigue"], "Diphyllobothriasis and sparganosis", "B70"],
    ["Worldwide", ["fecal-oral", "ingestion", "undercooked meat"], "parasitic", ["abdominal pain", "nausea", "diarrhea", "weight loss", "headache", "dizziness"], "Other cestode infections", "B71"],
    ["Africa", ["contaminated water", "ingestion", "water flea"], "parasitic", ["painful skin blister", "burning sensation", "fever", "nausea", "worm emerging from skin", "secondary bacterial infection"], "Dracunculiasis (Guinea-worm disease)", "B72"],
    ["Africa, Latin America", ["blackfly bite", "vector-borne", "skin penetration"], "parasitic", ["severe itching", "skin nodules", "vision changes", "blindness", "disfiguring skin", "rash"], "Onchocerciasis (river blindness)", "B73"],
    ["Africa, Asia, Americas (Tropical)", ["mosquito bite", "vector-borne", "lymphatic system"], "parasitic", ["lymphedema", "elephantiasis", "fever", "swollen lymph nodes", "genital swelling", "pain"], "Filariasis", "B74"],
    ["Worldwide", ["undercooked meat", "ingestion", "raw pork/wild game"], "parasitic", ["nausea", "diarrhea", "muscle pain", "fever", "facial swelling", "headache"], "Trichinellosis", "B75"],
    ["Worldwide (Tropical/Subtropical)", ["skin penetration", "contaminated soil", "fecal-oral"], "parasitic", ["itching rash at entry site", "cough", "abdominal pain", "diarrhea", "anemia", "fatigue"], "Hookworm diseases", "B76"],
    ["Worldwide", ["fecal-oral", "contaminated soil", "ingestion"], "parasitic", ["abdominal pain", "cough", "intestinal blockage", "nausea", "vomiting", "malnutrition"], "Ascariasis", "B77"],
    ["Worldwide (Tropical/Subtropical)", ["skin penetration", "contaminated soil", "fecal-oral"], "parasitic", ["abdominal pain", "diarrhea", "rash", "cough", "weight loss", "vomiting"], "Strongyloidiasis", "B78"],
    ["Worldwide", ["fecal-oral", "contaminated soil", "ingestion"], "parasitic", ["painful bowel movements", "bloody diarrhea", "abdominal pain", "rectal prolapse", "malnutrition", "anemia"], "Trichuriasis (whipworm)", "B79"],
    ["Worldwide", ["fecal-oral", "autoinfection", "contact"], "parasitic", ["anal itching", "insomnia", "irritability", "abdominal pain", "nausea", "visible worms in stool"], "Enterobiasis (pinworm)", "B80"],
    ["Worldwide", ["fecal-oral", "ingestion", "contaminated soil"], "parasitic", ["diarrhea", "abdominal pain", "malnutrition", "nausea", "fatigue", "weight loss"], "Other intestinal helminthiases", "B81"],
    ["Worldwide", ["fecal-oral", "ingestion", "contact"], "parasitic", ["diarrhea", "abdominal cramps", "bloating", "nausea", "fatigue", "unexplained weight loss"], "Unspecified intestinal parasitism", "B82"],
    ["Worldwide", ["ingestion", "skin penetration", "vector-borne"], "parasitic", ["abdominal pain", "diarrhea", "muscle aches", "fever", "rash", "cough"], "Other helminthiases", "B83"],
    ["Worldwide", ["close contact", "fomites", "sexual"], "parasitic", ["intense itching", "nits (eggs) in hair", "lice on scalp/body", "red bumps", "irritability", "difficulty sleeping"], "Pediculosis and phthiriasis (Lice)", "B85"],
    ["Worldwide", ["prolonged skin contact", "sexual", "fomites"], "parasitic", ["intense itching at night", "pimple-like rash", "burrow tracks on skin", "sores from scratching", "crusted skin", "lesions between fingers"], "Scabies", "B86"],
    ["Worldwide", ["fly larvae entering body", "open wounds", "vector-borne"], "parasitic", ["painful swelling", "sensation of movement", "pus drainage", "boil-like lesion", "fever", "tissue destruction"], "Myiasis", "B87"],
    ["Worldwide", ["contact", "vector-borne", "ingestion"], "parasitic", ["itching", "rash", "fever", "swelling", "diarrhea", "abdominal pain"], "Other infestations", "B88"],
    ["Worldwide", ["vector-borne", "fecal-oral", "contact"], "parasitic", ["fever", "fatigue", "diarrhea", "rash", "weight loss", "abdominal pain"], "Unspecified parasitic disease", "B89"],
    ["Worldwide", ["prior tuberculosis infection", "reactivation", "immunosuppression"], "bacterial", ["chronic cough", "lung scarring", "respiratory failure", "skeletal deformity", "neurological deficits", "renal dysfunction"], "Sequelae of tuberculosis", "B90"],
    ["Worldwide", ["prior polio infection", "muscle weakness", "fatigue"], "viral", ["muscle pain", "joint pain", "fatigue", "new muscle weakness", "breathing difficulties", "swallowing problems"], "Sequelae of poliomyelitis", "B91"],
    ["Worldwide", ["prior leprosy infection", "nerve damage", "disfigurement"], "bacterial", ["nerve pain", "muscle weakness", "loss of sensation", "skin lesions", "deformities of limbs", "blindness"], "Sequelae of leprosy", "B92"],
    ["Worldwide", ["previous infection", "chronic inflammation", "organ damage"], "viral", ["chronic fatigue", "joint pain", "cognitive impairment", "organ dysfunction", "persistent pain", "autoimmune disorders"], "Sequelae of other and unspecified infectious diseases", "B94"],
    ["Worldwide", ["contact", "droplet", "fomites"], "bacterial", ["pus formation", "inflammation", "fever", "site-specific pain", "sepsis", "abscess"], "Streptococcus, Staphylococcus, Enterococcus as cause of other diseases", "B95"],
    ["Worldwide", ["environment", "contact", "ingestion"], "bacterial", ["fever", "inflammation", "organ-specific symptoms", "sepsis", "diarrhea", "respiratory symptoms"], "Other bacterial agents as cause of other diseases", "B96"],
    ["Worldwide", ["droplet", "contact", "vector-borne"], "viral", ["fever", "inflammation", "rash", "respiratory symptoms", "neurological symptoms", "gastrointestinal symptoms"], "Viral agents as cause of other diseases", "B97"],
    ["Worldwide", ["contact", "ingestion", "airborne"], "bacterial", ["fever", "malaise", "inflammation", "pain", "organ dysfunction", "rash"], "Other infectious diseases", "B99"]
]

sectionC = [
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

sectionD = [
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

sectionE = [
    # E00-E07: Disorders of thyroid gland
    ["Areas of iodine deficiency", ["Nutritional deficiency", "Maternal", "Environmental"], "Nutritional", ["Stunted growth", "Intellectual disability", "Coarse facial features", "Protruding tongue", "Umbilical hernia", "Hoarse cry"], "Congenital iodine-deficiency syndrome", "E00"],
    ["Areas of iodine deficiency", ["Nutritional deficiency", "Environmental", "N/A"], "Nutritional", ["Goiter", "Hypothyroidism", "Fatigue", "Weight gain", "Cold intolerance", "Dry skin"], "Iodine-deficiency-related thyroid disorders", "E01"],
    ["Areas of iodine deficiency", ["Nutritional deficiency", "Environmental", "N/A"], "Nutritional", ["Often asymptomatic", "Mild fatigue", "Slight weight gain", "Elevated TSH", "Normal T4", "Mild depression"], "Subclinical iodine-deficiency hypothyroidism", "E02"],
    ["Worldwide", ["Autoimmune", "Iatrogenic (surgical/radiation)", "Idiopathic"], "Autoimmune", ["Fatigue", "Weight gain", "Cold intolerance", "Dry skin", "Constipation", "Depression"], "Hypothyroidism", "E03"],
    ["Worldwide", ["Idiopathic", "Genetic", "Environmental"], "Endocrine", ["Thyroid enlargement (goiter)", "Swelling in neck", "Difficulty swallowing", "Difficulty breathing", "Coughing", "Hoarseness"], "Non-toxic goitre", "E04"],
    ["Worldwide", ["Autoimmune (Graves' disease)", "Nodular goiter", "Medication"], "Autoimmune", ["Weight loss", "Rapid heartbeat (tachycardia)", "Anxiety", "Hand tremor", "Heat intolerance", "Sweating"], "Thyrotoxicosis (Hyperthyroidism)", "E05"],
    ["Worldwide", ["Autoimmune (Hashimoto's)", "Viral", "Bacterial"], "Autoimmune", ["Neck pain", "Goiter", "Fatigue", "Fever", "Hypothyroid symptoms", "Hyperthyroid symptoms"], "Thyroiditis", "E06"],
    ["Worldwide", ["Genetic", "Idiopathic", "Tumor"], "Endocrine", ["Varies by disorder", "Abnormal thyroid function tests", "Goiter", "Thyroid nodules", "Pain", "Systemic symptoms"], "Other disorders of thyroid", "E07"],
    
    # E08-E14: Diabetes mellitus
    ["Worldwide", ["Secondary to other disease", "Pancreatitis", "Cystic fibrosis"], "Metabolic", ["Hyperglycemia", "Symptoms of primary disease", "Polydipsia", "Polyuria", "Weight loss", "Fatigue"], "Diabetes mellitus due to underlying condition", "E08"],
    ["Worldwide", ["Iatrogenic", "Medication (e.g., steroids)", "Chemical exposure"], "Metabolic", ["Hyperglycemia", "Polydipsia", "Polyuria", "Fatigue", "Blurred vision", "History of drug/chemical use"], "Drug or chemical induced diabetes mellitus", "E09"],
    ["Worldwide (Higher in Europe, N. America)", ["Autoimmune", "Genetic", "Environmental trigger"], "Autoimmune", ["Polydipsia (excessive thirst)", "Polyuria (frequent urination)", "Polyphagia (excessive hunger)", "Unexplained weight loss", "Fatigue", "Blurred vision"], "Type 1 diabetes mellitus", "E10"],
    ["Worldwide", ["Lifestyle", "Genetic", "Insulin resistance"], "Metabolic", ["Polydipsia", "Polyuria", "Polyphagia", "Fatigue", "Blurred vision", "Slow-healing sores"], "Type 2 diabetes mellitus", "E11"],
    ["Tropical regions (Africa, Asia)", ["Malnutrition", "Pancreatic damage", "N/A"], "Nutritional", ["Underweight", "Hyperglycemia", "Abdominal pain", "Diarrhea", "Signs of malnutrition", "Low insulin levels"], "Malnutrition-related diabetes mellitus", "E12"],
    ["Worldwide", ["Genetic defects (MODY)", "Iatrogenic (drug-induced)", "Endocrinopathies"], "Genetic", ["Hyperglycemia", "Varies by cause", "Polydipsia", "Polyuria", "Fatigue", "Blurred vision"], "Other specified diabetes mellitus", "E13"],
    ["Worldwide", ["Unknown etiology", "N/A", "N/A"], "Metabolic", ["Hyperglycemia", "Polydipsia", "Polyuria", "Polyphagia", "Fatigue", "Blurred vision"], "Unspecified diabetes mellitus", "E14"],
    
    # E15-E16: Other disorders of glucose regulation and pancreatic internal secretion
    ["Worldwide", ["Medication", "Alcohol consumption", "Critical illness"], "Metabolic", ["Loss of consciousness", "Seizures", "Confusion", "Sweating", "Pallor", "Shakiness"], "Non-diabetic hypoglycaemic coma", "E15"],
    ["Worldwide", ["Tumor (insulinoma)", "Genetic", "Idiopathic"], "Endocrine", ["Hypoglycemia", "Hyperglycemia", "Abdominal pain", "Weight loss", "Diarrhea", "Vomiting"], "Other disorders of pancreatic internal secretion", "E16"],
    
    # E20-E35: Disorders of other endocrine glands
    ["Worldwide", ["Iatrogenic (surgical)", "Autoimmune", "Genetic"], "Endocrine", ["Hypocalcemia", "Tetany (muscle cramps)", "Paresthesia (tingling)", "Seizures", "Anxiety", "Fatigue"], "Hypoparathyroidism", "E20"],
    ["Worldwide", ["Adenoma", "Hyperplasia", "Idiopathic"], "Endocrine", ["Hypercalcemia", "Bone pain", "Kidney stones", "Abdominal pain", "Depression", "Fatigue"], "Hyperparathyroidism and other disorders of parathyroid gland", "E21"],
    ["Worldwide", ["Pituitary adenoma", "Genetic", "Idiopathic"], "Endocrine", ["Acromegaly (enlarged hands/feet)", "Headache", "Vision problems", "Hormone overproduction", "Cushing disease", "Prolactinoma symptoms"], "Hyperfunction of pituitary gland", "E22"],
    ["Worldwide", ["Pituitary tumor", "Iatrogenic (surgery/radiation)", "Trauma"], "Endocrine", ["Hormone deficiency", "Fatigue", "Weight loss", "Low blood pressure", "Growth failure (children)", "Infertility"], "Hypofunction and other disorders of pituitary gland", "E23"],
    ["Worldwide", ["Pituitary adenoma", "Adrenal tumor", "Ectopic ACTH production"], "Endocrine", ["Weight gain (central obesity)", "Moon face", "Buffalo hump", "Purple striae (stretch marks)", "High blood pressure", "Muscle weakness"], "Cushing syndrome", "E24"],
    ["Worldwide", ["Genetic (CAH)", "Adrenal tumors", "N/A"], "Genetic", ["Ambiguous genitalia (female infants)", "Early puberty (males)", "Infertility", "Hirsutism (excess hair)", "Acne", "Irregular periods"], "Adrenogenital disorders", "E25"],
    ["Worldwide", ["Adrenal adenoma (Conn's syndrome)", "Bilateral adrenal hyperplasia", "N/A"], "Endocrine", ["Hypertension (high blood pressure)", "Hypokalemia (low potassium)", "Muscle weakness", "Headache", "Fatigue", "Polydipsia"], "Hyperaldosteronism", "E26"],
    ["Worldwide", ["Autoimmune (Addison's disease)", "Infection", "Tumor"], "Autoimmune", ["Fatigue", "Muscle weakness", "Weight loss", "Hyperpigmentation (dark skin)", "Low blood pressure", "Salt craving"], "Other disorders of adrenal gland", "E27"],
    ["Worldwide", ["PCOS", "Premature ovarian failure", "Autoimmune"], "Endocrine", ["Irregular periods", "Infertility", "Hirsutism", "Acne", "Weight gain", "Hot flashes"], "Ovarian dysfunction", "E28"],
    ["Worldwide", ["Genetic (Klinefelter's)", "Infection (mumps)", "Trauma"], "Genetic", ["Infertility", "Low libido", "Erectile dysfunction", "Gynecomastia (breast enlargement)", "Reduced muscle mass", "Fatigue"], "Testicular dysfunction", "E29"],
    ["Worldwide", ["Idiopathic", "Genetic", "CNS tumors"], "Endocrine", ["Precocious (early) puberty", "Delayed puberty", "Varies by type", "Early breast development", "Early testicular enlargement", "Lack of secondary sex characteristics"], "Disorders of puberty, not elsewhere classified", "E30"],
    ["Worldwide", ["Autoimmune", "Genetic", "N/A"], "Autoimmune", ["Multiple hormone deficiencies", "Addison's disease", "Hypoparathyroidism", "Type 1 diabetes", "Thyroiditis", "Vitiligo"], "Polyglandular dysfunction", "E31"],
    ["Worldwide", ["Tumor (thymoma)", "Autoimmune (myasthenia gravis)", "Genetic"], "Endocrine", ["Often asymptomatic", "Chest pain", "Cough", "Shortness of breath", "Myasthenia gravis symptoms", "Immunodeficiency"], "Diseases of thymus", "E32"],
    ["Worldwide", ["Genetic", "Tumors", "Idiopathic"], "Endocrine", ["Varies widely", "Hormone excess symptoms", "Hormone deficiency symptoms", "Growth problems", "Metabolic issues", "Puberty disorders"], "Other endocrine disorders", "E34"],
    ["Worldwide", ["Secondary to other disease", "N/A", "N/A"], "Endocrine", ["Varies by primary disease", "Thyroid dysfunction", "Adrenal dysfunction", "Pituitary dysfunction", "Pancreatic dysfunction", "Gonadal dysfunction"], "Disorders of endocrine glands in diseases classified elsewhere", "E35"],
    
    # E40-E46: Malnutrition
    ["Developing countries", ["Nutritional deficiency (protein)", "Famine", "Poverty"], "Nutritional", ["Edema (swelling)", "Distended abdomen", "Hair changes (color/texture)", "Skin lesions", "Muscle wasting", "Lethargy"], "Kwashiorkor", "E40"],
    ["Developing countries", ["Nutritional deficiency (calories)", "Famine", "Poverty"], "Nutritional", ["Severe weight loss", "Muscle wasting", "Loss of subcutaneous fat", "Emaciation ('old man' face)", "Alert and irritable", "Hunger"], "Nutritional marasmus", "E41"],
    ["Developing countries", ["Nutritional deficiency (protein & calories)", "Famine", "Poverty"], "Nutritional", ["Edema", "Severe weight loss", "Muscle wasting", "Skin lesions", "Hair changes", "Lethargy"], "Marasmic kwashiorkor", "E42"],
    ["Developing countries", ["Nutritional deficiency", "Famine", "Poverty"], "Nutritional", ["Underweight", "Wasting", "Stunting", "Edema", "Varies", "Lethargy"], "Unspecified severe protein-energy malnutrition", "E43"],
    ["Worldwide", ["Nutritional deficiency", "Poverty", "Chronic illness"], "Nutritional", ["Underweight for age", "Stunting (low height for age)", "Wasting (low weight for height)", "Frequent infections", "Poor appetite", "Fatigue"], "Protein-energy malnutrition of moderate and mild degree", "E44"],
    ["Worldwide", ["Nutritional deficiency", "Chronic illness", "N/A"], "Nutritional", ["Stunting", "Cognitive impairment", "Delayed motor development", "History of malnutrition", "Poor physical growth", "Weak immune system"], "Retarded development following protein-energy malnutrition", "E45"],
    ["Worldwide", ["Nutritional deficiency", "Poverty", "Chronic illness"], "Nutritional", ["Underweight", "Fatigue", "Poor growth", "Frequent infections", "Apathy", "Varies"], "Unspecified protein-energy malnutrition", "E46"],
    
    # E50-E64: Other nutritional deficiencies
    ["Developing countries", ["Nutritional deficiency (Vitamin A)", "Malabsorption", "N/A"], "Nutritional", ["Night blindness", "Xerophthalmia (dry eyes)", "Bitot's spots", "Corneal ulceration", "Impaired immunity", "Dry skin"], "Vitamin A deficiency", "E50"],
    ["Worldwide (associated with alcoholism, poor diet)", ["Nutritional deficiency (Thiamine)", "Alcoholism", "Malabsorption"], "Nutritional", ["Beriberi (wet/dry)", "Wernicke-Korsakoff syndrome", "Confusion", "Muscle weakness", "Peripheral neuropathy", "Heart failure (wet beriberi)"], "Thiamine deficiency", "E51"],
    ["Areas of maize-based diets", ["Nutritional deficiency (Niacin)", "Malabsorption", "Alcoholism"], "Nutritional", ["Pellagra (dermatitis, diarrhea, dementia)", "Photosensitive rash", "Glossitis (sore tongue)", "Confusion", "Apathy", "Abdominal pain"], "Niacin deficiency (Pellagra)", "E52"],
    ["Worldwide", ["Nutritional deficiency", "Malabsorption", "Alcoholism"], "Nutritional", ["Varies (B6: neuropathy, B12: anemia, Folate: anemia)", "Glossitis", "Cheilitis (cracked lips)", "Anemia", "Peripheral neuropathy", "Cognitive changes"], "Deficiency of other B group vitamins", "E53"],
    ["Worldwide (rare in developed nations)", ["Nutritional deficiency (Vitamin C)", "Poor diet", "Smoking"], "Nutritional", ["Scurvy", "Bleeding gums", "Perifollicular hemorrhage (rash)", "Joint pain", "Poor wound healing", "Fatigue"], "Ascorbic acid deficiency (Scurvy)", "E54"],
    ["Worldwide (especially northern latitudes)", ["Nutritional deficiency (Vitamin D)", "Lack of sunlight", "Malabsorption"], "Nutritional", ["Rickets (children: bone deformities)", "Osteomalacia (adults: bone pain)", "Muscle weakness", "Bone fractures", "Fatigue", "Low blood calcium"], "Vitamin D deficiency", "E55"],
    ["Worldwide (rare)", ["Nutritional deficiency (E, K)", "Malabsorption", "N/A"], "Nutritional", ["Varies (E: neuropathy, K: bleeding)", "Neuropathy", "Ataxia", "Muscle weakness", "Easy bruising", "Prolonged bleeding time"], "Other vitamin deficiencies", "E56"],
    ["Worldwide", ["Nutritional deficiency (Calcium)", "Malabsorption", "Vitamin D deficiency"], "Nutritional", ["Hypocalcemia", "Muscle cramps (tetany)", "Paresthesia", "Osteoporosis (chronic)", "Bone fractures", "Seizures (severe)"], "Nutritional calcium deficiency", "E58"],
    ["Areas with low-selenium soil", ["Nutritional deficiency (Selenium)", "Malabsorption", "N/A"], "Nutritional", ["Keshan disease (cardiomyopathy)", "Kashin-Beck disease (osteoarthritis)", "Muscle pain", "Weakness", "Impaired immunity", "Thyroid dysfunction"], "Nutritional selenium deficiency", "E59"],
    ["Worldwide", ["Nutritional deficiency (Zinc)", "Malabsorption", "Acrodermatitis enteropathica"], "Nutritional", ["Growth retardation", "Delayed puberty", "Skin rash (acrodermatitis)", "Diarrhea", "Impaired wound healing", "Hair loss"], "Nutritional zinc deficiency", "E60"],
    ["Worldwide", ["Nutritional deficiency (Copper, Manganese, etc.)", "Malabsorption", "Genetic"], "Nutritional", ["Varies by element", "Anemia (copper)", "Neurological symptoms (copper)", "Bone deformities", "Impaired growth", "Skin changes"], "Deficiency of other nutrient elements", "E61"],
    ["Worldwide", ["Nutritional deficiency", "Malabsorption", "N/A"], "Nutritional", ["Varies by specific nutrient", "Fatigue", "Weight loss", "Skin problems", "Anemia", "Cognitive issues"], "Other nutritional deficiencies", "E63"],
    ["Worldwide", ["History of malnutrition", "N/A", "N/A"], "Nutritional", ["Stunting", "Cognitive impairment", "Metabolic changes", "Increased disease risk", "Reproductive issues", "Varies"], "Sequelae of malnutrition and other nutritional deficiencies", "E64"],
    
    # E65-E68: Obesity and other hyperalimentation
    ["Worldwide", ["Lifestyle", "Genetic", "N/A"], "Lifestyle", ["Excess fat in specific areas", "Body disproportion", "Cosmetic concern", "N/A", "N/A", "N/A"], "Localized adiposity", "E65"],
    ["Worldwide", ["Lifestyle", "Genetic", "Endocrine"], "Lifestyle", ["Excess body fat (high BMI)", "Increased risk of T2DM", "Increased risk of hypertension", "Increased risk of heart disease", "Joint pain", "Sleep apnea"], "Obesity", "E66"],
    ["Worldwide", ["Excessive nutritional intake", "N/A", "N/A"], "Lifestyle", ["Weight gain", "Symptoms of vitamin toxicity", "Metabolic imbalance", "Liver problems", "N/A", "N/A"], "Other hyperalimentation", "E67"],
    ["Worldwide", ["History of hyperalimentation", "N/A", "N/A"], "Lifestyle", ["Obesity", "Metabolic syndrome", "Vitamin toxicity effects", "Liver damage", "N/A", "N/A"], "Sequelae of hyperalimentation", "E68"],
    
    # E70-E88: Metabolic disorders
    ["Worldwide", ["Genetic", "Hereditary", "Autosomal recessive"], "Genetic", ["PKU: intellectual disability", "Alkaptonuria: dark urine, arthritis", "Tyrosinemia: liver disease", "Musty odor (PKU)", "Developmental delay", "Seizures"], "Disorders of aromatic amino-acid metabolism", "E70"],
    ["Worldwide", ["Genetic", "Hereditary", "N/A"], "Genetic", ["MSUD: maple syrup odor in urine", "Vomiting", "Lethargy", "Developmental delay", "Seizures", "Metabolic acidosis"], "Disorders of branched-chain amino-acid and fatty-acid metabolism", "E71"],
    ["Worldwide", ["Genetic", "Hereditary", "N/A"], "Genetic", ["Varies by disorder", "Developmental delay", "Seizures", "Lethargy", "Vomiting", "Metabolic acidosis"], "Other disorders of amino-acid metabolism", "E72"],
    ["Worldwide", ["Genetic", "Acquired", "N/A"], "Metabolic", ["Abdominal bloating", "Diarrhea", "Flatulence", "Abdominal cramps", "Nausea", "Occurs after dairy consumption"], "Lactose intolerance", "E73"],
    ["Worldwide", ["Genetic", "Hereditary", "N/A"], "Genetic", ["Glycogen storage disease: hepatomegaly, hypoglycemia", "Galactosemia: liver failure, cataracts", "Muscle weakness", "Lethargy", "Vomiting", "Failure to thrive"], "Other disorders of carbohydrate metabolism", "E74"],
    ["Worldwide (e.g., Ashkenazi Jewish)", ["Genetic", "Hereditary", "Lysosomal storage"], "Genetic", ["Gaucher: splenomegaly, bone pain", "Tay-Sachs: neurodegeneration", "Niemann-Pick: hepatosplenomegaly", "Developmental regression", "Cherry-red spot (retina)", "Seizures"], "Disorders of sphingolipid metabolism", "E75"],
    ["Worldwide", ["Genetic", "Hereditary", "Lysosomal storage"], "Genetic", ["Mucopolysaccharidoses (e.g., Hurler)", "Coarse facial features", "Skeletal deformities", "Hepatosplenomegaly", "Corneal clouding", "Developmental delay"], "Disorders of glycosaminoglycan metabolism", "E76"],
    ["Worldwide", ["Genetic", "Hereditary", "Lysosomal storage"], "Genetic", ["Varies by disorder", "Developmental delay", "Seizures", "Coarse facial features", "Skeletal abnormalities", "Organomegaly"], "Disorders of glycoprotein metabolism", "E77"],
    ["Worldwide", ["Genetic", "Lifestyle", "N/A"], "Metabolic", ["Hypercholesterolemia (high LDL)", "Hypertriglyceridemia (high TG)", "Xanthomas (fatty deposits)", "Xanthelasmas (eyelid deposits)", "Increased risk of heart disease", "Pancreatitis (high TG)"], "Disorders of lipoprotein metabolism and other lipidaemias", "E78"],
    ["Worldwide", ["Metabolic", "Genetic", "Lifestyle"], "Metabolic", ["Gout: severe joint pain (e.g., big toe)", "Tophi (urate crystals)", "Kidney stones", "Lesch-Nyhan: self-mutilation, neuro issues", "Joint swelling", "Redness in joint"], "Disorders of purine and pyrimidine metabolism", "E79"],
    ["Worldwide", ["Genetic", "Hereditary", "N/A"], "Genetic", ["Porphyria: abdominal pain, skin photosensitivity", "Jaundice (Gilbert, Crigler-Najjar)", "Neurological symptoms", "Dark urine", "Skin blisters", "Anemia"], "Disorders of porphyrin and bilirubin metabolism", "E80"],
    ["Worldwide", ["Genetic", "Nutritional (Copper, Zinc, Iron)", "N/A"], "Metabolic", ["Wilson's disease (Copper): liver disease, neuro symptoms", "Hemochromatosis (Iron): liver disease, diabetes", "Menkes (Copper): neurodegeneration", "Kayser-Fleischer rings (Wilson's)", "Fatigue", "Joint pain"], "Disorders of mineral metabolism", "E83"],
    ["Worldwide (Higher in European ancestry)", ["Genetic", "Hereditary", "Autosomal recessive"], "Genetic", ["Persistent cough", "Frequent lung infections", "Salty-tasting skin", "Poor growth (failure to thrive)", "Greasy, bulky stools", "Male infertility"], "Cystic fibrosis", "E84"],
    ["Worldwide", ["Idiopathic", "Secondary to chronic disease", "Genetic"], "Metabolic", ["Organ dysfunction (kidney, heart, liver)", "Nephrotic syndrome", "Cardiomyopathy", "Peripheral neuropathy", "Fatigue", "Weight loss"], "Amyloidosis", "E85"],
    ["Worldwide", ["Inadequate fluid intake", "Excessive fluid loss (diarrhea, vomiting)", "N/A"], "Metabolic", ["Thirst", "Dry mouth", "Decreased urine output", "Sunken eyes", "Tachycardia (fast heart rate)", "Hypotension (low blood pressure)"], "Volume depletion (Dehydration)", "E86"],
    ["Worldwide", ["Kidney disease", "Dehydration", "Medication"], "Metabolic", ["Varies by imbalance (e.g., hyponatremia, hyperkalemia)", "Muscle weakness", "Confusion", "Arrhythmias (irregular heartbeat)", "Seizures", "Nausea"], "Other disorders of fluid, electrolyte and acid-base balance", "E87"],
    ["Worldwide", ["Genetic", "Idiopathic", "N/A"], "Metabolic", ["Varies widely", "Fatigue", "Weight change", "Neurological symptoms", "Skin changes", "Abdominal pain"], "Other metabolic disorders", "E88"],
    
    # E89-E90: Other
    ["Worldwide", ["Iatrogenic", "Surgical complication", "N/A"], "Endocrine", ["Hypothyroidism (post-thyroidectomy)", "Hypoparathyroidism (post-surgical)", "Adrenal insufficiency", "Diabetes (post-pancreatectomy)", "Hormone deficiency", "Varies by procedure"], "Postprocedural endocrine and metabolic disorders", "E89"],
    ["Worldwide", ["Secondary to primary disease", "N/A", "N/A"], "Metabolic", ["Varies by primary disease", "Weight loss (cachexia)", "Vitamin deficiencies", "Mineral deficiencies", "Electrolyte imbalance", "Malnutrition"], "Nutritional and metabolic disorders in diseases classified elsewhere", "E90"]
]

sectionF = [
    # F00-F09: Organic, including symptomatic, mental disorders
    ['Worldwide', ['Age', 'Genetics (APOE-e4)', 'Lifestyle factors'], 'Neurodegenerative', ['Progressive memory loss', 'Confusion with time/place', 'Difficulty planning', 'Language problems', 'Mood changes', 'Withdrawal from social activities'], 'Dementia in Alzheimer disease', 'F00'],
    ['Worldwide', ['High blood pressure', 'Stroke history', 'Diabetes', 'Atherosclerosis'], 'Neurodegenerative', ['Sudden cognitive decline', 'Stepwise deterioration', 'Gait disturbance', 'Problems with reasoning', 'Slowed thought', 'Emotional lability'], 'Vascular dementia', 'F01'],
    ['Worldwide', ['Parkinson disease', 'Lewy body disease', 'Pick disease', 'Huntington disease'], 'Neurodegenerative', ['Varies by underlying disease', 'Visual hallucinations', 'Fluctuating attention', 'Movement symptoms', 'Personality changes', 'Memory impairment'], 'Dementia in other diseases classified elsewhere', 'F02'],
    ['Worldwide', ['Unknown etiology', 'Advanced age', 'Multiple risk factors'], 'Neurodegenerative', ['Cognitive decline', 'Memory loss', 'Functional impairment', 'Aphasia', 'Agnosia', 'Apraxia'], 'Unspecified dementia', 'F03'],
    ['Worldwide', ['Traumatic brain injury', 'Brain hypoxia', 'Infection (e.g., HIV)', 'Tumor'], 'Organic', ['Amnesia (anterograde/retrograde)', 'Inability to learn new info', 'Confabulation', 'Lack of insight', 'Temporal disorientation', 'Preserved remote memory'], 'Organic amnesic syndrome, not induced by alcohol/substances', 'F04'],
    ['Worldwide', ['Head injury', 'Stroke', 'Brain infection', 'Substance abuse'], 'Organic', ['Hallucinations (visual/auditory)', 'Delusions', 'Agitation', 'Fluctuating consciousness', 'Disorientation', 'Sleep-wake cycle disturbance'], 'Delirium, not induced by alcohol and other psychoactive substances', 'F05'],
    ['Worldwide', ['Brain damage', 'Stroke', 'Neurodegenerative disease', 'Substance use'], 'Organic', ['Varies by specific condition', 'Cognitive deficits', 'Mood disturbance', 'Personality change', 'Amnesia', 'Hallucinations'], 'Other mental disorders due to brain damage and dysfunction', 'F06'],
    ['Worldwide', ['Brain damage (e.g., frontal lobe)', 'Head trauma', 'Stroke'], 'Organic', ['Personality change', 'Emotional lability', 'Disinhibition', 'Apathy', 'Aggressiveness', 'Impaired judgment'], 'Personality and behavioural disorders due to brain disease', 'F07'],
    ['Worldwide', ['Etiology not specified', 'Suspected brain dysfunction', 'Mixed symptoms'], 'Organic', ['Non-specific cognitive symptoms', 'Mood changes', 'Behavioral issues', 'Suspected organic cause', 'Memory problems', 'Functional decline'], 'Unspecified organic mental disorder', 'F09'], # F08 is not a standard code

    # F10-F19: Mental and behavioural disorders due to psychoactive substance use
    ['Worldwide', ['Chronic alcohol use', 'Genetics', 'Social environment'], 'Substance-related', ['Craving', 'Loss of control', 'Tolerance', 'Withdrawal symptoms', 'Neglect of other activities', 'Continued use despite harm'], 'Disorders due to use of alcohol', 'F10'],
    ['Worldwide', ['Opioid use (heroin, prescription)', 'Genetics', 'Social factors'], 'Substance-related', ['Strong craving', 'Tolerance', 'Severe withdrawal', 'Pinpoint pupils', 'Sedation', 'Neglect of responsibilities'], 'Disorders due to use of opioids', 'F11'],
    ['Worldwide', ['Cannabis use (marijuana, hashish)', 'Psychological vulnerability', 'Social factors'], 'Substance-related', ['Impaired memory/coordination', 'Anxiety/paranoia', 'Red eyes', 'Increased appetite', 'Amotivational syndrome', 'Psychological dependence'], 'Disorders due to use of cannabinoids', 'F12'],
    ['Worldwide', ['Use of sedatives/hypnotics', 'Prescription misuse', 'Stress'], 'Substance-related', ['Drowsiness', 'Slurred speech', 'Incoordination', 'Memory impairment', 'Tolerance', 'Withdrawal (anxiety, insomnia, seizures)'], 'Disorders due to use of sedatives or hypnotics', 'F13'],
    ['Worldwide', ['Cocaine use (powder, crack)', 'Genetics', 'Environmental stress'], 'Substance-related', ['Euphoria', 'Increased energy', 'Paranoia', 'Agitation', 'Dilated pupils', 'Severe "crash" (depression)'], 'Disorders due to use of cocaine', 'F14'],
    ['Worldwide', ['Use of stimulants (e.g., amphetamine, caffeine)', 'Prescription misuse', 'Performance pressure'], 'Substance-related', ['Hyperactivity', 'Insomnia', 'Loss of appetite', 'Paranoia', 'Agitation', 'Psychotic symptoms'], 'Disorders due to use of other stimulants, including caffeine', 'F15'],
    ['Worldwide', ['Use of hallucinogens (e.g., LSD, psilocybin)', 'Psychological factors', 'Social context'], 'Substance-related', ['Altered perception', 'Hallucinations (visual/auditory)', 'Distorted sense of time', 'Mood swings', 'Flashbacks', 'Paranoia'], 'Disorders due to use of hallucinogens', 'F16'],
    ['Worldwide', ['Tobacco/Nicotine use', 'Social norms', 'Genetic predisposition'], 'Substance-related', ['Strong cravings', 'Withdrawal (irritability, anxiety)', 'Tolerance', 'Continued use despite health risks', 'Difficulty quitting', 'Use to relieve withdrawal'], 'Disorders due to use of tobacco', 'F17'],
    ['Worldwide', ['Inhalation of solvents (e.g., glue, gas)', 'Socioeconomic factors', 'Peer pressure'], 'Substance-related', ['Dizziness', 'Nystagmus', 'Incoordination', 'Slurred speech', 'Hallucinations', 'Brain/organ damage'], 'Disorders due to use of volatile solvents', 'F18'],
    ['Worldwide', ['Use of multiple substances', 'Polydrug abuse patterns', 'Complex dependencies'], 'Substance-related', ['Mixed intoxication symptoms', 'Complex withdrawal', 'Severe functional impairment', 'Cross-tolerance', 'Difficulty in diagnosis', 'High-risk behaviors'], 'Disorders due to multiple drug use and use of other substances', 'F19'],

    # F20-F29: Schizophrenia, schizotypal and delusional disorders
    ['Worldwide', ['Genetics', 'Brain chemistry (Dopamine)', 'Environmental stress'], 'Psychotic', ['Hallucinations (auditory)', 'Delusions (persecutory, grandiose)', 'Disorganized speech', 'Negative symptoms (apathy, alogia)', 'Cognitive deficits', 'Social withdrawal'], 'Schizophrenia', 'F20'],
    ['Worldwide', ['Genetic link to schizophrenia', 'Personality factors', 'Family environment'], 'Psychotic', ['Odd beliefs/magical thinking', 'Unusual perceptual experiences', 'Suspiciousness/paranoia', 'Inappropriate affect', 'Social anxiety', 'Eccentric behavior'], 'Schizotypal disorder', 'F21'],
    ['Worldwide', ['Genetics', 'Brain imbalance', 'Stress', 'Isolation'], 'Psychotic', ['Non-bizarre delusions (e.g., being followed, poisoned)', 'Functional impairment is minimal', 'No prominent hallucinations', 'No disorganized speech', 'Mood is congruent with delusion', 'Lack of insight'], 'Persistent delusional disorders', 'F22'],
    ['Worldwide', ['Extreme stress', 'Trauma', 'Postpartum period', 'Sleep deprivation'], 'Psychotic', ['Sudden onset of psychosis', 'Hallucinations', 'Delusions', 'Disorganized speech/behavior', 'Emotional turmoil', 'Symptoms resolve quickly (days/weeks)'], 'Acute and transient psychotic disorders', 'F23'],
    ['Worldwide', ['Unknown etiology', 'Genetic link to schizophrenia', 'Stress'], 'Psychotic', ['Delusions (often shared with another person)', 'Shared belief system', 'Lack of insight', 'Social isolation of the pair/group', 'Passive partner accepts delusion', 'Symptoms resolve on separation'], 'Induced delusional disorder (Folie à deux)', 'F24'],
    ['Worldwide', ['Genetics', 'Brain chemistry', 'Stress'], 'Psychotic', ['Symptoms of both schizophrenia and mood disorder', 'Manic or depressive episodes', 'Psychotic symptoms present during mood episodes', 'Psychotic symptoms also present *without* mood symptoms', 'Functional impairment', 'Mixed symptom picture'], 'Schizoaffective disorders', 'F25'],
    ['Worldwide', ['Unknown etiology', 'Atypical presentation', 'Insufficient information'], 'Psychotic', ['Psychotic symptoms present', 'Does not meet criteria for other F2x disorders', 'Non-specific psychosis', 'Atypical psychosis', 'Chronic hallucinatory psychosis', 'Functional decline'], 'Other non-organic psychotic disorders', 'F28'],
    ['Worldwide', ['Insufficient data', 'Provisional diagnosis', 'Complex symptom mix'], 'Psychotic', ['Psychotic symptoms present', 'Does not fit any specific category', 'Unspecified psychosis', 'Awaiting further diagnosis', 'Impaired reality testing', 'Behavioral disturbance'], 'Unspecified non-organic psychosis', 'F29'],

    # F30-F39: Mood [affective] disorders
    ['Worldwide', ['Genetics', 'Neurotransmitter imbalance', 'Stressful life events'], 'Mood', ['Elevated/irritable mood', 'Decreased need for sleep', 'Grandiosity', 'Pressured speech', 'Flight of ideas', 'Risky/impulsive behavior'], 'Manic episode', 'F30'],
    ['Worldwide', ['Genetics', 'Brain structure/chemistry', 'Environmental triggers'], 'Mood', ['Periods of mania/hypomania', 'Periods of depression', 'Significant mood swings', 'Changes in energy/activity', 'Functional impairment', 'Sleep disturbances'], 'Bipolar affective disorder', 'F31'],
    ['Worldwide', ['Genetics', 'Brain chemistry', 'Trauma/Stress', 'Hormonal changes'], 'Mood', ['Depressed mood (most of the day)', 'Anhedonia (loss of interest)', 'Weight change/appetite change', 'Insomnia/hypersomnia', 'Fatigue/loss of energy', 'Feelings of worthlessness/guilt'], 'Depressive episode', 'F32'],
    ['Worldwide', ['Genetics', 'Chronic stress', 'Personality factors'], 'Mood', ['History of two or more depressive episodes', 'No history of mania/hypomania', 'Full remission between episodes (or partial)', 'Symptoms match F32 during episode', 'Functional impairment', 'Persistent low mood'], 'Recurrent depressive disorder', 'F33'],
    ['Worldwide', ['Chronic stress', 'Genetics', 'Personality'], 'Mood', ['Chronic depressed mood (at least 2 years)', 'Less severe than major depression', 'Poor appetite/overeating', 'Insomnia/hypersomnia', 'Low energy', 'Low self-esteem'], 'Persistent mood [affective] disorders (Dysthymia)', 'F34'],
    ['Worldwide', ['Etiology varies', 'Atypical presentation', 'Mixed symptoms'], 'Mood', ['Mood symptoms are present', 'Do not meet full criteria for F30-F34', 'Mixed affective episodes', 'Atypical depression', 'Recurrent brief depression', 'Seasonal affective disorder (SAD)'], 'Other mood [affective] disorders', 'F38'],
    ['Worldwide', ['Insufficient data', 'Symptoms are unclear', 'Provisional diagnosis'], 'Mood', ['Mood disturbance is present', 'Does not fit any specific category', 'Unspecified mood disorder', 'Awaiting further assessment', 'Clinically significant distress', 'Functional impairment'], 'Unspecified mood [affective] disorder', 'F39'],

    # F40-F48: Neurotic, stress-related and somatoform disorders
    ['Worldwide', ['Traumatic conditioning', 'Genetics', 'Learned behavior'], 'Anxiety', ['Irrational fear of a specific object/situation', 'Avoidance behavior', 'Panic attacks when exposed', 'Agoraphobia (fear of open spaces/crowds)', 'Social phobia (fear of scrutiny)', 'Anticipatory anxiety'], 'Phobic anxiety disorders', 'F40'],
    ['Worldwide', ['Genetics', 'Brain chemistry (GABA, Serotonin)', 'Chronic stress'], 'Anxiety', ['Recurrent unexpected panic attacks', 'Persistent worry about future attacks', 'Generalized Anxiety Disorder (GAD)', 'Excessive, uncontrollable worry', 'Restlessness', 'Muscle tension'], 'Other anxiety disorders', 'F41'],
    ['Worldwide', ['Genetics', 'Brain structure (Frontal cortex)', 'Learned behaviors'], 'Anxiety', ['Obsessions (intrusive, unwanted thoughts)', 'Compulsions (repetitive behaviors/mental acts)', 'Obsessions cause anxiety', 'Compulsions aim to reduce anxiety', 'Time-consuming', 'Significant distress or impairment'], 'Obsessive-compulsive disorder', 'F42'],
    ['Worldwide', ['Experiencing severe trauma/stressor', 'Personality factors', 'Lack of social support'], 'Stress-related', ['Intrusive memories/flashbacks (PTSD)', 'Avoidance of trauma reminders (PTSD)', 'Hypervigilance (PTSD)', 'Acute stress reaction (ASR)', 'Adjustment disorder (difficulty coping)', 'Emotional distress post-stressor'], 'Reaction to severe stress, and adjustment disorders', 'F43'],
    ['Worldwide', ['Psychological conflict', 'Trauma', 'Stress'], 'Dissociative', ['Loss of memory (amnesia)', 'Sense of detachment (depersonalization)', 'Feeling unreal (derealization)', 'Identity confusion/alteration', 'Sudden unexpected travel (fugue)', 'Motor/sensory loss (conversion)'], 'Dissociative [conversion] disorders', 'F44'],
    ['Worldwide', ['Heightened body awareness', 'Anxiety', 'Cognitive biases'], 'Somatoform', ['Preoccupation with physical symptoms', 'Fear of having a serious illness (hypochondriasis)', 'Physical symptoms without medical cause (somatization)', 'Persistent pain (psychogenic)', 'Doctor shopping', 'Distress about health'], 'Somatoform disorders', 'F45'],
    ['Worldwide', ['Chronic stress', 'Psychological factors', 'Anxiety'], 'Somatoform', ['Neurasthenia (fatigue, weakness)', 'Irritability', 'Headaches', 'Insomnia', 'Inability to relax', 'Dizziness'], 'Other neurotic disorders (e.g., Neurasthenia)', 'F48'],

    # F50-F59: Behavioural syndromes associated with physiological disturbances
    ['Worldwide (higher in Western cultures)', ['Societal pressure', 'Genetics', 'Psychological factors (control, perfectionism)'], 'Behavioural', ['Distorted body image', 'Intense fear of weight gain', 'Food restriction (Anorexia)', 'Binge eating (Bulimia)', 'Purging behaviors (Bulimia)', 'Significant weight loss (Anorexia)'], 'Eating disorders', 'F50'],
    ['Worldwide', ['Stress', 'Anxiety', 'Depression', 'Poor sleep hygiene'], 'Behavioural', ['Insomnia (difficulty falling/staying asleep)', 'Hypersomnia (excessive sleepiness)', 'Parasomnias (nightmares, sleepwalking)', 'Sleep-wake schedule disturbance', 'Non-restorative sleep', 'Daytime fatigue'], 'Non-organic sleep disorders', 'F51'],
    ['Worldwide', ['Psychological factors', 'Relationship problems', 'Anxiety', 'Medical conditions'], 'Behavioural', ['Lack of sexual desire', 'Sexual aversion', 'Erectile dysfunction (psychogenic)', 'Orgasmic dysfunction (psychogenic)', 'Premature ejaculation', 'Vaginismus (psychogenic)'], 'Sexual dysfunction, not caused by organic disorder', 'F52'],
    ['Worldwide', ['Hormonal changes (puerperium)', 'Psychological stress', 'History of mood disorders'], 'Behavioural', ['Postpartum depression (mild to severe)', 'Postpartum psychosis (rare, severe)', 'Onset within 6 weeks of childbirth', 'Tearfulness ("baby blues")', 'Anxiety', 'Risk of harm to self or baby'], 'Mental disorders associated with the puerperium, NEC', 'F53'],
    ['Worldwide', ['Stress', 'Anxiety', 'Learned behavior', 'Underlying personality factors'], 'Behavioural', ['Deliberate self-harm (non-suicidal)', 'Factitious disorder (faking illness)', 'Pica (eating non-nutritive items)', 'Psychogenic vomiting', 'Teeth grinding (bruxism)', 'Thumb sucking'], 'Psychological factors affecting other medical conditions', 'F54'],
    ['Worldwide', ['Stress', 'Personality', 'Substance use'], 'Behavioural', ['Type A behavior (hostility, urgency)', 'Risk-taking behaviors', 'Poor adherence to medical treatment', 'Denial of illness', 'Stress-exacerbated physical illness', 'Non-compliance with diet/exercise'], 'Abuse of non-psychoactive substances', 'F55'], # F55 is abuse of laxatives, etc. F54 is psych factors.
    ['Worldwide', ['Etiology varies', 'Stress', 'Anxiety'], 'Behavioural', ['Symptoms related to physiological function', 'Psychogenic origin', 'Does not fit F50-F55', 'Example: Globus hystericus', 'Psychogenic cough', 'Psychogenic pruritus'], 'Other behavioural syndromes', 'F59'],

    # F60-F69: Disorders of adult personality and behaviour
    ['Worldwide', ['Genetics', 'Childhood trauma', 'Invalidating environment (BPD)'], 'Personality', ['Pervasive distrust (Paranoid)', 'Social detachment (Schizoid)', 'Emotional instability (Borderline)', 'Attention-seeking (Histrionic)', 'Grandiosity (Narcissistic)', 'Fear of rejection (Avoidant)'], 'Specific personality disorders', 'F60'],
    ['Worldwide', ['Genetics', 'Childhood experiences', 'Brain structure'], 'Personality', ['Personality traits causing distress', 'Does not meet criteria for F60', 'Mixed personality features', 'Eccentric traits', 'Impulsive traits', 'Anxious traits'], 'Mixed and other personality disorders', 'F61'],
    ['Worldwide', ['Chronic stress', 'Trauma (e.g., captivity, torture)', 'Personality changes post-trauma'], 'Personality', ['Enduring personality change after catastrophic stress', 'Hostile/distrustful attitude', 'Social withdrawal', 'Feelings of emptiness', 'Chronic "on edge" feeling', 'Not attributable to brain damage'], 'Enduring personality changes, not attributable to brain damage', 'F62'],
    ['Worldwide', ['Internal psychological conflict', 'Developmental factors', 'Stress'], 'Behavioural', ['Pathological gambling', 'Pathological fire-setting (pyromania)', 'Pathological stealing (kleptomania)', 'Trichotillomania (hair-pulling)', 'Intermittent explosive disorder', 'Inability to resist harmful impulse'], 'Habit and impulse disorders', 'F63'],
    ['Worldwide', ['Developmental factors', 'Psychological conflict', 'Hormonal factors'], 'Behavioural', ['Transsexualism (desire to live as other sex)', 'Fetishism', 'Paraphilia (e.g., voyeurism, exhibitionism)', 'Gender identity disorder of childhood', 'Uncertainty about gender identity', 'Distress about sexual orientation'], 'Gender identity disorders', 'F64'],
    ['Worldwide', ['Psychological distress', 'Relationship issues', 'Developmental factors'], 'Behavioural', ['Distress about sexual orientation', 'Anxiety/depression related to identity', 'Difficulty in forming relationships', 'No primary sexual dysfunction', 'Ego-dystonic sexual orientation', 'Conflict with societal norms'], 'Psychological and behavioural disorders associated with sexual development', 'F65'], # F65 is Paraphilias, F66 is psych disorders w/ sexual dev
    ['Worldwide', ['Psychological factors', 'Stress', 'Learned behavior'], 'Behavioural', ['Deliberate elaboration of physical symptoms', 'Exaggeration of symptoms (malingering)', 'Factitious disorder (Munchausen)', 'Seeking the "sick role"', 'Wandering from hospital to hospital', 'Self-inflicted injury for gain'], 'Other disorders of adult personality and behaviour', 'F68'],
    ['Worldwide', ['Insufficient data', 'Awaiting diagnosis', 'Complex presentation'], 'Personality', ['Personality disturbance present', 'Does not fit any specific category', 'Unspecified personality disorder', 'Clinically significant impairment', 'Pervasive pattern of behavior', 'Distress'], 'Unspecified disorder of adult personality and behaviour', 'F69'],

    # F70-F79: Mental retardation (Intellectual disabilities)
    ['Worldwide', ['Genetic conditions', 'Prenatal factors', 'Socioeconomic factors'], 'Developmental', ['IQ approx 50-69', 'Slower academic learning', 'Can achieve social/vocational skills', 'Needs some support', 'Concrete thinking', 'Social immaturity'], 'Mild intellectual disability', 'F70'],
    ['Worldwide', ['Genetic conditions (e.g., Down syndrome)', 'Birth complications', 'Prenatal infections'], 'Developmental', ['IQ approx 35-49', 'Marked developmental delays', 'Can learn basic self-care', 'Requires moderate supervision/support', 'Simple communication skills', 'Limited academic skills'], 'Moderate intellectual disability', 'F71'],
    ['Worldwide', ['Genetic syndromes', 'Severe birth trauma/hypoxia', 'Prenatal toxin exposure'], 'Developmental', ['IQ approx 20-34', 'Requires extensive support', 'Minimal communication skills', 'Can learn simple self-care tasks', 'Poor motor skills', 'Lifelong supervision needed'], 'Severe intellectual disability', 'F72'],
    ['Worldwide', ['Severe neurological disorders', 'Genetic abnormalities', 'Extreme prenatal damage'], 'Developmental', ['IQ below 20', 'Requires 24/7 care and supervision', 'Minimal or no communication', 'Severe motor impairment', 'High incidence of physical health problems', 'Basic sensory-motor function only'], 'Profound intellectual disability', 'F73'],
    ['Worldwide', ['Etiology varies', 'Comorbid conditions', 'Assessment difficulties'], 'Developmental', ['Significant intellectual deficits', 'Does not fit F70-F73 criteria', 'Atypical presentation', 'Associated with other disorders', 'Learning difficulties', 'Impaired adaptive functioning'], 'Other intellectual disabilities', 'F78'],
    ['Worldwide', ['Insufficient data', 'Assessment incomplete', 'Provisional diagnosis'], 'Developmental', ['Intellectual disability is present', 'Severity is not yet determined', 'Unspecified cognitive deficits', 'Impaired adaptive functioning', 'Awaiting further testing', 'Used when assessment is difficult'], 'Unspecified intellectual disability', 'F79'],

    # F80-F89: Disorders of psychological development
    ['Worldwide', ['Genetics', 'Neurological factors', 'Auditory processing issues'], 'Developmental', ['Delayed speech onset', 'Difficulty with articulation (phonology)', 'Limited vocabulary', 'Difficulty forming sentences (expressive)', 'Difficulty understanding language (receptive)', 'Normal non-verbal intelligence'], 'Specific developmental disorders of speech and language', 'F80'],
    ['Worldwide', ['Genetics', 'Neurological factors', 'Unknown etiology'], 'Developmental', ['Difficulty with reading (dyslexia)', 'Difficulty with spelling', 'Difficulty with mathematics (dyscalculia)', 'Academic performance below IQ', 'Not due to lack of schooling', 'Co-occurs with other F8x disorders'], 'Specific developmental disorders of scholastic skills', 'F81'],
    ['Worldwide', ['Neurological factors', 'Unknown etiology', 'Often co-occurs with F80/F81'], 'Developmental', ['Clumsiness', 'Poor coordination', 'Difficulty with fine motor skills (writing)', 'Difficulty with gross motor skills (sports)', 'Motor milestones may be delayed', 'Not due to other medical condition'], 'Specific developmental disorder of motor function', 'F82'],
    ['Worldwide', ['Etiology unclear', 'Atypical presentation', 'Mixed symptoms'], 'Developmental', ['Mix of symptoms from F80, F81, F82', 'Does not meet full criteria for any single one', 'Overlapping developmental delays', 'Learning difficulties', 'Speech problems', 'Coordination issues'], 'Mixed specific developmental disorders', 'F83'],
    ['Worldwide', ['Genetics', 'Neurological differences', 'Prenatal environment'], 'Developmental', ['Deficits in social-emotional reciprocity', 'Deficits in non-verbal communication', 'Repetitive motor movements/speech', 'Restricted, fixated interests', 'Sensory sensitivities', 'Need for routine (Autism Spectrum Disorder)'], 'Pervasive developmental disorders', 'F84'],
    ['Worldwide', ['Etiology varies', 'Atypical presentation', 'Comorbid conditions'], 'Developmental', ['Developmental disorder present', 'Does not fit F80-F84', 'Atypical autism', 'Asperger syndrome (historical)', 'Rett syndrome (historical)', 'Childhood disintegrative disorder (historical)'], 'Other disorders of psychological development', 'F88'],
    ['Worldwide', ['Insufficient data', 'Assessment incomplete', 'Provisional diagnosis'], 'Developmental', ['Developmental delay/disorder present', 'Specifics are undetermined', 'Unspecified developmental issue', 'Awaiting further assessment', 'Clinically significant impairment', 'Symptoms onset in childhood'], 'Unspecified disorder of psychological development', 'F89'],

    # F90-F98: Behavioural and emotional disorders with onset in childhood
    ['Worldwide', ['Genetics', 'Brain structure/function', 'Neurotransmitter imbalance'], 'Developmental', ['Inattention (easily distracted, poor organization)', 'Hyperactivity (fidgeting, inability to sit still)', 'Impulsivity (interrupting, risk-taking)', 'Symptoms present in multiple settings', 'Functional impairment (school, social)', 'Onset before age 12'], 'Hyperkinetic disorders (ADHD)', 'F90'],
    ['Worldwide', ['Harsh parenting', 'Family dysfunction', 'Peer rejection', 'Genetic factors'], 'Behavioural', ['Aggression towards people/animals', 'Destruction of property (fire-setting)', 'Deceitfulness or theft', 'Serious violation of rules (truancy, running away)', 'Lack of remorse or empathy', 'Persistent pattern of anti-social behavior'], 'Conduct disorders', 'F91'],
    ['Worldwide', ['Etiology unclear', 'Atypical presentation', 'Mixed symptoms'], 'Behavioural', ['Mix of conduct and emotional symptoms', 'Persistent depression/anxiety', 'Co-occurring aggression/defiance', 'Social withdrawal', 'Low self-esteem', 'Symptoms cause significant impairment'], 'Mixed disorders of conduct and emotions', 'F92'],
    ['Worldwide', ['Genetics', 'Anxiety-prone temperament', 'Stressful life events'], 'Behavioural', ['Separation anxiety disorder', 'Phobic disorder of childhood', 'Social anxiety of childhood', 'Generalized anxiety of childhood', 'Excessive worry', 'Avoidance behavior'], 'Emotional disorders with onset specific to childhood', 'F93'],
    ['Worldwide', ['Family dysfunction', 'Trauma/neglect', 'Social isolation'], 'Behavioural', ['Elective mutism (refusal to speak in certain situations)', 'Reactive attachment disorder (RAD)', 'Disinhibited social engagement disorder (DSED)', 'Poor social relationships', 'Withdrawal or inappropriate socialness', 'Onset in childhood'], 'Disorders of social functioning with onset specific to childhood', 'F94'],
    ['Worldwide', ['Neurological factors', 'Stress', 'Genetics'], 'Behavioural', ['Involuntary, repetitive motor movements (tics)', 'Involuntary vocalizations (tics)', 'Tourette syndrome (both motor and vocal tics)', 'Transient tic disorder', 'Chronic motor or vocal tic disorder', 'Tics worsen with stress'], 'Tic disorders', 'F95'],
    ['Worldwide', ['Stress', 'Developmental factors', 'Unknown etiology'], 'Behavioural', ['Enuresis (involuntary urination)', 'Encopresis (involuntary defecation)', 'Pica of infancy/childhood', 'Stuttering', 'Cluttering (rapid, disorganized speech)', 'Stereotyped movement disorders'], 'Other behavioural and emotional disorders with onset in childhood', 'F98'], 
    ['Worldwide', ['Insufficient data', 'Atypical presentation', 'Provisional diagnosis'], 'Unspecified', ['Psychological distress', 'Functional impairment','Does not meet full criteria for any other disorder', 'Atypical presentation of a known disorder', 'Symptoms are present but undefined', 'Used when diagnosis is uncertain'], 'Mental disorder, not otherwise specified', 'F99']
]

sectionG = [
    # (G00-G09) Inflammatory diseases of the central nervous system
    [
        "Worldwide",
        ["droplet", "direct_contact", "bloodborne"],
        "bacterial",
        ["severe_headache", "fever", "nuchal_rigidity", "photophobia", "confusion", "vomiting"],
        "Bacterial meningitis, not elsewhere classified",
        "G00"
    ],
    [
        "Varies (e.g., Africa)",
        ["vector_borne", "zoonotic", "waterborne"],
        "parasitic",
        ["headache", "fever", "stiff_neck", "seizures", "hallucinations", "altered_mental_state"],
        "Meningitis in other infectious and parasitic diseases",
        "G01"
    ],
    [
        "Worldwide",
        ["non_infectious", "secondary_disease", "autoimmune"],
        "autoimmune",
        ["headache", "confusion", "fever", "seizures", "mood_changes", "cognitive_decline"],
        "Meningitis in other specified diseases",
        "G02"
    ],
    [
        "Worldwide",
        ["idiopathic", "chemical", "drug_induced"],
        "idiopathic",
        ["headache", "fever", "nausea", "stiff_neck", "malaise", "photophobia"],
        "Meningitis due to other and unspecified causes",
        "G03"
    ],
    [
        "Worldwide",
        ["viral", "vector_borne", "post_infectious"],
        "viral",
        ["fever", "headache", "seizures", "confusion", "weakness", "sensory_loss"],
        "Encephalitis, myelitis and encephalomyelitis",
        "G04"
    ],
    [
        "Worldwide",
        ["autoimmune", "post_vaccinal", "secondary_disease"],
        "autoimmune",
        ["weakness", "numbness", "vision_loss", "fever", "headache", "paralysis"],
        "Encephalitis, myelitis and encephalomyelitis in diseases classified elsewhere",
        "G05"
    ],
    [
        "Worldwide",
        ["bacterial", "fungal", "direct_spread"],
        "bacterial",
        ["headache", "fever", "focal_neurological_deficits", "seizures", "nausea", "lethargy"],
        "Intracranial and intraspinal abscess and granuloma",
        "G06"
    ],
    [
        "Varies (e.g., Americas)",
        ["parasitic", "fungal", "secondary_disease"],
        "parasitic",
        ["seizures", "headache", "hydrocephalus", "focal_deficits", "vision_changes", "confusion"],
        "Intracranial and intraspinal abscess and granuloma in diseases classified elsewhere",
        "G07"
    ],
    [
        "Worldwide",
        ["post_infectious", "post_surgical", "hypercoagulable_state"],
        "vascular",
        ["headache", "seizures", "focal_neurological_deficits", "papilledema", "vision_loss", "altered_consciousness"],
        "Intracranial and intraspinal phlebitis and thrombophlebitis",
        "G08"
    ],
    [
        "Worldwide",
        ["not_applicable", "post_infectious", "chronic_phase"],
        "post_infectious",
        ["cognitive_impairment", "hearing_loss", "vision_loss", "motor_deficits", "seizure_disorder", "hydrocephalus"],
        "Sequelae of inflammatory diseases of central nervous system",
        "G09"
    ],

    # (G10-G14) Systemic atrophies primarily affecting the CNS
    [
        "Worldwide (European ancestry)",
        ["genetic", "autosomal_dominant", "hereditary"],
        "genetic",
        ["chorea", "cognitive_decline", "depression", "irritability", "poor_coordination", "difficulty_swallowing"],
        "Huntington's disease",
        "G10"
    ],
    [
        "Worldwide",
        ["genetic", "hereditary", "autosomal_recessive"],
        "genetic",
        ["gait_ataxia", "dysarthria", "nystagmus", "loss_of_reflexes", "scoliosis", "cardiomyopathy"],
        "Hereditary ataxia",
        "G11"
    ],
    [
        "Worldwide",
        ["genetic", "autosomal_recessive", "hereditary"],
        "genetic",
        ["progressive_muscle_weakness", "hypotonia", "absent_reflexes", "difficulty_breathing", "difficulty_swallowing", "scoliosis"],
        "Spinal muscular atrophy and related syndromes",
        "G12"
    ],
    [
        "Worldwide",
        ["secondary_disease", "prion", "metabolic"],
        "prion",
        ["rapid_cognitive_decline", "myoclonus", "ataxia", "vision_problems", "personality_changes", "insomnia"],
        "Systemic atrophies primarily affecting central nervous system in diseases classified elsewhere",
        "G13"
    ],
    [
        "Worldwide (polio survivors)",
        ["not_applicable", "post_infectious", "viral_sequelae"],
        "post_infectious",
        ["new_muscle_weakness", "fatigue", "joint_pain", "muscle_atrophy", "cold_intolerance", "breathing_difficulty"],
        "Postpolio syndrome",
        "G14"
    ],

    # (G20-G26) Extrapyramidal and movement disorders
    [
        "Worldwide",
        ["idiopathic", "genetic_factors", "environmental_factors"],
        "degenerative",
        ["bradykinesia", "resting_tremor", "rigidity", "postural_instability", "shuffling_gait", "masked_facies"],
        "Parkinson's disease",
        "G20"
    ],
    [
        "Worldwide",
        ["drug_induced", "vascular", "post_traumatic"],
        "environmental_toxin",
        ["parkinsonian_symptoms", "bradykinesia", "rigidity", "tremor", "gait_disturbance", "dementia"],
        "Secondary parkinsonism",
        "G21"
    ],
    [
        "Worldwide",
        ["secondary_disease", "degenerative", "infectious"],
        "degenerative",
        ["parkinsonian_symptoms", "ataxia", "dementia", "autonomic_dysfunction", "oculomotor_problems", "myoclonus"],
        "Parkinsonism in diseases classified elsewhere",
        "G22"
    ],
    [
        "Worldwide",
        ["genetic", "idiopathic", "degenerative"],
        "degenerative",
        ["gait_instability", "frequent_falls", "supranuclear_gaze_palsy", "dysarthria", "dysphagia", "cognitive_impairment"],
        "Other degenerative diseases of basal ganglia",
        "G23"
    ],
    [
        "Worldwide",
        ["idiopathic", "genetic", "post_traumatic"],
        "idiopathic",
        ["involuntary_muscle_contractions", "twisting_movements", "abnormal_postures", "task_specific_cramps", "blepharospasm", "torticollis"],
        "Dystonia",
        "G24"
    ],
    [
        "Worldwide",
        ["idiopathic", "genetic", "drug_induced"],
        "idiopathic",
        ["action_tremor", "head_tremor", "voice_tremor", "restless_legs", "myoclonus", "tics"],
        "Other extrapyramidal and movement disorders",
        "G25"
    ],
    [
        "Worldwide",
        ["secondary_disease", "metabolic", "infectious"],
        "metabolic",
        ["tremor", "dystonia", "parkinsonism", "psychiatric_symptoms", "liver_disease", "kayser_fleischer_rings"],
        "Extrapyramidal and movement disorders in diseases classified elsewhere",
        "G26"
    ],

    # (G30-G32) Other degenerative diseases of the nervous system
    [
        "Worldwide",
        ["idiopathic", "genetic_factors", "age_related"],
        "degenerative",
        ["memory_loss", "confusion", "language_difficulty", "poor_judgement", "mood_changes", "disorientation"],
        "Alzheimer's disease",
        "G30"
    ],
    [
        "Worldwide",
        ["idiopathic", "genetic", "degenerative"],
        "degenerative",
        ["cognitive_decline", "visual_hallucinations", "parkinsonism", "fluctuating_alertness", "rem_sleep_disorder", "autonomic_dysfunction"],
        "Other degenerative diseases of nervous system, not elsewhere classified",
        "G31"
    ],
    [
        "Worldwide",
        ["secondary_disease", "metabolic", "vitamin_deficiency"],
        "metabolic",
        ["numbness_tingling", "weakness", "ataxia", "vision_changes", "cognitive_impairment", "spasticity"],
        "Other degenerative disorders of nervous system in diseases classified elsewhere",
        "G32"
    ],

    # (G35-G37) Demyelinating diseases of the central nervous system
    [
        "Worldwide (high-latitude)",
        ["autoimmune", "idiopathic", "genetic_predisposition"],
        "autoimmune",
        ["optic_neuritis", "fatigue", "numbness_tingling", "spasticity", "gait_difficulty", "bladder_dysfunction"],
        "Multiple sclerosis",
        "G35"
    ],
    [
        "Worldwide",
        ["post_infectious", "post_vaccinal", "autoimmune"],
        "autoimmune",
        ["fever", "headache", "confusion", "seizures", "weakness", "vision_loss"],
        "Other acute disseminated demyelination",
        "G36"
    ],
    [
        "Worldwide",
        ["autoimmune", "idiopathic", "infectious"],
        "autoimmune",
        ["optic_neuritis", "transverse_myelitis", "paralysis", "sensory_loss", "bladder_dysfunction", "intractable_hiccups"],
        "Other demyelinating diseases of central nervous system",
        "G37"
    ],

    # (G40-G47) Episodic and paroxysmal disorders
    [
        "Worldwide",
        ["idiopathic", "genetic", "post_traumatic"],
        "idiopathic",
        ["seizures", "aura", "loss_of_consciousness", "convulsions", "automatisms", "postictal_confusion"],
        "Epilepsy",
        "G40"
    ],
    [
        "Worldwide",
        ["complication_of_epilepsy", "metabolic_insult", "infection"],
        "complication",
        ["prolonged_seizure", "recurrent_seizures_without_recovery", "loss_of_consciousness", "convulsive_movements", "autonomic_instability", "hyperthermia"],
        "Status epilepticus",
        "G41"
    ],
    [
        "Worldwide",
        ["idiopathic", "genetic_predisposition", "environmental_triggers"],
        "idiopathic",
        ["throbbing_headache", "nausea", "photophobia", "phonophobia", "aura", "vomiting"],
        "Migraine",
        "G43"
    ],
    [
        "Worldwide",
        ["idiopathic", "vascular", "autonomic"],
        "idiopathic",
        ["severe_unilateral_headache", "ipsilateral_autonomic_features", "restlessness", "lacrimation", "nasal_congestion", "ptosis"],
        "Other headache syndromes",
        "G44"
    ],
    [
        "Worldwide",
        ["vascular", "thromboembolic", "atherosclerosis"],
        "vascular",
        ["transient_focal_neurological_deficit", "slurred_speech", "unilateral_weakness", "vision_loss", "dizziness", "transient_aphasia"],
        "Transient cerebral ischaemic attacks (TIA) and related syndromes",
        "G45"
    ],
    [
        "Worldwide",
        ["vascular", "stroke", "hemorrhage"],
        "vascular",
        ["hemiplegia", "aphasia", "hemisensory_loss", "ataxia", "diplopia", "vertigo"],
        "Vascular syndromes of brain in cerebrovascular diseases",
        "G46"
    ],
    [
        "Worldwide",
        ["idiopathic", "neurological", "psychophysiological"],
        "idiopathic",
        ["excessive_daytime_sleepiness", "cataplexy", "sleep_paralysis", "hypnagogic_hallucinations", "insomnia", "sleep_apnea"],
        "Sleep disorders",
        "G47"
    ],

    # (G50-G59) Nerve, nerve root and plexus disorders
    [
        "Worldwide",
        ["idiopathic", "vascular_compression", "post_traumatic"],
        "idiopathic",
        ["severe_facial_pain", "electric_shock_pain", "pain_triggered_by_touch", "unilateral_pain", "brief_paroxysms_of_pain", "facial_numbness"],
        "Trigeminal nerve disorders",
        "G50"
    ],
    [
        "Worldwide",
        ["idiopathic", "viral", "autoimmune"],
        "idiopathic",
        ["unilateral_facial_paralysis", "inability_to_close_eye", "facial_droop", "hyperacusis", "loss_of_taste", "eye_dryness"],
        "Facial nerve disorders",
        "G51"
    ],
    [
        "Worldwide",
        ["vascular", "compression", "idiopathic"],
        "vascular",
        ["throat_pain", "ear_pain", "swallowing_difficulty", "diplopia", "vertigo", "hoarseness"],
        "Disorders of other cranial nerves",
        "G52"
    ],
    [
        "Worldwide",
        ["secondary_disease", "infectious", "neoplastic"],
        "infectious",
        ["facial_palsy", "diplopia", "hearing_loss", "vertigo", "headache", "meningitis_symptoms"],
        "Cranial nerve disorders in diseases classified elsewhere",
        "G53"
    ],
    [
        "Worldwide",
        ["physical_trauma", "compression", "autoimmune"],
        "physical_trauma",
        ["arm_weakness", "arm_numbness", "arm_pain", "paralysis_of_arm", "loss_of_reflexes", "muscle_atrophy"],
        "Nerve root and plexus disorders",
        "G54"
    ],
    [
        "Worldwide",
        ["secondary_disease", "neoplastic", "degenerative_disc_disease"],
        "degenerative",
        ["radicular_pain", "weakness_in_dermatome", "numbness_in_dermatome", "loss_of_reflexes", "gait_difficulty", "back_pain"],
        "Nerve root and plexus compressions in diseases classified elsewhere",
        "G55"
    ],
    [
        "Worldwide",
        ["compression", "repetitive_strain", "physical_trauma"],
        "compression",
        ["hand_numbness", "hand_tingling", "hand_pain", "weakness_of_grip", "thenar_atrophy", "night_symptoms"],
        "Mononeuropathies of upper limb",
        "G56"
    ],
    [
        "Worldwide",
        ["compression", "physical_trauma", "vascular"],
        "compression",
        ["leg_pain", "leg_numbness", "leg_weakness", "foot_drop", "tingling_down_leg", "loss_of_ankle_reflex"],
        "Mononeuropathies of lower limb",
        "G57"
    ],
    [
        "Worldwide",
        ["compression", "idiopathic", "post_surgical"],
        "compression",
        ["focal_weakness", "focal_numbness", "focal_pain", "muscle_atrophy", "intercostal_neuralgia", "focal_sensory_loss"],
        "Other mononeuropathies",
        "G58"
    ],
    [
        "Worldwide",
        ["secondary_disease", "vascular", "infectious"],
        "vascular",
        ["acute_focal_pain", "focal_weakness", "focal_numbness", "cranial_nerve_palsy", "muscle_wasting", "autonomic_symptoms"],
        "Mononeuropathy in diseases classified elsewhere",
        "G59"
    ],

    # (G60-G65) Polyneuropathies and other disorders of the peripheral nervous system
    [
        "Worldwide",
        ["genetic", "hereditary", "idiopathic"],
        "genetic",
        ["distal_weakness", "distal_muscle_atrophy", "high_arched_feet", "sensory_loss", "absent_reflexes", "gait_difficulty"],
        "Hereditary and idiopathic neuropathy",
        "G60"
    ],
    [
        "Worldwide",
        ["autoimmune", "post_infectious", "idiopathic"],
        "autoimmune",
        ["ascending_paralysis", "areflexia", "paresthesia", "autonomic_dysfunction", "respiratory_failure", "back_pain"],
        "Inflammatory polyneuropathy",
        "G61"
    ],
    [
        "Worldwide",
        ["metabolic", "environmental_toxin", "vitamin_deficiency"],
        "metabolic",
        ["distal_numbness", "tingling", "burning_pain", "loss_of_vibration_sense", "weakness", "glove_and_stocking_distribution"],
        "Other polyneuropathies",
        "G62"
    ],
    [
        "Worldwide",
        ["secondary_disease", "neoplastic", "infectious"],
        "infectious",
        ["skin_lesions", "sensory_loss", "motor_weakness", "thickened_nerves", "anhidrosis", "trophic_ulcers"],
        "Polyneuropathy in diseases classified elsewhere",
        "G63"
    ],
    [
        "Worldwide",
        ["idiopathic", "autoimmune", "toxic"],
        "idiopathic",
        ["sensory_disturbances", "motor_weakness", "autonomic_symptoms", "chronic_pain", "paresthesia", "dysesthesia"],
        "Other disorders of peripheral nervous system",
        "G64"
    ],
    [
        "Worldwide",
        ["not_applicable", "chronic_phase", "post_inflammatory"],
        "post_infectious",
        ["chronic_weakness", "residual_numbness", "gait_instability", "chronic_pain", "muscle_atrophy", "contractures"],
        "Sequelae of inflammatory polyneuropathy and other polyneuropathies",
        "G65"
    ],
    
    # (G70-G73) Diseases of myoneural junction and muscle
    [
        "Worldwide",
        ["autoimmune", "genetic", "idiopathic"],
        "autoimmune",
        ["fluctuating_muscle_weakness", "ptosis", "diplopia", "dysphagia", "dysarthria", "fatigability"],
        "Myasthenia gravis and other myoneural disorders",
        "G70"
    ],
    [
        "Worldwide",
        ["genetic", "hereditary", "degenerative"],
        "genetic",
        ["progressive_muscle_weakness", "gower_sign", "calf_pseudohypertrophy", "waddling_gait", "scoliosis", "cardiomyopathy"],
        "Primary disorders of muscles",
        "G71"
    ],
    [
        "Worldwide",
        ["drug_induced", "endocrine", "metabolic"],
        "drug_induced",
        ["muscle_pain", "muscle_weakness", "elevated_ck", "cramps", "fatigue", "rhabdomyolysis"],
        "Other myopathies",
        "G72"
    ],
    [
        "Worldwide",
        ["secondary_disease", "neoplastic", "endocrine"],
        "neoplastic",
        ["proximal_weakness", "autonomic_dysfunction", "dry_mouth", "absent_reflexes", "post_exercise_facilitation", "ptosis"],
        "Disorders of myoneural junction and muscle in diseases classified elsewhere",
        "G73"
    ],

    # (G80-G83) Cerebral palsy and other paralytic syndromes
    [
        "Worldwide",
        ["congenital", "perinatal_injury", "anoxia"],
        "congenital",
        ["motor_delay", "abnormal_muscle_tone", "spasticity", "ataxia", "dystonia", "seizures"],
        "Cerebral palsy",
        "G80"
    ],
    [
        "Worldwide",
        ["vascular", "post_traumatic", "neoplastic"],
        "vascular",
        ["unilateral_paralysis", "unilateral_weakness", "spasticity", "loss_of_sensation_one_side", "aphasia", "hemispatial_neglect"],
        "Hemiplegia",
        "G81"
    ],
    [
        "Worldwide",
        ["physical_trauma", "vascular", "infectious"],
        "physical_trauma",
        ["paralysis_of_legs", "paralysis_of_all_limbs", "loss_of_sensation_below_lesion", "bladder_dysfunction", "bowel_dysfunction", "spasticity"],
        "Paraplegia and tetraplegia",
        "G82"
    ],
    [
        "Worldwide",
        ["idiopathic", "post_infectious", "post_traumatic"],
        "idiopathic",
        ["transient_weakness_post_seizure", "monoplegia", "diplegia", "focal_paralysis", "flaccid_paralysis", "spastic_paralysis"],
        "Other paralytic syndromes",
        "G83"
    ],

    # (G90-G99) Other disorders of the nervous system
    [
        "Worldwide",
        ["idiopathic", "degenerative", "secondary_disease"],
        "idiopathic",
        ["orthostatic_intolerance", "tachycardia_on_standing", "dizziness", "syncope", "fatigue", "brain_fog"],
        "Disorders of autonomic nervous system",
        "G90"
    ],
    [
        "Worldwide",
        ["congenital", "post_infectious", "post_hemorrhagic"],
        "congenital",
        ["headache", "nausea", "vomiting", "papilledema", "gait_disturbance", "cognitive_decline"],
        "Hydrocephalus",
        "G91"
    ],
    [
        "Worldwide",
        ["environmental_toxin", "drug_induced", "metabolic"],
        "environmental_toxin",
        ["confusion", "memory_loss", "headache", "seizures", "personality_changes", "ataxia"],
        "Toxic encephalopathy",
        "G92"
    ],
    [
        "Worldwide",
        ["idiopathic", "vascular", "post_infectious"],
        "post_infectious",
        ["vomiting", "confusion", "lethargy", "seizures", "coma", "cerebral_edema"],
        "Other disorders of brain",
        "G93"
    ],
    [
        "Worldwide",
        ["secondary_disease", "metabolic", "endocrine"],
        "metabolic",
        ["confusion", "asterixis", "lethargy", "personality_changes", "coma", "somnolence"],
        "Other disorders of brain in diseases classified elsewhere",
        "G94"
    ],
    [
        "Worldwide",
        ["idiopathic", "congenital", "vascular"],
        "idiopathic",
        ["pain_and_temperature_loss", "cape_like_sensory_loss", "weakness", "spasticity", "scoliosis", "headache"],
        "Other diseases of spinal cord",
        "G95"
    ],
    [
        "Worldwide",
        ["idiopathic", "autoimmune", "physical_trauma"],
        "idiopathic",
        ["orthostatic_headache", "nausea", "tinnitus", "photophobia", "neck_pain", "muffled_hearing"],
        "Other disorders of central nervous system",
        "G96"
    ],
    [
        "Worldwide",
        ["post_surgical", "post_procedural", "iatrogenic"],
        "post_procedural",
        ["headache_after_lumbar_puncture", "nerve_damage", "postoperative_pain", "infection", "cranial_nerve_palsy", "anesthesia_complication"],
        "Postprocedural disorders of nervous system, not elsewhere classified",
        "G97"
    ],
    [
        "Worldwide",
        ["idiopathic", "unspecified", "multifactorial"],
        "idiopathic",
        ["unexplained_neurological_symptoms", "chronic_pain", "fatigue", "dizziness", "paresthesia", "weakness"],
        "Other disorders of nervous system, not elsewhere classified",
        "G98"
    ],
    [
        "Worldwide",
        ["secondary_disease", "endocrine", "neoplastic"],
        "endocrine",
        ["neuropathy", "myopathy", "cognitive_changes","autonomic_dysfunction", "seizures", "headache"],
        "Other disorders of nervous system in diseases classified elsewhere",
        "G99"
    ]
]

sectionH = [
    # H00-H06: Disorders of eyelid, lacrimal system and orbit
    ["Worldwide", ["bacterial spread", "blocked gland", "poor hygiene"], "bacterial", ["painful eyelid lump", "redness", "swelling", "tenderness", "eyelid irritation", "tearing"], "Hordeolum and Chalazion", "H00"],
    ["Worldwide", ["bacterial overgrowth", "clogged oil glands", "allergic reaction"], "inflammatory", ["red, swollen eyelids", "crusty eyelashes", "gritty sensation", "itching", "light sensitivity", "blurry vision"], "Blepharitis", "H01"],
    ["Worldwide", ["aging", "congenital", "nerve damage"], "structural", ["drooping upper eyelid", "inward-turned eyelid", "outward-turned eyelid", "difficulty closing eye", "impaired vision", "eye irritation"], "Disorders of eyelid (Ptosis, Entropion, Ectropion)", "H02"],
    ["Worldwide", ["secondary to systemic disease", "infection", "autoimmune"], "secondary", ["eyelid inflammation", "lesions", "ptosis", "rash on eyelid", "symptom of primary disease", "eyelid swelling"], "Eyelid disorder secondary to other disease", "H03"],
    ["Worldwide", ["blockage", "inflammation", "infection"], "inflammatory", ["excessive tearing (epiphora)", "dry eyes", "pain in inner corner", "swelling near nose", "recurrent eye infections", "mucus discharge"], "Disorders of lacrimal system (Dacryoadenitis, Dry Eye)", "H04"],
    ["Worldwide", ["bacterial infection", "fungal infection", "trauma"], "inflammatory", ["eye pain", "protruding eyeball (proptosis)", "swollen eyelid", "redness", "fever", "impaired eye movement"], "Disorders of orbit (Cellulitis, Graves')", "H05"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "inflammatory"], "secondary", ["dry eyes", "proptosis", "swelling", "pain", "symptom of primary disease", "vision changes"], "Lacrimal/Orbit disorder secondary to other disease", "H06"],

    # H10-H13: Disorders of conjunctiva
    ["Worldwide", ["viral", "bacterial", "allergic reaction"], "viral", ["eye redness", "gritty sensation", "itching", "discharge (watery or thick)", "crusting of eyelids", "light sensitivity"], "Conjunctivitis (Pink Eye)", "H10"],
    ["Worldwide (higher in sunny climates)", ["UV exposure", "chronic irritation", "wind/dust exposure"], "non-infectious", ["fleshy growth on eye", "redness", "irritation", "foreign body sensation", "blurry vision (if advanced)", "dryness"], "Other conjunctival disorders (Pterygium, Pinguecula)", "H11"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "allergic"], "secondary", ["chronic redness", "lesions on conjunctiva", "dryness", "irritation", "symptom of primary disease", "discharge"], "Conjunctival disorder secondary to other disease", "H13"],

    # H15-H22: Disorders of sclera, cornea, iris and ciliary body
    ["Worldwide", ["autoimmune", "idiopathic", "infection-related"], "autoimmune", ["severe, boring eye pain", "deep red/purple eye", "light sensitivity", "blurred vision", "headache", "pain on eye movement"], "Scleritis/Episcleritis", "H15"],
    ["Worldwide", ["bacterial", "viral (herpes)", "fungal"], "viral", ["severe eye pain", "redness", "blurred vision", "light sensitivity (photophobia)", "foreign body sensation", "excessive tearing"], "Keratitis", "H16"],
    ["Worldwide", ["trauma", "previous infection", "previous surgery"], "traumatic", ["blurry vision", "hazy/cloudy cornea", "vision loss", "glare", "halos around lights", "light sensitivity"], "Corneal scarring", "H17"],
    ["Worldwide", ["genetic", "degenerative", "metabolic"], "genetic", ["progressive vision loss", "blurry vision", "corneal thinning", "irregular astigmatism", "light sensitivity", "eye pain"], "Other corneal disorders (e.g., Dystrophies, Keratoconus)", "H18"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "metabolic"], "secondary", ["corneal deposits", "scleral thinning", "vision changes", "eye pain", "symptom of primary disease", "redness"], "Scleral/Corneal disorder secondary to other disease", "H19"],
    ["Worldwide", ["autoimmune", "idiopathic", "infection-related"], "autoimmune", ["eye pain", "redness (ciliary flush)", "light sensitivity", "blurred vision", "small/irregular pupil", "floaters"], "Iridocyclitis (Anterior Uveitis)", "H20"],
    ["Worldwide", ["trauma", "congenital", "degenerative"], "structural", ["irregular pupil shape", "vision loss", "eye pain", "cysts on iris", "floaters", "light sensitivity"], "Other iris/ciliary disorders", "H21"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "infectious"], "secondary", ["uveitis symptoms", "iris nodules", "pupil abnormalities", "symptom of primary disease", "eye pain", "vision changes"], "Iris/Ciliary disorder secondary to other disease", "H22"],

    # H25-H28: Disorders of lens
    ["Worldwide", ["aging", "oxidative stress", "UV exposure"], "degenerative", ["cloudy/blurry vision", "faded colors", "glare/halos at night", "poor night vision", "frequent prescription changes", "double vision in one eye"], "Age-related cataract", "H25"],
    ["Worldwide", ["trauma", "congenital", "steroid use"], "traumatic", ["cloudy/blurry vision", "glare", "light sensitivity", "vision loss", "milky white pupil", "faded colors"], "Other cataracts (Traumatic, Congenital)", "H26"],
    ["Worldwide", ["surgical removal", "trauma", "congenital"], "structural", ["absence of lens", "severe blurry vision", "difficulty focusing", "vision loss", "trembling iris", "monocular vision"], "Other lens disorders (Aphakia, Dislocation)", "H27"],
    ["Worldwide", ["secondary to systemic disease", "metabolic (diabetes)", "genetic syndrome"], "secondary", ["early-onset cataract", "vision changes", "cloudy lens", "symptom of primary disease", "blurry vision", "glare"], "Lens disorder secondary to other disease", "H28"],

    # H30-H36: Disorders of choroid and retina
    ["Worldwide", ["parasitic", "viral", "autoimmune"], "parasitic", ["floaters", "blurred vision", "vision loss", "scotoma (blind spot)", "eye pain", "light sensitivity"], "Chorioretinal inflammation (Posterior Uveitis)", "H30"],
    ["Worldwide", ["idiopathic", "degenerative", "traumatic"], "degenerative", ["vision distortion", "vision loss", "floaters", "flashes of light", "blind spots", "night blindness"], "Other choroidal disorders", "H31"],
    ["Worldwide", ["secondary to systemic disease", "infectious", "autoimmune"], "secondary", ["retinal lesions", "vision changes", "floaters", "symptom of primary disease", "inflammation", "vision loss"], "Chorioretinal disorder secondary to other disease", "H32"],
    ["Worldwide", ["trauma", "aging (PVD)", "high myopia"], "structural", ["sudden floaters", "flashes of light (photopsia)", "curtain/shadow in vision", "sudden blurred vision", "peripheral vision loss", "central vision loss"], "Retinal detachment", "H33"],
    ["Worldwide", ["thrombosis", "embolism", "hypertension"], "vascular", ["sudden, painless vision loss", "partial vision loss", "blurred vision", "scotoma", "vision distortion", "no pain"], "Retinal vascular occlusion (BRVO, CRVO)", "H34"],
    ["Worldwide", ["aging", "genetic", "smoking"], "degenerative", ["blurred central vision", "straight lines appear wavy", "difficulty reading", "dark spot in central vision", "color perception changes", "slow vision loss"], "Other retinal disorders (Macular Degeneration, Retinitis Pigmentosa)", "H35"],
    ["Worldwide", ["diabetes", "hypertension", "metabolic"], "secondary", ["blurry vision", "floaters", "dark spots in vision", "fluctuating vision", "vision loss", "poor night vision"], "Diabetic retinopathy", "H36"],

    # H40-H42: Glaucoma
    ["Worldwide", ["high intraocular pressure", "genetic", "aging"], "degenerative", ["peripheral vision loss (tunnel vision)", "no early symptoms", "sudden eye pain (acute)", "halos around lights", "headache", "nausea (acute)"], "Glaucoma", "H40"],
    ["Worldwide", ["secondary to systemic disease", "steroid use", "inflammation"], "secondary", ["peripheral vision loss", "elevated eye pressure", "symptom of primary disease", "eye pain", "redness", "blurry vision"], "Secondary glaucoma", "H42"],

    # H43-H45: Disorders of vitreous body and globe
    ["Worldwide", ["aging", "PVD", "inflammation"], "degenerative", ["floaters (specks, cobwebs)", "flashes of light", "blurred vision", "vitreous hemorrhage", "vision loss", "no pain"], "Vitreous disorders (Floaters, Detachment)", "H43"],
    ["Worldwide", ["post-surgical infection", "trauma", "bacterial"], "bacterial", ["severe eye pain", "rapid vision loss", "redness", "swollen eyelid", "pus in anterior chamber", "light sensitivity"], "Disorders of globe (Endophthalmitis, Atrophy)", "H44"],
    ["Worldwide", ["secondary to systemic disease", "infection", "autoimmune"], "secondary", ["inflammation (uveitis)", "hemorrhage", "floaters", "vision loss", "symptom of primary disease", "eye pain"], "Vitreous/Globe disorder secondary to other disease", "H45"],

    # H46-H48: Disorders of optic nerve and visual pathways
    ["Worldwide", ["autoimmune (MS)", "idiopathic", "viral"], "autoimmune", ["vision loss in one eye", "pain with eye movement", "faded color vision", "flashing lights", "central scotoma", "headache"], "Optic neuritis", "H46"],
    ["Worldwide", ["vascular", "compressive (tumor)", "genetic"], "vascular", ["painless vision loss", "swollen optic disc (papilledema)", "peripheral vision loss", "headache", "visual field defects", "optic atrophy"], "Other optic nerve disorders (Ischemic Optic Neuropathy)", "H47"],
    ["Worldwide", ["secondary to systemic disease", "nutritional deficiency", "toxic"], "secondary", ["progressive vision loss", "visual field defects", "optic atrophy", "symptom of primary disease", "color vision loss", "central scotoma"], "Optic nerve disorder secondary to other disease", "H48"],

    # H49-H52: Disorders of ocular muscles, binocular movement, accommodation and refraction
    ["Worldwide", ["nerve palsy (CN III, IV, VI)", "trauma", "vascular (diabetes)"], "neurological", ["double vision (diplopia)", "eye misalignment", "head tilt", "dizziness", "inability to move eye", "eyelid droop (ptosis)"], "Paralytic strabismus", "H49"],
    ["Worldwide", ["congenital", "refractive error", "muscle imbalance"], "structural", ["crossed eyes", "eyes point different directions", "poor depth perception", "double vision", "head tilt", "eye strain"], "Non-paralytic strabismus (Esotropia, Exotropia)", "H50"],
    ["Worldwide", ["neurological", "congenital", "trauma"], "neurological", ["nystagmus (involuntary eye movement)", "dizziness", "vertigo", "blurred vision", "difficulty focusing", "gaze palsy"], "Other binocular movement disorders (Nystagmus)", "H51"],
    ["Worldwide", ["genetic predisposition", "environmental factors", "aging"], "structural", ["blurry distance vision (myopia)", "blurry near vision (hyperopia)", "blurry vision at all distances (astigmatism)", "eye strain", "headaches", "difficulty focusing (presbyopia)"], "Refractive errors (Myopia, Hyperopia, Astigmatism)", "H52"],

    # H53-H54: Visual disturbances and blindness
    ["Worldwide", ["neurological", "retinal", "idiopathic"], "symptomatic", ["visual field defects", "color vision deficiencies", "night blindness", "diplopia", "light sensitivity", "visual distortion"], "Visual disturbances (Amblyopia, Color blindness)", "H53"],
    ["Worldwide", ["cataract", "glaucoma", "macular degeneration"], "symptomatic", ["severe vision loss", "inability to see light", "legal blindness", "peripheral vision loss", "central vision loss", "poor visual acuity"], "Blindness and low vision", "H54"],

    # H55-H59: Other disorders of eye and adnexa
    ["Worldwide", ["congenital", "neurological", "inner ear disorder"], "neurological", ["involuntary rhythmic eye movements", "blurred vision", "dizziness", "oscillopsia (world appears to shake)", "poor depth perception", "head tilt"], "Nystagmus", "H55"],
    ["Worldwide", ["idiopathic", "traumatic", "vascular"], "idiopathic", ["eye pain", "redness", "pupil abnormalities", "foreign body sensation", "headache", "vision changes"], "Other unspecified eye disorders", "H57"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "infectious"], "secondary", ["eye pain", "vision changes", "symptom of primary disease", "redness", "pupil changes", "inflammation"], "Eye disorder secondary to other disease", "H58"],
    ["Worldwide", ["post-surgical complication", "iatrogenic", "inflammation"], "traumatic", ["post-operative pain", "vision loss after surgery", "inflammation", "infection", "high eye pressure", "corneal edema"], "Postprocedural eye disorder", "H59"],

    # H60-H62: Diseases of external ear
    ["Worldwide", ["bacterial", "fungal", "water exposure"], "bacterial", ["ear pain (otalgia)", "itchy ear canal", "redness/swelling of ear canal", "ear discharge", "muffled hearing", "pain on touching earlobe"], "Otitis externa (Swimmer's Ear)", "H60"],
    ["Worldwide", ["trauma", "impacted cerumen", "congenital"], "structural", ["earwax blockage", "hearing loss", "ear pain", "ear canal mass", "deformed pinna", "dizziness"], "Other external ear disorders (Impacted cerumen)", "H61"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "dermatological"], "secondary", ["rash on ear", "lesions in ear canal", "inflammation", "symptom of primary disease", "ear pain", "discharge"], "External ear disorder secondary to other disease", "H62"],

    # H65-H75: Diseases of middle ear and mastoid
    ["Worldwide", ["eustachian tube dysfunction", "viral URI", "allergic"], "inflammatory", ["muffled hearing", "feeling of fullness in ear", "popping/cracking sounds", "balance problems", "hearing loss (conductive)", "no pain or fever"], "Otitis media with effusion (Glue Ear)", "H65"],
    ["Worldwide", ["bacterial", "viral", "eustachian tube dysfunction"], "bacterial", ["severe ear pain", "fever", "hearing loss", "ear discharge (pus)", "irritability (infants)", "feeling of fullness"], "Acute otitis media (Ear Infection)", "H66"],
    ["Worldwide", ["secondary to systemic disease", "viral", "bacterial"], "secondary", ["ear pain", "fever", "hearing loss", "symptom of primary disease (e.g., flu)", "discharge", "fullness"], "Otitis media secondary to other disease", "H67"],
    ["Worldwide", ["inflammation", "allergy", "infection (URI)"], "inflammatory", ["ear fullness", "muffled hearing", "popping sounds", "difficulty equalizing pressure", "ear pain", "dizziness"], "Eustachian tube dysfunction", "H68"],
    ["Worldwide", ["congenital", "structural", "idiopathic"], "structural", ["patulous eustachian tube", "autophony (hearing own voice)", "ear fullness", "popping", "hearing own breathing", "muffled hearing"], "Other Eustachian tube disorders", "H69"],
    ["Worldwide", ["bacterial (complication of otitis media)", "untreated ear infection", "spread of infection"], "bacterial", ["pain behind ear", "swelling/redness behind ear", "fever", "headache", "ear discharge", "hearing loss"], "Mastoiditis", "H70"],
    ["Worldwide", ["eanglian tube dysfunction", "chronic ear infections", "skin cell accumulation"], "structural", ["painless, foul-smelling ear discharge", "progressive hearing loss", "dizziness", "earache", "facial muscle weakness", "fullness in ear"], "Cholesteatoma", "H71"],
    ["Worldwide", ["trauma (q-tip)", "barotrauma (pressure)", "infection"], "traumatic", ["sudden ear pain", "whistling sound from ear", "hearing loss", "ear discharge (clear or bloody)", "ringing in ear (tinnitus)", "dizziness"], "Perforated eardrum", "H72"],
    ["Worldwide", ["inflammation", "trauma", "chronic infection"], "inflammatory", ["hearing loss", "ear pain", "retracted eardrum", "feeling of fullness", "muffled hearing", "tinnitus"], "Other eardrum disorders (Tympanosclerosis)", "H73"],
    ["Worldwide", ["trauma", "congenital", "idiopathic"], "structural", ["conductive hearing loss", "ossicular chain dislocation", "ear pain", "tinnitus", "dizziness", "eardrum retraction"], "Other middle ear disorders (Ossicular discontinuity)", "H74"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "congenital syndrome"], "secondary", ["hearing loss", "ear pain", "symptom of primary disease", "dizziness", "inflammation", "discharge"], "Middle ear disorder secondary to other disease", "H75"],

    # H80-H83: Diseases of inner ear
    ["Worldwide (more in Caucasians)", ["genetic", "hereditary", "unknown trigger"], "genetic", ["progressive conductive hearing loss", "tinnitus (ringing in ear)", "dizziness", "family history of hearing loss", "speaks quietly (own voice loud)", "paracusis willisii"], "Otosclerosis", "H80"],
    ["Worldwide", ["idiopathic", "fluid imbalance (endolymph)", "viral"], "idiopathic", ["episodic vertigo (spinning)", "tinnitus (roaring)", "fluctuating hearing loss", "aural fullness (pressure)", "nausea", "vomiting"], "Disorders of vestibular function (Meniere's, BPPV)", "H81"],
    ["Worldwide", ["secondary to systemic disease", "vascular", "neurological"], "secondary", ["vertigo", "dizziness", "symptom of primary disease", "nausea", "imbalance", "headache"], "Vertigo secondary to other disease", "H82"],
    ["Worldwide", ["viral", "autoimmune", "vascular"], "viral", ["sudden hearing loss", "tinnitus", "vertigo", "aural fullness", "imbalance", "nausea"], "Other inner ear diseases (Labyrinthitis, Vestibular Neuronitis)", "H83"],

    # H90-H95: Other disorders of ear
    ["Worldwide", ["noise exposure", "aging (presbycusis)", "genetic"], "degenerative", ["difficulty hearing speech", "muffled sounds", "tinnitus", "need to turn up volume", "difficulty in noisy places", "social withdrawal"], "Hearing loss (Conductive, Sensorineural)", "H90"],
    ["Worldwide", ["ototoxic drugs", "sudden idiopathic", "trauma"], "idiopathic", ["sudden deafness", "hearing loss after medication", "tinnitus", "muffled hearing", "aural fullness", "dizziness"], "Other hearing loss (Ototoxicity, Sudden Deafness)", "H91"],
    ["Worldwide", ["referred pain (dental, TMJ)", "infection", "inflammation"], "symptomatic", ["ear pain", "ear discharge", "hearing loss", "jaw pain", "headache", "fever"], "Otalgia (Ear pain)", "H92"],
    ["Worldwide", ["noise exposure", "hearing loss", "vascular"], "symptomatic", ["ringing in ears", "buzzing/hissing sound", "hearing loss", "dizziness", "hyperacusis (sound sensitivity)", "aural fullness"], "Tinnitus and other ear disorders", "H93"],
    ["Worldwide", ["secondary to systemic disease", "neurological", "autoimmune"], "secondary", ["hearing loss", "tinnitus", "dizziness", "symptom of primary disease", "ear pain", "inflammation"], "Ear disorder secondary to other disease", "H94"],
    ["Worldwide", ["post-surgical complication", "iatrogenic", "inflammation"], "traumatic", ["post-operative pain", "hearing loss after surgery", "dizziness", "infection", "ear discharge", "tinnitus"], "Postprocedural ear disorder", "H95"]
]

sectionI = [
    # I00-I02: Acute rheumatic fever
    {
        'icd_code': 'I00',
        'disease_name': 'Acute rheumatic fever without heart involvement',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Streptococcal infection', 'Autoimmune'],
        'disease_type': 'Infectious-Bacterial (complication)',
        'symptoms': ['Fever', 'Joint pain (arthritis)', 'Skin nodules', 'Erythema marginatum', 'Sydenham chorea (later)'],
    },
    {
        'icd_code': 'I01',
        'disease_name': 'Acute rheumatic fever with heart involvement',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Streptococcal infection', 'Autoimmune'],
        'disease_type': 'Infectious-Bacterial (complication)',
        'symptoms': ['Fever', 'Chest pain', 'Heart murmur', 'Shortness of breath', 'Fatigue', 'Joint pain'],
    },
    {
        'icd_code': 'I02',
        'disease_name': 'Rheumatic chorea',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Streptococcal infection', 'Autoimmune'],
        'disease_type': 'Infectious-Bacterial (complication)',
        'symptoms': ['Jerky movements', 'Uncontrolled movements', 'Muscle weakness', 'Emotional lability', 'Speech changes', 'Gait disturbance'],
    },
    # I05-I09: Chronic rheumatic heart diseases
    {
        'icd_code': 'I05',
        'disease_name': 'Chronic rheumatic mitral valve diseases',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Chronic inflammation', 'Untreated strep infection'],
        'disease_type': 'Inflammatory (post-infectious)',
        'symptoms': ['Shortness of breath', 'Fatigue', 'Heart murmur', 'Atrial fibrillation', 'Swollen ankles', 'Palpitations'],
    },
    {
        'icd_code': 'I06',
        'disease_name': 'Chronic rheumatic aortic valve diseases',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Chronic inflammation', 'Untreated strep infection'],
        'disease_type': 'Inflammatory (post-infectious)',
        'symptoms': ['Shortness of breath (on exertion)', 'Chest pain (angina)', 'Fainting (syncope)', 'Fatigue', 'Heart murmur', 'Dizziness'],
    },
    {
        'icd_code': 'I07',
        'disease_name': 'Chronic rheumatic tricuspid valve diseases',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Chronic inflammation', 'Untreated strep infection'],
        'disease_type': 'Inflammatory (post-infectious)',
        'symptoms': ['Abdominal swelling (ascites)', 'Swollen ankles (edema)', 'Fatigue', 'Fluttering neck veins', 'Heart murmur', 'Liver enlargement'],
    },
    {
        'icd_code': 'I08',
        'disease_name': 'Multiple valve diseases (rheumatic)',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Chronic inflammation', 'Untreated strep infection'],
        'disease_type': 'Inflammatory (post-infectious)',
        'symptoms': ['Shortness of breath', 'Fatigue', 'Chest pain', 'Dizziness', 'Swollen ankles', 'Heart murmurs'],
    },
    {
        'icd_code': 'I09',
        'disease_name': 'Other rheumatic heart diseases',
        'geography': 'Worldwide (higher in developing nations)',
        'transmission': ['Post-infectious', 'Chronic inflammation', 'Untreated strep infection'],
        'disease_type': 'Inflammatory (post-infectious)',
        'symptoms': ['Fatigue', 'Shortness of breath', 'Heart murmur', 'Chest discomfort', 'Palpitations', 'Joint pain history'],
    },
    # I10-I16: Hypertensive diseases
    {
        'icd_code': 'I10',
        'disease_name': 'Essential (primary) hypertension',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Genetic', 'Age-related'],
        'disease_type': 'Lifestyle-related',
        'symptoms': ['Often asymptomatic', 'Headaches', 'Dizziness', 'Nosebleeds', 'Blurred vision', 'Shortness of breath'],
    },
    {
        'icd_code': 'I11',
        'disease_name': 'Hypertensive heart disease',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Genetic', 'Chronic hypertension'],
        'disease_type': 'Lifestyle-related (complication)',
        'symptoms': ['Shortness of breath', 'Fatigue', 'Chest pain', 'Irregular heartbeat', 'Swollen ankles', 'Dizziness'],
    },
    {
        'icd_code': 'I12',
        'disease_name': 'Hypertensive renal disease',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Genetic', 'Chronic hypertension'],
        'disease_type': 'Lifestyle-related (complication)',
        'symptoms': ['Often asymptomatic (early)', 'Reduced urine output', 'Swelling (edema)', 'Fatigue', 'Nausea', 'High blood pressure'],
    },
    {
        'icd_code': 'I13',
        'disease_name': 'Hypertensive heart and renal disease',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Genetic', 'Chronic hypertension'],
        'disease_type': 'Lifestyle-related (complication)',
        'symptoms': ['Shortness of breath', 'Swelling (edema)', 'Fatigue', 'Reduced urine output', 'Chest pain', 'Irregular heartbeat'],
    },
    {
        'icd_code': 'I15',
        'disease_name': 'Secondary hypertension',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Medication side-effect', 'Hormonal imbalance'],
        'disease_type': 'Secondary (to other condition)',
        'symptoms': ['Very high blood pressure', 'Resistant hypertension', 'Sudden onset', 'Headaches', 'Dizziness', 'Symptoms of underlying cause'],
    },
    {
        'icd_code': 'I16',
        'disease_name': 'Hypertensive crisis',
        'geography': 'Worldwide',
        'transmission': ['Chronic hypertension', 'Medication non-compliance', 'Underlying condition'],
        'disease_type': 'Lifestyle-related (acute complication)',
        'symptoms': ['Severe headache', 'Blurred vision', 'Nausea/Vomiting', 'Severe chest pain', 'Shortness of breath', 'Confusion'],
    },
    # I20-I25: Ischaemic heart diseases
    {
        'icd_code': 'I20',
        'disease_name': 'Angina pectoris',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Lifestyle (smoking)', 'Atherosclerosis'],
        'disease_type': 'Lifestyle-related (Chronic)',
        'symptoms': ['Chest pain (pressure, tightness)', 'Pain radiating to arm/jaw', 'Shortness of breath', 'Nausea', 'Sweating', 'Dizziness'],
    },
    {
        'icd_code': 'I21',
        'disease_name': 'Acute myocardial infarction (Heart Attack)',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Thrombosis', 'Lifestyle (smoking)'],
        'disease_type': 'Lifestyle-related (Acute)',
        'symptoms': ['Severe chest pain', 'Pain radiating to arm/jaw', 'Shortness of breath', 'Cold sweat', 'Nausea/Vomiting', 'Lightheadedness'],
    },
    {
        'icd_code': 'I22',
        'disease_name': 'Subsequent myocardial infarction',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Previous MI', 'Lifestyle (diet)'],
        'disease_type': 'Lifestyle-related (Acute)',
        'symptoms': ['Severe chest pain', 'Shortness of breath', 'Nausea', 'Sweating', 'Symptoms like previous MI', 'Fatigue'],
    },
    {
        'icd_code': 'I23',
        'disease_name': 'Complications following acute myocardial infarction',
        'geography': 'Worldwide',
        'transmission': ['Post-MI complication', 'Cardiac tissue damage', 'Inflammation'],
        'disease_type': 'Complication (Post-MI)',
        'symptoms': ['Arrhythmia', 'Heart failure symptoms', 'New heart murmur', 'Pericarditis (chest pain)', 'Hypotension', 'Cardiogenic shock'],
    },
    {
        'icd_code': 'I24',
        'disease_name': 'Other acute ischaemic heart diseases',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Coronary artery spasm', 'Thrombosis'],
        'disease_type': 'Lifestyle-related (Acute)',
        'symptoms': ['Unstable angina (new/worsening)', 'Chest pain at rest', 'Prolonged chest pain', 'Sudden cardiac death', 'Arrhythmia', 'Shortness of breath'],
    },
    {
        'icd_code': 'I25',
        'disease_name': 'Chronic ischaemic heart disease',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Lifestyle (diet)', 'Age-related'],
        'disease_type': 'Lifestyle-related (Chronic)',
        'symptoms': ['Stable angina', 'Shortness of breath on exertion', 'Fatigue', 'Asymptomatic (sometimes)', 'Heart failure symptoms (late)', 'Arrhythmia'],
    },
    # I26-I28: Pulmonary heart disease and diseases of pulmonary circulation
    {
        'icd_code': 'I26',
        'disease_name': 'Pulmonary embolism',
        'geography': 'Worldwide',
        'transmission': ['Deep vein thrombosis (DVT)', 'Immobility', 'Hypercoagulability'],
        'disease_type': 'Thrombotic',
        'symptoms': ['Sudden shortness of breath', 'Sharp chest pain', 'Coughing up blood', 'Rapid heart rate', 'Dizziness', 'Leg swelling (DVT sign)'],
    },
    {
        'icd_code': 'I27',
        'disease_name': 'Other pulmonary heart diseases (Cor Pulmonale)',
        'geography': 'Worldwide',
        'transmission': ['Chronic lung disease (COPD)', 'Pulmonary hypertension', 'Hypoxia'],
        'disease_type': 'Chronic (secondary to lung disease)',
        'symptoms': ['Shortness of breath (worsening)', 'Fatigue', 'Swollen ankles (edema)', 'Chest pain', 'Wheezing', 'Cyanosis (bluish skin)'],
    },
    {
        'icd_code': 'I28',
        'disease_name': 'Other diseases of pulmonary vessels',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Idiopathic', 'Congenital'],
        'disease_type': 'Degenerative/Genetic',
        'symptoms': ['Shortness of breath', 'Chest pain', 'Dizziness', 'Fatigue', 'Cyanosis', 'Pulmonary hypertension symptoms'],
    },
    # I30-I52: Other forms of heart disease
    {
        'icd_code': 'I30',
        'disease_name': 'Acute pericarditis',
        'geography': 'Worldwide',
        'transmission': ['Idiopathic', 'Viral infection', 'Autoimmune'],
        'disease_type': 'Infectious-Viral (common) / Inflammatory',
        'symptoms': ['Sharp chest pain (worse lying down)', 'Pain relieved by leaning forward', 'Fever', 'Pericardial friction rub (sound)', 'Fatigue', 'Shortness of breath'],
    },
    {
        'icd_code': 'I31',
        'disease_name': 'Other diseases of pericardium',
        'geography': 'Worldwide',
        'transmission': ['Chronic inflammation', 'Post-injury', 'Idiopathic'],
        'disease_type': 'Inflammatory (Chronic)',
        'symptoms': ['Constrictive pericarditis symptoms', 'Heart failure symptoms', 'Fatigue', 'Swelling (edema)', 'Shortness of breath', 'Chest pain'],
    },
    {
        'icd_code': 'I32',
        'disease_name': 'Pericarditis in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Autoimmune (Lupus, RA)', 'Metabolic (Uremia)'],
        'disease_type': 'Inflammatory (Secondary)',
        'symptoms': ['Sharp chest pain', 'Fever', 'Pericardial friction rub', 'Symptoms of underlying disease', 'Fatigue', 'Shortness of breath'],
    },
    {
        'icd_code': 'I33',
        'disease_name': 'Acute and subacute endocarditis',
        'geography': 'Worldwide',
        'transmission': ['Bacterial infection', 'IV drug use', 'Prosthetic valves'],
        'disease_type': 'Infectious-Bacterial',
        'symptoms': ['Fever', 'Chills', 'New heart murmur', 'Fatigue', 'Osler nodes', 'Janeway lesions'],
    },
    {
        'icd_code': 'I34',
        'disease_name': 'Nonrheumatic mitral valve disorders',
        'geography': 'Worldwide',
        'transmission': ['Degenerative', 'Congenital', 'Idiopathic (e.g., MVP)'],
        'disease_type': 'Degenerative / Congenital',
        'symptoms': ['Heart murmur', 'Palpitations', 'Shortness of breath', 'Fatigue', 'Chest pain', 'Dizziness'],
    },
    {
        'icd_code': 'I35',
        'disease_name': 'Nonrheumatic aortic valve disorders',
        'geography': 'Worldwide',
        'transmission': ['Degenerative (calcification)', 'Congenital (bicuspid valve)', 'Age-related'],
        'disease_type': 'Degenerative / Congenital',
        'symptoms': ['Chest pain (angina)', 'Fainting (syncope)', 'Shortness of breath', 'Fatigue', 'Heart murmur', 'Dizziness'],
    },
    {
        'icd_code': 'I36',
        'disease_name': 'Nonrheumatic tricuspid valve disorders',
        'geography': 'Worldwide',
        'transmission': ['Congenital', 'Carcinoid syndrome', 'Secondary to right-heart failure'],
        'disease_type': 'Degenerative / Congenital',
        'symptoms': ['Swelling (edema)', 'Abdominal swelling (ascites)', 'Fatigue', 'Fluttering neck veins', 'Heart murmur', 'Liver enlargement'],
    },
    {
        'icd_code': 'I37',
        'disease_name': 'Nonrheumatic pulmonary valve disorders',
        'geography': 'Worldwide',
        'transmission': ['Congenital (most common)', 'Carcinoid syndrome', 'Degenerative'],
        'disease_type': 'Congenital',
        'symptoms': ['Heart murmur', 'Shortness of breath', 'Fatigue', 'Cyanosis (severe)', 'Chest pain', 'Fainting'],
    },
    {
        'icd_code': 'I38',
        'disease_name': 'Endocarditis, valve unspecified',
        'geography': 'Worldwide',
        'transmission': ['Bacterial infection', 'IV drug use', 'Prosthetic valves'],
        'disease_type': 'Infectious-Bacterial',
        'symptoms': ['Fever', 'Chills', 'New heart murmur', 'Fatigue', 'Night sweats', 'Unexplained weight loss'],
    },
    {
        'icd_code': 'I39',
        'disease_name': 'Endocarditis and heart valve disorders in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Autoimmune (Lupus)', 'Inflammatory'],
        'disease_type': 'Inflammatory (Secondary)',
        'symptoms': ['Fever', 'Heart murmur', 'Fatigue', 'Symptoms of underlying disease', 'Chills', 'Joint pain'],
    },
    {
        'icd_code': 'I40',
        'disease_name': 'Acute myocarditis',
        'geography': 'Worldwide',
        'transmission': ['Viral infection (Coxsackie B)', 'Autoimmune', 'Toxins'],
        'disease_type': 'Infectious-Viral (common) / Inflammatory',
        'symptoms': ['Chest pain', 'Shortness of breath', 'Fatigue', 'Fever', 'Arrhythmia', 'Heart failure symptoms'],
    },
    {
        'icd_code': 'I41',
        'disease_name': 'Myocarditis in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Infectious', 'Autoimmune'],
        'disease_type': 'Inflammatory (Secondary)',
        'symptoms': ['Chest pain', 'Fatigue', 'Arrhythmia', 'Symptoms of underlying disease', 'Fever', 'Shortness of breath'],
    },
    {
        'icd_code': 'I42',
        'disease_name': 'Cardiomyopathy',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Idiopathic', 'Alcohol abuse'],
        'disease_type': 'Genetic / Lifestyle-related / Idiopathic',
        'symptoms': ['Shortness of breath', 'Fatigue', 'Swelling (edema)', 'Arrhythmia', 'Dizziness', 'Chest pain'],
    },
    {
        'icd_code': 'I43',
        'disease_name': 'Cardiomyopathy in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Metabolic', 'Muscular dystrophy'],
        'disease_type': 'Genetic / Metabolic (Secondary)',
        'symptoms': ['Heart failure symptoms', 'Arrhythmia', 'Fatigue', 'Symptoms of underlying disease', 'Shortness of breath', 'Swelling (edema)'],
    },
    {
        'icd_code': 'I44',
        'disease_name': 'Atrioventricular and left bundle-branch block',
        'geography': 'Worldwide',
        'transmission': ['Age-related', 'Idiopathic fibrosis', 'Ischemic heart disease'],
        'disease_type': 'Degenerative / Electrical',
        'symptoms': ['Dizziness', 'Fainting (syncope)', 'Fatigue', 'Shortness of breath', 'Slow heart rate (bradycardia)', 'Chest pain'],
    },
    {
        'icd_code': 'I45',
        'disease_name': 'Other conduction disorders',
        'geography': 'Worldwide',
        'transmission': ['Age-related', 'Idiopathic fibrosis', 'Congenital'],
        'disease_type': 'Degenerative / Electrical / Congenital',
        'symptoms': ['Palpitations', 'Dizziness', 'Fainting (syncope)', 'Fatigue', 'Slow heart rate', 'Fast heart rate'],
    },
    {
        'icd_code': 'I46',
        'disease_name': 'Cardiac arrest',
        'geography': 'Worldwide',
        'transmission': ['Arrhythmia (VT/VF)', 'Ischemic heart disease', 'Cardiomyopathy'],
        'disease_type': 'Electrical (Acute event)',
        'symptoms': ['Sudden loss of consciousness', 'No breathing', 'No pulse', 'Collapse', '(Preceded by chest pain)', '(Preceded by palpitations)'],
    },
    {
        'icd_code': 'I47',
        'disease_name': 'Paroxysmal tachycardia',
        'geography': 'Worldwide',
        'transmission': ['Idiopathic', 'Accessory pathway (e.g., WPW)', 'Structural heart disease'],
        'disease_type': 'Electrical / Genetic',
        'symptoms': ['Palpitations (racing heart)', 'Dizziness', 'Shortness of breath', 'Chest discomfort', 'Fainting (syncope)', 'Anxiety'],
    },
    {
        'icd_code': 'I48',
        'disease_name': 'Atrial fibrillation and flutter',
        'geography': 'Worldwide',
        'transmission': ['Age-related', 'Hypertension', 'Heart failure'],
        'disease_type': 'Electrical / Lifestyle-related',
        'symptoms': ['Irregular heartbeat', 'Palpitations', 'Fatigue', 'Shortness of breath', 'Dizziness', 'Risk of stroke'],
    },
    {
        'icd_code': 'I49',
        'disease_name': 'Other cardiac arrhythmias',
        'geography': 'Worldwide',
        'transmission': ['Idiopathic', 'Electrolyte imbalance', 'Medication side-effect'],
        'disease_type': 'Electrical',
        'symptoms': ['Palpitations (skipped beats)', 'Slow heart rate', 'Fast heart rate', 'Dizziness', 'Fainting', 'Fatigue'],
    },
    {
        'icd_code': 'I50',
        'disease_name': 'Heart failure',
        'geography': 'Worldwide',
        'transmission': ['Ischemic heart disease', 'Hypertension', 'Cardiomyopathy'],
        'disease_type': 'Chronic (Syndrome)',
        'symptoms': ['Shortness of breath', 'Swelling (edema)', 'Fatigue', 'Orthopnea (SOB lying down)', 'Chronic cough/wheezing', 'Rapid weight gain'],
    },
    {
        'icd_code': 'I51',
        'disease_name': 'Complications and ill-defined descriptions of heart disease',
        'geography': 'Worldwide',
        'transmission': ['Varies', 'Structural damage', 'Idiopathic'],
        'disease_type': 'Varies / Unspecified',
        'symptoms': ['Cardiomegaly (enlarged heart)', 'Chest pain', 'Fatigue', 'Shortness of breath', 'Murmur', 'Ill-defined symptoms'],
    },
    {
        'icd_code': 'I52',
        'disease_name': 'Other heart disorders in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Metabolic', 'Inflammatory'],
        'disease_type': 'Secondary (to other condition)',
        'symptoms': ['Symptoms of underlying disease', 'Heart failure symptoms', 'Arrhythmia', 'Chest pain', 'Fatigue', 'Shortness of breath'],
    },
    # I60-I69: Cerebrovascular diseases
    {
        'icd_code': 'I60',
        'disease_name': 'Subarachnoid haemorrhage',
        'geography': 'Worldwide',
        'transmission': ['Aneurysm rupture', 'Trauma', 'AVM'],
        'disease_type': 'Hemorrhagic (Acute)',
        'symptoms': ['Sudden severe headache ("thunderclap")', 'Nausea/Vomiting', 'Loss of consciousness', 'Stiff neck', 'Photophobia (light sensitivity)', 'Seizure'],
    },
    {
        'icd_code': 'I61',
        'disease_name': 'Intracerebral haemorrhage',
        'geography': 'Worldwide',
        'transmission': ['Hypertension', 'Amyloid angiopathy', 'AVM'],
        'disease_type': 'Hemorrhagic (Acute)',
        'symptoms': ['Sudden severe headache', 'Nausea/Vomiting', 'Weakness (one side)', 'Loss of consciousness', 'Seizure', 'Speech difficulty'],
    },
    {
        'icd_code': 'I62',
        'disease_name': 'Other nontraumatic intracranial haemorrhage',
        'geography': 'Worldwide',
        'transmission': ['Hypertension', 'Aneurysm', 'Vascular malformation'],
        'disease_type': 'Hemorrhagic (Acute)',
        'symptoms': ['Headache', 'Neurological deficits', 'Nausea/Vomiting', 'Seizure', 'Altered consciousness', 'Stiff neck'],
    },
    {
        'icd_code': 'I63',
        'disease_name': 'Cerebral infarction (Ischemic Stroke)',
        'geography': 'Worldwide',
        'transmission': ['Thrombosis (atherosclerosis)', 'Embolism (e.g., from Atrial Fibrillation)', 'Lifestyle (smoking)'],
        'disease_type': 'Ischemic (Acute)',
        'symptoms': ['Facial drooping (one side)', 'Arm weakness (one side)', 'Speech difficulty (slurred)', 'Sudden confusion', 'Sudden vision loss', 'Sudden dizziness'],
    },
    {
        'icd_code': 'I64',
        'disease_name': 'Stroke, not specified as haemorrhage or infarction',
        'geography': 'Worldwide',
        'transmission': ['Varies (thrombosis, hemorrhage)', 'Hypertension', 'Lifestyle (diet)'],
        'disease_type': 'Acute (Unspecified)',
        'symptoms': ['Sudden weakness', 'Sudden speech difficulty', 'Sudden confusion', 'Sudden severe headache', 'Sudden vision loss', 'Sudden dizziness'],
    },
    {
        'icd_code': 'I65',
        'disease_name': 'Occlusion and stenosis of precerebral arteries',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Lifestyle (smoking)', 'Hypertension'],
        'disease_type': 'Lifestyle-related (Chronic)',
        'symptoms': ['Often asymptomatic', 'Transient ischemic attack (TIA)', 'Dizziness', 'Bruit (sound) over artery', 'Stroke symptoms', 'Vision changes'],
    },
    {
        'icd_code': 'I66',
        'disease_name': 'Occlusion and stenosis of cerebral arteries',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Hypertension', 'Lifestyle (diet)'],
        'disease_type': 'Lifestyle-related (Chronic)',
        'symptoms': ['Transient ischemic attack (TIA)', 'Stroke symptoms', 'Headache', 'Cognitive decline', 'Dizziness', 'Weakness'],
    },
    {
        'icd_code': 'I67',
        'disease_name': 'Other cerebrovascular diseases',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Idiopathic', 'Hypertension'],
        'disease_type': 'Degenerative / Genetic',
        'symptoms': ['Cognitive impairment (vascular dementia)', 'Headache', 'Dizziness', 'Seizures', 'Focal neurological deficits', 'Gait disturbance'],
    },
    {
        'icd_code': 'I68',
        'disease_name': 'Cerebrovascular disorders in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Inflammatory (vasculitis)', 'Infectious'],
        'disease_type': 'Secondary (to other condition)',
        'symptoms': ['Stroke symptoms', 'Headache', 'Seizures', 'Symptoms of underlying disease', 'Cognitive decline', 'Fever'],
    },
    {
        'icd_code': 'I69',
        'disease_name': 'Sequelae of cerebrovascular disease',
        'geography': 'Worldwide',
        'transmission': ['Post-stroke', 'Brain injury', 'N/A'],
        'disease_type': 'Post-Stroke (Chronic)',
        'symptoms': ['Hemiparesis (weakness)', 'Aphasia (speech loss)', 'Cognitive deficits', 'Depression', 'Spasticity', 'Gait problems'],
    },
    # I70-I79: Diseases of arteries, arterioles and capillaries
    {
        'icd_code': 'I70',
        'disease_name': 'Atherosclerosis',
        'geography': 'Worldwide',
        'transmission': ['Lifestyle (diet)', 'Lifestyle (smoking)', 'Age-related'],
        'disease_type': 'Lifestyle-related (Chronic)',
        'symptoms': ['Often asymptomatic', 'Angina (chest pain)', 'Claudication (leg pain)', 'Stroke symptoms (TIA)', 'Erectile dysfunction', 'High blood pressure'],
    },
    {
        'icd_code': 'I71',
        'disease_name': 'Aortic aneurysm and dissection',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Genetic (e.g., Marfan)', 'Hypertension'],
        'disease_type': 'Degenerative / Genetic',
        'symptoms': ['Often asymptomatic (aneurysm)', 'Sudden tearing chest/back pain (dissection)', 'Abdominal/Back pain', 'Pulsating abdominal mass', 'Shortness of breath', 'Hoarseness'],
    },
    {
        'icd_code': 'I72',
        'disease_name': 'Other aneurysm',
        'geography': 'Worldwide',
        'transmission': ['Atherosclerosis', 'Genetic', 'Trauma'],
        'disease_type': 'Degenerative / Genetic',
        'symptoms': ['Often asymptomatic', 'Pulsating mass', 'Pain in affected area', 'Symptoms of compression', 'Risk of rupture', 'Bruit (sound) over aneurysm'],
    },
    {
        'icd_code': 'I73',
        'disease_name': 'Other peripheral vascular diseases',
        'geography': 'Worldwide',
        'transmission': ['Autoimmune (Vasculitis)', 'Lifestyle (smoking)', 'Idiopathic (Raynaud)'],
        'disease_type': 'Inflammatory / Autoimmune / Vasospastic',
        'symptoms': ['Claudication (leg pain)', 'Finger/toe color changes (Raynaud)', 'Skin ulcers', 'Numbness/Tingling', 'Weak pulses', 'Skin discoloration'],
    },
    {
        'icd_code': 'I74',
        'disease_name': 'Arterial embolism and thrombosis',
        'geography': 'Worldwide',
        'transmission': ['Atrial fibrillation', 'Atherosclerosis', 'Hypercoagulability'],
        'disease_type': 'Thrombotic / Embolic',
        'symptoms': ['Sudden severe pain (in limb)', 'Pallor (pale limb)', 'Pulselessness', 'Paresthesia (numbness)', 'Paralysis', 'Poikilothermia (cold limb)'],
    },
    {
        'icd_code': 'I77',
        'disease_name': 'Other disorders of arteries and arterioles',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Inflammatory', 'Idiopathic'],
        'disease_type': 'Genetic / Inflammatory',
        'symptoms': ['Varies by specific disorder', 'Hypertension', 'Bleeding', 'Ischemia', 'Aneurysms', 'Vasculitis symptoms'],
    },
    {
        'icd_code': 'I78',
        'disease_name': 'Disorders of capillaries',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Idiopathic', 'Secondary'],
        'disease_type': 'Genetic / Degenerative',
        'symptoms': ['Telangiectasia (spider veins)', 'Easy bruising', 'Bleeding', 'Skin discoloration', 'Edema', 'Petechiae'],
    },
    {
        'icd_code': 'I79',
        'disease_name': 'Disorders of arteries, arterioles and capillaries in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Autoimmune (Lupus, RA)', 'Diabetes'],
        'disease_type': 'Secondary (to other condition)',
        'symptoms': ['Symptoms of underlying disease', 'Vasculitis', 'Skin lesions', 'Ischemia', 'Raynaud phenomenon', 'Poor wound healing'],
    },
    # I80-I89: Diseases of veins, lymphatic vessels and lymph nodes
    {
        'icd_code': 'I80',
        'disease_name': 'Phlebitis and thrombophlebitis (DVT)',
        'geography': 'Worldwide',
        'transmission': ['Immobility', 'Surgery/Trauma', 'Hypercoagulability'],
        'disease_type': 'Thrombotic / Inflammatory',
        'symptoms': ['Leg pain or tenderness', 'Leg swelling (edema)', 'Redness or warmth', 'Visible superficial veins', 'Fever', 'Risk of pulmonary embolism'],
    },
    {
        'icd_code': 'I81',
        'disease_name': 'Portal vein thrombosis',
        'geography': 'Worldwide',
        'transmission': ['Cirrhosis', 'Hypercoagulability', 'Abdominal infection/inflammation'],
        'disease_type': 'Thrombotic',
        'symptoms': ['Abdominal pain', 'Ascites (fluid buildup)', 'Splenomegaly (enlarged spleen)', 'Vomiting blood (varices)', 'Fever', 'Nausea/Vomiting'],
    },
    {
        'icd_code': 'I82',
        'disease_name': 'Other venous embolism and thrombosis',
        'geography': 'Worldwide',
        'transmission': ['Hypercoagulability', 'Malignancy', 'Immobility'],
        'disease_type': 'Thrombotic / Embolic',
        'symptoms': ['Pain and swelling (affected site)', 'Redness', 'Warmth', 'Symptoms specific to location (e.g., arm, brain)', 'Fever', 'Visible veins'],
    },
    {
        'icd_code': 'I83',
        'disease_name': 'Varicose veins of lower extremities',
        'geography': 'Worldwide',
        'transmission': ['Genetic', 'Prolonged standing', 'Pregnancy'],
        'disease_type': 'Degenerative (Venous insufficiency)',
        'symptoms': ['Visible twisted/bulging veins', 'Aching or heavy feeling in legs', 'Swelling', 'Itching around veins', 'Skin discoloration', 'Leg cramps (night)'],
    },
    {
        'icd_code': 'I84',
        'disease_name': 'Haemorrhoids (Hemorrhoids)',
        'geography': 'Worldwide',
        'transmission': ['Straining (constipation)', 'Pregnancy', 'Prolonged sitting'],
        'disease_type': 'Lifestyle-related (Venous)',
        'symptoms': ['Rectal bleeding (bright red)', 'Itching or irritation', 'Pain or discomfort', 'Swelling around anus', 'A lump near anus', 'Mucus discharge'],
    },
    {
        'icd_code': 'I85',
        'disease_name': 'Oesophageal varices',
        'geography': 'Worldwide',
        'transmission': ['Liver cirrhosis', 'Portal hypertension', 'Alcohol abuse'],
        'disease_type': 'Complication (of Cirrhosis)',
        'symptoms': ['Vomiting blood', 'Black, tarry stools', 'Lightheadedness', 'Loss of consciousness (severe)', 'Jaundice (liver disease sign)', 'Ascites (liver disease sign)'],
    },
    {
        'icd_code': 'I86',
        'disease_name': 'Varicose veins of other sites',
        'geography': 'Worldwide',
        'transmission': ['Portal hypertension', 'Pregnancy', 'Local pressure'],
        'disease_type': 'Degenerative (Venous)',
        'symptoms': ['Visible veins (site-specific)', 'Pain', 'Swelling', 'Bleeding', 'Discomfort', 'Symptoms of underlying cause'],
    },
    {
        'icd_code': 'I87',
        'disease_name': 'Other disorders of veins',
        'geography': 'Worldwide',
        'transmission': ['Post-thrombotic syndrome', 'Genetic', 'Chronic venous insufficiency'],
        'disease_type': 'Chronic (Venous insufficiency)',
        'symptoms': ['Leg swelling', 'Skin discoloration (brownish)', 'Leg ulcers', 'Pain', 'Aching', 'Itching'],
    },
    {
        'icd_code': 'I88',
        'disease_name': 'Nonspecific lymphadenitis',
        'geography': 'Worldwide',
        'transmission': ['Local infection (bacterial/viral)', 'Inflammation', 'Idiopathic'],
        'disease_type': 'Inflammatory / Infectious (Reactive)',
        'symptoms': ['Swollen lymph nodes', 'Tender lymph nodes', 'Redness over node', 'Fever', 'Malaise', 'Symptoms of local infection'],
    },
    {
        'icd_code': 'I89',
        'disease_name': 'Other noninfective disorders of lymphatic vessels',
        'geography': 'Worldwide',
        'transmission': ['Congenital', 'Post-surgical (lymph node removal)', 'Idiopathic'],
        'disease_type': 'Congenital / Post-procedural',
        'symptoms': ['Lymphedema (swelling)', 'Skin thickening', 'Heaviness in limb', 'Recurrent infections (cellulitis)', 'Restricted range of motion', 'Aching or discomfort'],
    },
    # I95-I99: Other and unspecified disorders of circulatory system
    {
        'icd_code': 'I95',
        'disease_name': 'Hypotension',
        'geography': 'Worldwide',
        'transmission': ['Idiopathic', 'Medication side-effect', 'Dehydration'],
        'disease_type': 'Symptomatic / Idiopathic',
        'symptoms': ['Dizziness', 'Lightheadedness', 'Fainting (syncope)', 'Blurred vision', 'Nausea', 'Fatigue'],
    },
    {
        'icd_code': 'I97',
        'disease_name': 'Postprocedural disorders of circulatory system',
        'geography': 'Worldwide',
        'transmission': ['Post-surgical complication', 'Post-intervention', 'N/A'],
        'disease_type': 'Post-procedural',
        'symptoms': ['Post-cardiotomy syndrome (fever, chest pain)', 'Lymphedema (post-mastectomy)', 'Graft failure', 'Hemorrhage', 'Thrombosis', 'Arrhythmia'],
    },
    {
        'icd_code': 'I98',
        'disease_name': 'Other disorders of circulatory system in diseases classified elsewhere',
        'geography': 'Worldwide',
        'transmission': ['Underlying condition', 'Metabolic', 'Endocrine'],
        'disease_type': 'Secondary (to other condition)',
        'symptoms': ['Symptoms of underlying disease', 'Cardiovascular manifestations', 'Vascular changes', 'Autonomic dysfunction', 'Hypotension', 'Hypertension'],
    },
    {
        'icd_code': 'I99',
        'disease_name': 'Other and unspecified disorders of circulatory system',
        'geography': 'Worldwide',
        'transmission': ['Idiopathic', 'Unspecified', 'Varies'],
        'disease_type': 'Unspecified',
        'symptoms': ['Vague symptoms', 'Dizziness', 'Fatigue', 'Chest discomfort', 'Pain', 'Unspecified circulatory issues'],
    },
]

sectionJ = [
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

sectionK = [
    # K00-K14: Diseases of oral cavity, salivary glands and jaws
    ["Worldwide", ["genetic", "developmental", "environmental"], "Developmental", ["missing teeth", "extra teeth", "abnormal tooth size", "abnormal tooth shape", "enamel defects", "dentin defects"], "Disorders of tooth development and eruption", "K00"],
    ["Worldwide", ["genetic", "developmental", "lack of space"], "Structural", ["unerupted tooth", "tooth pain", "swelling of gum", "misaligned teeth", "cyst formation", "damage to adjacent teeth"], "Embedded and impacted teeth", "K01"],
    ["Worldwide", ["bacterial", "dietary (high sugar)", "poor hygiene"], "Bacterial", ["toothache", "tooth sensitivity", "visible pits in teeth", "brown/black tooth staining", "pain when biting", "bad breath"], "Dental caries", "K02"],
    ["Worldwide", ["attrition (grinding)", "abrasion (brushing)", "erosion (acid)"], "Non-infectious", ["tooth sensitivity", "worn-down teeth", "tooth discoloration", "chipped teeth", "grooves on teeth", "tooth surface loss"], "Other diseases of hard tissues of teeth", "K03"],
    ["Worldwide", ["bacterial", "dental caries", "trauma"], "Bacterial", ["severe toothache", "gum swelling", "abscess", "pus drainage", "sensitivity to hot/cold", "fever"], "Diseases of pulp and periapical tissues", "K04"],
    ["Worldwide", ["bacterial", "plaque buildup", "poor hygiene"], "Bacterial", ["swollen gums", "bleeding gums", "red gums", "bad breath", "loose teeth", "receding gums"], "Gingivitis and periodontal diseases", "K05"],
    ["Worldwide", ["trauma", "ill-fitting dentures", "poor hygiene"], "Inflammatory", ["gum recession", "gum enlargement", "soreness", "bleeding", "ulcers on gums", "alveolar bone loss"], "Other disorders of gingiva and edentulous alveolar ridge", "K06"],
    ["Worldwide", ["genetic", "developmental", "habits (thumb sucking)"], "Developmental", ["misaligned teeth", "improper bite (malocclusion)", "crooked teeth", "jaw pain", "difficulty chewing", "facial asymmetry"], "Dentofacial anomalies (including malocclusion)", "K07"],
    ["Worldwide", ["age-related", "trauma", "periodontal disease"], "Non-infectious", ["tooth loss", "mobile teeth", "jaw bone loss", "difficulty chewing", "pain", "aesthetic concerns"], "Other disorders of teeth and supporting structures", "K08"],
    ["Worldwide", ["developmental", "idiopathic", "trauma"], "Structural", ["painless swelling", "facial asymmetry", "loose teeth", "jaw expansion", "numbness", "incidental finding on x-ray"], "Cysts of oral region, not elsewhere classified", "K09"],
    ["Worldwide", ["inflammatory", "genetic", "trauma"], "Inflammatory", ["jaw pain", "jaw swelling", "limited mouth opening", "facial deformity", "bone lesions", "numbness"], "Other diseases of jaws", "K10"],
    ["Worldwide", ["autoimmune (Sjögren's)", "viral (mumps)", "bacterial"], "Autoimmune", ["dry mouth (xerostomia)", "salivary gland swelling", "pain in gland", "difficulty swallowing", "bad taste", "fever"], "Diseases of salivary glands", "K11"],
    ["Worldwide", ["viral (herpes)", "autoimmune", "trauma"], "Viral", ["mouth ulcers (canker sores)", "pain in mouth", "redness", "swelling", "difficulty eating", "burning sensation"], "Stomatitis and related lesions", "K12"],
    ["Worldwide", ["tobacco use", "alcohol use", "chronic irritation"], "Inflammatory", ["white patches (leukoplakia)", "red patches (erythroplakia)", "ulcers", "lip swelling", "pain", "burning sensation"], "Other diseases of lip and oral mucosa", "K13"],
    ["Worldwide", ["viral", "fungal (thrush)", "nutritional deficiency"], "Inflammatory", ["sore tongue", "swollen tongue", "tongue discoloration", "patches on tongue", "loss of papillae (smooth tongue)", "burning sensation"], "Diseases of tongue", "K14"],
    
    # K20-K31: Diseases of esophagus, stomach and duodenum
    ["Worldwide", ["acid reflux", "infection (e.g., Candida)", "allergies (eosinophilic)"], "Inflammatory", ["heartburn", "difficulty swallowing (dysphagia)", "painful swallowing (odynophagia)", "chest pain", "food impaction", "coughing"], "Esophagitis", "K20"],
    ["Developed nations", ["lifestyle (diet, obesity)", "hiatal hernia", "weak lower esophageal sphincter"], "Lifestyle-related", ["heartburn (acid indigestion)", "acid regurgitation", "chest pain", "chronic cough", "hoarseness (laryngitis)", "difficulty swallowing"], "Gastro-esophageal reflux disease (GERD)", "K21"],
    ["Worldwide", ["motility disorder (achalasia)", "structural", "trauma"], "Structural", ["difficulty swallowing", "chest pain", "regurgitation of undigested food", "heartburn", "weight loss", "vomiting"], "Other diseases of esophagus", "K22"],
    ["Worldwide", ["systemic disease", "infection", "autoimmune"], "Systemic", ["difficulty swallowing", "painful swallowing", "heartburn", "regurgitation", "chest pain", "symptoms of underlying disease"], "Disorders of esophagus in diseases classified elsewhere", "K23"],
    ["Worldwide", ["bacterial (H. pylori)", "medication (NSAIDs)", "lifestyle (stress, smoking)"], "Bacterial", ["burning stomach pain", "bloating", "heartburn", "nausea", "vomiting", "feeling of fullness"], "Gastric ulcer", "K25"],
    ["Worldwide", ["bacterial (H. pylori)", "medication (NSAIDs)", "lifestyle (stress, smoking)"], "Bacterial", ["burning stomach pain", "pain worse at night", "pain relieved by eating", "bloating", "nausea", "dark tarry stools"], "Duodenal ulcer", "K26"],
    ["Worldwide", ["bacterial (H. pylori)", "medication (NSAIDs)", "stress"], "Bacterial", ["upper abdominal pain", "burning sensation", "nausea", "vomiting", "bloating", "indigestion"], "Peptic ulcer, site unspecified", "K27"],
    ["Worldwide", ["bariatric surgery", "ulcer", "stomach acid"], "Post-procedural", ["abdominal pain", "nausea", "vomiting", "GI bleeding", "weight loss", "diarrhea"], "Gastrojejunal ulcer", "K28"],
    ["Worldwide", ["bacterial (H. pylori)", "alcohol use", "medication (NSAIDs)"], "Inflammatory", ["upper abdominal pain", "nausea", "vomiting", "bloating", "loss of appetite", "indigestion (dyspepsia)"], "Gastritis and duodenitis", "K29"],
    ["Worldwide", ["idiopathic", "motility disorder", "psychosocial"], "Functional", ["upper abdominal pain", "fullness after eating", "early satiety", "bloating", "nausea", "belching"], "Functional dyspepsia", "K30"],
    ["Worldwide", ["motility disorder (gastroparesis)", "structural", "idiopathic"], "Functional", ["abdominal pain", "nausea", "vomiting (undigested food)", "bloating", "weight loss", "early satiety"], "Other diseases of stomach and duodenum", "K31"],
    
    # K35-K38: Diseases of appendix
    ["Worldwide", ["bacterial", "obstruction (fecalith)", "idiopathic"], "Bacterial", ["RLQ abdominal pain (McBurney's point)", "fever", "nausea", "vomiting", "loss of appetite", "rebound tenderness"], "Acute appendicitis", "K35"],
    ["Worldwide", ["bacterial", "obstruction", "recurrent"], "Bacterial", ["intermittent RLQ pain", "nausea", "fever", "vomiting", "loss of appetite", "previous appendicitis symptoms"], "Other appendicitis", "K36"],
    ["Worldwide", ["bacterial", "obstruction", "idiopathic"], "Bacterial", ["RLQ abdominal pain", "fever", "nausea", "vomiting", "loss of appetite", "tenderness"], "Unspecified appendicitis", "K37"],
    ["Worldwide", ["structural", "inflammation", "idiopathic"], "Structural", ["RLQ pain", "asymptomatic", "incidental finding", "appendiceal tumor", "mucocele", "diverticulum"], "Other diseases of appendix", "K38"],
    
    # K40-K46: Hernia
    ["Worldwide", ["congenital", "heavy lifting", "straining (coughing)"], "Structural", ["groin bulge", "groin pain", "pain on exertion", "burning sensation", "heaviness in groin", "scrotal swelling (males)"], "Inguinal hernia", "K40"],
    ["Worldwide", ["female predominance", "straining", "obesity"], "Structural", ["bulge in upper thigh", "groin pain", "pain on exertion", "nausea", "vomiting", "high risk of strangulation"], "Femoral hernia", "K41"],
    ["Worldwide", ["congenital (infants)", "obesity (adults)", "pregnancy"], "Structural", ["bulge near navel", "pain at navel", "swelling", "discomfort", "nausea", "vomiting"], "Umbilical hernia", "K42"],
    ["Worldwide", ["previous surgery (incisional)", "obesity", "straining"], "Structural", ["bulge at surgical scar", "abdominal pain", "swelling", "nausea", "vomiting", "bowel obstruction"], "Ventral hernia", "K43"],
    ["Worldwide", ["age-related", "obesity", "hiatal"], "Structural", ["heartburn", "acid reflux", "chest pain", "difficulty swallowing", "shortness of breath", "regurgitation"], "Diaphragmatic hernia", "K44"],
    ["Worldwide", ["congenital", "trauma", "straining"], "Structural", ["abdominal bulge (site-specific)", "pain", "swelling", "site-specific symptoms", "nausea", "vomiting"], "Other abdominal hernia", "K45"],
    ["Worldwide", ["congenital", "straining", "obesity"], "Structural", ["abdominal bulge", "pain", "discomfort", "swelling", "nausea", "vomiting"], "Unspecified abdominal hernia", "K46"],
    
    # K50-K52: Noninfective enteritis and colitis
    ["Developed nations", ["autoimmune", "genetic", "environmental (smoking)"], "Autoimmune", ["abdominal pain (cramping)", "diarrhea (non-bloody)", "weight loss", "fatigue", "fever", "anal fissures"], "Crohn's disease", "K50"],
    ["Developed nations", ["autoimmune", "genetic", "environmental"], "Autoimmune", ["bloody diarrhea", "abdominal cramping", "rectal urgency (tenesmus)", "weight loss", "fatigue", "fever"], "Ulcerative colitis", "K51"],
    ["Worldwide", ["medication (NSAIDs)", "radiation", "allergic"], "Inflammatory", ["diarrhea", "abdominal pain", "nausea", "vomiting", "weight loss", "malnutrition"], "Other noninfective gastroenteritis and colitis", "K52"],
    
    # K55-K64: Other diseases of intestines
    ["Worldwide", ["age-related", "atherosclerosis", "thrombosis"], "Vascular", ["sudden severe abdominal pain", "bloody diarrhea", "fever", "nausea", "vomiting", "shock"], "Vascular disorders of intestine", "K55"],
    ["Worldwide", ["post-surgical (adhesions)", "medication (opioids)", "obstruction"], "Functional", ["abdominal distension", "no bowel sounds (ileus)", "vomiting", "constipation (obstipation)", "nausea", "cramping pain"], "Paralytic ileus and intestinal obstruction without hernia", "K56"],
    ["Developed nations", ["dietary (low fiber)", "age-related", "obesity"], "Lifestyle-related", ["LLQ abdominal pain", "fever (diverticulitis)", "nausea", "constipation", "diarrhea", "bloating"], "Diverticular disease of intestine", "K57"],
    ["Worldwide", ["idiopathic", "psychosocial (stress)", "gut-brain axis disorder"], "Functional", ["abdominal pain (relieved by defecation)", "bloating", "diarrhea", "constipation", "alternating stools", "mucus in stool"], "Irritable bowel syndrome (IBS)", "K58"],
    ["Worldwide", ["dietary", "medication", "motility disorder"], "Functional", ["constipation", "diarrhea", "bloating", "incomplete evacuation", "straining", "abdominal pain"], "Other functional intestinal disorders", "K59"],
    ["Worldwide", ["constipation (hard stools)", "trauma", "IBD"], "Structural", ["severe anal pain during defecation", "bleeding during defecation", "itching", "swelling", "discharge (fistula)", "painful sitting"], "Fissure and fistula of anal and rectal regions", "K60"],
    ["Worldwide", ["bacterial", "blocked anal gland", "IBD"], "Bacterial", ["constant throbbing anal pain", "swelling", "redness", "fever", "pus drainage", "difficulty sitting"], "Abscess of anal and rectal regions", "K61"],
    ["Worldwide", ["trauma", "infection", "prolapse"], "Structural", ["rectal bleeding", "anal pain", "itching (pruritus ani)", "discharge", "fecal incontinence", "rectal prolapse"], "Other diseases of anus and rectum", "K62"],
    ["Worldwide", ["vascular", "inflammatory", "post-procedural"], "Inflammatory", ["abdominal pain", "diarrhea", "GI bleeding", "weight loss", "malnutrition", "nausea"], "Other diseases of intestine", "K63"],
    ["Worldwide", ["straining (constipation)", "pregnancy", "obesity"], "Vascular", ["anal itching", "anal pain", "bright red blood on toilet paper", "lump near anus", "swelling", "discomfort"], "Hemorrhoids and perianal venous thrombosis", "K64"],
    
    # K65-K68: Diseases of peritoneum and retroperitoneum
    ["Worldwide", ["bacterial", "organ rupture (appendix)", "dialysis"], "Bacterial", ["severe abdominal pain", "fever", "abdominal rigidity (guarding)", "nausea", "vomiting", "shock"], "Peritonitis", "K65"],
    ["Worldwide", ["post-surgical (adhesions)", "inflammatory", "cancer"], "Inflammatory", ["chronic abdominal pain", "bloating", "ascites", "fever", "bowel obstruction", "nausea"], "Other disorders of peritoneum", "K66"],
    ["Worldwide", ["bacterial (TB)", "parasitic", "viral"], "Infectious", ["abdominal pain", "fever", "ascites", "symptoms of primary infection", "weight loss", "malaise"], "Disorders of peritoneum in infectious diseases classified elsewhere", "K67"],
    ["Worldwide", ["bacterial", "trauma", "cancer"], "Inflammatory", ["flank pain", "fever", "abdominal mass", "weight loss", "nausea", "vomiting"], "Disorders of retroperitoneum", "K68"],
    
    # K70-K77: Diseases of liver
    ["Worldwide", ["alcohol use (chronic)", "genetic susceptibility", "malnutrition"], "Lifestyle-related", ["jaundice (yellow skin)", "ascites (fluid in abdomen)", "fatigue", "abdominal pain (RUQ)", "nausea", "weight loss"], "Alcoholic liver disease", "K70"],
    ["Worldwide", ["medication-induced (e.g., paracetamol)", "toxin exposure", "herbal supplements"], "Toxic", ["jaundice", "nausea", "fatigue", "vomiting", "abdominal pain (RUQ)", "dark urine"], "Toxic liver disease", "K71"],
    ["Worldwide", ["viral (hepatitis)", "toxic (drugs, alcohol)", "metabolic"], "Metabolic", ["jaundice", "confusion (encephalopathy)", "ascites", "bleeding tendency", "fatigue", "coma"], "Hepatic failure, not elsewhere classified", "K72"],
    ["Worldwide", ["viral (HBV, HCV)", "autoimmune", "idiopathic"], "Viral", ["fatigue", "jaundice (mild)", "RUQ pain", "loss of appetite", "nausea", "joint pain"], "Chronic hepatitis, not elsewhere classified", "K73"],
    ["Worldwide", ["alcohol use", "viral hepatitis (HBV, HCV)", "fatty liver (NAFLD)"], "Lifestyle-related", ["fatigue", "jaundice", "ascites", "easy bruising (coagulopathy)", "swelling (edema)", "confusion (encephalopathy)"], "Fibrosis and cirrhosis of liver", "K74"],
    ["Worldwide", ["autoimmune", "bacterial (abscess)", "viral"], "Autoimmune", ["fever", "RUQ pain", "jaundice", "fatigue", "nausea", "liver abscess"], "Other inflammatory liver diseases", "K75"],
    ["Worldwide", ["vascular (Budd-Chiari)", "metabolic", "structural (cysts)"], "Vascular", ["ascites", "abdominal pain", "jaundice", "fatigue", "liver cysts", "tumors"], "Other diseases of liver", "K76"],
    ["Worldwide", ["systemic infection", "parasitic (schistosomiasis)", "congenital"], "Systemic", ["jaundice", "fever", "fatigue", "RUQ pain", "symptoms of primary disease", "hepatomegaly (enlarged liver)"], "Liver disorders in diseases classified elsewhere", "K77"],
    
    # K80-K87: Disorders of gallbladder, biliary tract and pancreas
    ["Developed nations", ["dietary (high fat)", "female", "obesity"], "Metabolic", ["RUQ pain after eating (biliary colic)", "nausea", "vomiting", "jaundice", "fever", "indigestion"], "Cholelithiasis (Gallstones)", "K80"],
    ["Worldwide", ["gallstone obstruction", "bacterial", "idiopathic"], "Bacterial", ["severe constant RUQ pain", "fever", "nausea", "vomiting", "jaundice", "positive Murphy's sign"], "Cholecystitis", "K81"],
    ["Worldwide", ["structural", "inflammatory", "polyps"], "Structural", ["RUQ pain", "nausea", "vomiting", "indigestion", "jaundice", "asymptomatic"], "Other diseases of gallbladder", "K82"],
    ["Worldwide", ["gallstones", "post-surgical stricture", "tumors"], "Structural", ["jaundice", "RUQ pain", "fever (cholangitis)", "itching (pruritus)", "dark urine", "pale stools"], "Other diseases of biliary tract", "K83"],
    ["Worldwide", ["gallstones", "alcohol use", "medication"], "Inflammatory", ["severe upper abdominal pain", "pain radiating to back", "nausea", "vomiting", "fever", "tachycardia (rapid heart rate)"], "Acute pancreatitis", "K85"],
    ["Worldwide", ["alcohol use (chronic)", "genetic", "idiopathic"], "Lifestyle-related", ["chronic upper abdominal pain", "weight loss", "diarrhea (steatorrhea)", "diabetes (new onset)", "nausea", "vomiting"], "Other diseases of pancreas", "K86"],
    ["Worldwide", ["systemic infection (mumps)", "autoimmune", "trauma"], "Systemic", ["abdominal pain", "nausea", "vomiting", "fever", "jaundice", "symptoms of primary disease"], "Disorders of gallbladder, biliary tract and pancreas in diseases classified elsewhere", "K87"],
    
    # K90-K95: Other diseases of the digestive system
    ["Worldwide", ["celiac disease", "IBD (Crohn's)", "infection"], "Autoimmune", ["diarrhea (chronic)", "weight loss", "bloating", "fatigue", "anemia", "vitamin deficiencies"], "Intestinal malabsorption", "K90"],
    ["Worldwide", ["post-procedural", "adhesions", "infection"], "Post-procedural", ["abdominal pain", "nausea", "vomiting", "diarrhea", "fever", "bleeding"], "Intraoperative and postprocedural complications of digestive system", "K91"],
    ["Worldwide", ["vascular", "motility", "idiopathic"], "Functional", ["abdominal pain", "GI bleeding", "nausea", "vomiting", "diarrhea", "constipation"], "Other diseases of digestive system", "K92"],
    ["Worldwide", ["systemic disease", "autoimmune", "vascular"], "Systemic", ["abdominal pain", "nausea", "vomiting", "GI bleeding", "symptoms of primary disease", "weight loss"], "Disorders of other digestive organs in diseases classified elsewhere", "K93"]
]

sectionL = [
    {
        "icd_code": "L00",
        "disease_name": "Staphylococcal scalded skin syndrome",
        "geography": "Worldwide",
        "transmission": ["Toxin-mediated", "Direct contact", "Bacterial spread"],
        "disease_type": "Bacterial",
        "symptoms": ["Widespread blisters", "Red rash", "Skin peeling", "Fever", "Irritability", "Skin pain"]
    },
    {
        "icd_code": "L01",
        "disease_name": "Impetigo",
        "geography": "Worldwide",
        "transmission": ["Direct contact", "Contaminated fomites", "Autoinoculation"],
        "disease_type": "Bacterial",
        "symptoms": ["Red sores", "Honey-colored crusts", "Itching", "Blisters", "Swollen lymph nodes", "Painless sores"]
    },
    {
        "icd_code": "L02",
        "disease_name": "Cutaneous abscess, furuncle and carbuncle",
        "geography": "Worldwide",
        "transmission": ["Bacterial entry", "Blocked follicle", "Skin trauma"],
        "disease_type": "Bacterial",
        "symptoms": ["Painful lump", "Red skin", "Pus-filled center", "Swelling", "Fever", "Tenderness"]
    },
    {
        "icd_code": "L03",
        "disease_name": "Cellulitis",
        "geography": "Worldwide",
        "transmission": ["Bacterial entry", "Skin break", "Insect bite"],
        "disease_type": "Bacterial",
        "symptoms": ["Red area", "Swelling", "Warmth", "Pain", "Fever", "Chills"]
    },
    {
        "icd_code": "L04",
        "disease_name": "Acute lymphadenitis",
        "geography": "Worldwide",
        "transmission": ["Bacterial infection", "Viral infection", "Secondary to infection"],
        "disease_type": "Bacterial",
        "symptoms": ["Swollen lymph nodes", "Tender nodes", "Red skin over nodes", "Fever", "Malaise", "Hard nodes"]
    },
    {
        "icd_code": "L05",
        "disease_name": "Pilonidal cyst",
        "geography": "Worldwide",
        "transmission": ["Ingrown hair", "Friction", "Pressure"],
        "disease_type": "Non-infectious",
        "symptoms": ["Pain at tailbone", "Swelling", "Redness", "Pus drainage", "Foul smell", "Dimple in skin"]
    },
    {
        "icd_code": "L08",
        "disease_name": "Other local infections of skin and subcutaneous tissue",
        "geography": "Worldwide",
        "transmission": ["Bacterial entry", "Fungal overgrowth", "Skin trauma"],
        "disease_type": "Bacterial",
        "symptoms": ["Localized redness", "Pustules", "Itching", "Pain", "Erythema", "Mild swelling"]
    },
    {
        "icd_code": "L10",
        "disease_name": "Pemphigus",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Genetic predisposition"],
        "disease_type": "Autoimmune",
        "symptoms": ["Flaccid blisters", "Painful sores", "Skin erosion", "Mouth blisters", "Difficulty swallowing", "Skin peeling"]
    },
    {
        "icd_code": "L11",
        "disease_name": "Other acantholytic disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Unknown etiology"],
        "disease_type": "Genetic",
        "symptoms": ["Blisters", "Erosions", "Crusting", "Itching", "Skin fragility", "Scaly patches"]
    },
    {
        "icd_code": "L12",
        "disease_name": "Pemphigoid",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Age-related"],
        "disease_type": "Autoimmune",
        "symptoms": ["Tense blisters", "Severe itching", "Red rash", "Urticarial plaques", "Mouth sores", "Skin redness"]
    },
    {
        "icd_code": "L13",
        "disease_name": "Other bullous disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Drug-induced"],
        "disease_type": "Autoimmune",
        "symptoms": ["Blisters", "Itching", "Redness", "Erosions", "Skin fragility", "Varied blister types"]
    },
    {
        "icd_code": "L14",
        "disease_name": "Bullous disorders in diseases classified elsewhere",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Metabolic disorder"],
        "disease_type": "Non-infectious",
        "symptoms": ["Blisters", "Skin fragility", "Erosions", "Underlying disease symptoms", "Metabolic imbalance", "Nutritional deficiency"]
    },
    {
        "icd_code": "L20",
        "disease_name": "Atopic dermatitis (Eczema)",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic predisposition", "Immune dysfunction"],
        "disease_type": "Inflammatory",
        "symptoms": ["Dry skin", "Severe itching", "Red patches", "Scaly skin", "Oozing", "Crusting"]
    },
    {
        "icd_code": "L21",
        "disease_name": "Seborrhoeic dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Fungal overgrowth (Malassezia)", "Inflammatory reaction"],
        "disease_type": "Fungal",
        "symptoms": ["Dandruff", "Greasy scales", "Red skin", "Itching", "Scalp patches", "Face rash"]
    },
    {
        "icd_code": "L22",
        "disease_name": "Diaper dermatitis",
        "geography": "Americas",
        "transmission": ["Irritant contact", "Prolonged moisture", "Friction"],
        "disease_type": "Irritant",
        "symptoms": ["Red rash in diaper area", "Chafing", "Skin irritation", "Infant discomfort", "Peeling skin", "Bright red patches"]
    },
    {
        "icd_code": "L23",
        "disease_name": "Allergic contact dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Allergen contact", "Delayed hypersensitivity"],
        "disease_type": "Allergic",
        "symptoms": ["Itchy rash", "Redness", "Blisters", "Oozing", "Swelling", "Scaling"]
    },
    {
        "icd_code": "L24",
        "disease_name": "Irritant contact dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Irritant contact", "Chemical exposure"],
        "disease_type": "Irritant",
        "symptoms": ["Red rash", "Dryness", "Cracking", "Burning", "Itching", "Swelling"]
    },
    {
        "icd_code": "L25",
        "disease_name": "Unspecified contact dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Unknown contactant", "Inflammatory reaction"],
        "disease_type": "Inflammatory",
        "symptoms": ["Red rash", "Itching", "Swelling", "Dryness", "Blisters", "Oozing"]
    },
    {
        "icd_code": "L26",
        "disease_name": "Exfoliative dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Drug reaction", "Underlying skin disease"],
        "disease_type": "Inflammatory",
        "symptoms": ["Widespread redness", "Massive skin peeling", "Itching", "Chills", "Fever", "Swollen lymph nodes"]
    },
    {
        "icd_code": "L27",
        "disease_name": "Dermatitis due to substances taken internally",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Drug ingestion", "Food allergy"],
        "disease_type": "Allergic",
        "symptoms": ["Widespread rash", "Itching", "Hives", "Redness", "Swelling", "Morbilliform rash"]
    },
    {
        "icd_code": "L28",
        "disease_name": "Lichen simplex chronicus and prurigo",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Chronic scratching", "Psychogenic factors"],
        "disease_type": "Inflammatory",
        "symptoms": ["Thickened skin", "Intense itching", "Scaly plaques", "Hyperpigmentation", "Excoriations", "Nodules"]
    },
    {
        "icd_code": "L29",
        "disease_name": "Pruritus (Itching)",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Symptom of disease", "Dry skin"],
        "disease_type": "Symptom",
        "symptoms": ["Itching", "Scratch marks", "Dry skin", "Redness", "Skin irritation", "Underlying rash"]
    },
    {
        "icd_code": "L30",
        "disease_name": "Other dermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Unknown etiology", "Inflammatory reaction"],
        "disease_type": "Inflammatory",
        "symptoms": ["Rash", "Itching", "Redness", "Dryness", "Vesicles", "Scaling"]
    },
    {
        "icd_code": "L40",
        "disease_name": "Psoriasis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Genetic predisposition"],
        "disease_type": "Autoimmune",
        "symptoms": ["Red plaques", "Silvery scales", "Itching", "Dry skin", "Pitted nails", "Joint pain"]
    },
    {
        "icd_code": "L41",
        "disease_name": "Parapsoriasis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Unknown etiology", "Inflammatory"],
        "disease_type": "Inflammatory",
        "symptoms": ["Scaly patches", "Red-brown patches", "Thin plaques", "Mild itching", "Atrophy", "Resembles psoriasis"]
    },
    {
        "icd_code": "L42",
        "disease_name": "Pityriasis rosea",
        "geography": "Worldwide",
        "transmission": ["Viral (suspected)", "Non-infectious", "Unknown etiology"],
        "disease_type": "Viral",
        "symptoms": ["Herald patch", "Oval pink-red patches", "Fine scale", "Itching", "Christmas tree pattern", "Malaise"]
    },
    {
        "icd_code": "L43",
        "disease_name": "Lichen planus",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Hepatitis C association"],
        "disease_type": "Autoimmune",
        "symptoms": ["Purple papules", "Flat-topped papules", "Itching", "Wickham striae", "Mouth lesions", "Nail ridging"]
    },
    {
        "icd_code": "L44",
        "disease_name": "Other papulosquamous disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Unknown etiology"],
        "disease_type": "Inflammatory",
        "symptoms": ["Papules", "Scales", "Redness", "Itching", "Plaques", "Varied morphology"]
    },
    {
        "icd_code": "L45",
        "disease_name": "Papulosquamous disorders in diseases classified elsewhere",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Systemic illness"],
        "disease_type": "Non-infectious",
        "symptoms": ["Scaly papules", "Underlying disease symptoms", "Eruption", "Redness", "Plaques", "Itching"]
    },
    {
        "icd_code": "L50",
        "disease_name": "Urticaria (Hives)",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Allergic reaction", "Autoimmune"],
        "disease_type": "Allergic",
        "symptoms": ["Wheals", "Raised red welts", "Intense itching", "Swelling", "Transient lesions", "Angioedema"]
    },
    {
        "icd_code": "L51",
        "disease_name": "Erythema multiforme",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Infection (Herpes)", "Drug reaction"],
        "disease_type": "Hypersensitivity",
        "symptoms": ["Target lesions", "Red macules", "Papules", "Blisters", "Mouth sores", "Fever"]
    },
    {
        "icd_code": "L52",
        "disease_name": "Erythema nodosum",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Hypersensitivity", "Infection (Strep)"],
        "disease_type": "Hypersensitivity",
        "symptoms": ["Tender red nodules", "Shin lesions", "Joint pain", "Fever", "Malaise", "Bruise-like discoloration"]
    },
    {
        "icd_code": "L53",
        "disease_name": "Other erythematous conditions",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Unknown etiology"],
        "disease_type": "Inflammatory",
        "symptoms": ["Redness", "Rash", "Macules", "Papules", "Figurate erythema", "Itching"]
    },
    {
        "icd_code": "L54",
        "disease_name": "Erythema in diseases classified elsewhere",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Systemic illness"],
        "disease_type": "Non-infectious",
        "symptoms": ["Redness", "Rash", "Underlying disease symptoms", "Fever", "Malaise", "Warm skin"]
    },
    {
        "icd_code": "L55",
        "disease_name": "Sunburn",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "UV radiation", "Sun exposure"],
        "disease_type": "Environmental",
        "symptoms": ["Red skin", "Pain", "Swelling", "Blisters", "Peeling", "Headache"]
    },
    {
        "icd_code": "L56",
        "disease_name": "Other acute skin changes due to ultraviolet radiation",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "UV radiation", "Drug-induced photosensitivity"],
        "disease_type": "Environmental",
        "symptoms": ["Polymorphic light eruption", "Itchy rash", "Sun allergy", "Papules", "Vesicles", "Redness"]
    },
    {
        "icd_code": "L57",
        "disease_name": "Skin changes due to chronic exposure to nonionizing radiation",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Chronic sun exposure", "UV radiation"],
        "disease_type": "Environmental",
        "symptoms": ["Wrinkles", "Actinic keratosis", "Solar elastosis", "Leathery skin", "Age spots", "Telangiectasia"]
    },
    {
        "icd_code": "L58",
        "disease_name": "Radiodermatitis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Ionizing radiation", "Radiation therapy"],
        "disease_type": "Environmental",
        "symptoms": ["Redness", "Dryness", "Peeling", "Pain", "Ulceration", "Fibrosis"]
    },
    {
        "icd_code": "L59",
        "disease_name": "Other disorders of skin and subcutaneous tissue related to radiation",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Radiation exposure", "Unknown etiology"],
        "disease_type": "Environmental",
        "symptoms": ["Skin changes", "Pigmentation changes", "Atrophy", "Fibrosis", "Ulceration", "Chronic redness"]
    },
    {
        "icd_code": "L60",
        "disease_name": "Nail disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Trauma", "Fungal infection"],
        "disease_type": "Non-infectious",
        "symptoms": ["Pitting", "Discoloration", "Thickening", "Brittleness", "Splitting", "Ingrown nail"]
    },
    {
        "icd_code": "L62",
        "disease_name": "Nail disorders in diseases classified elsewhere",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Systemic illness"],
        "disease_type": "Non-infectious",
        "symptoms": ["Nail pitting (psoriasis)", "Clubbing (lung disease)", "Spoon nails (anemia)", "Beau lines", "Splinter hemorrhages", "Yellow nail syndrome"]
    },
    {
        "icd_code": "L63",
        "disease_name": "Alopecia areata",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Genetic predisposition"],
        "disease_type": "Autoimmune",
        "symptoms": ["Patchy hair loss", "Smooth bald patches", "Exclamation mark hairs", "Nail pitting", "Round patches", "Sudden onset"]
    },
    {
        "icd_code": "L64",
        "disease_name": "Androgenic alopecia",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Hormonal (DHT)"],
        "disease_type": "Genetic",
        "symptoms": ["Hair thinning", "Receding hairline", "Crown balding", "Gradual onset", "Patterned hair loss", "Miniaturized hairs"]
    },
    {
        "icd_code": "L65",
        "disease_name": "Other nonscarring hair loss",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Stress (telogen effluvium)", "Traction"],
        "disease_type": "Environmental",
        "symptoms": ["Diffuse hair shedding", "Hair thinning", "No scarring", "Increased hair in brush", "Stress-related onset", "Traction-related breakage"]
    },
    {
        "icd_code": "L66",
        "disease_name": "Scarring alopecia",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Autoimmune"],
        "disease_type": "Inflammatory",
        "symptoms": ["Permanent hair loss", "Scalp inflammation", "Scarring", "Itching", "Burning", "Follicular destruction"]
    },
    {
        "icd_code": "L67",
        "disease_name": "Hair color and hair shaft abnormalities",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Nutritional deficiency"],
        "disease_type": "Genetic",
        "symptoms": ["Hair breakage", "Dry hair", "Brittle hair", "Knotting", "Abnormal texture", "Premature graying"]
    },
    {
        "icd_code": "L68",
        "disease_name": "Hypertrichosis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Drug-induced"],
        "disease_type": "Genetic",
        "symptoms": ["Excessive hair growth", "Abnormal hair location", "Vellus hair", "Terminal hair", "Generalized growth", "Localized growth"]
    },
    {
        "icd_code": "L70",
        "disease_name": "Acne",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Hormonal", "Bacterial (P. acnes)"],
        "disease_type": "Inflammatory",
        "symptoms": ["Comedones (blackheads)", "Whiteheads", "Pimples", "Cysts", "Nodules", "Oily skin"]
    },
    {
        "icd_code": "L71",
        "disease_name": "Rosacea",
        "geography": "Europe",
        "transmission": ["Non-infectious", "Inflammatory", "Genetic predisposition"],
        "disease_type": "Inflammatory",
        "symptoms": ["Facial redness", "Flushing", "Visible blood vessels", "Pimples", "Thickened skin (rhinophyma)", "Eye irritation"]
    },
    {
        "icd_code": "L72",
        "disease_name": "Follicular cysts of skin and subcutaneous tissue",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Blocked follicle", "Unknown etiology"],
        "disease_type": "Non-infectious",
        "symptoms": ["Painless lump", "Epidermoid cyst", "Pilar cyst", "Round nodule", "Movable under skin", "Cheesy discharge"]
    },
    {
        "icd_code": "L73",
        "disease_name": "Other follicular disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Bacterial", "Inflammatory"],
        "disease_type": "Inflammatory",
        "symptoms": ["Folliculitis", "Acne keloidalis nuchae", "Itchy bumps", "Pustules at hair follicle", "Scalp bumps", "Keloidal scars"]
    },
    {
        "icd_code": "L74",
        "disease_name": "Eccrine sweat disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Heat", "Blocked sweat duct"],
        "disease_type": "Non-infectious",
        "symptoms": ["Miliaria (heat rash)", "Prickly heat", "Small red blisters", "Itching", "Anhidrosis (no sweat)", "Hyperhidrosis (excess sweat)"]
    },
    {
        "icd_code": "L75",
        "disease_name": "Apocrine sweat disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Bacterial", "Inflammatory"],
        "disease_type": "Inflammatory",
        "symptoms": ["Hidradenitis suppurativa", "Painful lumps", "Abscesses", "Tracts", "Scarring", "Bromhidrosis (foul odor)"]
    },
    {
        "icd_code": "L80",
        "disease_name": "Vitiligo",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Genetic predisposition"],
        "disease_type": "Autoimmune",
        "symptoms": ["White skin patches", "Depigmentation", "Symmetrical patches", "Hair whitening", "Mucous membrane involvement", "No scaling"]
    },
    {
        "icd_code": "L81",
        "disease_name": "Other disorders of pigmentation",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Sun exposure"],
        "disease_type": "Pigmentation",
        "symptoms": ["Hyperpigmentation", "Hypopigmentation", "Freckles", "Melasma", "Age spots", "Uneven skin tone"]
    },
    {
        "icd_code": "L82",
        "disease_name": "Seborrhoeic keratosis",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Age-related", "Genetic"],
        "disease_type": "Benign neoplasm",
        "symptoms": ["Warty growth", "Brown or black lesion", "Stuck-on appearance", "Waxy texture", "Itching", "Multiple lesions"]
    },
    {
        "icd_code": "L83",
        "disease_name": "Acanthosis nigricans",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Insulin resistance", "Obesity"],
        "disease_type": "Metabolic",
        "symptoms": ["Dark velvety patches", "Thickened skin", "Neck folds", "Armpits", "Groin", "Skin tags"]
    },
    {
        "icd_code": "L84",
        "disease_name": "Corns and callosities",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Friction", "Pressure"],
        "disease_type": "Environmental",
        "symptoms": ["Thick hard skin", "Pain on pressure", "Foot lesions", "Central core (corn)", "Diffuse thickening (callus)", "Dry skin"]
    },
    {
        "icd_code": "L85",
        "disease_name": "Other epidermal thickening",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Genetic", "Inflammatory"],
        "disease_type": "Genetic",
        "symptoms": ["Keratoderma", "Thickened palms", "Thickened soles", "Scaling", "Cracking", "Pain"]
    },
    {
        "icd_code": "L86",
        "disease_name": "Keratoderma in diseases classified elsewhere",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Systemic illness"],
        "disease_type": "Non-infectious",
        "symptoms": ["Thickened palms", "Thickened soles", "Underlying disease symptoms", "Scaling", "Fissures", "Inflammation"]
    },
    {
        "icd_code": "L87",
        "disease_name": "Transepidermal elimination disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Unknown etiology"],
        "disease_type": "Inflammatory",
        "symptoms": ["Papules", "Crusting", "Itching", "Umbilicated lesions", "Collarette of scale", "Elimination of dermal material"]
    },
    {
        "icd_code": "L88",
        "disease_name": "Pyoderma gangrenosum",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Associated with IBD"],
        "disease_type": "Autoimmune",
        "symptoms": ["Painful ulcer", "Rapidly expanding ulcer", "Violaceous border", "Pustule progressing to ulcer", "Leg lesions", "Pathergy"]
    },
    {
        "icd_code": "L89",
        "disease_name": "Decubitus ulcer (Pressure ulcer)",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Prolonged pressure", "Immobility"],
        "disease_type": "Environmental",
        "symptoms": ["Skin redness", "Broken skin", "Ulceration", "Pain", "Necrosis", "Infection"]
    },
    {
        "icd_code": "L90",
        "disease_name": "Atrophic disorders of skin",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Aging"],
        "disease_type": "Inflammatory",
        "symptoms": ["Thin skin", "Wrinkling", "Loss of elasticity", "Anetoderma", "Striae (stretch marks)", "Lichen sclerosus"]
    },
    {
        "icd_code": "L91",
        "disease_name": "Hypertrophic disorders of skin",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Abnormal healing", "Genetic"],
        "disease_type": "Non-infectious",
        "symptoms": ["Keloid scar", "Hypertrophic scar", "Raised scar", "Itching", "Pain", "Extends beyond wound border"]
    },
    {
        "icd_code": "L92",
        "disease_name": "Granulomatous disorders of skin and subcutaneous tissue",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Inflammatory", "Unknown etiology"],
        "disease_type": "Inflammatory",
        "symptoms": ["Granuloma annulare", "Annular plaques", "Ring-shaped lesions", "Papules", "No scale", "Necrobiosis lipoidica"]
    },
    {
        "icd_code": "L93",
        "disease_name": "Lupus erythematosus",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Genetic predisposition"],
        "disease_type": "Autoimmune",
        "symptoms": ["Butterfly rash (malar)", "Discoid rash", "Photosensitivity", "Scaly patches", "Atrophy", "Joint pain"]
    },
    {
        "icd_code": "L94",
        "disease_name": "Other localized connective tissue disorders",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Inflammatory"],
        "disease_type": "Autoimmune",
        "symptoms": ["Morphea (localized scleroderma)", "Hardened skin patches", "Waxy texture", "Loss of hair in patch", "Joint pain", "Linear scleroderma"]
    },
    {
        "icd_code": "L95",
        "disease_name": "Vasculitis limited to skin, not elsewhere classified",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Autoimmune", "Hypersensitivity"],
        "disease_type": "Autoimmune",
        "symptoms": ["Palpable purpura", "Red or purple spots", "Non-blanching rash", "Leg lesions", "Itching", "Burning"]
    },
    {
        "icd_code": "L97",
        "disease_name": "Non-pressure chronic ulcer of lower limb",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Venous insufficiency", "Arterial disease"],
        "disease_type": "Vascular",
        "symptoms": ["Leg ulcer", "Slow healing", "Pain", "Swelling", "Skin discoloration", "Discharge"]
    },
    {
        "icd_code": "L98",
        "disease_name": "Other disorders of skin and subcutaneous tissue, NEC",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Unknown etiology", "Various causes"],
        "disease_type": "Non-infectious",
        "symptoms": ["Skin ulcer", "Chronic skin changes", "Edema", "Fibrosis", "Hygroma", "Calcinosis"]
    },
    {
        "icd_code": "L99",
        "disease_name": "Other disorders of skin and subcutaneous tissue in diseases NEC",
        "geography": "Worldwide",
        "transmission": ["Non-infectious", "Secondary to disease", "Systemic illness"],
        "disease_type": "Non-infectious",
        "symptoms": ["Amyloidosis cutis", "Metastatic calcification", "Skin manifestations of internal disease", "Porphyria cutanea tarda", "Xanthomas", "Dermopathy"]
    }
]

sectionM = [
    # M00-M14: Inflammatory polyarthropathies
    {
        "Geography": "Worldwide",
        "Transmission": ["bacterial-spread", "bloodstream", "direct-inoculation"],
        "Disease Type": "bacterial",
        "Symptoms": ["sudden-joint-pain", "severe-joint-swelling", "fever", "chills", "limited-range-of-motion", "skin-redness-over-joint"],
        "Label": "Pyogenic arthritis",
        "ICD Code": "M00"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["viral-spread", "parasitic-spread", "fungal-spread"],
        "Disease Type": "viral", # Can be any of them
        "Symptoms": ["joint-pain", "joint-swelling", "fever", "rash", "symptoms-of-primary-infection", "malaise"],
        "Label": "Direct infections of joint in infectious and parasitic diseases",
        "ICD Code": "M01"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["gastrointestinal-infection", "genitourinary-infection", "post-infection"], # Trigger transmission
        "Disease Type": "bacterial", # Trigger type
        "Symptoms": ["arthritis-pain", "eye-inflammation", "urethritis", "swollen-toes-or-fingers", "heel-pain", "lower-back-pain"],
        "Label": "Reactive arthropathies",
        "ICD Code": "M02"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["post-infection", "N/A", "N/A"], # Trigger transmission
        "Disease Type": "bacterial", # Trigger type (can be others)
        "Symptoms": ["joint-inflammation", "follows-infection", "joint-stiffness", "fever", "fatigue", "symptoms-of-primary-disease"],
        "Label": "Postinfective and reactive arthropathies in diseases classified elsewhere",
        "ICD Code": "M03"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["recurrent-fever", "joint-pain", "skin-rash", "abdominal-pain", "mouth-sores", "fatigue"],
        "Label": "Autoinflammatory syndromes",
        "ICD Code": "M04"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["symmetrical-joint-pain", "morning-stiffness", "joint-swelling", "rheumatoid-nodules", "fatigue", "low-grade-fever"],
        "Label": "Seropositive rheumatoid arthritis",
        "ICD Code": "M05"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-swelling", "morning-stiffness", "fatigue", "malaise", "negative-rheumatoid-factor"],
        "Label": "Other rheumatoid arthritis",
        "ICD Code": "M06"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "psoriatic-skin-rash", "nail-changes", "swollen-fingers-or-toes", "back-pain", "eye-inflammation"],
        "Label": "Psoriatic and enteropathic arthropathies",
        "ICD Code": "M07"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain-in-child", "joint-swelling-in-child", "persistent-fever", "rash", "limping", "growth-problems"],
        "Label": "Juvenile arthritis",
        "ICD Code": "M08"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain-in-child", "underlying-disease-symptoms", "fever", "fatigue", "limited-movement", "swelling"],
        "Label": "Juvenile arthritis in diseases classified elsewhere",
        "ICD Code": "M09"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["severe-joint-pain", "big-toe-pain", "joint-redness", "joint-swelling", "tophi-deposits", "limited-range-of-motion"],
        "Label": "Gout",
        "ICD Code": "M10"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-swelling", "calcium-crystal-deposits", "stiffness", "pseudo-gout", "cartilage-calcification"],
        "Label": "Other crystal arthropathies",
        "ICD Code": "M11"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-instability", "recurrent-swelling", "joint-stiffness", "clicking-or-locking", "history-of-trauma"],
        "Label": "Other specific arthropathies",
        "ICD Code": "M12"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-stiffness", "swelling", "inflammation", "crepitus", "reduced-mobility"],
        "Label": "Other arthritis",
        "ICD Code": "M13"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "underlying-disease-symptoms", "joint-stiffness", "swelling", "inflammation", "systemic-symptoms"],
        "Label": "Arthropathies in other diseases classified elsewhere",
        "ICD Code": "M14"
    },

    # M15-M19: Osteoarthritis
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["pain-in-multiple-joints", "stiffness-after-rest", "bony-enlargements-hands", "grating-sensation", "limited-range-of-motion", "aching-pain"],
        "Label": "Polyosteoarthritis",
        "ICD Code": "M15"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["hip-pain", "groin-pain", "stiffness-in-hip", "limited-hip-motion", "limping", "pain-worse-with-activity"],
        "Label": "Coxarthrosis [osteoarthritis of hip]",
        "ICD Code": "M16"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["knee-pain", "knee-stiffness", "swelling-in-knee", "grating-sensation", "buckling-of-knee", "difficulty-climbing-stairs"],
        "Label": "Gonarthrosis [osteoarthritis of knee]",
        "ICD Code": "M17"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["thumb-base-pain", "difficulty-gripping", "stiffness-at-thumb-base", "swelling-at-thumb-base", "bony-lump", "grinding-sensation"],
        "Label": "Osteoarthritis of first carpometacarpal joint",
        "ICD Code": "M18"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-stiffness", "limited-range-of-motion", "swelling", "crepitus", "pain-after-use"],
        "Label": "Other osteoarthritis",
        "ICD Code": "M19"
    },

    # M20-M25: Other joint disorders
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["deformed-finger", "deformed-toe", "hammer-toe", "mallet-finger", "bunion", "pain-with-footwear"],
        "Label": "Acquired deformities of fingers and toes",
        "ICD Code": "M20"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["unequal-leg-length", "limb-deformity", "gait-abnormality", "pain", "functional-limitation", "joint-contracture"],
        "Label": "Other acquired deformities of limbs",
        "ICD Code": "M21"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["anterior-knee-pain", "pain-behind-kneecap", "kneecap-instability", "kneecap-dislocation", "grinding-sensation", "pain-sitting-long-periods"],
        "Label": "Disorders of patella",
        "ICD Code": "M22"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["knee-locking", "knee-catching", "knee-giving-way", "knee-pain", "knee-swelling", "meniscus-tear-symptoms"],
        "Label": "Internal derangement of knee",
        "ICD Code": "M23"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-locking", "joint-clicking", "joint-instability", "pain", "swelling", "reduced-range-of-motion"],
        "Label": "Other specific joint derangements",
        "ICD Code": "M24"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-swelling", "joint-stiffness", "popping-sound", "grinding-sensation", "joint-effusion"],
        "Label": "Other joint disorders, not elsewhere classified",
        "ICD Code": "M25"
    },

    # M30-M36: Systemic connective tissue disorders
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["fever", "weight-loss", "fatigue", "muscle-pain", "joint-pain", "skin-lesions"],
        "Label": "Polyarteritis nodosa and related conditions",
        "ICD Code": "M30"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["respiratory-problems", "kidney-problems", "sinusitis", "rash", "fever", "joint-pain"],
        "Label": "Other necrotizing vasculopathies",
        "ICD Code": "M31"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["butterfly-rash-face", "joint-pain", "fatigue", "fever", "sun-sensitivity", "kidney-problems"],
        "Label": "Systemic lupus erythematosus (SLE)",
        "ICD Code": "M32"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["muscle-weakness", "skin-rash-eyelids", "skin-rash-knuckles", "difficulty-swallowing", "fatigue", "muscle-pain"],
        "Label": "Dermatopolymyositis",
        "ICD Code": "M33"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["skin-thickening", "skin-hardening", "raynauds-phenomenon", "joint-pain", "difficulty-swallowing", "shortness-of-breath"],
        "Label": "Systemic sclerosis [scleroderma]",
        "ICD Code": "M34"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["dry-eyes", "dry-mouth", "joint-pain", "fatigue", "swollen-glands", "raynauds-phenomenon"],
        "Label": "Other systemic involvement of connective tissue",
        "ICD Code": "M35"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["connective-tissue-symptoms", "underlying-disease-symptoms", "joint-pain", "skin-changes", "fatigue", "organ-involvement"],
        "Label": "Systemic disorders of connective tissue in diseases classified elsewhere",
        "ICD Code": "M36"
    },

    # M40-M43: Deforming dorsopathies
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["abnormal-spinal-curvature", "back-pain", "rounded-upper-back", "swayback-lower-back", "stiffness", "fatigue"],
        "Label": "Kyphosis and lordosis",
        "ICD Code": "M40"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["sideways-spinal-curvature", "uneven-shoulders", "uneven-waist", "one-hip-higher", "back-pain", "leaning-to-one-side"],
        "Label": "Scoliosis",
        "ICD Code": "M41"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "stiffness", "spinal-deformity", "activity-related-pain", "reduced-spinal-mobility", "vertebral-wedging"],
        "Label": "Spinal osteochondrosis",
        "ICD Code": "M42"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "spinal-stiffness", "deformity", "torticollis", "neck-pain", "reduced-range-of-motion"],
        "Label": "Other deforming dorsopathies",
        "ICD Code": "M43"
    },

    # M45-M49: Spondylopathies
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["chronic-lower-back-pain", "morning-back-stiffness", "pain-improves-with-exercise", "spinal-fusion", "hunched-posture", "fatigue"],
        "Label": "Ankylosing spondylitis",
        "ICD Code": "M45"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "spinal-stiffness", "inflammation", "sacroiliac-joint-pain", "enthesitis", "uveitis"],
        "Label": "Other inflammatory spondylopathies",
        "ICD Code": "M46"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-or-neck-pain", "spinal-stiffness", "bone-spurs-spine", "numbness-in-limbs", "tingling-in-limbs", "weakness-in-limbs"],
        "Label": "Spondylosis",
        "ICD Code": "M47"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "spinal-stenosis-symptoms", "vertebral-fracture", "nerve-compression", "pain-radiating-to-limbs", "spinal-instability"],
        "Label": "Other spondylopathies",
        "ICD Code": "M48"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "underlying-disease-symptoms", "spinal-inflammation", "stiffness", "vertebral-lesions", "neurological-deficits"],
        "Label": "Spondylopathies in diseases classified elsewhere",
        "ICD Code": "M49"
    },

    # M50-M54: Other dorsopathies
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["neck-pain", "pain-radiating-to-arm", "arm-numbness", "arm-tingling", "arm-weakness", "headache"],
        "Label": "Cervical disc disorders",
        "ICD Code": "M50"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["lower-back-pain", "pain-radiating-to-leg", "leg-numbness", "leg-tingling", "leg-weakness", "sciatica"],
        "Label": "Other intervertebral disc disorders",
        "ICD Code": "M51"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "neck-pain", "stiffness", "muscle-spasm", "headache", "postural-pain"],
        "Label": "Other dorsopathies, not elsewhere classified",
        "ICD Code": "M53"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["back-pain", "muscle-ache-back", "shooting-pain", "stabbing-pain", "pain-radiating-down-leg", "limited-back-flexibility"],
        "Label": "Dorsalgia",
        "ICD Code": "M54"
    },

    # M60-M63: Disorders of muscles
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A", # Can be infectious, but often autoimmune
        "Symptoms": ["muscle-weakness", "muscle-pain", "fatigue", "difficulty-climbing-stairs", "difficulty-lifting-arms", "falling"],
        "Label": "Myositis",
        "ICD Code": "M60"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["painful-muscle-lump", "bone-formation-in-muscle", "history-of-trauma", "limited-range-of-motion", "stiffness", "swelling"],
        "Label": "Calcification and ossification of muscle",
        "ICD Code": "M61"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["muscle-cramps", "muscle-spasm", "muscle-stiffness", "muscle-wasting", "muscle-weakness", "muscle-rupture-nontraumatic"],
        "Label": "Other disorders of muscle",
        "ICD Code": "M62"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["muscle-weakness", "muscle-pain", "underlying-disease-symptoms", "fatigue", "malaise", "inflammation"],
        "Label": "Disorders of muscle in diseases classified elsewhere",
        "ICD Code": "M63"
    },

    # M65-M68: Disorders of synovium and tendon
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["pain-along-tendon", "swelling-along-tendon", "tenderness", "creaking-sensation", "trigger-finger", "de-quervains-tenosynovitis"],
        "Label": "Synovitis and tenosynovitis",
        "ICD Code": "M65"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["sudden-severe-pain", "snapping-or-popping-sensation", "inability-to-move-joint", "gap-or-defect-in-tendon", "swelling", "weakness"],
        "Label": "Spontaneous rupture of synovium and tendon",
        "ICD Code": "M66"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-swelling", "tendon-stiffness", "ganglion-cyst", "palmar-fasciitis", "reduced-mobility"],
        "Label": "Other disorders of synovium and tendon",
        "ICD Code": "M67"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["tendon-pain", "synovial-inflammation", "underlying-disease-symptoms", "swelling", "stiffness", "reduced-joint-function"],
        "Label": "Disorders of synovium and tendon in diseases classified elsewhere",
        "ICD Code": "M68"
    },

    # M70-M79: Other soft tissue disorders
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["pain-from-overuse", "bursitis", "tendinitis", "pain-with-specific-motion", "tenderness-at-insertion-point", "swelling"],
        "Label": "Soft tissue disorders related to use, overuse and pressure",
        "ICD Code": "M70"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "swelling-over-joint", "tenderness", "pain-with-movement", "baker-cyst", "olecranon-bursitis"],
        "Label": "Other bursopathies",
        "ICD Code": "M71"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["thickening-of-palmar-fascia", "finger-contracture", "nodules-in-palm", "plantar-fascial-fibromatosis", "inability-to-straighten-finger", "painless-lumps"],
        "Label": "Fibroblastic disorders",
        "ICD Code": "M72"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["soft-tissue-pain", "swelling", "inflammation", "underlying-disease-symptoms", "stiffness", "reduced-function"],
        "Label": "Soft tissue disorders in diseases classified elsewhere",
        "ICD Code": "M73"
    },
    # M74 is not a valid code
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["shoulder-pain", "difficulty-lifting-arm", "pain-at-night", "rotator-cuff-syndrome", "frozen-shoulder", "shoulder-stiffness"],
        "Label": "Shoulder lesions",
        "ICD Code": "M75"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["hip-pain", "knee-pain", "tendon-pain-leg", "pain-at-tendon-insertion", "greater-trochanteric-pain", "patellar-tendinitis"],
        "Label": "Enthesopathies of lower limb, excluding foot",
        "ICD Code": "M76"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["heel-pain", "plantar-fasciitis", "tennis-elbow", "golfers-elbow", "pain-at-tendon-insertion", "achilles-tendinitis"],
        "Label": "Other enthesopathies",
        "ICD Code": "M77"
    },
    # M78 is not a valid code
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["widespread-pain", "tender-points", "fatigue", "sleep-disturbances", "cognitive-difficulties", "headaches"],
        "Label": "Other soft tissue disorders, not elsewhere classified",
        "ICD Code": "M79"
    },

    # M80-M85: Disorders of bone density and structure
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["fracture-from-minor-trauma", "back-pain", "loss-of-height", "stooped-posture", "hip-fracture", "wrist-fracture"],
        "Label": "Osteoporosis with pathological fracture",
        "ICD Code": "M80"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["silent-disease", "no-symptoms-until-fracture", "low-bone-density-scan", "back-pain", "loss-of-height", "stooped-posture"],
        "Label": "Osteoporosis without pathological fracture",
        "ICD Code": "M81"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["low-bone-density", "underlying-disease-symptoms", "fracture-risk", "back-pain", "bone-pain", "steroid-use-history"],
        "Label": "Osteoporosis in diseases classified elsewhere",
        "ICD Code": "M82"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["bone-pain", "muscle-weakness", "difficulty-walking", "bone-tenderness", "low-vitamin-d", "waddling-gait"],
        "Label": "Adult osteomalacia",
        "ICD Code": "M83"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["fracture-nonunion", "fracture-malunion", "delayed-fracture-healing", "pain-at-fracture-site", "deformity", "stress-fracture"],
        "Label": "Disorders of continuity of bone",
        "ICD Code": "M84"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["bone-pain", "bone-cysts", "fibrous-dysplasia", "bone-deformity", "abnormal-bone-density", "asymptomatic-bone-lesion"],
        "Label": "Other disorders of bone density and structure",
        "ICD Code": "M85"
    },

    # M86-M90: Other osteopathies
    {
        "Geography": "Worldwide",
        "Transmission": ["bacterial-spread", "bloodstream", "direct-inoculation"],
        "Disease Type": "bacterial",
        "Symptoms": ["bone-pain", "fever", "chills", "swelling-over-bone", "redness-over-bone", "pus-drainage"],
        "Label": "Osteomyelitis",
        "ICD Code": "M86"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "pain-worse-at-night", "limited-range-of-motion", "hip-pain", "knee-pain", "bone-collapse"],
        "Label": "Osteonecrosis",
        "ICD Code": "M87"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["bone-pain", "enlarged-skull", "bowed-legs", "bone-deformity", "hearing-loss", "frequent-fractures"],
        "Label": "Paget's disease of bone [osteitis deformans]",
        "ICD Code": "M88"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["bone-pain", "bone-hypertrophy", "bone-lesion", "inflammation-of-bone", "swelling", "tenderness"],
        "Label": "Other disorders of bone",
        "ICD Code": "M89"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["bone-pain", "underlying-disease-symptoms", "bone-changes", "fracture-risk", "bone-deformity", "bone-lesions"],
        "Label": "Osteopathies in diseases classified elsewhere",
        "ICD Code": "M90"
    },

    # M91-M94: Chondropathies
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["hip-pain-in-child", "limping-in-child", "groin-pain", "limited-hip-motion", "stiffness", "thigh-pain"],
        "Label": "Juvenile osteochondrosis of hip and pelvis",
        "ICD Code": "M91"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain-in-child", "swelling", "stiffness", "activity-related-pain", "limping", "osgood-schlatter-disease"],
        "Label": "Other juvenile osteochondrosis",
        "ICD Code": "M92"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-pain", "joint-locking", "swelling", "cartilage-fragmentation", "stiffness", "clicking-sensation"],
        "Label": "Other osteochondropathies",
        "ICD Code": "M93"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["cartilage-inflammation", "ear-redness", "nose-cartilage-pain", "joint-pain", "costochondritis", "tracheal-collapse"],
        "Label": "Disorders of cartilage",
        "ICD Code": "M94"
    },

    # M95-M99: Other disorders
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["acquired-deformity", "facial-asymmetry", "cauliflower-ear", "nasal-septum-deviation", "postural-deformity", "pain"],
        "Label": "Other acquired deformities of musculoskeletal system",
        "ICD Code": "M95"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["post-surgical-pain", "post-surgical-complication", "joint-stiffness-after-surgery", "scar-tissue-formation", "instability-after-surgery", "implant-failure"],
        "Label": "Postprocedural musculoskeletal disorders",
        "ICD Code": "M96"
    },
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["pain-around-prosthesis", "fracture-near-implant", "sudden-pain-after-surgery", "inability-to-bear-weight", "swelling", "instability"],
        "Label": "Periprosthetic fracture around internal prosthetic joint",
        "ICD Code": "M97"
    },
    # M98 is not a valid code
    {
        "Geography": "Worldwide",
        "Transmission": ["N/A", "N/A", "N/A"],
        "Disease Type": "N/A",
        "Symptoms": ["joint-dysfunction", "segmental-dysfunction", "back-pain", "neck-pain", "stiffness", "reduced-mobility-segmental"],
        "Label": "Biomechanical lesions, not elsewhere classified",
        "ICD Code": "M99"
    }
]

sectionN = [
    # (N00-N08) Glomerular diseases
    ["Worldwide", ["post-infectious", "autoimmune", "idiopathic"], "inflammatory", ["hematuria", "proteinuria", "edema", "hypertension", "oliguria", "azotemia"], "Acute nephritic syndrome", "N00"],
    ["Worldwide", ["autoimmune", "vasculitis", "idiopathic"], "autoimmune", ["rapid kidney failure", "hematuria", "proteinuria", "oliguria", "edema", "hypertension"], "Rapidly progressive nephritic syndrome", "N01"],
    ["Worldwide", ["genetic", "autoimmune", "idiopathic"], "inflammatory", ["hematuria", "proteinuria (mild)", "flank pain", "normal kidney function", "recurrent gross hematuria", "microscopic hematuria"], "Recurrent and persistent hematuria", "N02"],
    ["Worldwide", ["autoimmune", "post-infectious", "genetic"], "inflammatory", ["proteinuria", "hematuria", "hypertension", "edema", "progressive kidney failure", "fatigue"], "Chronic nephritic syndrome", "N03"],
    ["Worldwide", ["idiopathic", "autoimmune", "diabetes"], "inflammatory", ["massive proteinuria", "hypoalbuminemia", "edema", "hyperlipidemia", "fatigue", "foamy urine"], "Nephrotic syndrome", "N04"],
    ["Worldwide", ["idiopathic", "unclassified", "autoimmune"], "inflammatory", ["hematuria", "proteinuria", "edema", "hypertension", "renal impairment", "oliguria"], "Unspecified nephritic syndrome", "N05"],
    ["Worldwide", ["genetic", "idiopathic", "secondary"], "structural", ["proteinuria", "foamy urine", "edema (mild)", "normal GFR", "bland urine sediment", "asymptomatic"], "Isolated proteinuria with specified morphological lesion", "N06"],
    ["Worldwide", ["genetic", "mutation", "hereditary"], "genetic", ["hematuria", "proteinuria", "hearing loss", "eye abnormalities", "progressive kidney failure", "family history"], "Hereditary nephropathy, not elsewhere classified", "N07"],
    ["Worldwide", ["diabetes", "amyloidosis", "lupus"], "secondary", ["proteinuria", "hematuria", "renal insufficiency", "edema", "hypertension", "underlying disease symptoms"], "Glomerular disorders in diseases classified elsewhere", "N08"],

    # (N10-N16) Renal tubulo-interstitial diseases
    ["Worldwide", ["drug-reaction", "infection", "autoimmune"], "inflammatory", ["fever", "rash", "eosinophilia", "acute kidney failure", "flank pain", "hematuria"], "Acute tubulo-interstitial nephritis", "N10"],
    ["Worldwide", ["chronic infection", "drug-toxicity", "autoimmune"], "inflammatory", ["polyuria", "nocturia", "anemia", "chronic kidney disease", "hypertension", "malaise"], "Chronic tubulo-interstitial nephritis", "N11"],
    ["Worldwide", ["idiopathic", "unspecified", "drug-reaction"], "inflammatory", ["renal dysfunction", "pyuria", "hematuria", "proteinuria (mild)", "fatigue", "electrolyte imbalance"], "Tubulo-interstitial nephritis, not specified as acute or chronic", "N12"],
    ["Worldwide", ["obstruction", "reflux", "congenital"], "structural", ["flank pain", "urinary tract infection", "hematuria", "difficulty urinating", "hydronephrosis", "kidney damage"], "Obstructive and reflux uropathy", "N13"],
    ["Worldwide", ["drug-toxicity", "heavy metals", "iatrogenic"], "toxic", ["acute kidney failure", "chronic kidney disease", "electrolyte imbalance", "proteinuria", "glycosuria (renal)", "polyuria"], "Tubulo-interstitial and tubular conditions caused by drugs and heavy metals", "N14"],
    ["Worldwide", ["idiopathic", "genetic", "metabolic"], "structural", ["renal cysts (medullary)", "kidney stones", "UTI", "renal dysfunction", "electrolyte imbalance", "Balkan nephropathy"], "Other renal tubulo-interstitial diseases", "N15"],
    ["Worldwide", ["sarcoidosis", "lupus", "myeloma"], "secondary", ["renal insufficiency", "proteinuria", "hematuria", "electrolyte imbalance", "underlying disease symptoms", "pyuria"], "Renal tubulo-interstitial disorders in diseases classified elsewhere", "N16"],

    # (N17-N19) Kidney failure
    ["Worldwide", ["ischemia", "sepsis", "nephrotoxins"], "functional", ["oliguria", "anuria", "azotemia", "fluid overload", "electrolyte imbalance", "nausea"], "Acute kidney failure", "N17"],
    ["Worldwide", ["diabetes", "hypertension", "glomerulonephritis"], "functional", ["fatigue", "edema", "anemia", "pruritus", "nausea", "progressive GFR decline"], "Chronic kidney disease (CKD)", "N18"],
    ["Worldwide", ["idiopathic", "unspecified", "late presentation"], "functional", ["azotemia", "uremic symptoms", "edema", "oliguria", "anemia", "electrolyte imbalance"], "Unspecified kidney failure", "N19"],

    # (N20-N23) Urolithiasis
    ["Worldwide", ["metabolic", "diet", "dehydration"], "metabolic", ["severe flank pain", "renal colic", "hematuria", "nausea", "vomiting", "dysuria"], "Calculus of kidney and ureter", "N20"],
    ["Worldwide", ["metabolic", "obstruction", "infection"], "metabolic", ["dysuria", "hematuria", "urinary retention", "pelvic pain", "frequent urination", "weak stream"], "Calculus of lower urinary tract", "N21"],
    ["Worldwide", ["hyperparathyroidism", "gout", "metabolic disorder"], "secondary", ["renal colic", "hematuria", "UTI", "underlying disease symptoms", "dysuria", "flank pain"], "Calculus of urinary tract in diseases classified elsewhere", "N22"],
    ["Worldwide", ["idiopathic", "urolithiasis", "obstruction"], "symptomatic", ["severe flank pain", "radiating pain", "nausea", "vomiting", "hematuria", "restlessness"], "Unspecified renal colic", "N23"],

    # (N25-N29) Other disorders of kidney and ureter
    ["Worldwide", ["genetic", "acquired", "drug-toxicity"], "functional", ["polyuria", "polydipsia", "electrolyte imbalance", "acidosis", "growth retardation (children)", "bone disease"], "Disorders resulting from impaired renal tubular function", "N25"],
    ["Worldwide", ["hypertension", "chronic nephritis", "idiopathic"], "structural", ["chronic kidney disease", "hypertension", "anemia", "small kidneys on imaging", "proteinuria", "fatigue"], "Unspecified contracted kidney", "N26"],
    ["Worldwide", ["congenital", "idiopathic", "vascular"], "structural", ["asymptomatic", "hypertension", "renal insufficiency", "discovered incidentally", "unilateral", "bilateral"], "Small kidney of unknown cause", "N27"],
    ["Worldwide", ["congenital", "vascular", "trauma"], "structural", ["renal artery stenosis", "hydronephrosis", "renal cyst", "flank pain", "hypertension", "hematuria"], "Other disorders of kidney and ureter, not elsewhere classified", "N28"],
    ["Worldwide", ["tuberculosis", "schistosomiasis", "complication"], "secondary", ["renal dysfunction", "hematuria", "pyuria", "flank pain", "underlying disease symptoms", "calcification"], "Other disorders of kidney and ureter in diseases classified elsewhere", "N29"],

    # (N30-N39) Other diseases of urinary system
    ["Worldwide", ["bacterial", "interstitial", "radiation"], "bacterial", ["dysuria", "urinary frequency", "urinary urgency", "suprapubic pain", "hematuria", "cloudy urine"], "Cystitis", "N30"],
    ["Worldwide", ["neurological", "spinal cord injury", "diabetes"], "functional", ["urinary incontinence", "urinary retention", "urinary frequency", "urinary urgency", "neurogenic bladder", "hesitancy"], "Neuromuscular dysfunction of bladder, not elsewhere classified", "N31"],
    ["Worldwide", ["idiopathic", "structural", "inflammatory"], "structural", ["bladder diverticulum", "bladder fistula", "bladder rupture", "hematuria", "pelvic pain", "dysuria"], "Other disorders of bladder", "N32"],
    ["Worldwide", ["schistosomiasis", "tuberculosis", "complication"], "secondary", ["hematuria", "dysuria", "urinary frequency", "pelvic pain", "underlying disease symptoms", "bladder calcification"], "Bladder disorders in diseases classified elsewhere", "N33"],
    ["Worldwide", ["bacterial", "viral", "idiopathic"], "bacterial", ["dysuria", "urethral discharge", "pruritus (urethral)", "urinary frequency", "hematuria", "pain during intercourse"], "Urethritis and urethral syndrome", "N34"],
    ["Worldwide", ["trauma", "infection", "iatrogenic"], "structural", ["weak urinary stream", "straining to void", "urinary retention", "incomplete emptying", "spraying stream", "dysuria"], "Urethral stricture", "N35"],
    ["Worldwide", ["structural", "trauma", "congenital"], "structural", ["urethral caruncle", "urethral diverticulum", "urethral fistula", "hematuria", "dysuria", "discharge"], "Other disorders of urethra", "N36"],
    ["Worldwide", ["complication", "infection", "trauma"], "secondary", ["urethritis (gonococcal)", "urethral discharge", "dysuria", "underlying disease symptoms", "stricture", "fistula"], "Urethral disorders in diseases classified elsewhere", "N37"],
    ["Worldwide", ["idiopathic", "functional", "structural"], "functional", ["urinary incontinence (stress)", "urinary incontinence (urge)", "nocturia", "urinary retention", "hematuria (unspecified)", "proteinuria (unspecified)"], "Other disorders of urinary system", "N39"],

    # (N40-N51) Diseases of male genital organs
    ["Worldwide", ["age-related", "hormonal", "idiopathic"], "non-infectious", ["urinary frequency", "urinary urgency", "nocturia", "weak stream", "hesitancy", "incomplete emptying"], "Benign prostatic hyperplasia", "N40"],
    ["Worldwide", ["bacterial", "idiopathic", "inflammatory"], "bacterial", ["prostatitis (acute)", "prostatitis (chronic)", "pelvic pain", "dysuria", "fever", "painful ejaculation"], "Inflammatory diseases of prostate", "N41"],
    ["Worldwide", ["structural", "idiopathic", "calculus"], "structural", ["prostatic calculus", "prostatic atrophy", "prostatic dysplasia", "pelvic pain", "hematospermia", "voiding symptoms"], "Other disorders of prostate", "N42"],
    ["Worldwide", ["idiopathic", "trauma", "infection"], "structural", ["scrotal swelling", "painless lump", "heaviness in scrotum", "transilluminates", "spermatocele", "hydrocele"], "Hydrocele and spermatocele", "N43"],
    ["Worldwide", ["trauma", "congenital", "idiopathic"], "structural", ["sudden severe testicular pain", "scrotal swelling", "nausea", "vomiting", "abdominal pain", "absent cremasteric reflex"], "Torsion of testis", "N44"],
    ["Worldwide", ["bacterial", "viral (mumps)", "STI"], "bacterial", ["testicular pain", "testicular swelling", "scrotal redness", "fever", "dysuria", "epididymal tenderness"], "Orchitis and epididymitis", "N45"],
    ["Worldwide", ["idiopathic", "genetic", "hormonal"], "functional", ["inability to conceive", "low sperm count", "abnormal sperm motility", "abnormal sperm morphology", "hormonal imbalance", "varicocele"], "Male infertility", "N46"],
    ["Worldwide", ["congenital", "hygiene-related", "idiopathic"], "structural", ["inability to retract foreskin", "painful retraction", "swelling of glans", "pain", "infection (balanitis)", "urinary obstruction"], "Redundant prepuce, phimosis and paraphimosis", "N47"],
    ["Worldwide", ["idiopathic", "trauma", "vascular"], "structural", ["Peyronie disease", "priapism", "balanitis", "penile curvature", "painful erection", "penile plaque"], "Other disorders of penis", "N48"],
    ["Worldwide", ["bacterial", "fungal", "STI"], "bacterial", ["balanitis", "cavernitis", "scrotal abscess", "penile inflammation", "scrotal inflammation", "pain"], "Inflammatory disorders of male genital organs, not elsewhere classified", "N49"],
    ["Worldwide", ["idiopathic", "congenital", "vascular"], "structural", ["testicular atrophy", "varicocele", "seminal vesiculitis", "scrotal pain", "hematospermia", "infertility"], "Other disorders of male genital organs", "N50"],
    ["Worldwide", ["tuberculosis", "mumps", "complication"], "secondary", ["mumps orchitis", "tuberculous epididymitis", "infertility", "testicular atrophy", "underlying disease symptoms", "pain"], "Disorders of male genital organs in diseases classified elsewhere", "N51"],

    # (N60-N65) Disorders of breast
    ["Worldwide", ["hormonal", "idiopathic", "age-related"], "non-infectious", ["breast lumpiness", "breast pain (mastalgia)", "fibrocystic changes", "cyclical pain", "nipple discharge (clear/yellow)", "breast cysts"], "Benign mammary dysplasia", "N60"],
    ["Worldwide", ["bacterial", "idiopathic", "lactation-related"], "bacterial", ["mastitis", "breast abscess", "breast pain", "breast redness", "breast swelling", "fever"], "Inflammatory disorders of breast", "N61"],
    ["Worldwide", ["hormonal", "idiopathic", "drug-induced"], "non-infectious", ["gynecomastia (male)", "macromastia (female)", "breast enlargement", "breast tenderness", "hormonal imbalance", "psychosocial distress"], "Hypertrophy of breast", "N62"],
    ["Worldwide", ["idiopathic", "benign", "malignant (unspecified)"], "unspecified", ["breast lump", "painless lump", "painful lump", "skin changes (dimpling)", "nipple retraction", "axillary lymphadenopathy"], "Unspecified lump in breast", "N63"],
    ["Worldwide", ["idiopathic", "hormonal", "structural"], "structural", ["nipple discharge", "galactorrhea", "mastalgia", "breast atrophy", "fat necrosis of breast", "mammary duct ectasia"], "Other disorders of breast", "N64"],
    ["Worldwide", ["complication", "surgical", "iatrogenic"], "non-infectious", ["implant rupture", "capsular contracture", "asymmetry", "pain", "implant malposition", "skin necrosis"], "Deformity and disproportion of reconstructed breast", "N65"],

    # (N70-N77) Inflammatory diseases of female pelvic organs
    ["Worldwide", ["bacterial", "STI", "ascending infection"], "bacterial", ["pelvic pain", "fever", "vaginal discharge", "pain during intercourse", "adnexal tenderness", "infertility"], "Salpingitis and oophoritis", "N70"],
    ["Worldwide", ["bacterial", "postpartum", "post-procedural"], "bacterial", ["endometritis", "myometritis", "pelvic pain", "fever", "abnormal uterine bleeding", "purulent vaginal discharge"], "Inflammatory disease of uterus, except cervix", "N71"],
    ["Worldwide", ["bacterial", "viral (HPV)", "STI"], "bacterial", ["cervicitis", "purulent cervical discharge", "post-coital bleeding", "intermenstrual bleeding", "pelvic pain", "dysuria"], "Inflammatory disease of cervix uteri", "N72"],
    ["Worldwide", ["bacterial", "STI", "polymicrobial"], "bacterial", ["pelvic inflammatory disease (PID)", "pelvic pain", "fever", "vaginal discharge", "cervical motion tenderness", "infertility"], "Other female pelvic inflammatory diseases", "N73"],
    ["Worldwide", ["tuberculosis", "gonorrhea", "chlamydia"], "secondary", ["tuberculous endometritis", "gonococcal salpingitis", "chlamydial PID", "pelvic pain", "infertility", "underlying infection"], "Female pelvic inflammatory disorders in diseases classified elsewhere", "N74"],
    ["Worldwide", ["bacterial", "obstruction", "idiopathic"], "bacterial", ["Bartholin cyst", "Bartholin abscess", "vulvar pain", "vulvar swelling", "pain during walking", "dyspareunia"], "Diseases of Bartholin gland", "N75"],
    ["Worldwide", ["bacterial", "fungal", "parasitic"], "bacterial", ["vaginitis", "vulvitis", "vaginal discharge", "vaginal itching", "vaginal odor", "dysuria"], "Other inflammation of vagina and vulva", "N76"],
    ["Worldwide", ["viral (herpes)", "parasitic", "autoimmune"], "secondary", ["herpes simplex ulcer", "Behcet disease", "vulvar ulcer", "vaginal ulcer", "pain", "underlying disease symptoms"], "Vulvovaginal ulceration and inflammation in diseases classified elsewhere", "N77"],

    # (N80-N98) Noninflammatory disorders of female genital tract
    ["Worldwide", ["hormonal", "idiopathic", "immune-dysfunction"], "non-infectious", ["pelvic pain", "dysmenorrhea", "dyspareunia", "infertility", "abnormal uterine bleeding", "painful defecation"], "Endometriosis", "N80"],
    ["Worldwide", ["childbirth", "age-related", "weak pelvic floor"], "structural", ["pelvic pressure", "vaginal bulge", "urinary incontinence", "difficulty defecating", "cystocele", "rectocele"], "Female genital prolapse", "N81"],
    ["Worldwide", ["obstetric trauma", "surgical", "radiation"], "structural", ["vesicovaginal fistula", "rectovaginal fistula", "continuous urine leakage", "fecal incontinence (vaginal)", "recurrent UTI", "vaginal discharge"], "Fistulae involving female genital tract", "N82"],
    ["Worldwide", ["idiopathic", "hormonal", "congenital"], "structural", ["ovarian cyst", "polycystic ovaries", "ovarian torsion", "hydrosalpinx", "pelvic pain", "menstrual irregularity"], "Noninflammatory disorders of ovary, fallopian tube and broad ligament", "N83"],
    ["Worldwide", ["hormonal", "idiopathic", "inflammatory"], "neoplastic", ["cervical polyp", "endometrial polyp", "intermenstrual bleeding", "post-coital bleeding", "menorrhagia", "asymptomatic"], "Polyp of female genital tract", "N84"],
    ["Worldwide", ["hormonal", "idiopathic", "structural"], "structural", ["uterine fibroids", "adenomyosis", "endometrial hyperplasia", "menorrhagia", "pelvic pain", "infertility"], "Other noninflammatory disorders of uterus, except cervix", "N85"],
    ["Worldwide", ["hormonal", "congenital", "idiopathic"], "structural", ["cervical ectropion", "post-coital bleeding", "vaginal discharge", "asymptomatic", "cervical redness", "mucus discharge"], "Erosion and ectropion of cervix uteri", "N86"],
    ["Worldwide", ["viral (HPV)", "immune-status", "smoking"], "viral", ["asymptomatic", "abnormal Pap smear", "CIN 1", "CIN 2", "CIN 3", "post-coital bleeding (rare)"], "Dysplasia of cervix uteri", "N87"],
    ["Worldwide", ["idiopathic", "trauma", "structural"], "structural", ["cervical stenosis", "cervical incompetence", "Nabothian cyst", "leukoplakia of cervix", "infertility", "preterm birth"], "Other noninflammatory disorders of cervix uteri", "N88"],
    ["Worldwide", ["idiopathic", "trauma", "age-related"], "structural", ["vaginal stenosis", "vaginal dryness", "vaginal atrophy", "leukoplakia of vagina", "dyspareunia", "vaginal discharge"], "Other noninflammatory disorders of vagina", "N89"],
    ["Worldwide", ["idiopathic", "autoimmune", "age-related"], "structural", ["vulvar atrophy", "vulvar dystrophy", "lichen sclerosus", "vulvar vestibulitis", "vulvar pruritus", "vulvar pain"], "Other noninflammatory disorders of vulva and perineum", "N90"],
    ["Worldwide", ["hormonal", "nutritional", "stress"], "functional", ["amenorrhea", "oligomenorrhea", "hypomenorrhea", "infertility", "hormonal imbalance", "low body weight"], "Absent, scanty and rare menstruation", "N91"],
    ["Worldwide", ["hormonal", "structural", "idiopathic"], "functional", ["menorrhagia", "metrorrhagia", "polymenorrhea", "anemia", "fatigue", "dysfunctional uterine bleeding"], "Excessive, frequent and irregular menstruation", "N92"],
    ["Worldwide", ["hormonal", "trauma", "idiopathic"], "functional", ["post-coital bleeding", "intermenstrual bleeding", "ovulation bleeding", "postmenopausal bleeding", "abnormal bleeding", "unspecified bleeding"], "Other abnormal uterine and vaginal bleeding", "N93"],
    ["Worldwide", ["idiopathic", "hormonal", "psychosomatic"], "functional", ["dysmenorrhea", "premenstrual syndrome (PMS)", "dyspareunia", "mittelschmerz", "vaginismus", "vulvodynia"], "Pain and other conditions associated with female genital organs and menstrual cycle", "N94"],
    ["Worldwide", ["age-related", "hormonal", "ovarian failure"], "functional", ["hot flashes", "night sweats", "vaginal dryness", "insomnia", "mood changes", "irregular menses"], "Menopausal and other perimenopausal disorders", "N95"],
    ["Worldwide", ["genetic", "autoimmune", "structural"], "functional", ["recurrent miscarriage", "inability to carry pregnancy", "chromosomal abnormalities", "uterine anomalies", "antiphospholipid syndrome", "hormonal imbalance"], "Habitual aborter", "N96"],
    ["Worldwide", ["ovulatory dysfunction", "tubal factor", "endometriosis"], "functional", ["inability to conceive", "irregular menses", "anovulation", "pelvic pain", "PCOS symptoms", "history of PID"], "Female infertility", "N97"],
    ["Worldwide", ["iatrogenic", "hormonal", "complication"], "non-infectious", ["ovarian hyperstimulation syndrome (OHSS)", "multiple pregnancy", "ectopic pregnancy", "infection", "bleeding", "complication of procedure"], "Complications associated with artificial fertilization", "N98"],

    # (N99) Intraoperative and postprocedural complications
    ["Worldwide", ["iatrogenic", "surgical", "complication"], "non-infectious", ["post-surgical hemorrhage", "post-surgical infection", "urethral stricture (post-proc)", "adhesions", "fistula formation", "organ injury"], "Intraoperative and postprocedural complications and disorders of genitourinary system, not elsewhere classified", "N99"]
]

sectionO = [
    {
        "ICD Code": "O00",
        "Disease Name": "Ectopic pregnancy",
        "Geography": "Global",
        "Transmission": ["Prior tubal surgery", "Pelvic inflammatory disease", "IUD use"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Abdominal pain", "Vaginal bleeding", "Missed period", "Dizziness", "Fainting", "Shoulder tip pain"]
    },
    {
        "ICD Code": "O01",
        "Disease Name": "Hydatidiform mole",
        "Geography": "Global (higher in Asia)",
        "Transmission": ["Unknown etiology", "Abnormal fertilization", "Maternal age extremes"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Uterine size larger than dates", "Severe nausea/vomiting", "High hCG levels", "Grape-like vesicles", "No fetal heart tones"]
    },
    {
        "ICD Code": "O02",
        "Disease Name": "Other abnormal products of conception",
        "Geography": "Global",
        "Transmission": ["Chromosomal abnormality", "Failed fertilization", "Blighted ovum"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal cramping", "Missed period", "Passing tissue", "Loss of pregnancy symptoms", "Decreasing hCG levels"]
    },
    {
        "ICD Code": "O03",
        "Disease Name": "Spontaneous abortion (Miscarriage)",
        "Geography": "Global",
        "Transmission": ["Chromosomal abnormality", "Maternal health condition", "Uterine abnormality"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal cramping", "Passing tissue", "Loss of pregnancy symptoms", "Back pain", "Decreasing hCG levels"]
    },
    {
        "ICD Code": "O04",
        "Disease Name": "Medical abortion",
        "Geography": "Global",
        "Transmission": ["Medication induced", "Patient choice", "Therapeutic procedure"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal cramping", "Passing clots/tissue", "Nausea", "Dizziness", "Fever (transient)"]
    },
    {
        "ICD Code": "O05",
        "Disease Name": "Other abortion",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Varies", "See sub-codes"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal pain", "Incomplete evacuation", "Infection risk", "Hemorrhage", "Cervical dilation"]
    },
    {
        "ICD Code": "O06",
        "Disease Name": "Unspecified abortion",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Unknown", "Incomplete history"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal pain", "Incomplete history", "Gestational sac present", "No fetal pole", "Variable hCG"]
    },
    {
        "ICD Code": "O07",
        "Disease Name": "Failed attempted abortion",
        "Geography": "Global",
        "Transmission": ["Incomplete procedure", "Medication failure", "Resistant pregnancy"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Continued pregnancy symptoms", "Minimal bleeding", "Positive pregnancy test", "Fetal heartbeat present", "Uterine growth", "Failed expulsion"]
    },
    {
        "ICD Code": "O08",
        "Disease Name": "Complications following abortion",
        "Geography": "Global",
        "Transmission": ["Incomplete procedure", "Non-sterile instruments", "Retained products"],
        "Disease Type": "Bacterial",
        "Symptoms": ["Fever", "Prolonged bleeding", "Severe abdominal pain", "Foul-smelling discharge", "Hemorrhage", "Shock"]
    },
    {
        "ICD Code": "O09",
        "Disease Name": "Supervision of high-risk pregnancy",
        "Geography": "Global",
        "Transmission": ["Pre-existing condition", "Advanced maternal age", "Multiple gestation"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Asymptomatic (status)", "Underlying condition symptoms", "Frequent monitoring", "Fetal growth restriction", "Preterm labor risk", "Maternal anxiety"]
    },
    {
        "ICD Code": "O10",
        "Disease Name": "Pre-existing hypertension",
        "Geography": "Global",
        "Transmission": ["Genetic predisposition", "Lifestyle factors", "Chronic condition"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood pressure", "Often asymptomatic", "Headaches", "Vision changes", "Proteinuria (if worsening)", "Edema"]
    },
    {
        "ICD Code": "O11",
        "Disease Name": "Pre-existing hypertension with superimposed pre-eclampsia",
        "Geography": "Global",
        "Transmission": ["Chronic hypertension", "Pregnancy complication", "Placental factors"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood pressure", "New onset proteinuria", "Severe headache", "Vision changes", "Upper abdominal pain", "Edema"]
    },
    {
        "ICD Code": "O12",
        "Disease Name": "Gestational oedema and proteinuria without hypertension",
        "Geography": "Global",
        "Transmission": ["Pregnancy induced", "Placental factors", "Unknown etiology"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Swelling (edema)", "Protein in urine", "Normal blood pressure", "Weight gain", "Puffy face", "Hand swelling"]
    },
    {
        "ICD Code": "O13",
        "Disease Name": "Gestational hypertension",
        "Geography": "Global",
        "Transmission": ["Pregnancy induced", "Placental factors", "Unknown etiology"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood pressure (new onset)", "No proteinuria", "Often asymptomatic", "Headache", "Edema", "Occurs after 20 weeks"]
    },
    {
        "ICD Code": "O14",
        "Disease Name": "Pre-eclampsia",
        "Geography": "Global",
        "Transmission": ["Placental factors", "First pregnancy", "Maternal age extremes"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood pressure", "Proteinuria", "Severe headache", "Vision changes", "Upper abdominal pain", "Rapid swelling"]
    },
    {
        "ICD Code": "O15",
        "Disease Name": "Eclampsia",
        "Geography": "Global",
        "Transmission": ["Complication of pre-eclampsia", "CNS involvement", "Unknown etiology"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Seizures", "High blood pressure", "Proteinuria", "Severe headache", "Altered mental state", "Hyperreflexia"]
    },
    {
        "ICD Code": "O16",
        "Disease Name": "Unspecified maternal hypertension",
        "Geography": "Global",
        "Transmission": ["Unknown etiology", "Pregnancy related", "Incomplete diagnosis"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood pressure", "Variable symptoms", "Headache", "Dizziness", "Edema", "Asymptomatic"]
    },
    {
        "ICD Code": "O20",
        "Disease Name": "Haemorrhage in early pregnancy",
        "Geography": "Global",
        "Transmission": ["Threatened abortion", "Ectopic pregnancy", "Cervical changes"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Abdominal cramping", "Back pain", "Dizziness", "Passing clots", "Variable fetal status"]
    },
    {
        "ICD Code": "O21",
        "Disease Name": "Hyperemesis gravidarum (Excessive vomiting)",
        "Geography": "Global",
        "Transmission": ["Hormonal changes (hCG)", "Multiple gestation", "Molar pregnancy"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Severe nausea", "Persistent vomiting", "Weight loss", "Dehydration", "Electrolyte imbalance", "Ketonuria"]
    },
    {
        "ICD Code": "O22",
        "Disease Name": "Venous complications in pregnancy (e.g., DVT)",
        "Geography": "Global",
        "Transmission": ["Hypercoagulability of pregnancy", "Immobility", "Obesity"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Leg swelling", "Leg pain", "Redness/warmth in leg", "Shortness of breath (if PE)", "Chest pain (if PE)", "Positive Homan's sign"]
    },
    {
        "ICD Code": "O23",
        "Disease Name": "Infections of genitourinary tract in pregnancy",
        "Geography": "Global",
        "Transmission": ["Bacterial ascent", "Catheter use", "Urinary stasis"],
        "Disease Type": "Bacterial",
        "Symptoms": ["Painful urination", "Urinary frequency", "Fever", "Back pain", "Cloudy urine", "Vaginal discharge"]
    },
    {
        "ICD Code": "O24",
        "Disease Name": "Diabetes mellitus in pregnancy",
        "Geography": "Global",
        "Transmission": ["Pre-existing diabetes", "Gestational onset", "Insulin resistance"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["High blood sugar", "Excessive thirst", "Frequent urination", "Fatigue", "Large fetus (macrosomia)", "Often asymptomatic (gestational)"]
    },
    {
        "ICD Code": "O25",
        "Disease Name": "Malnutrition in pregnancy",
        "Geography": "Low-income regions",
        "Transmission": ["Poor diet", "Food insecurity", "Malabsorption"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Low maternal weight gain", "Fatigue", "Anemia", "Vitamin deficiency", "Fetal growth restriction", "Edema"]
    },
    {
        "ICD Code": "O26",
        "Disease Name": "Other maternal disorders predominantly related to pregnancy",
        "Geography": "Global",
        "Transmission": ["Varies (e.g., liver disorders)", "Pregnancy induced", "Pre-existing condition"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Itching (cholestasis)", "Abnormal liver enzymes", "Back pain (pelvic girdle)", "Fatigue", "Anemia", "Varies widely"]
    },
    {
        "ICD Code": "O28",
        "Disease Name": "Abnormal findings on antenatal screening",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Diagnostic finding", "Fetal anomaly risk"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Asymptomatic (finding)", "Abnormal blood test", "Abnormal ultrasound", "Maternal anxiety", "Increased fetal risk", "Requires further testing"]
    },
    {
        "ICD Code": "O29",
        "Disease Name": "Complications of anaesthesia during pregnancy",
        "Geography": "Global",
        "Transmission": ["Procedure complication", "Allergic reaction", "Difficult intubation"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Hypotension", "Respiratory distress", "Nausea/vomiting", "Headache (spinal)", "Allergic rash", "Failed block"]
    },
    {
        "ICD Code": "O30",
        "Disease Name": "Multiple gestation",
        "Geography": "Global",
        "Transmission": ["Spontaneous", "Fertility treatment", "Maternal age"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Rapid uterine growth", "Severe morning sickness", "High hCG/AFP", "Multiple fetal heartbeats", "Increased fetal movement", "Early fatigue"]
    },
    {
        "ICD Code": "O31",
        "Disease Name": "Complications specific to multiple gestation",
        "Geography": "Global",
        "Transmission": ["Shared placenta (TTTS)", "Preterm labor", "Malpresentation"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Disparate fetal growth", "Polyhydramnios", "Preterm contractions", "Placental abruption", "Fetal distress", "Cord entanglement"]
    },
    {
        "ICD Code": "O32",
        "Disease Name": "Maternal care for malpresentation of fetus",
        "Geography": "Global",
        "Transmission": ["Uterine abnormality", "Multiple gestation", "Random occurrence"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Breech position", "Transverse lie", "Unstable lie", "Fetal head not engaged", "Palpable fetal parts", "Requires external version or C-section"]
    },
    {
        "ICD Code": "O33",
        "Disease Name": "Maternal care for known or suspected disproportion",
        "Geography": "Global",
        "Transmission": ["Large fetus (macrosomia)", "Small maternal pelvis", "Fetal hydrocephalus"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Large fundal height", "Ultrasound finding", "Failed descent in labor", "Obstructed labor", "High fetal station", "Maternal diabetes"]
    },
    {
        "ICD Code": "O34",
        "Disease Name": "Maternal care for abnormality of pelvic organs",
        "Geography": "Global",
        "Transmission": ["Uterine fibroids", "Bicornuate uterus", "Prior C-section scar"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Pelvic pain", "Obstructed labor", "Malpresentation", "History of surgery", "Uterine rupture risk", "Infertility history"]
    },
    {
        "ICD Code": "O35",
        "Disease Name": "Maternal care for known or suspected fetal abnormality",
        "Geography": "Global",
        "Transmission": ["Genetic abnormality", "Teratogen exposure", "Unknown etiology"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Abnormal ultrasound", "Abnormal genetic screen", "Polyhydramnios", "Oligohydramnios", "Fetal growth restriction", "Family history"]
    },
    {
        "ICD Code": "O36",
        "Disease Name": "Maternal care for other fetal problems",
        "Geography": "Global",
        "Transmission": ["Rh isoimmunization", "Fetal anemia", "Fetal growth restriction"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Maternal antibodies (Rh)", "Fetal hydrops", "Poor fetal growth", "Abnormal dopplers", "Decreased fetal movement", "Maternal viral infection"]
    },
    {
        "ICD Code": "O40",
        "Disease Name": "Polyhydramnios",
        "Geography": "Global",
        "Transmission": ["Maternal diabetes", "Fetal anomaly", "Idiopathic"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Large uterine size", "Shortness of breath", "Abdominal discomfort", "Fetal parts hard to feel", "Preterm labor", "Rapid uterine growth"]
    },
    {
        "ICD Code": "O41",
        "Disease Name": "Other disorders of amniotic fluid and membranes",
        "Geography": "Global",
        "Transmission": ["Ruptured membranes", "Placental insufficiency", "Fetal renal anomaly"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Leaking fluid", "Low fluid (oligohydramnios)", "Fetal growth restriction", "Variable decelerations (fetal heart)", "Meconium staining", "Amnionitis risk"]
    },
    {
        "ICD Code": "O42",
        "Disease Name": "Premature rupture of membranes (PROM)",
        "Geography": "Global",
        "Transmission": ["Bacterial infection", "Cervical weakness", "Unknown etiology"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Gush of fluid", "Continuous leaking", "Absence of labor", "Fever (if infected)", "Fetal tachycardia (if infected)", "Positive nitrazine test"]
    },
    {
        "ICD Code": "O43",
        "Disease Name": "Placental disorders (e.g., Placenta accreta)",
        "Geography": "Global",
        "Transmission": ["Prior C-section", "Placenta previa", "Advanced maternal age"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Often asymptomatic pre-delivery", "Hemorrhage at delivery", "Retained placenta", "Ultrasound finding", "Vaginal bleeding (if previa)", "Risk of uterine rupture"]
    },
    {
        "ICD Code": "O44",
        "Disease Name": "Placenta previa",
        "Geography": "Global",
        "Transmission": ["Prior C-section", "Multiparity", "Advanced maternal age"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Painless bright red bleeding", "Bleeding after 20 weeks", "Fetal malpresentation", "Uterus soft, non-tender", "Ultrasound diagnosis", "Intermittent bleeding"]
    },
    {
        "ICD Code": "O45",
        "Disease Name": "Placental abruption",
        "Geography": "Global",
        "Transmission": ["Maternal hypertension", "Trauma", "Cocaine use"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Painful vaginal bleeding", "Uterine tenderness", "Rigid/hard uterus", "Fetal distress", "Sudden abdominal pain", "Hypovolemic shock"]
    },
    {
        "ICD Code": "O46",
        "Disease Name": "Antepartum haemorrhage, not elsewhere classified",
        "Geography": "Global",
        "Transmission": ["Cervical lesions", "Vasa previa", "Unknown cause"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding", "Variable pain", "Fetal distress (vasa previa)", "Exclusion of previa/abruption", "Cervical bleeding", "Bloody show"]
    },
    {
        "ICD Code": "O47",
        "Disease Name": "False labour",
        "Geography": "Global",
        "Transmission": ["Uterine irritability", "Dehydration", "Unknown"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Irregular contractions", "Contractions do not intensify", "No cervical change", "Pain in lower abdomen", "Relieved by walking", "No bloody show"]
    },
    {
        "ICD Code": "O48",
        "Disease Name": "Prolonged pregnancy (Post-term)",
        "Geography": "Global",
        "Transmission": ["First pregnancy", "Incorrect dating", "Genetic factors"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Pregnancy beyond 42 weeks", "Decreased amniotic fluid", "Meconium staining", "Fetal distress risk", "Large fetus", "Placental insufficiency risk"]
    },
    {
        "ICD Code": "O60",
        "Disease Name": "Preterm labour",
        "Geography": "Global",
        "Transmission": ["Infection", "Multiple gestation", "Cervical incompetence"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Regular contractions (<37 wks)", "Cervical dilation", "Pelvic pressure", "Backache", "Increased vaginal discharge", "Cramping"]
    },
    {
        "ICD Code": "O61",
        "Disease Name": "Failed induction of labour",
        "Geography": "Global",
        "Transmission": ["Unfavorable cervix", "Cephalopelvic disproportion", "Medication failure"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["No cervical change", "Lack of regular contractions", "Prolonged induction", "Maternal exhaustion", "Fetal intolerance", "Leads to C-section"]
    },
    {
        "ICD Code": "O62",
        "Disease Name": "Abnormalities of forces of labour (Uterine inertia)",
        "Geography": "Global",
        "Transmission": ["Uterine muscle fatigue", "Maternal exhaustion", "Epidural use"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Weak contractions", "Infrequent contractions", "Arrest of dilation", "Prolonged first stage", "Maternal fatigue", "Requires augmentation"]
    },
    {
        "ICD Code": "O63",
        "Disease Name": "Long labour (Prolonged labour)",
        "Geography": "Global",
        "Transmission": ["Cephalopelvic disproportion", "Malposition", "Uterine inertia"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Prolonged first stage", "Prolonged second stage", "Maternal exhaustion", "Fetal distress", "Arrest of descent", "Increased infection risk"]
    },
    {
        "ICD Code": "O64",
        "Disease Name": "Obstructed labour due to malposition and malpresentation",
        "Geography": "Global",
        "Transmission": ["Occiput posterior", "Transverse lie", "Brow presentation"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Arrest of descent", "No progress despite strong contractions", "Severe back pain", "Fetal distress", "Molding of fetal head", "Requires operative delivery"]
    },
    {
        "ICD Code": "O65",
        "Disease Name": "Obstructed labour due to maternal pelvic abnormality",
        "Geography": "Global",
        "Transmission": ["Contracted pelvis", "Pelvic shape (android)", "Prior pelvic fracture"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Arrest of descent", "Cephalopelvic disproportion", "Failed engagement", "Strong but ineffective contractions", "Fetal distress", "Requires C-section"]
    },
    {
        "ICD Code": "O66",
        "Disease Name": "Other obstructed labour (e.g., Shoulder dystocia)",
        "Geography": "Global",
        "Transmission": ["Large fetus (macrosomia)", "Conjoined twins", "Rapid descent"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Shoulder dystocia", "Turtle sign", "Fetal head retracts", "Failed delivery of shoulders", "Requires maneuvers", "Risk of brachial plexus injury"]
    },
    {
        "ICD Code": "O67",
        "Disease Name": "Labour and delivery complicated by intrapartum haemorrhage",
        "Geography": "Global",
        "Transmission": ["Placental abruption", "Placenta previa", "Uterine rupture"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Vaginal bleeding during labor", "Fetal distress", "Maternal tachycardia", "Hypotension", "Uterine tenderness", "Variable pain"]
    },
    {
        "ICD Code": "O68",
        "Disease Name": "Labour and delivery complicated by fetal distress",
        "Geography": "Global",
        "Transmission": ["Cord compression", "Placental insufficiency", "Maternal hypotension"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Abnormal fetal heart rate", "Late decelerations", "Variable decelerations", "Fetal tachycardia", "Bradycardia", "Meconium-stained fluid"]
    },
    {
        "ICD Code": "O69",
        "Disease Name": "Labour and delivery complicated by umbilical cord complications",
        "Geography": "Global",
        "Transmission": ["Nuchal cord", "Cord prolapse", "Vasa previa"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Variable decelerations", "Sudden fetal bradycardia", "Palpable cord (prolapse)", "Bleeding (vasa previa)", "Fetal distress", "Requires emergency C-section"]
    },
    {
        "ICD Code": "O70",
        "Disease Name": "Perineal laceration during delivery",
        "Geography": "Global",
        "Transmission": ["Operative delivery", "Macrosomia", "Precipitate labor"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Tear of perineum", "Bleeding", "Pain", "Rectal involvement (3rd/4th degree)", "Swelling", "Requires repair"]
    },
    {
        "ICD Code": "O71",
        "Disease Name": "Other obstetric trauma (e.g., Uterine rupture)",
        "Geography": "Global",
        "Transmission": ["Operative delivery", "Obstructed labor", "Prior C-section (VBAC)"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Uterine rupture", "Cervical laceration", "High vaginal tear", "Severe pain", "Hemorrhage", "Maternal shock"]
    },
    {
        "ICD Code": "O72",
        "Disease Name": "Postpartum haemorrhage (PPH)",
        "Geography": "Global",
        "Transmission": ["Uterine atony", "Retained placenta", "Lacerations"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Excessive bleeding after delivery", "Boggy uterus", "Maternal tachycardia", "Hypotension", "Dizziness", "Shock"]
    },
    {
        "ICD Code": "O73",
        "Disease Name": "Retained placenta and membranes",
        "Geography": "Global",
        "Transmission": ["Placenta accreta", "Uterine atony", "Manual removal failure"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Placenta not delivered > 30 min", "Postpartum hemorrhage", "Uterine cramping", "Missing placental cotyledons", "Risk of infection", "Requires manual removal"]
    },
    {
        "ICD Code": "O74",
        "Disease Name": "Complications of anaesthesia during labour and delivery",
        "Geography": "Global",
        "Transmission": ["Epidural complication", "Spinal headache", "Allergic reaction"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Hypotension", "Failed block", "Spinal headache", "Nausea/vomiting", "Respiratory distress", "Nerve injury"]
    },
    {
        "ICD Code": "O75",
        "Disease Name": "Other complications of labour and delivery, NEC",
        "Geography": "Global",
        "Transmission": ["Maternal exhaustion", "Amniotic fluid embolism", "Precipitate labor"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Sudden cardiovascular collapse (AFE)", "Rapid delivery (<3 hours)", "Maternal distress", "Pyrexia during labor", "Shock", "Coagulopathy (AFE)"]
    },
    {
        "ICD Code": "O80",
        "Disease Name": "Single spontaneous vaginal delivery",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Physiological event", "Normal process"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Regular contractions", "Cervical dilation", "Spontaneous delivery", "Vertex presentation", "No complications", "Minimal bleeding"]
    },
    {
        "ICD Code": "O81",
        "Disease Name": "Single delivery by forceps or vacuum extractor",
        "Geography": "Global",
        "Transmission": ["Prolonged second stage", "Fetal distress", "Maternal exhaustion"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Requires assistance", "Fetal head visible", "Maternal pushing", "Risk of laceration", "Fetal cephalohematoma", "Instrument application"]
    },
    {
        "ICD Code": "O82",
        "Disease Name": "Single delivery by caesarean section",
        "Geography": "Global",
        "Transmission": ["Fetal distress", "Obstructed labor", "Breech presentation"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Surgical procedure", "Abdominal incision", "Uterine incision", "Delivery of infant", "Post-operative pain", "Bleeding"]
    },
    {
        "ICD Code": "O83",
        "Disease Name": "Other assisted single delivery (e.g., Breech extraction)",
        "Geography": "Global",
        "Transmission": ["Breech extraction", "Version and extraction", "Rare procedures"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Internal maneuvers", "High-risk procedure", "Requires skilled operator", "Breech presentation", "Fetal distress", "Maternal trauma risk"]
    },
    {
        "ICD Code": "O84",
        "Disease Name": "Multiple delivery",
        "Geography": "Global",
        "Transmission": ["Multiple gestation", "Spontaneous", "Fertility treatment"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Delivery of more than one infant", "Vaginal or C-section", "Increased risk of PPH", "Preterm delivery", "Malpresentation common", "Neonatal team needed"]
    },
    {
        "ICD Code": "O85",
        "Disease Name": "Puerperal sepsis",
        "Geography": "Global",
        "Transmission": ["Bacterial infection", "Prolonged ROM", "Retained products"],
        "Disease Type": "Bacterial",
        "Symptoms": ["Fever", "Chills", "Foul-smelling lochia", "Uterine tenderness", "Tachycardia", "Malaise"]
    },
    {
        "ICD Code": "O86",
        "Disease Name": "Other puerperal infections (e.g., Wound infection, UTI)",
        "Geography": "Global",
        "Transmission": ["Bacterial infection", "Wound contamination", "Urinary stasis"],
        "Disease Type": "Bacterial",
        "Symptoms": ["Wound redness (C-section/episiotomy)", "Wound drainage", "Painful urination (UTI)", "Breast pain/redness (mastitis)", "Fever", "Malaise"]
    },
    {
        "ICD Code": "O87",
        "Disease Name": "Venous complications in the puerperium (e.g., DVT)",
        "Geography": "Global",
        "Transmission": ["Hypercoagulability", "Post-operative immobility", "C-section"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Leg swelling", "Leg pain", "Warmth/redness in leg", "Shortness of breath (PE)", "Chest pain (PE)", "Positive Homan's sign"]
    },
    {
        "ICD Code": "O88",
        "Disease Name": "Obstetric embolism",
        "Geography": "Global",
        "Transmission": ["Amniotic fluid embolism", "Thromboembolism (DVT)", "Air embolism"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Sudden shortness of breath", "Cardiovascular collapse", "Hypoxia", "Coagulopathy", "Seizures", "Altered mental state"]
    },
    {
        "ICD Code": "O89",
        "Disease Name": "Complications of anaesthesia during the puerperium",
        "Geography": "Global",
        "Transmission": ["Spinal headache", "Epidural complication", "Allergic reaction"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Postural headache", "Back pain", "Nerve irritation", "Nausea", "Dizziness", "Failed pain relief"]
    },
    {
        "ICD Code": "O90",
        "Disease Name": "Complications of the puerperium, not elsewhere classified",
        "Geography": "Global",
        "Transmission": ["Hematoma formation", "Wound dehiscence", "Subinvolution of uterus"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Perineal pain/swelling (hematoma)", "Wound opening", "Prolonged lochia", "Uterine tenderness", "Anemia", "Urinary retention"]
    },
    {
        "ICD Code": "O91",
        "Disease Name": "Infections of breast associated with childbirth (Mastitis)",
        "Geography": "Global",
        "Transmission": ["Bacterial infection (Staph. aureus)", "Milk stasis", "Nipple trauma"],
        "Disease Type": "Bacterial",
        "Symptoms": ["Breast pain", "Redness/swelling", "Wedge-shaped red area", "Fever", "Chills", "Malaise"]
    },
    {
        "ICD Code": "O92",
        "Disease Name": "Other disorders of breast and lactation",
        "Geography": "Global",
        "Transmission": ["Hormonal changes", "Poor latch", "Milk oversupply"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Engorgement", "Sore nipples", "Inverted nipples", "Agalactia (no milk)", "Cracked nipples", "Painful latch"]
    },
    {
        "ICD Code": "O94",
        "Disease Name": "Sequelae of complication of pregnancy, childbirth, and the puerperium",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Prior complication", "Chronic condition"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Chronic pelvic pain", "Infertility", "Vesicovaginal fistula", "Persistent hypertension", "Psychological trauma", "Varies by original complication"]
    },
    {
        "ICD Code": "O95",
        "Disease Name": "Obstetric death of unknown cause",
        "Geography": "Global",
        "Transmission": ["Not applicable", "Unknown", "Sudden event"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Sudden maternal death", "Cause undetermined", "During pregnancy/labor", "Within 42 days of delivery", "Autopsy inconclusive", "Rare"]
    },
    {
        "ICD Code": "O96",
        "Disease Name": "Maternal death from any obstetric cause >42 days but <1 year",
        "Geography": "Global",
        "Transmission": ["Sequelae of complication", "Thromboembolism", "Cardiomyopathy"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Death >42 days post-delivery", "Direct obstetric cause", "Indirect obstetric cause", "Cardiomyopathy", "Sepsis sequelae", "Cerebrovascular accident"]
    },
    {
        "ICD Code": "O97",
        "Disease Name": "Death from sequelae of direct obstetric causes (>1 year)",
        "Geography": "Global",
        "Transmission": ["Prior complication", "Hemorrhage sequelae", "Eclampsia sequelae"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Death >1 year post-delivery", "Direct obstetric cause", "Cerebral hemorrhage", "Renal failure", "Hepatic failure", "Cardiomyopathy"]
    },
    {
        "ICD Code": "O98",
        "Disease Name": "Maternal infectious and parasitic diseases complicating pregnancy",
        "Geography": "Global",
        "Transmission": ["Sexual contact (HIV)", "Blood-borne (HBV)", "Mosquito-borne (Zika)"],
        "Disease Type": "Viral",
        "Symptoms": ["Fever", "Rash", "Jaundice", "Asymptomatic carrier", "Risk of vertical transmission", "Underlying infection symptoms"]
    },
    {
        "ICD Code": "O99",
        "Disease Name": "Other maternal diseases complicating pregnancy",
        "Geography": "Global",
        "Transmission": ["Pre-existing condition", "Autoimmune", "Respiratory disease"],
        "Disease Type": "Non-infectious",
        "Symptoms": ["Varies widely", "Anemia", "Thyroid dysfunction", "Lupus flare", "Asthma exacerbation", "Mental health condition"]
    }
]

sectionP = [
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

sectionQ = [
    ['Worldwide', ['Multifactorial', 'Folic acid deficiency', 'Genetic factors'], 'Structural', ['Absence of brain', 'Absence of cranium (skull)', 'Exposed neural tissue', 'Facial abnormalities', 'Brainstem presence', 'Non-viable at birth'], 'Anencephaly and similar malformations', 'Q00'],
    ['Worldwide', ['Neural tube defect', 'Genetic factors', 'Prenatal factors'], 'Structural', ['Sac-like protrusion of brain/meninges', 'Protrusion through skull opening', 'Hydrocephalus', 'Vision problems', 'Seizures', 'Developmental delay'], 'Encephalocele', 'Q01'],
    ['Worldwide', ['Genetic factors', 'Prenatal infection (e.g., Zika)', 'Teratogen exposure'], 'Structural', ['Small head circumference', 'Developmental delay', 'Intellectual disability', 'Seizures', 'Facial distortions', 'Poor motor function'], 'Microcephaly', 'Q02'],
    ['Worldwide', ['Genetic factors', 'Prenatal infection', 'Aqueductal stenosis'], 'Structural', ['Rapidly increasing head size', 'Bulging fontanelle', 'Seizures', 'Poor feeding', 'Vomiting', 'Developmental delay'], 'Congenital hydrocephalus', 'Q03'],
    ['Worldwide', ['Genetic factors', 'Prenatal factors', 'Spontaneous mutation'], 'Structural', ['Varies widely', 'Seizures', 'Developmental delay', 'Motor impairment', 'Intellectual disability', 'Abnormal head shape'], 'Other congenital malformations of brain', 'Q04'],
    ['Worldwide', ['Neural tube defect', 'Folic acid deficiency', 'Genetic factors'], 'Structural', ['Opening in vertebral column', 'Protrusion of spinal cord (meningocele)', 'Nerve damage', 'Leg paralysis', 'Bowel/bladder problems', 'Hydrocephalus'], 'Spina bifida', 'Q05'],
    ['Worldwide', ['Genetic factors', 'Vascular disruption', 'Developmental anomaly'], 'Structural', ['Varies widely', 'Seizures', 'Hemiparesis', 'Developmental delay', 'Absence of spinal cord part', 'Sensory loss'], 'Other congenital malformations of spinal cord', 'Q06'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Headache', 'Hydrocephalus', 'Syringomyelia', 'Cranial nerve palsies', 'Balance problems'], 'Other congenital malformations of nervous system', 'Q07'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Blindness', 'Cataracts', 'Glaucoma', 'Microphthalmia', 'Strabismus'], 'Congenital malformations of eye (general)', 'Q10'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal infection (e.g., Rubella)'], 'Structural', ['Cloudy lens at birth', 'Vision impairment', 'White pupil (leukocoria)', 'Nystagmus (involuntary eye movement)', 'Strabismus', 'Microphthalmia'], 'Congenital cataract', 'Q11'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Small eyeball (microphthalmia)', 'Absent eyeball (anophthalmia)', 'Large eyeball (macrophthalmia)', 'Vision impairment', 'Orbital cysts', 'Associated facial anomalies'], 'Anophthalmos, microphthalmos and macrophthalmos', 'Q12'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Corneal opacity', 'Glaucoma', 'Iris abnormalities (aniridia)', 'Scleral abnormalities', 'Varies by specific condition', 'Vision impairment'], 'Congenital malformations of anterior segment of eye', 'Q13'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Retinal detachment', 'Chorioretinal coloboma', 'Optic nerve hypoplasia', 'Vitreous abnormalities', 'Poor vision', 'Nystagmus'], 'Congenital malformations of posterior segment of eye', 'Q14'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Drooping eyelid (ptosis)', 'Inability to open eye', 'Ectropion (eyelid outward)', 'Entropion (eyelid inward)', 'Coloboma of eyelid', 'Abnormal eyelash growth'], 'Congenital malformations of eyelid, lacrimal apparatus and orbit', 'Q15'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Small or absent outer ear (microtia/anotia)', 'Blocked ear canal (atresia)', 'Hearing loss', 'Preauricular skin tags', 'Abnormal ear position', 'Associated facial anomalies'], 'Congenital malformations of ear causing impairment of hearing', 'Q16'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Protruding ears', 'Malformed ear cartilage', 'Low-set ears', 'Preauricular sinus', 'Accessory auricle', 'Does not typically impair hearing'], 'Other congenital malformations of ear', 'Q17'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Facial asymmetry', 'Malformed facial bones', 'Hearing loss', 'Ear abnormalities', 'Mandibular hypoplasia', 'Varies widely'], 'Other congenital malformations of face and neck', 'Q18'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health (e.g., diabetes)'], 'Structural', ['Cyanosis (blue skin)', 'Shortness of breath', 'Poor feeding (infants)', 'Heart murmur', 'Fatigue', 'Edema (swelling)'], 'Congenital malformations of cardiac chambers and connections', 'Q20'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Heart murmur', 'Shortness of breath on exertion', 'Fatigue', 'Palpitations', 'Right heart enlargement', 'Pulmonary hypertension'], 'Congenital malformations of cardiac septa (ASD, VSD)', 'Q21'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Heart murmur', 'Valve stenosis (narrowing)', 'Valve regurgitation (leaky)', 'Shortness of breath', 'Chest pain', 'Fatigue'], 'Congenital malformations of pulmonary and tricuspid valves', 'Q22'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Associated syndromes (e.g., Marfan)'], 'Structural', ['Heart murmur', 'Valve stenosis (narrowing)', 'Valve regurgitation (leaky)', 'Shortness of breath', 'Fatigue', 'Left ventricular hypertrophy'], 'Congenital malformations of aortic and mitral valves', 'Q23'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Cyanosis', 'Shortness of breath', 'Poor feeding', 'Clubbing of fingers/toes', 'Heart murmur', 'Varies by specific defect (e.g., Tetralogy of Fallot)'], 'Other congenital malformations of heart', 'Q24'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Hypertension in arms', 'Low blood pressure in legs', 'Leg cramps', 'Weak femoral pulse', 'Heart murmur', 'Shortness of breath'], 'Congenital malformations of great arteries (e.g., Coarctation of aorta)', 'Q25'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Often asymptomatic', 'Pulmonary hypertension', 'Edema', 'Shortness of breath', 'Heart murmur'], 'Congenital malformations of great veins', 'Q26'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Arteriovenous malformation (AVM)', 'Telangiectasia', 'Hemangioma', 'Port-wine stain', 'Risk of bleeding'], 'Other congenital malformations of peripheral vascular system', 'Q27'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Lymphedema (swelling)', 'Cyanosis', 'Heart failure', 'Respiratory distress', 'Varies by specific defect'], 'Other congenital malformations of circulatory system', 'Q28'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Blocked nasal passage (choanal atresia)', 'Deviated septum (congenital)', 'Nasal hypoplasia', 'Breathing difficulty', 'Feeding difficulty', 'Single nostril'], 'Congenital malformations of nose', 'Q30'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Laryngeal web', 'Laryngomalacia (floppy larynx)', 'Stridor (noisy breathing)', 'Hoarse cry', 'Respiratory distress', 'Feeding difficulties'], 'Congenital malformations of larynx', 'Q31'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Tracheal stenosis', 'Tracheomalacia (floppy trachea)', 'Tracheoesophageal fistula', 'Stridor', 'Barking cough', 'Recurrent pneumonia'], 'Congenital malformations of trachea and bronchus', 'Q32'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Congenital pulmonary airway malformation (CPAM)', 'Pulmonary sequestration', 'Agenesis of lung', 'Respiratory distress', 'Recurrent infections', 'Cyanosis'], 'Congenital malformations of lung', 'Q33'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Varies widely', 'Pleural effusion', 'Mediastinal cyst', 'Thymic abnormalities', 'Respiratory distress', 'Chest pain'], 'Other congenital malformations of respiratory system', 'Q34'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure (e.g., smoking)'], 'Structural', ['Opening in roof of mouth', 'Feeding difficulties', 'Speech difficulties', 'Recurrent ear infections', 'Nasal regurgitation of food', 'Dental problems'], 'Cleft palate', 'Q35'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure (e.g., smoking)'], 'Structural', ['Opening in upper lip', 'May involve one or both sides', 'Nasal deformity', 'Feeding difficulties', 'Speech difficulties', 'Dental problems'], 'Cleft lip', 'Q36'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure'], 'Structural', ['Opening in lip and roof of mouth', 'Feeding difficulties', 'Speech difficulties', 'Recurrent ear infections', 'Nasal deformity', 'Dental problems'], 'Cleft palate with cleft lip', 'Q37'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Short tongue (ankyloglossia)', 'Large tongue (macroglossia)', 'Cleft tongue', 'Speech difficulties', 'Feeding difficulties', 'Breathing difficulties (if large)'], 'Other congenital malformations of tongue, mouth and pharynx', 'Q38'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Esophageal atresia (blocked esophagus)', 'Tracheoesophageal fistula', 'Vomiting', 'Choking', 'Inability to feed', 'Excessive drooling'], 'Congenital malformations of esophagus', 'Q39'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Pyloric stenosis', 'Gastric duplication cyst', 'Microgastria', 'Projectile vomiting (pyloric stenosis)', 'Abdominal pain', 'Failure to thrive'], 'Other congenital malformations of stomach', 'Q40'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Duodenal atresia (blockage)', 'Intestinal malrotation', 'Meckel diverticulum', 'Abdominal distension', 'Vomiting (often bile-stained)', 'Inability to pass meconium'], 'Congenital absence, atresia and stenosis of small intestine', 'Q41'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Anal atresia (imperforate anus)', 'Colonic atresia', 'Hirschsprung disease', 'Inability to pass meconium', 'Abdominal distension', 'Vomiting'], 'Congenital absence, atresia and stenosis of large intestine', 'Q42'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Omphalocele (organs outside body)', 'Gastroschisis (organs outside body)', 'Malrotation', 'Intestinal duplication', 'Abdominal wall defect'], 'Other congenital malformations of intestine', 'Q43'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Biliary atresia (blocked bile ducts)', 'Choledochal cyst', 'Agenesis of gallbladder', 'Jaundice', 'Pale stools', 'Dark urine'], 'Congenital malformations of gallbladder, bile ducts and liver', 'Q44'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Pancreatic divisum', 'Annular pancreas', 'Pancreatic agenesis', 'Abdominal pain', 'Pancreatitis', 'Digestive problems'], 'Other congenital malformations of digestive system', 'Q45'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Ambiguous genitalia', 'Ovarian dysgenesis', 'Vaginal agenesis', 'Amenorrhea (no period)', 'Infertility', 'Hormonal imbalance'], 'Congenital malformations of ovaries, fallopian tubes and broad ligaments', 'Q50'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Uterine agenesis (MRKH syndrome)', 'Bicornuate uterus', 'Septate uterus', 'Recurrent miscarriages', 'Infertility', 'Amenorrhea'], 'Congenital malformations of uterus and cervix', 'Q51'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Vaginal atresia', 'Transverse vaginal septum', 'Imperforate hymen', 'Amenorrhea', 'Pelvic pain', 'Difficulty with intercourse'], 'Other congenital malformations of female genitalia', 'Q52'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Undescended testis (cryptorchidism)', 'Testicular agenesis', 'Testicular hypoplasia', 'Infertility risk', 'Increased cancer risk', 'Often asymptomatic'], 'Undescended testicle', 'Q53'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Hypospadias (urethral opening on underside)', 'Epispadias (urethral opening on top)', 'Chordee (penile curvature)', 'Difficulty urinating', 'Infertility', 'Surgical correction often needed'], 'Hypospadias', 'Q54'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Micropenis', 'Penile agenesis', 'Penile duplication', 'Varies widely', 'Hormonal imbalance', 'Psychosocial distress'], 'Other congenital malformations of male genital organs', 'Q55'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Ambiguous genitalia', 'Ovotesticular disorder (true hermaphroditism)', 'Gonadal dysgenesis', 'Hormonal imbalance', 'Infertility', 'Complex psychosocial issues'], 'Indeterminate sex and pseudohermaphroditism', 'Q56'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Maternal health (e.g., diabetes)'], 'Structural', ['Bilateral agenesis (Potter syndrome, fatal)', 'Unilateral agenesis (often asymptomatic)', 'Oligohydramnios (low amniotic fluid)', 'Pulmonary hypoplasia', 'Facial anomalies', 'Hypertension (later in life)'], 'Renal agenesis and other reduction defects of kidney', 'Q60'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Polycystic kidney disease (ARPKD/ADPKD)', 'Renal cysts', 'Enlarged kidneys', 'Hypertension', 'Kidney failure', 'Urinary tract infections'], 'Cystic kidney disease', 'Q61'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Vesicoureteral reflux (VUR)', 'Ureteral obstruction', 'Hydronephrosis (swollen kidney)', 'Recurrent urinary tract infections', 'Kidney damage', 'Flank pain'], 'Congenital obstructive defects of renal pelvis and malformations of ureter', 'Q62'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Horseshoe kidney', 'Ectopic kidney', 'Renal hypoplasia', 'Often asymptomatic', 'Increased risk of stones', 'Increased risk of infection'], 'Other congenital malformations of kidney', 'Q63'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Bladder exstrophy (bladder outside body)', 'Urethral atresia', 'Posterior urethral valves (males)', 'Urinary incontinence', 'Recurrent infections', 'Difficulty urinating'], 'Other congenital malformations of urinary system', 'Q64'],
    ['Worldwide', ['Multifactorial', 'Breech presentation', 'Genetic factors (lax joints)'], 'Structural', ['Hip joint instability', 'Asymmetrical leg creases', 'Limited range of motion', 'Limping (when walking)', 'Uneven leg lengths', 'Audible "clunk" on exam (Ortolani test)'], 'Congenital deformities of hip', 'Q65'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Genetic factors'], 'Structural', ['Clubfoot (talipes equinovarus)', 'Foot turned inward and downward', 'Metatarsus adductus', 'Rocker-bottom foot', 'Difficulty walking', 'Requires casting or surgery'], 'Congenital deformities of feet', 'Q66'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Genetic factors'], 'Structural', ['Varies widely', 'Genu varum (bowlegs)', 'Genu valgum (knock-knees)', 'Tibial torsion', 'Femoral torsion', 'Gait abnormalities'], 'Congenital musculoskeletal deformities of knee', 'Q67'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Amniotic band syndrome'], 'Structural', ['Varies widely', 'Congenital scoliosis', 'Torticollis (wry neck)', 'Facial asymmetry', 'Skull deformities (plagiocephaly)', 'Chest wall deformities'], 'Other congenital musculoskeletal deformities', 'Q68'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Developmental anomaly'], 'Structural', ['Extra finger or toe', 'Can be skin tag or fully formed digit', 'Often hereditary', 'May be associated with syndromes', 'Generally functional impact is low', 'Surgical removal common'], 'Polydactyly', 'Q69'],
    ['Worldwide', ['Genetic factors', 'Spontaneous mutation', 'Part of a syndrome (e.g., Apert)'], 'Structural', ['Webbed fingers', 'Webbed toes', 'Bony or soft tissue fusion', 'Reduced hand/foot function', 'Can be simple or complex', 'Requires surgical separation'], 'Syndactyly', 'Q70'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing limb (amelia)', 'Partially formed limb (meromelia)', 'Phocomelia (hands/feet attached to trunk)', 'Limb hypoplasia', 'Prosthetics may be needed', 'Varies widely in severity'], 'Reduction defects of upper limb', 'Q71'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing limb (amelia)', 'Partially formed limb (meromelia)', 'Phocomelia (hands/feet attached to trunk)', 'Limb hypoplasia', 'Prosthetics may be needed', 'Varies widely in severity'], 'Reduction defects of lower limb', 'Q72'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing hand/foot', 'Missing finger/toe', 'Split hand/foot (ectrodactyly)', 'Varies widely', 'Functional impairment', 'Surgical/prosthetic options'], 'Reduction defects of unspecified limb', 'Q73'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Radial club hand', 'Madelung deformity', 'Shoulder/scapula anomalies', 'Limb length discrepancy', 'Joint contractures', 'Functional impairment'], 'Other congenital malformations of upper limb(s)', 'Q74'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Congenital shortening of femur', 'Tibial/fibular hemimelia', 'Limb length discrepancy', 'Gait abnormalities', 'Joint instability', 'Surgical intervention common'], 'Other congenital malformations of lower limb(s)', 'Q75'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Amniotic band syndrome'], 'Structural', ['Varies widely', 'Scoliosis (congenital)', 'Klippel-Feil syndrome (fused vertebrae)', 'Hemivertebrae', 'Back pain', 'Reduced mobility'], 'Congenital malformations of spine', 'Q76'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Pectus excavatum (sunken chest)', 'Pectus carinatum (pigeon chest)', 'Absent ribs', 'Fused ribs', 'Respiratory difficulties (if severe)', 'Cosmetic concerns'], 'Congenital malformations of bony thorax', 'Q77'],
    ['Worldwide', ['Genetic factors', 'Spontaneous mutation', 'Hereditary'], 'Genetic (Skeletal)', ['Short stature (dwarfism)', 'Disproportionate limbs', 'Macrocephaly (large head)', 'Joint laxity or stiffness', 'Skeletal abnormalities', 'Varies by type (e.g., Achondroplasia)'], 'Osteochondrodysplasia with defects of growth of long bones and spine', 'Q78'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Craniosynostosis (premature skull fusion)', 'Abnormal head shape', 'Facial asymmetry', 'Protruding eyes', 'Increased intracranial pressure', 'Developmental delay (if severe)'], 'Congenital malformations of skull and face bones', 'Q79'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Dry, scaly skin', 'Thickened skin', 'Skin "fish-like" scales', 'Overheating (impaired sweating)', 'Risk of skin infection', 'Reduced joint movement'], 'Congenital ichthyosis', 'Q80'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Skin blistering', 'Fragile skin', 'Blisters form from minor friction', 'Risk of infection', 'Scarring', 'Internal blistering (severe forms)'], 'Epidermolysis bullosa', 'Q81'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Varies widely', 'Abnormal hair growth (hypertrichosis)', 'Missing hair (atrichia)', 'Pigmentation disorders (albinism)', 'Vascular anomalies (port-wine stain)', 'Skin laxity (cutis laxa)'], 'Other congenital malformations of skin', 'Q82'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Unknown etiology'], 'Genetic (Skin)', ['Absent breasts (amastia)', 'Extra nipples (polythelia)', 'Underdeveloped breasts (hypoplasia)', 'Gynaecomastia (males, congenital)', 'Often asymptomatic', 'Cosmetic concerns'], 'Congenital malformations of breast', 'Q83'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Ectodermal dysplasia', 'Abnormal nails', 'Abnormal hair', 'Abnormal teeth', 'Absent sweat glands', 'Heat intolerance'], 'Other congenital malformations of integument', 'Q84'],
    ['Worldwide', ['Genetic factors', 'Hereditary (Autosomal dominant)', 'Spontaneous mutation'], 'Genetic (Neurocutaneous)', ['Cafe-au-lait spots (NF1)', 'Neurofibromas (benign tumors)', 'Lisch nodules (eye)', 'Learning disabilities', 'Ash-leaf spots (Tuberous Sclerosis)', 'Seizures (Tuberous Sclerosis)'], 'Phakomatoses, not elsewhere classified (e.g., NF, TS)', 'Q85'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Associated syndromes'], 'Multifactorial', ['Varies widely', 'Marfan syndrome (connective tissue)', 'Ehlers-Danlos syndrome (joint hypermobility)', 'Tall stature', 'Joint laxity', 'Aortic dissection risk (Marfan)'], 'Congenital malformation syndromes due to known exogenous causes', 'Q86'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Prenatal factors'], 'Multifactorial', ['Varies widely', 'Prader-Willi syndrome', 'Angelman syndrome', 'Sotos syndrome (overgrowth)', 'Beckwith-Wiedemann syndrome', 'Specific facial features'], 'Other specified congenital malformation syndromes', 'Q87'],
    ['Worldwide', ['Unknown etiology', 'Genetic factors', 'Developmental anomaly'], 'Structural', ['Varies widely', 'Congenital anomaly not fitting other categories', 'Rare disorders', 'Unique combinations of features', 'Consult specialist for diagnosis', 'Varies'], 'Other specified congenital malformations, not elsewhere classified', 'Q89'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Maternal age factor', 'Translocation'], 'Chromosomal (Trisomy 21)', ['Intellectual disability', 'Flat facial profile', 'Upward slanting eyes', 'Single palmar crease', 'Congenital heart defects', 'Hypotonia (low muscle tone)'], 'Down syndrome', 'Q90'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Maternal age factor', 'Translocation'], 'Chromosomal (Trisomy 18/13)', ['Severe intellectual disability', 'Congenital heart defects', 'Rocker-bottom feet (T18)', 'Clenched hands (T18)', 'Cleft lip/palate (T13)', 'Polydactyly (T13)'], 'Edwards syndrome (Q91.0-3) and Patau syndrome (Q91.4-7)', 'Q91'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Translocation', 'Meiotic error'], 'Chromosomal', ['Varies by chromosome', 'Developmental delay', 'Intellectual disability', 'Congenital anomalies', 'Dysmorphic features', 'Growth restriction'], 'Other trisomies and partial trisomies, not elsewhere classified', 'Q92'],
    ['Worldwide', ['Chromosomal deletion', 'Spontaneous mutation', 'Inherited translocation'], 'Chromosomal', ['High-pitched cat-like cry (Cri-du-chat)', 'Intellectual disability', 'Low birth weight', 'Hypotonia', 'Microcephaly', 'Dysmorphic facial features'], 'Monosomies and deletions from the autosomes, not elsewhere classified', 'Q93'],
    ['Worldwide', ['Chromosomal translocation', 'Chromosomal inversion', 'Hereditary'], 'Chromosomal', ['Often asymptomatic (carrier)', 'Risk of infertility', 'Recurrent miscarriages', 'Risk of child with unbalanced translocation', 'No net loss/gain of genetic material', 'Varies'], 'Balanced rearrangements and structural markers, not elsewhere classified', 'Q95'],
    ['Worldwide', ['Chromosomal nondisjunction (X)', 'Monosomy X', 'Mosaicism'], 'Chromosomal (XO)', ['Short stature', 'Ovarian failure (infertility)', 'Webbed neck', 'Broad chest', 'Congenital heart defects', 'Amenorrhea'], 'Turner syndrome', 'Q96'],
    ['Worldwide', ['Chromosomal nondisjunction (X)', 'Meiotic error', 'Maternal age factor'], 'Chromosomal (e.g., XXX)', ['Often asymptomatic', 'Tall stature', 'Learning disabilities', 'Delayed speech', 'Motor skill delays', 'Premature ovarian failure (rare)'], 'Other sex chromosome abnormalities, female phenotype, not elsewhere classified', 'Q97'],
    ['Worldwide', ['Chromosomal nondisjunction (X/Y)', 'Meiotic error', 'Maternal/paternal age factor'], 'Chromosomal (e.g., XXY)', ['Tall stature', 'Small testes (hypogonadism)', 'Infertility', 'Gynecomastia (breast development)', 'Learning disabilities', 'Reduced facial/body hair'], 'Other sex chromosome abnormalities, male phenotype, not elsewhere classified', 'Q98'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Mosaicism', 'Structural abnormality'], 'Chromosomal', ['Varies widely', 'Ambiguous genitalia', 'Infertility', 'Developmental delay', 'Hormonal imbalances', 'Associated anomalies'], 'Other sex chromosome abnormalities, both female and male phenotype', 'Q99']
]

sectionR = [
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Palpitations", "Dizziness", "Shortness of breath", "Chest pain", "Fainting (syncope)", "Fatigue"],
        "label": "Abnormalities of heart beat",
        "icd_code": "R00"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Shortness of breath", "Chest pain", "Dizziness", "Fatigue", "Swelling in legs"],
        "label": "Cardiac murmurs and other cardiac sounds",
        "icd_code": "R01"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Discoloration of skin (blue/black)", "Numbness", "Severe pain", "Foul-smelling discharge", "Coldness in affected area", "Loss of sensation"],
        "label": "Gangrene, not elsewhere classified",
        "icd_code": "R02"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Headache", "Dizziness", "Blurred vision", "Nosebleeds", "Shortness of breath"],
        "label": "Abnormal blood-pressure reading, without diagnosis",
        "icd_code": "R03"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Coughing up blood (hemoptysis)", "Nosebleed (epistaxis)", "Shortness of breath", "Chest pain", "Dizziness", "Fever"],
        "label": "Hemorrhage from respiratory passages",
        "icd_code": "R04"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Sputum production", "Sore throat", "Runny nose", "Fever", "Shortness of breath", "Wheezing"],
        "label": "Cough",
        "icd_code": "R05"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Shortness of breath (dyspnea)", "Wheezing", "Rapid breathing (tachypnea)", "Shallow breathing", "Pauses in breathing (apnea)", "Noisy breathing (stridor)"],
        "label": "Abnormalities of breathing",
        "icd_code": "R06"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Sharp pain", "Dull ache", "Burning sensation", "Pain on swallowing", "Pain on breathing", "Sore throat"],
        "label": "Pain in throat and chest",
        "icd_code": "R07"
    },
    # R08 is not a valid code in this context
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Asphyxia", "Nasal congestion", "Nosebleed (epistaxis)", "Palpitations", "Fatigue", "Dizziness"],
        "label": "Other symptoms and signs involving the circulatory and respiratory systems",
        "icd_code": "R09"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Nausea", "Vomiting", "Bloating", "Diarrhea", "Constipation", "Fever"],
        "label": "Abdominal and pelvic pain",
        "icd_code": "R10"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abdominal pain", "Dizziness", "Diarrhea", "Fever", "Headache", "Loss of appetite"],
        "label": "Nausea and vomiting",
        "icd_code": "R11"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Burning sensation in chest", "Sour taste in mouth", "Regurgitation", "Bloating", "Burping", "Difficulty swallowing"],
        "label": "Heartburn",
        "icd_code": "R12"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Pain while swallowing (odynophagia)", "Sensation of food stuck in throat", "Coughing or gagging when swallowing", "Drooling", "Hoarseness", "Regurgitation"],
        "label": "Dysphagia",
        "icd_code": "R13"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abdominal bloating", "Abdominal pain or cramping", "Excessive gas passage", "Burping", "Rumbling in abdomen (borborygmi)", "Indigestion"],
        "label": "Flatulence and related conditions",
        "icd_code": "R14"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Involuntary passage of stool", "Leaking stool", "Inability to control gas", "Diarrhea", "Constipation", "Abdominal cramping"],
        "label": "Fecal incontinence",
        "icd_code": "R15"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Abdominal fullness or pain", "Fatigue", "Jaundice (yellowing skin/eyes)", "Nausea", "Weight loss"],
        "label": "Hepatomegaly and splenomegaly, not elsewhere classified",
        "icd_code": "R16"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Yellowing of skin and eyes", "Dark urine", "Pale stools", "Itching (pruritus)", "Fatigue", "Abdominal pain"],
        "label": "Unspecified jaundice",
        "icd_code": "R17"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abdominal swelling", "Weight gain", "Shortness of breath", "Abdominal discomfort or pain", "Loss of appetite", "Nausea"],
        "label": "Ascites",
        "icd_code": "R18"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abdominal distension (gaseous)", "Changes in bowel habit", "Halitosis (bad breath)", "Visible peristalsis", "Abdominal rigidity", "Abnormal fecal findings"],
        "label": "Other symptoms and signs involving the digestive system and abdomen",
        "icd_code": "R19"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Numbness (anesthesia)", "Tingling or pins and needles (paresthesia)", "Increased sensitivity (hyperesthesia)", "Decreased sensitivity (hypoesthesia)", "Burning sensation", "Itching (pruritus)"],
        "label": "Disturbances of skin sensation",
        "icd_code": "R20"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Itching (pruritus)", "Redness (erythema)", "Bumps (papules)", "Blisters (vesicles)", "Dryness or scaling", "Fever"],
        "label": "Rash and other nonspecific skin eruption",
        "icd_code": "R21"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Visible lump", "Pain or tenderness", "Redness", "Warmth over area", "Change in skin texture", "Change in size"],
        "label": "Localized swelling, mass and lump of skin and subcutaneous tissue",
        "icd_code": "R22"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Cyanosis (blueish discoloration)", "Pallor (paleness)", "Flushing", "Peeling", "Thickening", "Ulceration"],
        "label": "Other skin changes",
        "icd_code": "R23"
    },
    # R24 is not a valid code
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Tremor", "Muscle twitching (fasciculation)", "Spasms", "Jerking movements (myoclonus)", "Writhing movements (athetosis)", "Restlessness (akathisia)"],
        "label": "Abnormal involuntary movements",
        "icd_code": "R25"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Unsteady gait (ataxia)", "Limping", "Shuffling", "Difficulty initiating movement", "Frequent falls", "Dragging foot"],
        "label": "Abnormalities of gait and mobility",
        "icd_code": "R26"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Clumsiness", "Difficulty with fine motor skills", "Vertigo", "Dizziness", "Nystagmus (involuntary eye movement)", "Poor balance"],
        "label": "Other lack of coordination",
        "icd_code": "R27"
    },
    # R28 is not a valid code
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Muscle weakness", "Stiffness", "Cramps", "Abnormal reflexes", "Loss of sensation", "Meningismus (neck stiffness)"],
        "label": "Other symptoms and signs involving the nervous and musculoskeletal systems",
        "icd_code": "R29"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Burning sensation", "Stinging pain", "Urinary frequency", "Urinary urgency", "Cloudy urine", "Blood in urine (hematuria)"],
        "label": "Pain associated with micturition",
        "icd_code": "R30"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Pink, red, or brown urine", "Often asymptomatic", "Painful urination", "Frequent urination", "Abdominal pain", "Fever"],
        "label": "Unspecified hematuria",
        "icd_code": "R31"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Leaking urine when coughing/sneezing", "Sudden, strong urge to urinate", "Involuntary loss of urine", "Frequent urination", "Nocturia (urinating at night)", "Bedwetting (enuresis)"],
        "label": "Unspecified urinary incontinence",
        "icd_code": "R32"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Inability to urinate", "Weak urine stream", "Straining to urinate", "Abdominal pain or fullness", "Frequent urge to urinate", "Dribbling"],
        "label": "Retention of urine",
        "icd_code": "R33"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["No urine output (anuria)", "Very low urine output (oliguria)", "Swelling (edema)", "Nausea", "Fatigue", "Shortness of breath"],
        "label": "Anuria and oliguria",
        "icd_code": "R34"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Excessive urination volume", "Frequent urination", "Nocturia (urinating at night)", "Thirst (polydipsia)", "Fatigue", "Weight loss"],
        "label": "Polyuria",
        "icd_code": "R35"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Discharge from urethra", "Painful urination", "Itching", "Frequent urination", "Blood in discharge", "Foul odor"],
        "label": "Urethral discharge",
        "icd_code": "R36"
    },
    # R37, R38 are not valid codes
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Urinary urgency", "Hesitancy", "Weak stream", "Incomplete bladder emptying", "Cloudy urine", "Foul-smelling urine"],
        "label": "Other symptoms and signs involving the urinary system",
        "icd_code": "R39"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Excessive drowsiness (somnolence)", "Unresponsiveness (stupor)", "Unconsciousness (coma)", "Confusion", "Slurred speech", "Abnormal breathing"],
        "label": "Somnolence, stupor and coma",
        "icd_code": "R40"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Memory loss (amnesia)", "Confusion", "Disorientation (time, place, person)", "Difficulty concentrating", "Altered mental status", "Agnosia (inability to recognize)"],
        "label": "Other symptoms and signs involving cognitive functions and awareness",
        "icd_code": "R41"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Sensation of spinning (vertigo)", "Lightheadedness", "Unsteadiness", "Faintness", "Nausea", "Blurred vision"],
        "label": "Dizziness and giddiness",
        "icd_code": "R42"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Loss of smell (anosmia)", "Reduced smell (hyposmia)", "Loss of taste (ageusia)", "Reduced taste (hypogeusia)", "Distorted smell (parosmia)", "Distorted taste (dysgeusia)"],
        "label": "Disturbances of smell and taste",
        "icd_code": "R43"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Hallucinations (auditory)", "Hallucinations (visual)", "Hallucinations (tactile)", "Illusions", "Tinnitus (ringing in ears)", "Vertigo"],
        "label": "Other symptoms and signs involving general sensations and perceptions",
        "icd_code": "R44"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Anxiety", "Agitation", "Depressed mood", "Irritability", "Apathy", "Panic attacks"],
        "label": "Symptoms and signs involving emotional state",
        "icd_code": "R45"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Poor personal hygiene", "Bizarre behavior", "Slowed movements", "Restlessness", "Social withdrawal", "Lack of impulse control"],
        "label": "Symptoms and signs involving appearance and behavior",
        "icd_code": "R46"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Slurred speech (dysarthria)", "Difficulty finding words (anomia)", "Inability to speak (aphasia)", "Stuttering", "Pressured speech", "Muteness"],
        "label": "Speech disturbances, not elsewhere classified",
        "icd_code": "R47"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Difficulty reading", "Difficulty spelling", "Difficulty writing (dysgraphia)", "Difficulty with math (dyscalculia)", "Inability to recognize objects (agnosia)", "Inability to perform tasks (apraxia)"],
        "label": "Dyslexia and other symbolic dysfunctions, not elsewhere classified",
        "icd_code": "R48"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Hoarseness", "Loss of voice (aphonia)", "Weak voice", "Raspy voice", "Voice breaks", "Strained voice"],
        "label": "Voice disturbances",
        "icd_code": "R49"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Elevated body temperature", "Chills", "Sweating", "Headache", "Muscle aches", "Fatigue"],
        "label": "Fever of other and unknown origin",
        "icd_code": "R50"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Throbbing pain", "Dull ache", "Pain in specific area", "Nausea", "Sensitivity to light (photophobia)", "Sensitivity to sound (phonophobia)"],
        "label": "Headache",
        "icd_code": "R51"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Acute pain", "Chronic pain", "Sharp pain", "Dull pain", "Aching", "Burning pain"],
        "label": "Pain, not elsewhere classified",
        "icd_code": "R52"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["General feeling of discomfort", "Lack of energy", "Weakness", "Drowsiness", "Difficulty concentrating", "Apathy"],
        "label": "Malaise and fatigue",
        "icd_code": "R53"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Memory loss", "Cognitive decline", "Physical frailty", "Reduced mobility", "Loss of appetite", "General decline in health"],
        "label": "Senility",
        "icd_code": "R54"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Fainting", "Loss of consciousness (brief)", "Lightheadedness before episode", "Dizziness", "Blurred vision", "Palpitations"],
        "label": "Syncope and collapse",
        "icd_code": "R55"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Involuntary muscle contractions", "Loss of consciousness", "Staring spells", "Jerking movements", "Confusion after episode", "Loss of bladder control"],
        "label": "Convulsions, not elsewhere classified",
        "icd_code": "R56"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Low blood pressure (hypotension)", "Rapid, weak pulse", "Rapid breathing", "Cold, clammy skin", "Confusion", "Cyanosis (blue lips/skin)"],
        "label": "Shock, not elsewhere classified",
        "icd_code": "R57"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Visible bleeding", "Bruising", "Dizziness", "Weakness", "Low blood pressure", "Rapid pulse"],
        "label": "Hemorrhage, not elsewhere classified",
        "icd_code": "R58"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Swollen lumps (neck, armpit, groin)", "Tenderness or pain", "Fever", "Night sweats", "Weight loss", "Fatigue"],
        "label": "Enlarged lymph nodes",
        "icd_code": "R59"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Swelling or puffiness", "Stretched or shiny skin", "Skin that retains a dimple (pitting)", "Increased abdominal size", "Shortness of breath", "Weight gain"],
        "label": "Edema, not elsewhere classified",
        "icd_code": "R60"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Excessive sweating", "Sweating in specific areas (palms, soles, underarms)", "Sweat soaking through clothing", "Clammy skin", "Skin maceration", "Social anxiety"],
        "label": "Hyperhidrosis",
        "icd_code": "R61"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Delayed milestones (e.g., walking, talking)", "Failure to thrive (poor weight/height gain)", "Delayed puberty", "Short stature", "Cognitive delays", "Lack of secondary sexual characteristics"],
        "label": "Lack of expected normal physiological development in childhood and adult",
        "icd_code": "R62"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Anorexia (loss of appetite)", "Polydipsia (excessive thirst)", "Polyphagia (excessive eating)", "Weight loss", "Weight gain", "Difficulty feeding"],
        "label": "Symptoms and signs concerning food and fluid intake",
        "icd_code": "R63"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Severe weight loss", "Muscle wasting", "Anorexia (loss of appetite)", "Fatigue", "Weakness", "Anemia"],
        "label": "Cachexia",
        "icd_code": "R64"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Fever or hypothermia", "Tachycardia (high heart rate)", "Tachypnea (high respiratory rate)", "High or low white blood cell count", "Altered mental status", "Hypotension (low blood pressure)"],
        "label": "Systemic inflammatory response syndrome (SIRS)",
        "icd_code": "R65"
    },
    # R66, R67 are not valid codes
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Chills", "Night sweats", "Weight changes", "Generalized pain", "Low body temperature", "Clubbing of fingers"],
        "label": "Other general symptoms and signs",
        "icd_code": "R68"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Symptoms not clearly defined", "Multiple vague complaints", "Unexplained illness", "No clear diagnosis", "Failure to thrive (unspecified)", "Debility (unspecified)"],
        "label": "Unknown and unspecified causes of morbidity",
        "icd_code": "R69"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Fever", "Fatigue", "Pain", "Stiffness", "Weight loss"],
        "label": "Elevated erythrocyte sedimentation rate and abnormality of plasma viscosity",
        "icd_code": "R70"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Fatigue", "Weakness", "Pale skin (pallor)", "Shortness of breath", "Dizziness", "Jaundice"],
        "label": "Abnormality of red blood cells",
        "icd_code": "R71"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Frequent infections", "Fever", "Fatigue", "Easy bruising", "Enlarged lymph nodes", "Weight loss"],
        "label": "Abnormality of white blood cells, not elsewhere classified",
        "icd_code": "R72"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Excessive thirst (polydipsia)", "Frequent urination (polyuria)", "Increased hunger (polyphagia)", "Blurred vision", "Fatigue"],
        "label": "Elevated blood glucose level",
        "icd_code": "R73"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Jaundice", "Abdominal pain", "Fatigue", "Nausea", "Muscle weakness"],
        "label": "Abnormal serum enzyme levels",
        "icd_code": "R74"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Anxiety", "Requires follow-up testing", "No physical symptoms", "Patient counseling", "Further blood draw", "Waiting period"],
        "label": "Inconclusive laboratory evidence of human immunodeficiency virus (HIV)",
        "icd_code": "R75"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Joint pain", "Fatigue", "Rash", "Fever", "Recurrent infections"],
        "label": "Other abnormal immunological findings in serum",
        "icd_code": "R76"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Edema (swelling)", "Fatigue", "Weight loss", "Frequent infections", "Bone pain"],
        "label": "Other abnormalities of plasma proteins",
        "icd_code": "R77"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Varies by substance", "Altered mental status", "Nausea", "Drowsiness", "Toxicity symptoms", "Asymptomatic"],
        "label": "Findings of drugs and other substances, not normally found in blood",
        "icd_code": "R78"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Fatigue", "Nausea", "Confusion", "Muscle weakness", "Abnormal heart rhythm"],
        "label": "Other abnormal findings of blood chemistry",
        "icd_code": "R79"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Foamy urine", "Swelling (edema) in hands, feet, abdomen", "Fatigue", "Shortness of breath", "Loss of appetite"],
        "label": "Proteinuria, isolated",
        "icd_code": "R80"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Excessive thirst", "Frequent urination", "Fatigue", "Blurred vision", "Weight loss"],
        "label": "Glycosuria",
        "icd_code": "R81"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Cloudy urine", "Foul-smelling urine", "Abnormal urine color", "Painful urination", "Fever", "Abdominal pain"],
        "label": "Other abnormal findings in urine",
        "icd_code": "R82"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Headache", "Fever", "Neck stiffness", "Nausea", "Vomiting", "Altered mental status"],
        "label": "Abnormal findings in cerebrospinal fluid",
        "icd_code": "R83"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Cough", "Shortness of breath", "Chest pain", "Sputum production", "Fever", "Weight loss"],
        "label": "Abnormal findings in specimens from respiratory organs and thorax",
        "icd_code": "R84"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abdominal pain", "Nausea", "Vomiting", "Diarrhea", "Jaundice", "Blood in stool"],
        "label": "Abnormal findings in specimens from digestive organs and abdominal cavity",
        "icd_code": "R85"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Urethral discharge", "Testicular pain or swelling", "Blood in semen", "Painful urination", "Infertility", "Lump"],
        "label": "Abnormal findings in specimens from male genital organs",
        "icd_code": "R86"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Abnormal vaginal bleeding", "Vaginal discharge", "Pelvic pain", "Painful intercourse", "Abnormal Pap smear", "Infertility"],
        "label": "Abnormal findings in specimens from female genital organs",
        "icd_code": "R87"
    },
    # R88 is not a valid code
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Symptoms vary by site", "Pain", "Swelling", "Abnormal function", "Fever", "Fatigue"],
        "label": "Abnormal findings in specimens from other organs, systems and tissues",
        "icd_code": "R89"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Headache", "Seizures", "Weakness", "Numbness", "Cognitive changes", "Vision problems"],
        "label": "Abnormal findings on diagnostic imaging of central nervous system",
        "icd_code": "R90"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Cough", "Shortness of breath", "Chest pain", "Fever", "Weight loss"],
        "label": "Abnormal findings on diagnostic imaging of lung",
        "icd_code": "R91"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Breast lump", "Breast pain", "Nipple discharge", "Skin changes (dimpling, redness)", "Change in breast size/shape"],
        "label": "Abnormal findings on diagnostic imaging of breast",
        "icd_code": "R92"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Pain in affected area", "Swelling", "Lump", "Organ dysfunction", "Abdominal pain"],
        "label": "Abnormal findings on diagnostic imaging of other body structures",
        "icd_code": "R93"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Symptoms related to organ system", "Fatigue", "Shortness of breath", "Pain", "Dizziness", "Cognitive changes"],
        "label": "Abnormal results of function studies",
        "icd_code": "R94"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Unexpected death of infant", "No symptoms prior", "Occurs during sleep", "Infant under 1 year", "No clear cause found", "Autopsy inconclusive"],
        "label": "Sudden infant death syndrome (SIDS)",
        "icd_code": "R95"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Symptom"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Unexpected death", "No obvious cause", "Death not witnessed", "Occurs outside infancy", "Autopsy inconclusive", "Sudden collapse"],
        "label": "Other sudden death, cause unknown",
        "icd_code": "R96"
    },
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Often asymptomatic", "Weight loss", "Fatigue", "Pain", "Lump", "Changes in bowel/bladder"],
        "label": "Abnormal tumor markers",
        "icd_code": "R97"
    },
    # R98 is not a valid code
    {
        "geography": "Worldwide",
        "transmission": ["Varies by cause", "Not infectious", "Finding"],
        "disease_type": "Varies/Non-infectious",
        "common_symptoms": ["Death", "Cause not determined", "Lack of information", "Conflicting findings", "Advanced decomposition", "No autopsy"],
        "label": "Ill-defined and unknown causes of mortality",
        "icd_code": "R99"
    }
]

sectionS = [
    # S00-S09: Injuries to the head
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion', 'Contusion'], 'Superficial injury of head', 'S00'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tissue damage'], 'Open wound of head', 'S01'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Swelling', 'Deformity', 'Loss of function', 'Bruising', 'Crepitus'], 'Fracture of skull and facial bones', 'S02'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Jaw pain', 'Difficulty opening mouth', 'Clicking sound', 'Joint locking', 'Headache', 'Neck pain'], 'Dislocation, sprain and strain of joints and ligaments of head', 'S03'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Loss of smell', 'Vision problems', 'Facial droop', 'Deafness', 'Dizziness', 'Difficulty swallowing'], 'Injury of cranial nerves', 'S04'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Vision loss', 'Eye pain', 'Double vision', 'Bleeding in eye', 'Swelling of eyelid', 'Foreign body sensation'], 'Injury of eye and orbit', 'S05'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Headache', 'Vomiting', 'Confusion', 'Loss of consciousness', 'Seizure', 'Drowsiness'], 'Intracranial injury', 'S06'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe tissue damage', 'Deformity', 'Massive swelling', 'Bleeding', 'Neurological deficit', 'Pain'], 'Crushing injury of head', 'S07'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of body part', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of head', 'S08'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Headache', 'Dizziness', 'Tenderness'], 'Other and unspecified injuries of head', 'S09'],

    # S10-S19: Injuries to the neck
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Redness', 'Superficial scratch', 'Contusion'], 'Superficial injury of neck', 'S10'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Hoarseness'], 'Open wound of neck', 'S11'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Neck pain', 'Swelling', 'Deformity', 'Difficulty swallowing', 'Limited motion', 'Crepitus'], 'Fracture of neck', 'S12'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Neck pain', 'Stiffness', 'Muscle spasm', 'Headache', 'Limited range of motion', 'Whiplash'], 'Dislocation, sprain and strain of joints and ligaments of neck', 'S13'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in arms', 'Tingling', 'Weakness', 'Paralysis', 'Loss of sensation', 'Loss of bladder control'], 'Injury of nerves and spinal cord at neck level', 'S14'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pulsating hematoma', 'Active bleeding', 'Bruit', 'Neurological deficit', 'Diminished pulse', 'Shock'], 'Injury of blood vessels at neck level', 'S15'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Stiffness', 'Weakness', 'Muscle spasm', 'Difficulty turning head', 'Swelling'], 'Injury of muscle, fascia and tendon at neck level', 'S16'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Airway obstruction', 'Difficulty breathing', 'Crushing deformity', 'Bruising'], 'Crushing injury of neck', 'S17'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Decapitation', 'Severe bleeding', 'Pain', 'Shock', 'Non-survivable', 'Risk of infection'], 'Traumatic amputation at neck level', 'S18'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Stiffness', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of neck', 'S19'],

    # S20-S29: Injuries to the thorax
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest wall pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion', 'Contusion'], 'Superficial injury of thorax', 'S20'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Sucking chest wound'], 'Open wound of thorax', 'S21'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe chest pain', 'Pain on breathing', 'Shortness of breath', 'Deformity of rib cage', 'Bruising', 'Crepitus'], 'Fracture of rib(s), sternum and thoracic spine', 'S22'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest pain', 'Back pain', 'Stiffness', 'Muscle spasm', 'Limited range of motion', 'Pain with twisting'], 'Dislocation, sprain and strain of joints and ligaments of thorax', 'S23'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in chest', 'Tingling', 'Weakness in legs', 'Paralysis', 'Loss of sensation below injury', 'Bowel/bladder dysfunction'], 'Injury of nerves and spinal cord at thorax level', 'S24'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Massive internal bleeding', 'Shock', 'Shortness of breath', 'Chest pain', 'Hemothorax', 'Diminished pulses'], 'Injury of blood vessels of thorax', 'S25'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with breathing', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle spasm', 'Difficulty twisting torso'], 'Injury of muscle, fascia and tendon at thorax level', 'S26'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Crushing deformity', 'Difficulty breathing', 'Flail chest', 'Internal organ damage', 'Shock'], 'Crushing injury of thorax and traumatic asphyxia', 'S27'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of arm at shoulder', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of thorax', 'S28'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest pain', 'Swelling', 'Bruising', 'Shortness of breath', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of thorax', 'S29'],

    # S30-S39: Injuries to the abdomen, lower back, lumbar spine and pelvis
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal pain', 'Back pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of abdomen, lower back and pelvis', 'S30'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Evisceration'], 'Open wound of abdomen, lower back and pelvis', 'S31'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe back pain', 'Pelvic pain', 'Inability to stand', 'Deformity', 'Bruising', 'Crepitus'], 'Fracture of lumbar spine and pelvis', 'S32'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Lower back pain', 'Stiffness', 'Muscle spasm', 'Sciatica', 'Limited range of motion', 'Pain with bending'], 'Dislocation, sprain and strain of joints and ligaments of lumbar spine and pelvis', 'S33'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in legs', 'Weakness', 'Paralysis', 'Loss of sensation', 'Bowel/bladder dysfunction', 'Cauda equina syndrome'], 'Injury of nerves and spinal cord at abdomen, lower back and pelvis level', 'S34'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Internal bleeding', 'Abdominal rigidity', 'Shock', 'Hypotension', 'Bruising', 'Pulsatile mass'], 'Injury of blood vessels at abdomen, lower back and pelvis level', 'S35'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal muscle pain', 'Back muscle strain', 'Tenderness', 'Swelling', 'Muscle spasm', 'Pain with movement'], 'Injury of muscle, fascia and tendon at abdomen, lower back and pelvis level', 'S36'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Internal organ damage', 'Internal bleeding', 'Shock', 'Pelvic instability'], 'Crushing injury of abdomen, lower back and pelvis', 'S37'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Traumatic dismemberment', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of abdomen, lower back and pelvis', 'S38'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal pain', 'Back pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of abdomen, lower back and pelvis', 'S39'],

    # S40-S49: Injuries to the shoulder and upper arm
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Shoulder pain', 'Arm pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of shoulder and upper arm', 'S40'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced arm mobility'], 'Open wound of shoulder and upper arm', 'S41'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe shoulder pain', 'Severe arm pain', 'Inability to lift arm', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of shoulder and upper arm', 'S42'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Shoulder joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Arm weakness'], 'Dislocation, sprain and strain of joints and ligaments of shoulder girdle', 'S43'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in arm', 'Tingling', 'Weakness', 'Wrist drop', 'Loss of sensation', 'Shooting pain'], 'Injury of nerves at shoulder and upper arm level', 'S44'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in wrist', 'Pale arm', 'Cold arm', 'Bruit'], 'Injury of blood vessels at shoulder and upper arm level', 'S45'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with movement', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle weakness', 'Rotator cuff tear symptoms'], 'Injury of muscle, fascia and tendon at shoulder and upper arm level', 'S46'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of shoulder and upper arm', 'S47'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of arm', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of shoulder and upper arm', 'S48'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Arm pain', 'Shoulder pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of shoulder and upper arm', 'S49'],

    # S50-S59: Injuries to the elbow and forearm
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Elbow pain', 'Forearm pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of elbow and forearm', 'S50'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced wrist/hand mobility'], 'Open wound of elbow and forearm', 'S51'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe elbow pain', 'Severe forearm pain', 'Inability to rotate forearm', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of elbow and forearm', 'S52'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Elbow joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Tennis elbow symptoms'], 'Dislocation, sprain and strain of joints and ligaments of elbow', 'S53'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in hand', 'Tingling', 'Weakness of grip', 'Claw hand', 'Loss of sensation in fingers', 'Shooting pain'], 'Injury of nerves at forearm level', 'S54'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in wrist', 'Pale hand', 'Cold hand', 'Bruit'], 'Injury of blood vessels at forearm level', 'S55'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with gripping', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle weakness', 'Pain on wrist movement'], 'Injury of muscle, fascia and tendon at forearm level', 'S56'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of elbow and forearm', 'S57'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of forearm/hand', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of elbow and forearm', 'S58'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Forearm pain', 'Elbow pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of elbow and forearm', 'S59'],

    # S60-S69: Injuries to the wrist, hand and fingers
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Wrist pain', 'Hand pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of wrist, hand and fingers', 'S60'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tendon exposure'], 'Open wound of wrist, hand and fingers', 'S61'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe wrist pain', 'Severe hand pain', 'Inability to grip', 'Finger deformity', 'Swelling', 'Crepitus'], 'Fracture at wrist and hand level', 'S62'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Wrist joint pain', 'Finger joint pain', 'Instability', 'Swelling', 'Limited range of motion', 'Jammed finger'], 'Dislocation, sprain and strain of joints and ligaments at wrist and hand level', 'S63'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in fingers', 'Tingling', 'Weakness of grip', 'Loss of sensation', 'Carpal tunnel symptoms', 'Clumsiness'], 'Injury of nerves at wrist and hand level', 'S64'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Poor capillary refill', 'Pale fingers', 'Cold fingers', 'Loss of pulse'], 'Injury of blood vessels at wrist and hand level', 'S65'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with gripping', 'Tendon rupture', 'Inability to extend/flex finger', 'Tenderness', 'Swelling', 'Trigger finger'], 'Injury of muscle, fascia and tendon at wrist and hand level', 'S66'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Crushing deformity', 'Mangling injury', 'Vascular compromise', 'Nerve damage'], 'Crushing injury of wrist, hand and fingers', 'S67'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of finger(s)/hand', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of wrist, hand and fingers', 'S68'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hand pain', 'Wrist pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of wrist, hand and fingers', 'S69'],

    # S70-S79: Injuries to the hip and thigh
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip pain', 'Thigh pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of hip and thigh', 'S70'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced leg mobility'], 'Open wound of hip and thigh', 'S71'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe hip pain', 'Inability to bear weight', 'Shortened leg', 'Externally rotated leg', 'Severe thigh pain', 'Deformity'], 'Fracture of femur', 'S72'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Groin pain'], 'Dislocation, sprain and strain of joint and ligaments of hip', 'S73'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in leg', 'Tingling', 'Weakness', 'Foot drop', 'Loss of sensation', 'Sciatic pain'], 'Injury of nerves at hip and thigh level', 'S74'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in foot', 'Pale leg', 'Cold leg', 'Shock'], 'Injury of blood vessels at hip and thigh level', 'S75'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with walking', 'Hamstring strain', 'Quadriceps strain', 'Tenderness', 'Swelling', 'Muscle weakness'], 'Injury of muscle, fascia and tendon at hip and thigh level', 'S76'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of hip and thigh', 'S77'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of leg', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of hip and thigh', 'S78'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip pain', 'Thigh pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of hip and thigh', 'S79'],

    # S80-S89: Injuries to the knee and lower leg
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee pain', 'Lower leg pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of knee and lower leg', 'S80'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Joint exposure'], 'Open wound of knee and lower leg', 'S81'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe knee pain', 'Severe leg pain', 'Inability to bear weight', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of lower leg, including ankle', 'S82'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee joint pain', 'Instability', 'Knee giving way', 'Swelling', 'Limited range of motion', 'Ligament tear (ACL/MCL)'], 'Dislocation, sprain and strain of joints and ligaments of knee', 'S83'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in foot', 'Tingling', 'Weakness', 'Foot drop', 'Loss of sensation', 'Shooting pain'], 'Injury of nerves at lower leg level', 'S84'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in foot', 'Pale foot', 'Cold foot', 'Bruit'], 'Injury of blood vessels at lower leg level', 'S85'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Calf pain', 'Achilles tendon rupture', 'Inability to stand on toes', 'Tenderness', 'Swelling', 'Muscle weakness'], 'Injury of muscle, fascia and tendon at lower leg level', 'S86'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of knee and lower leg', 'S87'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of lower leg/foot', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of knee and lower leg', 'S88'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee pain', 'Lower leg pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of knee and lower leg', 'S89'],

    # S90-S99: Injuries to the ankle and foot
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle pain', 'Foot pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of ankle, foot and toes', 'S90'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tendon exposure'], 'Open wound of ankle, foot and toes', 'S91'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe ankle pain', 'Severe foot pain', 'Inability to bear weight', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of foot and ankle', 'S92'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle joint pain', 'Instability', 'Ankle giving way', 'Swelling', 'Limited range of motion', 'Ankle sprain'], 'Dislocation, sprain and strain of joints and ligaments of ankle, foot and toes', 'S93'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in foot', 'Tingling in toes', 'Weakness', 'Loss of sensation', 'Morton\'s neuroma symptoms', 'Burning pain'], 'Injury of nerves at ankle and foot level', 'S94'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Poor capillary refill', 'Pale toes', 'Cold toes', 'Loss of pulse'], 'Injury of blood vessels at ankle and foot level', 'S9Z'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with walking', 'Tendon rupture', 'Plantar fasciitis', 'Tenderness', 'Swelling', 'Inability to stand on toes'], 'Injury of muscle, fascia and tendon at ankle and foot level', 'S96'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Crushing deformity', 'Mangling injury', 'Vascular compromise', 'Nerve damage'], 'Crushing injury of ankle, foot and toes', 'S97'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of foot/toes', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of ankle, foot and toes', 'S98'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle pain', 'Foot pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of ankle, foot and toes', 'S99']
]

sectionT = [

    # T00-T07: Injuries involving multiple body regions
    ['Worldwide', ['blunt-trauma', 'sharp-trauma', 'fall'], 'Mechanical', ['pain', 'swelling', 'bleeding', 'bruising', 'laceration', 'loss-of-function'], 'Superficial injuries involving multiple body regions', 'T00'],
    ['Worldwide', ['sharp-trauma', 'penetration', 'fall'], 'Mechanical', ['bleeding', 'pain', 'open-wound', 'tissue-damage', 'infection-risk', 'laceration'], 'Open wounds involving multiple body regions', 'T01'],
    ['Worldwide', ['blunt-trauma', 'high-impact', 'fall'], 'Mechanical', ['severe-pain', 'deformity', 'swelling', 'loss-of-function', 'crepitus', 'bruising'], 'Fractures involving multiple body regions', 'T02'],
    ['Worldwide', ['twisting-force', 'sudden-impact', 'overextension'], 'Mechanical', ['pain', 'swelling', 'joint-instability', 'limited-motion', 'bruising', 'popping-sensation'], 'Dislocations, sprains and strains involving multiple body regions', 'T03'],
    ['Worldwide', ['compression', 'heavy-impact', 'machinery-accident'], 'Mechanical', ['severe-pain', 'swelling', 'bruising', 'compartment-syndrome', 'tissue-necrosis', 'numbness'], 'Crushing injuries involving multiple body regions', 'T04'],
    ['Worldwide', ['sharp-trauma', 'avulsion', 'machinery-accident'], 'Mechanical', ['missing-limb', 'severe-bleeding', 'pain', 'shock', 'stump-trauma', 'infection-risk'], 'Traumatic amputations involving multiple body regions', 'T05'],
    ['Worldwide', ['blunt-trauma', 'penetration', 'varied-trauma'], 'Mechanical', ['pain', 'bleeding', 'nerve-damage', 'vessel-damage', 'internal-injury', 'swelling'], 'Other injuries involving multiple body regions', 'T06'],
    ['Worldwide', ['unspecified-trauma', 'severe-accident', 'catastrophe'], 'Mechanical', ['multiple-injuries', 'pain', 'bleeding', 'shock', 'unconsciousness', 'systemic-failure'], 'Unspecified multiple injuries', 'T07'],

    # T08-T14: Injuries to unspecified part of trunk, limb or body region
    ['Worldwide', ['fall', 'blunt-trauma', 'high-impact'], 'Mechanical', ['back-pain', 'numbness', 'tingling', 'paralysis', 'loss-of-function', 'swelling'], 'Fracture of spine, level unspecified', 'T08'],
    ['Worldwide', ['blunt-trauma', 'twisting-force', 'penetration'], 'Mechanical', ['back-pain', 'chest-pain', 'abdominal-pain', 'bruising', 'swelling', 'limited-motion'], 'Other injuries of spine and trunk, level unspecified', 'T09'],
    ['Worldwide', ['fall', 'blunt-trauma', 'direct-impact'], 'Mechanical', ['arm-pain', 'swelling', 'deformity', 'loss-of-function', 'bruising', 'crepitus'], 'Fracture of upper limb, level unspecified', 'T10'],
    ['Worldwide', ['fall', 'laceration', 'overextension'], 'Mechanical', ['arm-pain', 'swelling', 'bruising', 'bleeding', 'numbness', 'limited-motion'], 'Other injuries of upper limb, level unspecified', 'T11'],
    ['Worldwide', ['fall', 'blunt-trauma', 'high-impact'], 'Mechanical', ['leg-pain', 'swelling', 'deformity', 'inability-to-walk', 'bruising', 'crepitus'], 'Fracture of lower limb, level unspecified', 'T12'],
    ['Worldwide', ['fall', 'laceration', 'twisting-force'], 'Mechanical', ['leg-pain', 'swelling', 'bruising', 'bleeding', 'numbness', 'limited-motion'], 'Other injuries of lower limb, level unspecified', 'T13'],
    ['Worldwide', ['unspecified-trauma', 'accident', 'impact'], 'Mechanical', ['pain', 'swelling', 'bruising', 'laceration', 'bleeding', 'loss-of-function'], 'Injury of unspecified body region', 'T14'],

    # T15-T19: Effects of foreign body entering through natural orifice
    ['Worldwide', ['insertion', 'environmental-exposure', 'accident'], 'Foreign Body', ['eye-pain', 'irritation', 'redness', 'tearing', 'blurred-vision', 'scratchiness'], 'Foreign body on external eye', 'T15'],
    ['Worldwide', ['insertion', 'accident', 'q-tip-use'], 'Foreign Body', ['ear-pain', 'hearing-loss', 'fullness-sensation', 'dizziness', 'bleeding', 'tinnitus'], 'Foreign body in ear', 'T16'],
    ['Worldwide', ['inhalation', 'aspiration', 'choking'], 'Foreign Body', ['coughing', 'wheezing', 'choking', 'shortness-of-breath', 'cyanosis', 'chest-pain'], 'Foreign body in respiratory tract', 'T17'],
    ['Worldwide', ['ingestion', 'swallowing', 'accident'], 'Foreign Body', ['difficulty-swallowing', 'abdominal-pain', 'vomiting', 'choking', 'drooling', 'chest-pain'], 'Foreign body in alimentary tract', 'T18'],
    ['Worldwide', ['insertion', 'accident', 'retained-object'], 'Foreign Body', ['pain', 'bleeding', 'urinary-obstruction', 'discharge', 'infection', 'discomfort'], 'Foreign body in genitourinary tract', 'T19'],

    # T20-T32: Burns and corrosions
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'electrical-current'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'facial-edema'], 'Burn and corrosion of head, face, and neck', 'T20'],
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'scald'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'tissue-damage'], 'Burn and corrosion of trunk', 'T21'],
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'scald'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'loss-of-function'], 'Burn and corrosion of shoulder and upper limb, except wrist and hand', 'T22'],
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'electrical-contact'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'reduced-dexterity'], 'Burn and corrosion of wrist and hand', 'T23'],
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'scald'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'difficulty-walking'], 'Burn and corrosion of hip and lower limb, except ankle and foot', 'T24'],
    ['Worldwide', ['heat-exposure', 'chemical-contact', 'scald'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'difficulty-walking'], 'Burn and corrosion of ankle and foot', 'T25'],
    ['Worldwide', ['chemical-splash', 'heat-exposure', 'radiation'], 'Thermal/Chemical', ['eye-pain', 'vision-loss', 'redness', 'tearing', 'light-sensitivity', 'corneal-ulcer'], 'Burn and corrosion confined to eye and adnexa', 'T26'],
    ['Worldwide', ['smoke-inhalation', 'hot-gas-inhalation', 'chemical-fumes'], 'Thermal/Chemical', ['shortness-of-breath', 'coughing', 'wheezing', 'hoarseness', 'soot-in-mouth', 'chest-pain'], 'Burn and corrosion of respiratory tract', 'T27'],
    ['Worldwide', ['caustic-ingestion', 'acid-ingestion', 'severe-trauma'], 'Thermal/Chemical', ['abdominal-pain', 'nausea', 'vomiting', 'bleeding', 'difficulty-swallowing', 'shock'], 'Burn and corrosion of other internal organs', 'T28'],
    ['Worldwide', ['fire', 'explosion', 'large-chemical-spill'], 'Thermal/Chemical', ['widespread-pain', 'large-area-blistering', 'shock', 'hypothermia', 'fluid-loss', 'infection-risk'], 'Burns and corrosions of multiple body regions', 'T29'],
    ['Worldwide', ['fire', 'chemical-spill', 'scald'], 'Thermal/Chemical', ['pain', 'redness', 'blistering', 'swelling', 'charred-skin', 'tissue-damage'], 'Burn and corrosion, body region unspecified', 'T30'],
    ['Worldwide', ['fire', 'explosion', 'scald'], 'Thermal', ['large-area-burn', 'systemic-shock', 'hypothermia', 'infection-risk', 'fluid-loss', 'organ-failure-risk'], 'Burns classified according to extent of body surface involved', 'T31'],
    ['Worldwide', ['chemical-spill', 'industrial-accident', 'assault'], 'Chemical', ['large-area-chemical-burn', 'deep-tissue-necrosis', 'systemic-toxicity', 'fluid-loss', 'shock', 'infection-risk'], 'Corrosions classified according to extent of body surface involved', 'T32'],

    # T33-T35: Frostbite
    ['Cold Climates', ['cold-exposure', 'wind-chill', 'wet-conditions'], 'Thermal', ['numbness', 'tingling', 'white-skin', 'waxy-skin', 'itching', 'redness'], 'Superficial frostbite', 'T33'],
    ['Cold Climates', ['prolonged-cold-exposure', 'severe-wind-chill', 'wet-conditions'], 'Thermal', ['hard-frozen-tissue', 'black-skin', 'blistering', 'severe-pain-on-rewarming', 'loss-of-sensation', 'tissue-loss'], 'Frostbite with tissue necrosis', 'T34'],
    ['Cold Climates', ['prolonged-cold-exposure', 'immersion', 'severe-weather'], 'Thermal', ['widespread-numbness', 'multiple-areas-affected', 'hard-frozen-tissue', 'systemic-hypothermia', 'blistering', 'mottled-skin'], 'Frostbite involving multiple body regions and unspecified frostbite', 'T35'],

    # T36-T50: Poisoning by drugs, medicaments and biological substances
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['rash', 'nausea', 'diarrhea', 'anaphylaxis', 'dizziness', 'fever'], 'Poisoning by systemic antibiotics', 'T36'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['nausea', 'vomiting', 'headache', 'dizziness', 'rash', 'seizures'], 'Poisoning by other systemic anti-infectives and antiparasitics', 'T37'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['nausea', 'vomiting', 'headache', 'fluid-retention', 'mood-changes', 'weakness'], 'Poisoning by hormones and their synthetic substitutes and antagonists, NEC', 'T38'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['nausea', 'vomiting', 'abdominal-pain', 'tinnitus', 'drowsiness', 'metabolic-acidosis'], 'Poisoning by nonopioid analgesics, antipyretics and antirheumatics', 'T39'],
    ['Worldwide', ['ingestion', 'overdose', 'injection'], 'Poisoning', ['respiratory-depression', 'pinpoint-pupils', 'sedation', 'confusion', 'hallucinations', 'coma'], 'Poisoning by narcotics and psychodysleptics [hallucinogens]', 'T40'],
    ['Worldwide', ['inhalation', 'overdose', 'iatrogenic'], 'Poisoning', ['drowsiness', 'confusion', 'unconsciousness', 'low-blood-pressure', 'slow-breathing', 'nausea'], 'Poisoning by anesthetics and therapeutic gases', 'T41'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['drowsiness', 'slurred-speech', 'ataxia', 'confusion', 'respiratory-depression', 'coma'], 'Poisoning by antiepileptic, sedative-hypnotic and antiparkinsonism drugs', 'T42'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['drowsiness', 'agitation', 'tachycardia', 'seizures', 'dry-mouth', 'blurred-vision'], 'Poisoning by psychotropic drugs, NEC', 'T43'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['dry-mouth', 'blurred-vision', 'tachycardia', 'urinary-retention', 'confusion', 'flushing'], 'Poisoning by drugs primarily affecting the autonomic nervous system', 'T44'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['bleeding', 'bruising', 'weakness', 'pallor', 'nausea', 'headache'], 'Poisoning by primarily systemic and hematological agents, NEC', 'T45'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['bradycardia', 'hypotension', 'arrhythmia', 'dizziness', 'syncope', 'chest-pain'], 'Poisoning by agents primarily affecting the cardiovascular system', 'T46'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['nausea', 'vomiting', 'diarrhea', 'abdominal-cramps', 'dehydration', 'electrolyte-imbalance'], 'Poisoning by agents primarily affecting the gastrointestinal system', 'T47'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['muscle-weakness', 'respiratory-distress', 'shortness-of-breath', 'paralysis', 'wheezing', 'cough'], 'Poisoning by agents primarily acting on smooth and skeletal muscles and the respiratory system', 'T48'],
    ['Worldwide', ['skin-contact', 'ingestion', 'overdose'], 'Poisoning', ['skin-irritation', 'rash', 'burning-sensation', 'nausea', 'vomiting', 'dizziness'], 'Poisoning by topical agents primarily affecting skin and mucous membrane and by ophthalmological, otorhinolaryngological and dental drugs', 'T49'],
    ['Worldwide', ['ingestion', 'overdose', 'iatrogenic'], 'Poisoning', ['dehydration', 'electrolyte-imbalance', 'dizziness', 'weakness', 'hypotension', 'muscle-cramps'], 'Poisoning by diuretics and other and unspecified drugs, medicaments and biological substances', 'T50'],

    # T51-T65: Toxic effects of substances chiefly nonmedicinal as to source
    ['Worldwide', ['ingestion', 'binge-drinking', 'chronic-use'], 'Toxic Effect', ['slurred-speech', 'ataxia', 'nausea', 'vomiting', 'sedation', 'respiratory-depression'], 'Toxic effect of alcohol', 'T51'],
    ['Worldwide', ['inhalation', 'skin-contact', 'ingestion'], 'Toxic Effect', ['dizziness', 'headache', 'nausea', 'confusion', 'skin-irritation', 'respiratory-irritation'], 'Toxic effect of organic solvents', 'T52'],
    ['Worldwide', ['inhalation', 'ingestion', 'skin-contact'], 'Toxic Effect', ['drowsiness', 'headache', 'liver-damage', 'kidney-damage', 'nausea', 'confusion'], 'Toxic effect of halogen derivatives of aliphatic and aromatic hydrocarbons', 'T53'],
    ['Worldwide', ['ingestion', 'skin-contact', 'inhalation'], 'Toxic Effect', ['severe-pain', 'burns-to-mouth', 'drooling', 'difficulty-swallowing', 'abdominal-pain', 'vomiting-blood'], 'Toxic effect of corrosive substances', 'T54'],
    ['Worldwide', ['ingestion', 'eye-contact', 'skin-contact'], 'Toxic Effect', ['nausea', 'vomiting', 'diarrhea', 'skin-irritation', 'eye-irritation', 'coughing'], 'Toxic effect of soaps and detergents', 'T55'],
    ['Worldwide', ['ingestion', 'inhalation', 'skin-contact'], 'Toxic Effect', ['nausea', 'vomiting', 'abdominal-pain', 'headache', 'neuropathy', 'kidney-damage'], 'Toxic effect of metals', 'T56'],
    ['Worldwide', ['ingestion', 'inhalation', 'skin-contact'], 'Toxic Effect', ['nausea', 'vomiting', 'headache', 'dizziness', 'respiratory-distress', 'skin-irritation'], 'Toxic effect of other inorganic substances', 'T57'],
    ['Worldwide', ['inhalation', 'incomplete-combustion', 'enclosed-space'], 'Toxic Effect', ['headache', 'dizziness', 'nausea', 'weakness', 'chest-pain', 'confusion'], 'Toxic effect of carbon monoxide', 'T58'],
    ['Worldwide', ['inhalation', 'industrial-exposure', 'fire'], 'Toxic Effect', ['coughing', 'shortness-of-breath', 'eye-irritation', 'headache', 'nausea', 'dizziness'], 'Toxic effect of other gases, fumes and vapors', 'T59'],
    ['Worldwide', ['ingestion', 'skin-contact', 'inhalation'], 'Toxic Effect', ['nausea', 'vomiting', 'diarrhea', 'salivation', 'sweating', 'muscle-twitching'], 'Toxic effect of pesticides', 'T60'],
    ['Worldwide', ['ingestion', 'contaminated-seafood', 'marine-toxins'], 'Toxic Effect', ['nausea', 'vomiting', 'diarrhea', 'abdominal-cramps', 'numbness', 'tingling'], 'Toxic effect of noxious substances eaten as seafood', 'T61'],
    ['Worldwide', ['ingestion', 'food-poisoning', 'contamination'], 'Toxic Effect', ['nausea', 'vomiting', 'diarrhea', 'abdominal-pain', 'fever', 'headache'], 'Toxic effect of other noxious substances eaten as food', 'T62'],
    ['Worldwide', ['bite', 'sting', 'envenomation'], 'Toxic Effect', ['localized-pain', 'swelling', 'redness', 'nausea', 'muscle-weakness', 'anaphylaxis'], 'Toxic effect of contact with venomous animals', 'T63'],
    ['Worldwide', ['ingestion', 'contaminated-food', 'mold'], 'Toxic Effect', ['jaundice', 'abdominal-pain', 'nausea', 'vomiting', 'liver-failure', 'ascites'], 'Toxic effect of aflatoxin and other mycotoxin food contaminants', 'T64'],
    ['Worldwide', ['ingestion', 'inhalation', 'skin-contact'], 'Toxic Effect', ['nausea', 'vomiting', 'dizziness', 'headache', 'confusion', 'organ-damage'], 'Toxic effect of other and unspecified substances', 'T65'],

    # T66-T78: Other and unspecified effects of external causes
    ['Worldwide', ['radiation-exposure', 'nuclear-accident', 'radiotherapy'], 'External Cause Effect', ['nausea', 'vomiting', 'fatigue', 'hair-loss', 'skin-burns', 'immunosuppression'], 'Unspecified effects of radiation', 'T66'],
    ['Worldwide', ['heat-exposure', 'sun-exposure', 'hot-environment'], 'External Cause Effect', ['fatigue', 'dizziness', 'muscle-cramps', 'headache', 'nausea', 'syncope'], 'Effects of heat and light', 'T67'],
    ['Worldwide', ['cold-exposure', 'immersion', 'inadequate-clothing'], 'External Cause Effect', ['shivering', 'confusion', 'drowsiness', 'slurred-speech', 'weak-pulse', 'slow-breathing'], 'Hypothermia', 'T68'],
    ['Worldwide', ['cold-exposure', 'cold-object-contact', 'wind-chill'], 'External Cause Effect', ['numbness', 'tingling', 'skin-discoloration', 'pain', 'swelling', 'blisters'], 'Other effects of reduced temperature', 'T69'],
    ['Worldwide', ['diving', 'aviation', 'decompression'], 'External Cause Effect', ['joint-pain', 'dizziness', 'ear-pain', 'fatigue', 'shortness-of-breath', 'paralysis'], 'Effects of air pressure and water pressure', 'T70'],
    ['Worldwide', ['suffocation', 'strangulation', 'drowning'], 'External Cause Effect', ['shortness-of-breath', 'gasping', 'loss-of-consciousness', 'cyanosis', 'chest-pain', 'confusion'], 'Asphyxiation', 'T71'],
    # T72 is not a valid code
    ['Worldwide', ['starvation', 'dehydration', 'neglect'], 'External Cause Effect', ['hunger', 'thirst', 'fatigue', 'weakness', 'dizziness', 'weight-loss'], 'Effects of other deprivation', 'T73'],
    ['Worldwide', ['abuse', 'neglect', 'violence'], 'External Cause Effect', ['unexplained-injuries', 'bruises', 'burns', 'fractures', 'malnutrition', 'developmental-delay'], 'Maltreatment syndromes', 'T74'],
    ['Worldwide', ['vibration', 'motion-sickness', 'lightning-strike'], 'External Cause Effect', ['dizziness', 'nausea', 'headache', 'tinnitus', 'fatigue', 'anxiety'], 'Effects of other external causes', 'T75'],
    ['Worldwide', ['abuse', 'neglect', 'assault'], 'External Cause Effect', ['fear', 'anxiety', 'depression', 'physical-injuries', 'withdrawal', 'behavioral-changes'], 'Certain specified adult and child abuse, neglect and other maltreatment, suspected', 'T76'],
    # T77 is not a valid code
    ['Worldwide', ['allergy', 'hypersensitivity', 'anaphylaxis'], 'External Cause Effect', ['rash', 'hives', 'itching', 'swelling', 'dizziness', 'shortness-of-breath'], 'Adverse effects, not elsewhere classified', 'T78'],

    # T79: Certain early complications of trauma
    ['Worldwide', ['severe-trauma', 'crush-injury', 'major-surgery'], 'Complication', ['shock', 'hemorrhage', 'fat-embolism', 'infection', 'crush-syndrome', 'compartment-syndrome'], 'Certain early complications of trauma, NEC', 'T79'],

    # T80-T88: Complications of surgical and medical care
    ['Worldwide', ['iatrogenic', 'infusion', 'transfusion'], 'Complication', ['fever', 'chills', 'rash', 'hypotension', 'infection', 'phlebitis'], 'Complications following infusion, transfusion and therapeutic injection', 'T80'],
    ['Worldwide', ['iatrogenic', 'surgery', 'procedure'], 'Complication', ['bleeding', 'infection', 'hematoma', 'wound-dehiscence', 'shock', 'organ-damage'], 'Complications of procedures, NEC', 'T81'],
    ['Worldwide', ['iatrogenic', 'implant', 'graft'], 'Complication', ['infection', 'thrombosis', 'hemorrhage', 'device-failure', 'pain', 'embolism'], 'Complications of cardiac and vascular prosthetic devices, implants and grafts', 'T82'],
    ['Worldwide', ['iatrogenic', 'implant', 'catheter'], 'Complication', ['infection', 'pain', 'urinary-obstruction', 'device-erosion', 'hematuria', 'device-failure'], 'Complications of genitourinary prosthetic devices, implants and grafts', 'T83'],
    ['Worldwide', ['iatrogenic', 'implant', 'joint-replacement'], 'Complication', ['infection', 'pain', 'joint-stiffness', 'device-loosening', 'dislocation', 'fracture'], 'Complications of internal orthopedic prosthetic devices, implants and grafts', 'T84'],
    ['Worldwide', ['iatrogenic', 'implant', 'pacemaker'], 'Complication', ['infection', 'pain', 'device-failure', 'device-migration', 'bleeding', 'obstruction'], 'Complications of other internal prosthetic devices, implants and grafts', 'T85'],
    ['Worldwide', ['transplant', 'immunosuppression', 'graft'], 'Complication', ['fever', 'tenderness-at-site', 'fatigue', 'organ-dysfunction', 'swelling', 'malaise'], 'Failure and rejection of transplanted organs and tissues', 'T86'],
    ['Worldwide', ['surgery', 'amputation', 'reattachment'], 'Complication', ['infection', 'necrosis', 'stump-pain', 'phantom-limb-pain', 'hematoma', 'edema'], 'Complications peculiar to reattachment and amputation', 'T87'],
    ['Worldwide', ['iatrogenic', 'surgery', 'anesthesia'], 'Complication', ['anaphylactic-shock', 'fever', 'hypothermia', 'electrolyte-imbalance', 'malignant-hyperthermia', 'air-embolism'], 'Other complications of surgical and medical care, NEC', 'T88'],

    # T90-T98: Sequelae of injuries, of poisoning and of other consequences of external causes
    ['Worldwide', ['past-trauma', 'head-injury', 'concussion'], 'Sequelae', ['chronic-headache', 'cognitive-deficits', 'seizures', 'dizziness', 'personality-change', 'motor-deficit'], 'Sequelae of injuries of head', 'T90'],
    ['Worldwide', ['past-trauma', 'spinal-injury', 'trunk-injury'], 'Sequelae', ['chronic-pain', 'reduced-mobility', 'paralysis', 'deformity', 'organ-dysfunction', 'neuropathy'], 'Sequelae of injuries of neck and trunk', 'T91'],
    ['Worldwide', ['past-trauma', 'arm-injury', 'fracture'], 'Sequelae', ['chronic-pain', 'stiffness', 'weakness', 'reduced-range-of-motion', 'contracture', 'neuropathy'], 'Sequelae of injuries of upper limb', 'T92'],
    ['Worldwide', ['past-trauma', 'leg-injury', 'fracture'], 'Sequelae', ['chronic-pain', 'gait-disturbance', 'stiffness', 'weakness', 'instability', 'contracture'], 'Sequelae of injuries of lower limb', 'T93'],
    ['Worldwide', ['past-trauma', 'multiple-injuries', 'severe-accident'], 'Sequelae', ['chronic-pain', 'multiple-disabilities', 'reduced-mobility', 'fatigue', 'cognitive-issues', 'psychological-distress'], 'Sequelae of injuries involving multiple and unspecified body regions', 'T94'],
    ['Worldwide', ['past-burn', 'past-frostbite', 'past-corrosion'], 'Sequelae', ['scarring', 'contractures', 'chronic-pain', 'neuropathy', 'loss-of-function', 'disfigurement'], 'Sequelae of burns, corrosions and frostbite', 'T95'],
    ['Worldwide', ['past-poisoning', 'drug-overdose', 'iatrogenic'], 'Sequelae', ['chronic-organ-damage', 'neuropathy', 'cognitive-impairment', 'movement-disorders', 'visual-disturbance', 'addiction'], 'Sequelae of poisoning by drugs, medicaments and biological substances', 'T96'],
    ['Worldwide', ['past-poisoning', 'toxic-exposure', 'environmental-exposure'], 'Sequelae', ['chronic-organ-damage', 'neuropathy', 'cognitive-impairment', 'respiratory-problems', 'skin-conditions', 'cancer'], 'Sequelae of toxic effects of substances chiefly nonmedicinal as to source', 'T97'],
    ['Worldwide', ['past-trauma', 'past-external-cause', 'complication'], 'Sequelae', ['chronic-fatigue', 'chronic-pain', 'psychological-distress', 'organ-dysfunction', 'neurological-deficits', 'reduced-mobility'], 'Sequelae of other and unspecified effects of external causes', 'T98']
]

trauma_symptoms = ["Fracture", "Laceration", "Contusion", "Abrasion", "Concussion", "Internal injury"]
head_trauma_symptoms = ["Head injury", "Fracture", "Laceration", "Concussion", "Traumatic brain injury", "Contusion"]
multi_trauma_symptoms = ["Multiple trauma", "Fracture", "Internal bleeding", "Head injury", "Laceration", "Spinal injury"]
water_symptoms_drown = ["Asphyxiation", "Hypoxia", "Water inhalation", "Hypothermia", "Cardiac arrest", "Loss of consciousness"]
water_symptoms_injury = ["Fracture", "Laceration", "Hypothermia", "Contusion", "Head injury", "Sprain"]
unspecified_symptoms = ["Trauma (unspecified)", "Pain", "Laceration", "Fracture", "Head injury", "Contusion"]

# "Transmission" for transport accidents relates to the mechanism of injury
land_transport_mechanism = ["Collision", "Physical impact", "Kinetic energy transfer"]
water_transport_mechanism = ["Submersion", "Impact", "Environmental exposure"]
air_transport_mechanism = ["High-velocity impact", "Deceleration trauma", "Gravitational force"]
unspecified_mechanism = ["Physical impact", "Trauma", "Unspecified event"]

sectionV = [
    # V01-V09: Pedestrian injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with pedal cycle",
        "ICD_Code": "V01"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V02"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with car, pick-up truck or van",
        "ICD_Code": "V03"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V04"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with railway train or railway vehicle",
        "ICD_Code": "V05"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with other nonmotor vehicle",
        "ICD_Code": "V06"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Pedestrian injured in other and unspecified transport accidents",
        "ICD_Code": "V09"
    },

    # V10-V19: Pedal cyclist injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with pedestrian or animal",
        "ICD_Code": "V10"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with other pedal cycle",
        "ICD_Code": "V11"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V12"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with car, pick-up truck or van",
        "ICD_Code": "V13"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V14"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with railway train or railway vehicle",
        "ICD_Code": "V15"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with other nonmotor vehicle",
        "ICD_Code": "V16"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with fixed or stationary object",
        "ICD_Code": "V17"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in noncollision transport accident",
        "ICD_Code": "V18"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Pedal cyclist injured in other and unspecified transport accidents",
        "ICD_Code": "V19"
    },

    # V20-V29: Motorcycle rider injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with pedestrian or animal",
        "ICD_Code": "V20"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with pedal cycle",
        "ICD_Code": "V21"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V22"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with car, pick-up truck or van",
        "ICD_Code": "V23"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V24"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with railway train or railway vehicle",
        "ICD_Code": "V25"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with other nonmotor vehicle",
        "ICD_Code": "V26"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with fixed or stationary object",
        "ICD_Code": "V27"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in noncollision transport accident",
        "ICD_Code": "V28"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Motorcycle rider injured in other and unspecified transport accidents",
        "ICD_Code": "V29"
    },

    # V30-V39: Occupant of three-wheeled motor vehicle injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with pedestrian or animal",
        "ICD_Code": "V30"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with pedal cycle",
        "ICD_Code": "V31"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V32"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with car, pick-up truck or van",
        "ICD_Code": "V33"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V34"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with railway train or railway vehicle",
        "ICD_Code": "V35"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with other nonmotor vehicle",
        "ICD_Code": "V36"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with fixed or stationary object",
        "ICD_Code": "V37"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in noncollision transport accident",
        "ICD_Code": "V38"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in other and unspecified transport accidents",
        "ICD_Code": "V39"
    },

    # V40-V49: Car occupant injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with pedestrian or animal",
        "ICD_Code": "V40"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with pedal cycle",
        "ICD_Code": "V41"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V42"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with car, pick-up truck or van",
        "ICD_Code": "V43"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Car occupant injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V44"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Car occupant injured in collision with railway train or railway vehicle",
        "ICD_Code": "V45"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with other nonmotor vehicle",
        "ICD_Code": "V46"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with fixed or stationary object",
        "ICD_Code": "V47"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in noncollision transport accident",
        "ICD_Code": "V48"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Car occupant injured in other and unspecified transport accidents",
        "ICD_Code": "V49"
    },

    # V50-V59: Occupant of pick-up truck or van injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with pedestrian or animal",
        "ICD_Code": "V50"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with pedal cycle",
        "ICD_Code": "V51"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V52"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with car, pick-up truck or van",
        "ICD_Code": "V53"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V54"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with railway train or railway vehicle",
        "ICD_Code": "V55"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with other nonmotor vehicle",
        "ICD_Code": "V56"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with fixed or stationary object",
        "ICD_Code": "V57"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in noncollision transport accident",
        "ICD_Code": "V58"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of pick-up truck or van injured in other and unspecified transport accidents",
        "ICD_Code": "V59"
    },

    # V60-V69: Occupant of heavy transport vehicle injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with pedestrian or animal",
        "ICD_Code": "V60"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with pedal cycle",
        "ICD_Code": "V61"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V62"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with car, pick-up truck or van",
        "ICD_Code": "V63"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V64"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with railway train or railway vehicle",
        "ICD_Code": "V65"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with other nonmotor vehicle",
        "ICD_Code": "V66"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with fixed or stationary object",
        "ICD_Code": "V67"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in noncollision transport accident",
        "ICD_Code": "V68"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in other and unspecified transport accidents",
        "ICD_Code": "V69"
    },

    # V70-V79: Bus occupant injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with pedestrian or animal",
        "ICD_Code": "V70"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with pedal cycle",
        "ICD_Code": "V71"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V72"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with car, pick-up truck or van",
        "ICD_Code": "V73"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Bus occupant injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V74"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Bus occupant injured in collision with railway train or railway vehicle",
        "ICD_Code": "V75"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with other nonmotor vehicle",
        "ICD_Code": "V76"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with fixed or stationary object",
        "ICD_Code": "V77"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in noncollision transport accident",
        "ICD_Code": "V78"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Bus occupant injured in other and unspecified transport accidents",
        "ICD_Code": "V79"
    },

    # V80-V89: Other land transport accidents
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Animal-rider or occupant of animal-drawn vehicle injured in transport accident",
        "ICD_Code": "V80"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of railway train or railway vehicle injured in transport accident",
        "ICD_Code": "V81"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of streetcar injured in transport accident",
        "ICD_Code": "V82"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special vehicle mainly used on industrial premises injured in transport accident",
        "ICD_Code": "V83"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special vehicle mainly used in agriculture injured in transport accident",
        "ICD_Code": "V84"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special construction vehicle injured in transport accident",
        "ICD_Code": "V85"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special all-terrain or other motor vehicle designed primarily for off-road use, injured in transport accident",
        "ICD_Code": "V86"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Traffic accident of specified type but victim's mode of transport unknown",
        "ICD_Code": "V87"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Nontraffic accident of specified type but victim's mode of transport unknown",
        "ICD_Code": "V88"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Motor- or nonmotor-vehicle accident, type of vehicle unspecified",
        "ICD_Code": "V89"
    },

    # V90-V94: Water transport accidents
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_drown,
        "Label": "Drowning and submersion due to accident to watercraft",
        "ICD_Code": "V90"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_injury,
        "Label": "Other injury due to accident to watercraft",
        "ICD_Code": "V91"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_drown,
        "Label": "Drowning and submersion due to fall overboard",
        "ICD_Code": "V92"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_injury,
        "Label": "Accident on board watercraft without accident to watercraft, not causing drowning and submersion",
        "ICD_Code": "V93"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other and unspecified water transport accidents",
        "ICD_Code": "V94"
    },

    # V95-V97: Air and space transport accidents
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Accident to powered aircraft causing injury to occupant",
        "ICD_Code": "V95"
    },
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Accident to nonpowered aircraft causing injury to occupant",
        "ICD_Code": "V96"
    },
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other specified air transport accidents",
        "ICD_Code": "V97"
    },

    # V98-V99: Other and unspecified transport accidents
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other specified transport accidents",
        "ICD_Code": "V98"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Unspecified transport accident",
        "ICD_Code": "V99"
    }
]

sectionW = [
    {
        "Geography": "Cold climates / Outdoors",
        "How_the_disease_transmits": ["Slippery surface", "Loss of balance", "Weather condition"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Contusion", "Sprain", "Head injury", "Laceration", "Back pain"],
        "Label": "Fall on same level involving ice and snow",
        "ICD_code": "W00"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Slippery surface", "Uneven ground", "Loss of balance"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Sprain", "Fracture", "Contusion", "Laceration", "Head injury", "Hip fracture"],
        "Label": "Fall on same level from slip, trip and stumble",
        "ICD_code": "W01"
    },
    {
        "Geography": "Worldwide / Recreational areas",
        "How_the_disease_transmits": ["Recreational activity", "Loss of balance", "Equipment failure"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture (wrist/ankle)", "Sprain", "Head injury (concussion)", "Contusion", "Laceration", "Joint dislocation"],
        "Label": "Fall involving ice-skates, skis, roller-skates or skateboards",
        "ICD_code": "W02"
    },
    {
        "Geography": "Worldwide / Public spaces",
        "How_the_disease_transmits": ["Collision with person", "Pushing", "Loss of balance"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Contusion", "Fracture", "Sprain", "Laceration", "Minor head injury", "Fall-related injury"],
        "Label": "Other fall on same level due to collision with, or pushing by, another person",
        "ICD_code": "W03"
    },
    {
        "Geography": "Worldwide / Healthcare / Residential",
        "How_the_disease_transmits": ["Mobility equipment", "Loss of balance", "Transferring patient"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Hip fracture", "Contusion", "Laceration", "Head injury", "Fracture", "Sprain"],
        "Label": "Fall while being carried or supported by other persons",
        "ICD_code": "W04"
    },
    {
        "Geography": "Worldwide / Healthcare / Residential",
        "How_the_disease_transmits": ["Mobility equipment failure", "Loss of balance", "Improper use"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Contusion", "Head injury", "Sprain", "Laceration", "Injury (elderly)"],
        "Label": "Fall involving wheelchair",
        "ICD_code": "W05"
    },
    {
        "Geography": "Worldwide / Residential / Healthcare",
        "How_the_disease_transmits": ["Loss of balance", "Transferring", "Weakness"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Hip fracture", "Contusion", "Head injury", "Fracture", "Laceration", "Back injury"],
        "Label": "Fall involving bed",
        "ICD_code": "W06"
    },
    {
        "Geography": "Worldwide / Residential",
        "How_the_disease_transmits": ["Loss of balance", "Transferring", "Weakness"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Contusion", "Fracture", "Head injury", "Laceration", "Sprain", "Joint injury"],
        "Label": "Fall involving chair",
        "ICD_code": "W07"
    },
    {
        "Geography": "Worldwide / Residential",
        "How_the_disease_transmits": ["Loss of balance", "Transferring", "Slippery surface"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Contusion", "Head injury", "Laceration", "Sprain", "Back injury"],
        "Label": "Fall involving other furniture",
        "ICD_code": "W08"
    },
    {
        "Geography": "Worldwide / Recreational areas",
        "How_the_disease_transmits": ["Recreational activity", "Equipment failure", "Loss of balance"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Head injury (concussion)", "Sprain", "Contusion", "Laceration", "Internal injury"],
        "Label": "Fall involving playground equipment",
        "ICD_code": "W09"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Loss of balance", "Slipping", "Misstep"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Ankle fracture", "Wrist fracture", "Head injury (concussion)", "Contusion", "Back injury", "Sprain"],
        "Label": "Fall on and from stairs and steps",
        "ICD_code": "W10"
    },
    {
        "Geography": "Worldwide / Industrial / Residential",
        "How_the_disease_transmits": ["Loss of balance", "Equipment failure", "Improper use"],
        "Disease_type": "Blunt trauma / Fall from height",
        "Symptoms": ["Fracture (extremity)", "Spinal injury", "Head injury", "Internal injury", "Contusion", "Death"],
        "Label": "Fall on and from ladder",
        "ICD_code": "W11"
    },
    {
        "Geography": "Worldwide / Industrial / Construction",
        "How_the_disease_transmits": ["Loss of balance", "Equipment failure", "Lack of safety harness"],
        "Disease_type": "Blunt trauma / Fall from height",
        "Symptoms": ["Severe fracture", "Spinal cord injury", "Traumatic brain injury", "Internal bleeding", "Polytrauma", "Death"],
        "Label": "Fall on and from scaffolding",
        "ICD_code": "W12"
    },
    {
        "Geography": "Worldwide / Industrial / Residential",
        "How_the_disease_transmits": ["Structural failure", "Loss of balance", "Construction work"],
        "Disease_type": "Blunt trauma / Fall from height",
        "Symptoms": ["Multiple fractures", "Traumatic brain injury", "Spinal injury", "Internal injury", "Pelvic fracture", "Death"],
        "Label": "Fall from, out of or through building or structure",
        "ICD_code": "W13"
    },
    {
        "Geography": "Worldwide / Outdoors / Recreational",
        "How_the_disease_transmits": ["Loss of balance", "Recreational activity", "Misstep"],
        "Disease_type": "Blunt trauma / Fall from height",
        "Symptoms": ["Fracture (ankle/leg)", "Sprain", "Head injury", "Contusion", "Back injury", "Laceration"],
        "Label": "Fall from tree",
        "ICD_code": "W14"
    },
    {
        "Geography": "Worldwide / Outdoors",
        "How_the_disease_transmits": ["Loss of balance", "Uneven terrain", "Recreational activity (hiking)"],
        "Disease_type": "Blunt trauma / Fall from height",
        "Symptoms": ["Severe fracture", "Head injury", "Spinal injury", "Internal injury", "Multiple contusions", "Death"],
        "Label": "Fall from cliff",
        "ICD_code": "W15"
    },
    {
        "Geography": "Worldwide / Industrial / Residential",
        "How_the_disease_transmits": ["Loss of balance", "Entering/exiting", "Structural failure"],
        "Disease_type": "Blunt trauma / Fall into hole",
        "Symptoms": ["Fracture", "Contusion", "Head injury", "Sprain", "Crush injury", "Laceration"],
        "Label": "Fall into, or striking against, hole, shaft or other opening in surface",
        "ICD_code": "W16"
    },
    {
        "Geography": "Worldwide / Recreational / Transport",
        "How_the_disease_transmits": ["Loss of balance", "Sudden stop", "Jumping"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Head injury", "Contusion", "Internal injury", "Laceration", "Sprain"],
        "Label": "Other fall from one level to another",
        "ICD_code": "W17"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Loss of balance", "Tripping", "Misstep"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture (wrist/hip)", "Contusion", "Sprain", "Head injury", "Laceration", "Joint dislocation"],
        "Label": "Other fall on same level",
        "ICD_code": "W18"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Loss of balance", "Unknown cause", "Unwitnessed event"],
        "Disease_type": "Blunt trauma / Fall",
        "Symptoms": ["Fracture", "Head injury", "Contusion", "Sprain", "Laceration", "Internal injury"],
        "Label": "Unspecified fall",
        "ICD_code": "W19"
    },
    {
        "Geography": "Worldwide / Industrial / Outdoors",
        "How_the_disease_transmits": ["Falling object", "Projected object", "Gravity"],
        "Disease_type": "Impact trauma / Blunt or Penetrating",
        "Symptoms": ["Head injury (concussion)", "Fracture", "Laceration", "Contusion", "Eye injury", "Internal injury"],
        "Label": "Struck by thrown, projected or falling object",
        "ICD_code": "W20"
    },
    {
        "Geography": "Worldwide / Recreational areas",
        "How_the_disease_transmits": ["Sporting activity", "Collision", "Improper use"],
        "Disease_type": "Impact trauma / Blunt",
        "Symptoms": ["Contusion", "Fracture", "Sprain", "Head injury (concussion)", "Laceration", "Joint dislocation"],
        "Label": "Striking against or struck by sports equipment",
        "ICD_code": "W21"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Collision", "Misjudging space", "Walking into object"],
        "Disease_type": "Impact trauma / Blunt",
        "Symptoms": ["Contusion", "Laceration", "Fracture (e.g., toe)", "Head injury (minor)", "Sprain", "Bruising"],
        "Label": "Striking against or struck by other objects",
        "ICD_code": "W22"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Caught in machinery", "Hair entanglement", "Clothing entanglement"],
        "Disease_type": "Crush injury / Avulsion / Amputation",
        "Symptoms": ["Avulsion (scalp)", "Amputation (finger/limb)", "Laceration", "Fracture", "Crush syndrome", "Degloving injury"],
        "Label": "Caught, crushed, jammed or pinched in or between objects",
        "ICD_code": "W23"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Contact with sharp edge", "Handling object", "Accident"],
        "Disease_type": "Penetrating trauma / Laceration",
        "Symptoms": ["Laceration", "Bleeding", "Tendon damage", "Nerve damage", "Infection risk", "Puncture wound"],
        "Label": "Contact with lifting and transmission devices, not elsewhere classified",
        "ICD_code": "W24"
    },
    {
        "Geography": "Worldwide / Residential / Industrial",
        "How_the_disease_transmits": ["Contact with sharp object", "Improper handling", "Breakage"],
        "Disease_type": "Penetrating trauma / Laceration",
        "Symptoms": ["Laceration", "Bleeding", "Puncture wound", "Tendon damage", "Nerve damage", "Infection risk"],
        "Label": "Contact with sharp glass",
        "ICD_code": "W25"
    },
    {
        "Geography": "Worldwide / Residential / Industrial",
        "How_the_disease_transmits": ["Contact with sharp object", "Tool use", "Kitchen accident"],
        "Disease_type": "Penetrating trauma / Laceration",
        "Symptoms": ["Laceration (finger/hand)", "Bleeding", "Puncture wound", "Tendon injury", "Nerve injury", "Infection risk"],
        "Label": "Contact with knife, sword or dagger",
        "ICD_code": "W26"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Contact with sharp object", "Tool use", "Gardening"],
        "Disease_type": "Penetrating trauma / Laceration",
        "Symptoms": ["Laceration", "Puncture wound", "Bleeding", "Tendon injury", "Infection risk", "Amputation (finger)"],
        "Label": "Contact with non-powered hand tools",
        "ICD_code": "W27"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Contact with moving part", "Tool use", "Gardening"],
        "Disease_type": "Trauma / Laceration / Amputation",
        "Symptoms": ["Laceration", "Amputation (finger/toe)", "Fracture", "Bleeding", "Avulsion", "Crush injury"],
        "Label": "Contact with lawn-mower",
        "ICD_code": "W28"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Contact with moving part", "Tool use", "Workshop accident"],
        "Disease_type": "Trauma / Laceration / Amputation",
        "Symptoms": ["Laceration", "Amputation (finger)", "Puncture wound", "Bleeding", "Fracture", "Eye injury (projectile)"],
        "Label": "Contact with other powered hand tools and household machinery",
        "ICD_code": "W29"
    },
    {
        "Geography": "Worldwide / Industrial / Farm",
        "How_the_disease_transmits": ["Contact with moving part", "Occupational hazard", "Entanglement"],
        "Disease_type": "Trauma / Crush / Amputation",
        "Symptoms": ["Amputation (limb)", "Crush injury", "Severe laceration", "Fracture", "Degloving injury", "Polytrauma"],
        "Label": "Contact with agricultural machinery",
        "ICD_code": "W30"
    },
    {
        "Geography": "Worldwide / Industrial",
        "How_the_disease_transmits": ["Contact with moving part", "Occupational hazard", "Entanglement"],
        "Disease_type": "Trauma / Crush / Amputation",
        "Symptoms": ["Amputation (finger/limb)", "Crush injury", "Severe laceration", "Fracture", "Avulsion", "Polytrauma"],
        "Label": "Contact with other and unspecified machinery",
        "ICD_code": "W31"
    },
    {
        "Geography": "Worldwide",
        "How_the_disease_transmits": ["Equipment failure", "Overpressure", "Malfunction"],
        "Disease_type": "Penetrating trauma / Blast injury",
        "Symptoms": ["Laceration", "Puncture wound", "Burn", "Fracture", "Foreign body", "Tinnitus"],
        "Label": "Accidental non-explosive rupture of firearm",
        "ICD_code": "W32"
    },
    {
        "Geography": "Worldwide",
        "How_the_disease_transmits": ["Accidental discharge", "Improper handling", "Hunting accident"],
        "Disease_type": "Penetrating trauma / Gunshot wound",
        "Symptoms": ["Gunshot wound", "Severe bleeding", "Internal injury", "Fracture", "Shock", "Death"],
        "Label": "Accidental rifle, shotgun and larger firearm discharge",
        "ICD_code": "W33"
    },
    {
        "Geography": "Worldwide",
        "How_the_disease_transmits": ["Accidental discharge", "Improper handling", "Cleaning firearm"],
        "Disease_type": "Penetrating trauma / Gunshot wound",
        "Symptoms": ["Gunshot wound", "Bleeding", "Internal injury", "Fracture", "Nerve damage", "Shock"],
        "Label": "Accidental discharge from other and unspecified firearms",
        "ICD_code": "W34"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Explosion", "Chemical reaction", "Overpressure"],
        "Disease_type": "Blast injury / Burn / Trauma",
        "Symptoms": ["Burn", "Laceration", "Fracture", "Tinnitus", "Puncture wound (shrapnel)", "Internal injury"],
        "Label": "Explosion and rupture of boiler",
        "ICD_code": "W35"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Explosion", "Overpressure", "Equipment failure"],
        "Disease_type": "Blast injury / Burn / Trauma",
        "Symptoms": ["Burn", "Laceration", "Fracture", "Eye injury", "Tinnitus", "Contusion"],
        "Label": "Explosion and rupture of gas cylinder",
        "ICD_code": "W36"
    },
    {
        "Geography": "Worldwide / Home / Automotive",
        "How_the_disease_transmits": ["Explosion", "Overpressure", "Equipment failure"],
        "Disease_type": "Blast injury / Burn / Chemical",
        "Symptoms": ["Burn (thermal/chemical)", "Laceration", "Fracture", "Eye injury", "Contusion", "Hearing loss"],
        "Label": "Explosion and rupture of pressurized tire, pipe or hose",
        "ICD_code": "W37"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Explosion", "Overpressure", "Malfunction"],
        "Disease_type": "Blast injury / Burn / Trauma",
        "Symptoms": ["Burn", "Laceration (shrapnel)", "Fracture", "Tinnitus", "Contusion", "Internal injury"],
        "Label": "Explosion and rupture of other specified pressurized devices",
        "ICD_code": "W38"
    },
    {
        "Geography": "Worldwide / Recreational",
        "How_the_disease_transmits": ["Explosion", "Improper handling", "Malfunction"],
        "Disease_type": "Blast injury / Burn / Amputation",
        "Symptoms": ["Burn (hand/face)", "Amputation (finger)", "Laceration", "Eye injury", "Tinnitus", "Fracture"],
        "Label": "Accidental discharge of fireworks",
        "ICD_code": "W39"
    },
    {
        "Geography": "Worldwide / Industrial / Military",
        "How_the_disease_transmits": ["Explosion", "Occupational hazard", "Accident"],
        "Disease_type": "Blast injury / Polytrauma",
        "Symptoms": ["Polytrauma", "Amputation (limb)", "Severe burns", "Internal injury", "Tinnitus / Hearing loss", "Traumatic brain injury"],
        "Label": "Explosion of blasting materials",
        "ICD_code": "W40"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Explosion", "Chemical reaction", "Improper storage"],
        "Disease_type": "Blast injury / Burn / Chemical",
        "Symptoms": ["Burn (chemical/thermal)", "Laceration", "Eye injury", "Respiratory distress", "Fracture", "Tinnitus"],
        "Label": "Explosion of other materials",
        "ICD_code": "W41"
    },
    {
        "Geography": "Worldwide / Industrial / Recreational",
        "How_the_disease_transmits": ["High-pressure contact", "Equipment failure", "Accident"],
        "Disease_type": "Penetrating trauma / Injection",
        "Symptoms": ["Puncture wound", "Severe pain", "Swelling", "Tissue necrosis", "Compartment syndrome", "Foreign body"],
        "Label": "Exposure to high pressure jet",
        "ICD_code": "W42"
    },
    {
        "Geography": "Worldwide / Industrial",
        "How_the_disease_transmits": ["Noise exposure", "Occupational hazard", "Lack of protection"],
        "Disease_type": "Hearing loss / Auditory",
        "Symptoms": ["Hearing loss (gradual/sudden)", "Tinnitus", "Hyperacusis", "Acoustic trauma", "Ear pain", "Vertigo"],
        "Label": "Exposure to noise",
        "ICD_code": "W43"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Inhalation", "Ingestion", "Insertion"],
        "Disease_type": "Foreign body / Obstruction",
        "Symptoms": ["Choking", "Coughing", "Wheezing", "Pain", "Dysphagia", "Respiratory distress"],
        "Label": "Foreign body entering into or through eye or natural orifice",
        "ICD_code": "W44"
    },
    {
        "Geography": "Worldwide / Indoors & Outdoors",
        "How_the_disease_transmits": ["Puncture", "Stepping on object", "Accident"],
        "Disease_type": "Penetrating trauma / Foreign body",
        "Symptoms": ["Puncture wound", "Pain", "Bleeding", "Infection risk", "Foreign body sensation", "Laceration"],
        "Label": "Foreign body or object entering through skin",
        "ICD_code": "W45"
    },
    {
        "Geography": "Worldwide / Industrial / Medical",
        "How_the_disease_transmits": ["Accidental puncture", "Tool use", "Medical procedure"],
        "Disease_type": "Penetrating trauma / Puncture",
        "Symptoms": ["Puncture wound", "Bleeding", "Pain", "Infection risk (bloodborne)", "Nerve damage", "Foreign body"],
        "Label": "Contact with hypodermic needle",
        "ICD_code": "W46"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Vibration exposure", "Tool use", "Occupational hazard"],
        "Disease_type": "Neurological / Vascular",
        "Symptoms": ["Numbness (fingers)", "Tingling", "Pain (hand/arm)", "Weakness (grip)", "Raynaud's phenomenon", "Carpal tunnel syndrome"],
        "Label": "Exposure to vibration",
        "ICD_code": "W49"
    },
    {
        "Geography": "Worldwide / Public spaces",
        "How_the_disease_transmits": ["Altercation", "Assault", "Accident"],
        "Disease_type": "Blunt trauma / Laceration / Bite",
        "Symptoms": ["Contusion", "Laceration", "Fracture", "Human bite wound", "Infection risk", "Head injury"],
        "Label": "Hit, struck, kicked, twisted, bitten or scratched by other person",
        "ICD_code": "W50"
    },
    {
        "Geography": "Worldwide / Public spaces",
        "How_the_disease_transmits": ["Accident", "Collision", "Crowd"],
        "Disease_type": "Blunt trauma",
        "Symptoms": ["Contusion", "Sprain", "Fracture", "Laceration", "Minor head injury", "Fall-related injury"],
        "Label": "Striking against or bumped into by another person",
        "ICD_code": "W51"
    },
    {
        "Geography": "Worldwide / Public events",
        "How_the_disease_transmits": ["Crowd surge", "Panic", "Large gathering"],
        "Disease_type": "Crush injury / Asphyxiation",
        "Symptoms": ["Crush injury", "Traumatic asphyxia", "Fracture", "Contusion", "Respiratory distress", "Death"],
        "Label": "Crushed, pushed or stepped on by crowd or human stampede",
        "ICD_code": "W52"
    },
    {
        "Geography": "Worldwide / Urban / Impoverished areas",
        "How_the_disease_transmits": ["Animal bite", "Poor sanitation", "Infestation"],
        "Disease_type": "Animal bite / Infection",
        "Symptoms": ["Puncture wound", "Bleeding", "Infection (e.g., Rat-bite fever)", "Cellulitis", "Swelling", "Pain"],
        "Label": "Bitten by rat",
        "ICD_code": "W53"
    },
    {
        "Geography": "Worldwide / Residential",
        "How_the_disease_transmits": ["Animal bite", "Human interaction", "Provocation"],
        "Disease_type": "Animal bite / Trauma",
        "Symptoms": ["Puncture wound", "Laceration", "Bleeding", "Infection (e.g., Rabies risk)", "Crush injury", "Cellulitis"],
        "Label": "Bitten or struck by dog",
        "ICD_code": "W54"
    },
    {
        "Geography": "Worldwide / Rural / Residential",
        "How_the_disease_transmits": ["Animal bite", "Handling animal", "Provocation"],
        "Disease_type": "Animal bite / Trauma",
        "Symptoms": ["Laceration", "Puncture wound", "Bleeding", "Infection (e.g., Cat-scratch fever)", "Cellulitis", "Rabies risk"],
        "Label": "Bitten or struck by other mammals",
        "ICD_code": "W55"
    },
    {
        "Geography": "Coastal / Marine",
        "How_the_disease_transmits": ["Animal contact", "Sting", "Bite"],
        "Disease_type": "Venom / Trauma / Sting",
        "Symptoms": ["Puncture wound", "Laceration", "Pain (severe)", "Swelling", "Venom reaction (systemic)", "Bleeding"],
        "Label": "Contact with marine animal",
        "ICD_code": "W56"
    },
    {
        "Geography": "Worldwide",
        "How_the_disease_transmits": ["Insect bite", "Insect sting", "Allergic reaction"],
        "Disease_type": "Sting / Bite / Allergic",
        "Symptoms": ["Local swelling", "Itching", "Pain", "Redness", "Anaphylaxis (if allergic)", "Urticaria (hives)"],
        "Label": "Bitten or stung by nonvenomous insect and other nonvenomous arthropods",
        "ICD_code": "W57"
    },
    {
        "Geography": "Tropical / Subtropical",
        "How_the_disease_transmits": ["Animal bite", "Animal attack", "Water activity"],
        "Disease_type": "Animal bite / Trauma",
        "Symptoms": ["Severe laceration", "Amputation", "Crush injury", "Massive bleeding", "Infection (severe)", "Death"],
        "Label": "Bitten or struck by crocodile or alligator",
        "ICD_code": "W58"
    },
    {
        "Geography": "Worldwide",
        "How_the_disease_transmits": ["Animal bite", "Animal handling", "Animal attack"],
        "Disease_type": "Animal bite / Venom",
        "Symptoms": ["Puncture wound", "Laceration", "Pain", "Swelling", "Venom reaction (if venomous)", "Infection risk"],
        "Label": "Bitten or struck by other and unspecified reptiles",
        "ICD_code": "W59"
    },
    {
        "Geography": "Worldwide / Outdoors",
        "How_the_disease_transmits": ["Plant contact", "Gardening", "Hiking"],
        "Disease_type": "Penetrating trauma / Laceration",
        "Symptoms": ["Puncture wound", "Laceration", "Foreign body (spine)", "Infection risk", "Local irritation", "Pain"],
        "Label": "Contact with plant thorns and spines and sharp leaves",
        "ICD_code": "W60"
    },
    {
        "Geography": "Worldwide / Industrial / Farm",
        "How_the_disease_transmits": ["Animal attack", "Handling animal", "Occupational hazard"],
        "Disease_type": "Blunt trauma / Crush",
        "Symptoms": ["Contusion", "Fracture", "Crush injury", "Internal injury", "Laceration", "Head injury"],
        "Label": "Exposure to other and unspecified animate mechanical forces",
        "ICD_code": "W64"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Loss of consciousness", "Slipping", "Unsupervised (child/elderly)"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Pulmonary edema", "Death"],
        "Label": "Drowning and submersion while in bath-tub",
        "ICD_code": "W65"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Fall into object", "Unsupervised (child)", "Accident"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Pulmonary edema", "Death"],
        "Label": "Drowning and submersion after fall into bath-tub",
        "ICD_code": "W66"
    },
    {
        "Geography": "Worldwide / Outdoors / Recreational",
        "How_the_disease_transmits": ["Inability to swim", "Exhaustion", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Hypothermia", "Death"],
        "Label": "Drowning and submersion while in swimming-pool",
        "ICD_code": "W67"
    },
    {
        "Geography": "Worldwide / Outdoors / Recreational",
        "How_the_disease_transmits": ["Fall into water", "Accident", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Hypothermia", "Death"],
        "Label": "Drowning and submersion after fall into swimming-pool",
        "ICD_code": "W68"
    },
    {
        "Geography": "Worldwide / Outdoors / Recreational",
        "How_the_disease_transmits": ["Inability to swim", "Currents", "Boating accident"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Hypothermia", "Death"],
        "Label": "Drowning and submersion while in natural water",
        "ICD_code": "W69"
    },
    {
        "Geography": "Worldwide / Outdoors / Recreational",
        "How_the_disease_transmits": ["Fall into water", "Accident", "Boating accident"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Hypothermia", "Death"],
        "Label": "Drowning and submersion after fall into natural water",
        "ICD_code": "W70"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Fall into object", "Unsupervised (child)", "Accident"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Pulmonary edema", "Death"],
        "Label": "Drowning and submersion while in other specified water",
        "ICD_code": "W73"
    },
    {
        "Geography": "Worldwide / Indoors / Outdoors",
        "How_the_disease_transmits": ["Unknown circumstance", "Unwitnessed event", "Accident"],
        "Disease_type": "Asphyxiation / Drowning",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Pulmonary edema", "Death"],
        "Label": "Drowning and submersion, unspecified",
        "ICD_code": "W74"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Positional asphyxia", "Entanglement", "Unsafe sleep (infant)"],
        "Disease_type": "Asphyxiation / Suffocation",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Cyanosis", "Death"],
        "Label": "Accidental suffocation and strangulation in bed",
        "ICD_code": "W75"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Positional asphyxia", "Entanglement", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Suffocation",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Cyanosis", "Death"],
        "Label": "Other accidental suffocation and strangulation in bed",
        "ICD_code": "W76"
    },
    {
        "Geography": "Worldwide / Industrial / Farm",
        "How_the_disease_transmits": ["Cave-in", "Engulfment", "Silo accident"],
        "Disease_type": "Asphyxiation / Crush",
        "Symptoms": ["Traumatic asphyxia", "Crush injury", "Hypoxia", "Respiratory arrest", "Fracture", "Death"],
        "Label": "Threat to breathing due to cave-in, falling earth or other substances",
        "ICD_code": "W77"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Choking", "Foreign body", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Obstruction",
        "Symptoms": ["Choking", "Coughing", "Stridor", "Respiratory distress", "Hypoxia", "Cardiac arrest"],
        "Label": "Inhalation and ingestion of food causing obstruction of respiratory tract",
        "ICD_code": "W78"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Choking", "Foreign body", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Obstruction",
        "Symptoms": ["Choking", "Coughing", "Wheezing", "Respiratory distress", "Hypoxia", "Cardiac arrest"],
        "Label": "Inhalation and ingestion of other objects causing obstruction of respiratory tract",
        "ICD_code": "W79"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Vomiting", "Reduced consciousness", "Aspiration"],
        "Disease_type": "Asphyxiation / Aspiration",
        "Symptoms": ["Aspiration pneumonitis", "Respiratory distress", "Hypoxia", "Coughing", "Wheezing", "Fever"],
        "Label": "Inhalation of gastric contents",
        "ICD_code": "W80"
    },
    {
        "Geography": "Worldwide / Industrial / Confined space",
        "How_the_disease_transmits": ["Gas leak", "Oxygen displacement", "Occupational hazard"],
        "Disease_type": "Asphyxiation / Hypoxia",
        "Symptoms": ["Hypoxia", "Loss of consciousness", "Headache", "Dizziness", "Brain damage", "Death"],
        "Label": "Inhalation or ingestion of other gas or vapor",
        "ICD_code": "W81"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Plastic bag", "Entrapment", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Suffocation",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Cyanosis", "Death"],
        "Label": "Accidental suffocation by plastic bag",
        "ICD_code": "W83"
    },
    {
        "Geography": "Worldwide / Indoors / Residential",
        "How_the_disease_transmits": ["Entrapment", "Positional asphyxia", "Unsupervised (child)"],
        "Disease_type": "Asphyxiation / Suffocation",
        "Symptoms": ["Hypoxia", "Respiratory arrest", "Cardiac arrest", "Brain damage", "Cyanosis", "Death"],
        "Label": "Other specified threats to breathing",
        "ICD_code": "W84"
    },
    {
        "Geography": "Worldwide / Industrial / Outdoors",
        "How_the_disease_transmits": ["Direct contact", "Arc flash", "Occupational hazard"],
        "Disease_type": "Electrical injury / Burn",
        "Symptoms": ["Electrical burn (entry/exit)", "Cardiac arrhythmia", "Respiratory arrest", "Muscle damage (rhabdomyolysis)", "Neurological damage", "Seizure"],
        "Label": "Exposure to electric transmission lines",
        "ICD_code": "W85"
    },
    {
        "Geography": "Worldwide / Industrial / Home",
        "How_the_disease_transmits": ["Faulty wiring", "Improper handling", "Water contact"],
        "Disease_type": "Electrical injury / Burn",
        "Symptoms": ["Electrical burn", "Cardiac arrhythmia", "Loss of consciousness", "Muscle spasm", "Neurological symptoms", "Fall (secondary)"],
        "Label": "Exposure to other and unspecified electric current",
        "ICD_code": "W86"
    },
    {
        "Geography": "Worldwide / Outdoors",
        "How_the_disease_transmits": ["Weather event", "Direct strike", "Ground current"],
        "Disease_type": "Electrical injury / Burn / Trauma",
        "Symptoms": ["Cardiac arrest", "Respiratory arrest", "Burns (Lichtenberg figures)", "Neurological damage", "Tympanic membrane rupture", "Death"],
        "Label": "Exposure to lightning",
        "ICD_code": "W87"
    },
    {
        "Geography": "Worldwide / Industrial / Medical",
        "How_the_disease_transmits": ["Occupational exposure", "Medical procedure", "Accident"],
        "Disease_type": "Radiation exposure",
        "Symptoms": ["Radiation sickness", "Burns (radiation)", "Nausea", "Vomiting", "Hair loss", "Increased cancer risk"],
        "Label": "Exposure to ionizing radiation",
        "ICD_code": "W88"
    },
    {
        "Geography": "Worldwide / Industrial / Medical",
        "How_the_disease_transmits": ["Occupational exposure", "Sun exposure", "Welding"],
        "Disease_type": "Radiation exposure / Burn",
        "Symptoms": ["Sunburn", "Photokeratitis (welder's flash)", "Skin aging", "Skin cancer risk", "Cataracts", "Heat stroke"],
        "Label": "Exposure to artificial visible and ultraviolet light",
        "ICD_code": "W89"
    },
    {
        "Geography": "Worldwide / Industrial / Medical",
        "How_the_disease_transmits": ["Occupational exposure", "Accident", "Medical device"],
        "Disease_type": "Radiation exposure",
        "Symptoms": ["Burns", "Headache", "Nausea", "Eye damage", "Tissue damage (internal)", "Skin irritation"],
        "Label": "Exposure to other nonionizing radiation",
        "ICD_code": "W90"
    },
    {
        "Geography": "Worldwide / Industrial / Medical",
        "How_the_disease_transmits": ["Occupational exposure", "Accident", "Unknown source"],
        "Disease_type": "Radiation exposure",
        "Symptoms": ["Radiation sickness", "Burns", "Nausea", "Vomiting", "Hair loss", "Increased cancer risk"],
        "Label": "Exposure to unspecified type of radiation",
        "ICD_code": "W91"
    },
    {
        "Geography": "Hot climates / Outdoors",
        "How_the_disease_transmits": ["Environmental exposure", "Dehydration", "Overexertion"],
        "Disease_type": "Heat-related illness",
        "Symptoms": ["Heat stroke", "Heat exhaustion", "Syncope (fainting)", "Dehydration", "Muscle cramps", "Headache"],
        "Label": "Exposure to excessive heat of man-made origin",
        "ICD_code": "W92"
    },
    {
        "Geography": "Cold climates / Outdoors",
        "How_the_disease_transmits": ["Environmental exposure", "Lack of protection", "Immersion"],
        "Disease_type": "Cold-related illness",
        "Symptoms": ["Hypothermia", "Frostbite", "Chilblains", "Shivering (uncontrollable)", "Confusion", "Loss of coordination"],
        "Label": "Exposure to excessive cold of man-made origin",
        "ICD_code": "W93"
    },
    {
        "Geography": "Worldwide / Aviation / Diving",
        "How_the_disease_transmits": ["Rapid ascent/descent", "Environmental change", "Occupational hazard"],
        "Disease_type": "Barotrauma / Decompression",
        "Symptoms": ["Decompression sickness ('the bends')", "Ear pain (barotrauma)", "Vertigo", "Joint pain", "Neurological deficit", "Shortness of breath"],
        "Label": "Exposure to high and low air pressure and changes in air pressure",
        "ICD_code": "W94"
    },
    {
        "Geography": "Worldwide / Industrial / Urban",
        "How_the_disease_transmits": ["Chemical exposure", "Pollution", "Unspecified hazard"],
        "Disease_type": "Environmental exposure",
        "Symptoms": ["Respiratory distress", "Skin irritation", "Toxic effect", "Headache", "Nausea", "Unspecified illness"],
        "Label": "Exposure to other and unspecified man-made environmental factors",
        "ICD_code": "W99"
    }
]

sectionX = [
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

sectionY = [
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
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Cardiovascular"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Hypotension", "Bradycardia", "Cough", "Dizziness", "Electrolyte imbalance", "Arrhythmia"],
        "Label": "Adverse effect of cardiovascular drugs (duplicate, distinct code)",
        "ICD_Code": "Y52"
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
        "Transmission_Mechanism": ["Adverse effect", "Therapeutic use", "Various"],
        "Cause_Type": "Adverse Drug Effect (Therapeutic Use)",
        "Associated_Outcomes": ["Varies", "Rash", "Nausea", "Headache", "Dizziness", "Vomiting"],
        "Label": "Adverse effect of other and unspecified drugs and medicaments",
        "ICD_Code": "Y57"
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

uncommonOrder = [sectionT, sectionO, sectionL, sectionI]
for i in range(len(sectionI)):
    sectionI[i] = {key: sectionI[i][key] for key in ["geography", "transmission", "disease_type", "symptoms", "disease_name", "icd_code"]}
for k in range(len(sectionL)):
    sectionL[k] = {key: sectionL[k][key] for key in ["geography", "transmission", "disease_type", "symptoms", "disease_name", "icd_code"]}
for j in range(len(sectionO)):
    sectionO[j] = {key: sectionO[j][key] for key in ["Geography", "Transmission", "Disease Type", "Symptoms", "Disease Name", "ICD Code"]}

for a in range(len(sectionD)):
    sectionD[a] = sectionD[a].values()
for b in range(len(sectionI)):
    sectionI[b] = sectionI[b].values()
for c in range(len(sectionL)):
    sectionL[c] = sectionL[c].values()
for d in range(len(sectionM)):
    sectionM[d] = sectionM[d].values()
for e in range(len(sectionO)):
    sectionO[e] = sectionO[e].values()
for f in range(len(sectionR)):
    sectionR[f] = sectionR[f].values()
for h in range(len(sectionV)):
    sectionV[h] = sectionV[h].values()
for i in range(len(sectionW)):
    sectionW[i] = sectionW[i].values()
for j in range(len(sectionX)):
    sectionX[j] = sectionX[j].values()
for k in range(len(sectionY)):
    sectionY[k] = sectionY[k].values()

df = pd.DataFrame(columns = columns, data = sectionA + sectionB + sectionC + sectionD + sectionE + sectionF + sectionG + sectionH + sectionI + sectionJ + sectionK + sectionL + sectionM + sectionN + sectionO + sectionP + sectionQ + sectionR + sectionS + sectionT + sectionV + sectionW + sectionX + sectionY)
df.to_csv("NEAtrainset.csv")