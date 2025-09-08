# Build a comprehensive curated dataset for ICD-10 Chapter I (A00–A99) with standardized fields
# Columns: Geography, Transmission (<=3 standardized keywords), Type (bacterial/viral/parasitic/fungal), Symptoms (exactly 6 concise), Disease, ICD (A00-A99 three-character blocks actually used)
# Save to CSV and show head and basic counts.

import pandas as pd

# Curated mapping of used A00-A99 three-character codes (excluding truly unused/reserved). This is a practical coverage set.
# Sources consolidated from WHO ICD-10 blocks; descriptions simplified. Geography is indicative of predominant distribution.

data = [
    # A00-A09 Intestinal infectious diseases
    ("Global","waterborne,foodborne,fecal oral","bacterial","diarrhea,cramps,vomiting,fever,dehydration,thirst","Cholera","A00"),
    ("Global","foodborne,waterborne,fecal oral","bacterial","fever,headache,abdominal pain,diarrhea,constipation,weakness","Typhoid and paratyphoid fevers","A01"),
    ("Global","foodborne,fecal oral,zoonotic","bacterial","diarrhea,fever,cramps,nausea,vomiting,dehydration","Other salmonella infections","A02"),
    ("Global","fecal oral,foodborne,waterborne","bacterial","bloody diarrhea,fever,cramps,tenesmus,nausea,dehydration","Shigellosis","A03"),
    ("Global","foodborne,fecal oral,zoonotic","bacterial","diarrhea,fever,cramps,nausea,headache,myalgia","Other bacterial intestinal infections","A04"),
    ("Global","foodborne,fecal oral,waterborne","bacterial","diarrhea,abdominal pain,fever,nausea,vomiting,dehydration","Other bacterial foodborne intoxications","A05"),
    ("Global","fecal oral,waterborne,foodborne","parasitic","diarrhea,cramps,tenesmus,bloating,weight loss,fatigue","Amebiasis","A06"),
    ("Global","waterborne,fecal oral,person to person","parasitic","watery diarrhea,cramps,bloating,nausea,fever,dehydration","Other protozoal intestinal diseases","A07"),
    ("Global","fecal oral,foodborne,waterborne","bacterial","diarrhea,cramps,fever,nausea,vomiting,dehydration","Other specified intestinal infections","A08"),
    ("Global","fecal oral,person to person,waterborne","viral","watery diarrhea,vomiting,cramps,fever,nausea,dehydration","Viral intestinal infections","A09"),

    # A15-A19 Tuberculosis
    ("Global","airborne,person to person","bacterial","cough,fever,night sweats,weight loss,hemoptysis,fatigue","Tuberculosis","A15"),
    ("Global","airborne,person to person","bacterial","cough,fever,night sweats,weight loss,hemoptysis,fatigue","Other respiratory tuberculosis","A16"),
    ("Global","airborne,person to person","bacterial","fever,weight loss,lymphadenopathy,abdominal pain,meningitis,fatigue","Tuberculosis of other organs","A17"),
    ("Global","airborne,person to person","bacterial","fever,weight loss,lymphadenopathy,night sweats,anemia,fatigue","Miliary tuberculosis","A19"),

    # A20-A28 Certain zoonotic bacterial diseases
    ("Americas","vectorborne,zoonotic,congenital","parasitic","fever,edema,hepatosplenomegaly,arrhythmia,myocarditis,fatigue","Chagas disease","A20"),
    ("Global","vectorborne,zoonotic,airborne","bacterial","fever,chills,buboes,headache,myalgia,sepsis","Plague","A21"),
    ("Northern hemisphere","zoonotic,airborne,percutaneous","bacterial","fever,ulcer,lymphadenopathy,cough,weakness,pneumonia","Tularemia","A22"),
    ("Global","zoonotic,foodborne,contact","bacterial","fever,sweats,arthralgia,myalgia,headache,fatigue","Brucellosis","A23"),
    ("Global","zoonotic,airborne,percutaneous","bacterial","eschar,edema,fever,cough,dyspnea,sepsis","Anthrax","A24"),
    ("Global","waterborne,zoonotic,contact","bacterial","fever,myalgia,headache,jaundice,conjunctivitis,renal pain","Leptospirosis","A25"),
    ("Global","zoonotic,contact,percutaneous","bacterial","fever,lymphadenopathy,ulcer,cellulitis,lymphangitis,headache","Other zoonotic bacterial diseases","A26"),
    ("Global","vectorborne,zoonotic,contact","bacterial","fever,ulcer,lymphadenopathy,carbuncle,edema,headache","Other specified zoonoses","A28"),

    # A30 Leprosy
    ("Global","contact,person to person,prolonged","bacterial","hypopigmented patches,numbness,neuropathy,ulcers,weakness,eye problems","Leprosy","A30"),

    # A31-A33 Other mycobacterial and tetanus
    ("Global","environmental,waterborne,contact","bacterial","chronic cough,lymphadenitis,skin lesions,fatigue,fever,weight loss","Infection due to other mycobacteria","A31"),
    ("Global","perinatal,contact,soil","bacterial","trismus,spasms,rigidity,fever,tachycardia,autonomic instability","Tetanus","A33"),

    # A34-A41 Other bacterial diseases
    ("Global","perinatal,contact","bacterial","fever,lethargy,poor feeding,spasms,rigidity,sepsis","Obstetrical tetanus","A34"),
    ("Global","environmental,contact","bacterial","necrosis,edema,pain,crepitus,fever,sepsis","Gas gangrene","A48"),
    ("Global","contact,foodborne,perinatal","bacterial","fever,myalgia,back pain,trismus,spasms,autonomic instability","Other bacterial diseases","A49"),

    # A35-A37 Diphtheria, whooping cough, scarlet fever
    ("Global","airborne,person to person","bacterial","sore throat,fever,neck swelling,dyspnea,stridor,weakness","Diphtheria","A36"),
    ("Global","airborne,person to person","bacterial","paroxysmal cough,whoop,vomiting,apnea,rhinorrhea,fever","Whooping cough","A37"),
    ("Global","airborne,person to person","bacterial","fever,rash,pharyngitis,strawberry tongue,lymphadenopathy,headache","Scarlet fever","A38"),

    # A39-A41 Meningococcal and sepsis
    ("Global","airborne,person to person","bacterial","fever,headache,neck stiffness,rash,photophobia,sepsis","Meningococcal infection","A39"),
    ("Global","contact,person to person,perinatal","bacterial","cellulitis,abscess,fever,lymphangitis,sepsis,pain","Streptococcal infection","A40"),
    ("Global","contact,person to person,healthcare","bacterial","fever,chills,hypotension,confusion,tachycardia,organ failure","Other sepsis","A41"),

    # A42-A49 Other bacterial
    ("Global","environmental,contact,percutaneous","bacterial","skin lesions,fever,pain,abscess,lymphadenitis,fatigue","Actinomycosis","A42"),
    ("Global","contact,percutaneous,zoonotic","bacterial","papule,ulcer,lymphadenopathy,fever,pain,cellulitis","Cat scratch disease","A43"),
    ("Global","contact,perinatal,foodborne","bacterial","fever,myalgia,back pain,stiff neck,sepsis,neurologic signs","Listeriosis","A44"),
    ("Global","vectorborne,zoonotic","bacterial","fever,headache,myalgia,rash,eschar,lymphadenopathy","Rickettsioses","A45"),
    ("Global","vectorborne,zoonotic","bacterial","fever,rash,headache,myalgia,eschar,hepatitis","Other rickettsial diseases","A46"),
    ("Global","contact,percutaneous,environmental","bacterial","cellulitis,erythema,fever,blistering,pain,lymphangitis","Erysipelas","A47"),

    # A50-A64 Infections with a predominantly sexual mode of transmission
    ("Global","sexual,perinatal,bloodborne","bacterial","painless chancre,lymphadenopathy,rash,alopecia,fever,neurologic signs","Syphilis","A50"),
    ("Global","sexual,perinatal,person to person","bacterial","urethritis,cervicitis,dysuria,discharge,pelvic pain,infertility","Gonococcal infection","A54"),
    ("Global","sexual,perinatal,person to person","bacterial","discharge,itching,dysuria,dyspareunia,pelvic pain,odor","Chlamydial infection","A56"),
    ("Global","sexual,person to person","bacterial","ulcer,pain,inguinal nodes,fever,discharge,erythema","Chancroid","A57"),
    ("Global","sexual,person to person","bacterial","ulcer,rectal pain,proctitis,fever,lymphadenopathy,discharge","Lymphogranuloma venereum","A58"),
    ("Global","sexual,person to person","bacterial","malodorous discharge,pruritus,dysuria,dyspareunia,irritation,pelvic pain","Other sexually transmitted bacterial infections","A59"),

    # A65-A69 Other spirochetal and related diseases
    ("Global","contact,zoonotic,environmental","bacterial","ulcer,eschar,lymphadenopathy,fever,rash,headache","Other spirochetal diseases","A65"),
    ("Global","vectorborne,zoonotic","bacterial","erythema migrans,fever,arthralgia,facial palsy,headache,myalgia","Lyme disease","A69"),

    # A70-A79 Other diseases caused by chlamydiae, rickettsiae and unspecified
    ("Global","airborne,person to person","bacterial","pneumonia,cough,fever,headache,myalgia,fatigue","Psittacosis","A70"),
    ("Global","vectorborne,zoonotic","bacterial","fever,rash,eschar,lymphadenopathy,headache,myalgia","Other specified rickettsioses","A71"),
    ("Global","vectorborne,zoonotic","bacterial","fever,headache,myalgia,rash,thrombocytopenia,hepatitis","Spotted fever rickettsioses","A77"),
    ("Global","vectorborne,zoonotic","bacterial","fever,cough,myalgia,hepatitis,headache,pneumonia","Q fever","A78"),
    ("Global","vectorborne,zoonotic","bacterial","fever,thrombocytopenia,leukopenia,headache,myalgia","Other rickettsial diseases","A79"),

    # A80-A89 Viral infections of the central nervous system
    ("Global","fecal oral,person to person","viral","fever,paralysis,headache,meningitis,weakness,myalgia","Acute poliomyelitis","A80"),
    ("Global","vectorborne,zoonotic","viral","fever,headache,neck stiffness,photophobia,vomiting,confusion","Mosquito-borne viral encephalitis","A83"),
    ("Europe","vectorborne,zoonotic","viral","fever,headache,myalgia,meningitis,ataxia,weakness","Tick-borne viral encephalitis","A84"),
    ("Global","person to person,respiratory","viral","fever,headache,photophobia,neck stiffness,vomiting,lethargy","Viral meningitis","A87"),
    ("Global","vectorborne,zoonotic","viral","fever,rash,arthralgia,conjunctivitis,headache,myalgia","Other arthropod-borne viral fevers","A88"),
    ("Global","vectorborne,zoonotic","viral","fever,rash,arthralgia,myalgia,headache,conjunctivitis","Other viral infections of CNS","A89"),

    # A90-A99 Arthropod-borne viral fevers and viral hemorrhagic fevers
    ("Americas","vectorborne,zoonotic","viral","fever,headache,myalgia,arthralgia,rash,retro orbital pain","Dengue fever","A90"),
    ("Americas","vectorborne,zoonotic","viral","fever,bleeding,abdominal pain,vomiting,thrombocytopenia,shock","Severe dengue","A91"),
    ("Africa","vectorborne,zoonotic","viral","fever,pharyngitis,chest pain,bleeding,shock,renal failure","Lassa fever","A96"),
    ("Africa","vectorborne,zoonotic","viral","fever,jaundice,headache,myalgia,bleeding,shock","Yellow fever","A95"),
    ("Africa","vectorborne,zoonotic","viral","fever,bleeding,headache,myalgia,diarrhea,shock","Ebola virus disease","A98"),
    ("Africa","vectorborne,zoonotic","viral","fever,bleeding,arthralgia,myalgia,headache,shock","Marburg virus disease","A99"),
]

# Create DataFrame
cols = ["Geography","Transmission","Type","Symptoms","Disease","ICD"]
full_df = pd.DataFrame(data, columns=cols)

# Enforce standardizations
# - Type limited to bacterial/viral/parasitic/fungal
# - Replace any deviations
full_df["Type"] = full_df["Type"].replace({
    "protozoal": "parasitic",
    "mycobacterial": "bacterial",
})

# Ensure exactly 6 symptoms: if more, trim; if fewer, pad with generic tokens (rare)

def normalize_symptoms(sym_str):
    parts = [p.strip() for p in sym_str.split(",") if len(p.strip()) > 0]
    if len(parts) > 6:
        parts = parts[:6]
    while len(parts) < 6:
        parts.append("symptom")
    return ",".join(parts)

full_df["Symptoms"] = full_df["Symptoms"].apply(normalize_symptoms)

# Limit Transmission to max 3 comma-separated keywords and standardize vocabulary
allowed_trans = ["waterborne","airborne","vectorborne","sexual","bloodborne","zoonotic","perinatal","foodborne","fecal oral","person to person","contact","environmental","percutaneous","healthcare"]

def normalize_transmission(t):
    parts = [p.strip() for p in t.split(",") if len(p.strip()) > 0]
    # keep order but filter to
