"""
ICD-10 O-Block (O00-O99) Disease Dataset Rows

This list contains 100 rows representing the ICD-10 codes from O00 to O99
(Pregnancy, childbirth, and the puerperium). The data is generalized for
AI training purposes.

Each row is a dictionary with the following structure:
- ICD Code: The generalized ICD-10 code (string).
- Disease Name: The common name for the condition (string).
- Geography: A broad region where the condition is prominent (string).
- Transmission: Key risk factors or transmission pathways (list of 3 strings).
- Disease Type: Categorized as 'Non-infectious', 'Bacterial', 'Viral', etc. (string).
- Symptoms: A list of 6 common associated symptoms (list of 6 strings).
"""

icd_data_rows = [
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

# Example of how to access the first row:
# print(icd_data_rows[0])
# Example of how to access the Disease Name of the 86th row (O85):
# print(icd_data_rows[85]["Disease Name"])
