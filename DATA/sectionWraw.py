# ICD-10 W00-W99 "External Causes of Morbidity" Dataset
#
# NOTE: The W00-W99 codes represent injuries and accidents, not diseases.
# To fit the requested structure, the following features have been re-interpreted:
# 1. 'Disease_type' is interpreted as 'Injury_Category' (e.g., "Blunt trauma").
# 2. 'How_the_disease_transmits' is interpreted as 'Mechanism_of_Injury' (e.g., ["Loss of balance", "Slippery surface"]).
# 3. 'Symptoms' is interpreted as 'Common_Resulting_Injuries' (e.g., ["Fracture", "Sprain"]).

icd_w_data = [
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

# Example of how to access the first row
if __name__ == "__main__":
    if icd_w_data:
        print("Total rows generated:", len(icd_w_data))
        print("\nExample first row (W00):")
        print(icd_w_data[0])
        print("\nExample last row (W99):")
        print(icd_w_data[-1])
