# This Python file contains data rows for ICD-10 codes E00-E99.
# The data is intended for use in training an A.I. model.
#
# Each row is a list with the following 6-column structure:
# 1. Geography (str): General area where the disease is prominent.
# 2. Etiology/Transmission (list[str, str, str]): Keywords for how the disease arises.
#    (Note: Most of these are non-infectious, so "Transmission" is adapted to "Etiology"
#     e.g., "Genetic", "Autoimmune", "Nutritional deficiency".)
# 3. Disease Type (str): The nature of the disease.
#    (Note: The requested "bacterial, viral, etc." types are not applicable to
#     most endocrine/metabolic diseases. I have used more accurate categories
#     like "Endocrine", "Metabolic", "Nutritional", "Autoimmune", "Genetic"
#     to provide better features for A.I. training.)
# 4. Symptoms (list[str, ...]): 6 common associated symptoms.
# 5. Disease Name (str): The common name of the disease (the label).
# 6. ICD Code (str): The ICD-10 code.
#

disease_data = [
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

# Example of how to access the first row (E00):
# print(disease_data[0])
#
# Example of how to access the Disease Name and Symptoms for the first row:
# print(f"Disease: {disease_data[0][4]}")
# print(f"Symptoms: {disease_data[0][3]}")
