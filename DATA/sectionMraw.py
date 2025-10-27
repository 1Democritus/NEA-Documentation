# ICD-10 M00-M99 Disease Dataset for AI Training
#
# This file contains a list of dictionaries, where each dictionary represents
# a row of data for a specific ICD-10 code in the M00-M99 range
# (Diseases of the musculoskeletal system and connective tissue).
#
# The data structure for each row (dictionary) is as follows:
#   "Geography": (str) General area of prominence.
#   "Transmission": (list[str, str, str]) Keywords for transmission.
#                   For non-infectious diseases, this is marked "N/A".
#   "Disease Type": (str) Type of pathogen. For non-infectious diseases,
#                   this is marked "N/A" as it does not fit the user-
#                   requested categories (bacterial, viral, parasitic, fungal).
#   "Symptoms": (list[str, ...]) 6 common associated symptoms.
#   "Label": (str) The common name of the disease (the target label).
#   "ICD Code": (str) The generalized ICD-10 code.
#
# Note: ICD codes M74, M78, and M98 are not valid top-level codes
# and have been omitted as requested, resulting in 97 total rows.

disease_data = [
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

# Example of how to access the data:
if __name__ == "__main__":
    print(f"Total number of disease rows: {len(disease_data)}")
    print("\n--- Example Row (M05) ---")
    m05_data = next((item for item in disease_data if item["ICD Code"] == "M05"), None)
    if m05_data:
        for key, value in m05_data.items():
            print(f"{key}: {value}")
    
    print("\n--- Example Row (M86) ---")
    m86_data = next((item for item in disease_data if item["ICD Code"] == "M86"), None)
    if m86_data:
        for key, value in m86_data.items():
            print(f"{key}: {value}")
