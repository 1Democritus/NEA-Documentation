# ICD-10 N00-N99 Disease Dataset Rows
# Each row: [Geography, Etiology/Risk Factors, Disease Type, [Symptom 1-6], Disease Name, ICD Code]

disease_data = [
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
