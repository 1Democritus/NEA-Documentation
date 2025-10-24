# ICD-10 G00-G99 Disease Dataset
# This file contains sample data for diseases of the nervous system.
# Each row is a list with the following structure:
# [
#     "Geography" (str),
#     ["Transmission_1", "Transmission_2", "Transmission_3"] (list[str]),
#     "Disease_Type" (str),
#     ["Symptom_1", "Symptom_2", "Symptom_3", "Symptom_4", "Symptom_5", "Symptom_6"] (list[str]),
#     "Disease_Name" (str, Label),
#     "ICD_Code" (str, Additional Column)
# ]
#
# Note on Disease_Type: The list has been expanded beyond the initial four
# types (bacterial, viral, parasitic, fungal) to accurately represent
# the diverse nature of neurological disorders (e.g., genetic, autoimmune,
# degenerative, vascular, idiopathic).

disease_data = [
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

# Example of how to access the first row (G00)
# print(disease_data[0])
# Example of how to write this to a CSV file (requires 'csv' module)
# import csv
#
# header = ["Geography", "Transmission", "Disease_Type", "Symptoms", "Disease_Name", "ICD_Code"]
#
# with open("g_code_diseases.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for row in disease_data:
#         # The list-based columns (Transmission, Symptoms) will be written
#         # as their string representation (e.g., "['droplet', 'contact', 'bloodborne']")
#         # This may need to be handled during your ML preprocessing step.
#         writer.writerow(row)
