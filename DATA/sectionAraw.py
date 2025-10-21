# This Python file contains a synthetic dataset for ICD-10 codes A00-A99
# (Certain infectious and parasitic diseases) intended for AI training.
#
# Structure of each row (list):
# 1. Geography (str): Main area of prominence (Feature 1)
# 2. Transmission (str): Comma-separated list of 3 keywords (Feature 2)
# 3. Disease Type (str): 'bacterial', 'viral', 'parasitic', or 'fungal' (Feature 3)
# 4. Symptoms (str): Comma-separated list of 6 common symptoms (Feature 4)
# 5. Disease Name (str): The Label
# 6. ICD Code (str): The Additional column
#
# NOTE: Codes A10-A14, A29, A45, A47, A61-A62, A72-A73, A76, A85.1, A97 (etc.) are
# generally unused or reserved for future expansion within the three-character category
# or are not primary categories in this range, resulting in 87 rows.

ICD_A00_A99_DATASET = [
    # Header Row
    ['Geography', 'Transmission', 'Disease Type', 'Symptoms', 'Disease Name', 'ICD Code'],

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
