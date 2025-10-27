# This file contains a dataset of ICD-10 codes L00-L99 (Diseases of the skin and subcutaneous tissue)
# for AI training.
# Each item is a dictionary with the following structure:
# - icd_code: The ICD-10 code (string)
# - disease_name: The common name of the disease/condition (string)
# - geography: General geographical prevalence (string)
# - transmission: Key methods of transmission or causal factors (list of 3 strings)
# - disease_type: The nature of the disease (string)
# - symptoms: A list of 6 common symptoms (list of 6 strings)

disease_data = [
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

# Example of how to access the data:
# print(f"Total rows: {len(disease_data)}")
# print("\nExample row (L01 Impetigo):")
# for item in disease_data:
#     if item["icd_code"] == "L01":
#         print(item)
#
# print("\nExample row (L40 Psoriasis):")
# for item in disease_data:
#     if item["icd_code"] == "L40":
#         print(item)
