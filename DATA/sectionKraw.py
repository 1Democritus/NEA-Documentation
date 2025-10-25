# ICD-10 K00-K99 Disease Dataset
# This file contains dataset rows for diseases of the digestive system (ICD-10 Chapter XI).
# Each row contains 6 features:
# 1. Geography: General area where the disease is prominent.
# 2. Transmission (Causative Factors): A list of 3 key factors.
# 3. Disease_Type: The nature of the disease (e.g., Bacterial, Inflammatory, Lifestyle-related).
# 4. Symptoms: A list of 6 common associated symptoms.
# 5. Disease_Name: The label for the disease (based on the ICD-10 block title).
# 6. ICD_Code: The ICD-10 code.

header = ["Geography", "Transmission", "Disease_Type", "Symptoms", "Disease_Name", "ICD_Code"]

disease_data = [
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
