# ICD-10 H00-H99 Disease Dataset Rows
# This file contains data for training an AI model.
# Each row follows the structure:
# [Geography, [Transmission_1, Transmission_2, Transmission_3], Disease_Type, [Symptom_1, ..., Symptom_6], Disease_Name, ICD_Code]

disease_data = [
    # H00-H06: Disorders of eyelid, lacrimal system and orbit
    ["Worldwide", ["bacterial spread", "blocked gland", "poor hygiene"], "bacterial", ["painful eyelid lump", "redness", "swelling", "tenderness", "eyelid irritation", "tearing"], "Hordeolum and Chalazion", "H00"],
    ["Worldwide", ["bacterial overgrowth", "clogged oil glands", "allergic reaction"], "inflammatory", ["red, swollen eyelids", "crusty eyelashes", "gritty sensation", "itching", "light sensitivity", "blurry vision"], "Blepharitis", "H01"],
    ["Worldwide", ["aging", "congenital", "nerve damage"], "structural", ["drooping upper eyelid", "inward-turned eyelid", "outward-turned eyelid", "difficulty closing eye", "impaired vision", "eye irritation"], "Disorders of eyelid (Ptosis, Entropion, Ectropion)", "H02"],
    ["Worldwide", ["secondary to systemic disease", "infection", "autoimmune"], "secondary", ["eyelid inflammation", "lesions", "ptosis", "rash on eyelid", "symptom of primary disease", "eyelid swelling"], "Eyelid disorder secondary to other disease", "H03"],
    ["Worldwide", ["blockage", "inflammation", "infection"], "inflammatory", ["excessive tearing (epiphora)", "dry eyes", "pain in inner corner", "swelling near nose", "recurrent eye infections", "mucus discharge"], "Disorders of lacrimal system (Dacryoadenitis, Dry Eye)", "H04"],
    ["Worldwide", ["bacterial infection", "fungal infection", "trauma"], "inflammatory", ["eye pain", "protruding eyeball (proptosis)", "swollen eyelid", "redness", "fever", "impaired eye movement"], "Disorders of orbit (Cellulitis, Graves')", "H05"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "inflammatory"], "secondary", ["dry eyes", "proptosis", "swelling", "pain", "symptom of primary disease", "vision changes"], "Lacrimal/Orbit disorder secondary to other disease", "H06"],

    # H10-H13: Disorders of conjunctiva
    ["Worldwide", ["viral", "bacterial", "allergic reaction"], "viral", ["eye redness", "gritty sensation", "itching", "discharge (watery or thick)", "crusting of eyelids", "light sensitivity"], "Conjunctivitis (Pink Eye)", "H10"],
    ["Worldwide (higher in sunny climates)", ["UV exposure", "chronic irritation", "wind/dust exposure"], "non-infectious", ["fleshy growth on eye", "redness", "irritation", "foreign body sensation", "blurry vision (if advanced)", "dryness"], "Other conjunctival disorders (Pterygium, Pinguecula)", "H11"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "allergic"], "secondary", ["chronic redness", "lesions on conjunctiva", "dryness", "irritation", "symptom of primary disease", "discharge"], "Conjunctival disorder secondary to other disease", "H13"],

    # H15-H22: Disorders of sclera, cornea, iris and ciliary body
    ["Worldwide", ["autoimmune", "idiopathic", "infection-related"], "autoimmune", ["severe, boring eye pain", "deep red/purple eye", "light sensitivity", "blurred vision", "headache", "pain on eye movement"], "Scleritis/Episcleritis", "H15"],
    ["Worldwide", ["bacterial", "viral (herpes)", "fungal"], "viral", ["severe eye pain", "redness", "blurred vision", "light sensitivity (photophobia)", "foreign body sensation", "excessive tearing"], "Keratitis", "H16"],
    ["Worldwide", ["trauma", "previous infection", "previous surgery"], "traumatic", ["blurry vision", "hazy/cloudy cornea", "vision loss", "glare", "halos around lights", "light sensitivity"], "Corneal scarring", "H17"],
    ["Worldwide", ["genetic", "degenerative", "metabolic"], "genetic", ["progressive vision loss", "blurry vision", "corneal thinning", "irregular astigmatism", "light sensitivity", "eye pain"], "Other corneal disorders (e.g., Dystrophies, Keratoconus)", "H18"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "metabolic"], "secondary", ["corneal deposits", "scleral thinning", "vision changes", "eye pain", "symptom of primary disease", "redness"], "Scleral/Corneal disorder secondary to other disease", "H19"],
    ["Worldwide", ["autoimmune", "idiopathic", "infection-related"], "autoimmune", ["eye pain", "redness (ciliary flush)", "light sensitivity", "blurred vision", "small/irregular pupil", "floaters"], "Iridocyclitis (Anterior Uveitis)", "H20"],
    ["Worldwide", ["trauma", "congenital", "degenerative"], "structural", ["irregular pupil shape", "vision loss", "eye pain", "cysts on iris", "floaters", "light sensitivity"], "Other iris/ciliary disorders", "H21"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "infectious"], "secondary", ["uveitis symptoms", "iris nodules", "pupil abnormalities", "symptom of primary disease", "eye pain", "vision changes"], "Iris/Ciliary disorder secondary to other disease", "H22"],

    # H25-H28: Disorders of lens
    ["Worldwide", ["aging", "oxidative stress", "UV exposure"], "degenerative", ["cloudy/blurry vision", "faded colors", "glare/halos at night", "poor night vision", "frequent prescription changes", "double vision in one eye"], "Age-related cataract", "H25"],
    ["Worldwide", ["trauma", "congenital", "steroid use"], "traumatic", ["cloudy/blurry vision", "glare", "light sensitivity", "vision loss", "milky white pupil", "faded colors"], "Other cataracts (Traumatic, Congenital)", "H26"],
    ["Worldwide", ["surgical removal", "trauma", "congenital"], "structural", ["absence of lens", "severe blurry vision", "difficulty focusing", "vision loss", "trembling iris", "monocular vision"], "Other lens disorders (Aphakia, Dislocation)", "H27"],
    ["Worldwide", ["secondary to systemic disease", "metabolic (diabetes)", "genetic syndrome"], "secondary", ["early-onset cataract", "vision changes", "cloudy lens", "symptom of primary disease", "blurry vision", "glare"], "Lens disorder secondary to other disease", "H28"],

    # H30-H36: Disorders of choroid and retina
    ["Worldwide", ["parasitic", "viral", "autoimmune"], "parasitic", ["floaters", "blurred vision", "vision loss", "scotoma (blind spot)", "eye pain", "light sensitivity"], "Chorioretinal inflammation (Posterior Uveitis)", "H30"],
    ["Worldwide", ["idiopathic", "degenerative", "traumatic"], "degenerative", ["vision distortion", "vision loss", "floaters", "flashes of light", "blind spots", "night blindness"], "Other choroidal disorders", "H31"],
    ["Worldwide", ["secondary to systemic disease", "infectious", "autoimmune"], "secondary", ["retinal lesions", "vision changes", "floaters", "symptom of primary disease", "inflammation", "vision loss"], "Chorioretinal disorder secondary to other disease", "H32"],
    ["Worldwide", ["trauma", "aging (PVD)", "high myopia"], "structural", ["sudden floaters", "flashes of light (photopsia)", "curtain/shadow in vision", "sudden blurred vision", "peripheral vision loss", "central vision loss"], "Retinal detachment", "H33"],
    ["Worldwide", ["thrombosis", "embolism", "hypertension"], "vascular", ["sudden, painless vision loss", "partial vision loss", "blurred vision", "scotoma", "vision distortion", "no pain"], "Retinal vascular occlusion (BRVO, CRVO)", "H34"],
    ["Worldwide", ["aging", "genetic", "smoking"], "degenerative", ["blurred central vision", "straight lines appear wavy", "difficulty reading", "dark spot in central vision", "color perception changes", "slow vision loss"], "Other retinal disorders (Macular Degeneration, Retinitis Pigmentosa)", "H35"],
    ["Worldwide", ["diabetes", "hypertension", "metabolic"], "secondary", ["blurry vision", "floaters", "dark spots in vision", "fluctuating vision", "vision loss", "poor night vision"], "Diabetic retinopathy", "H36"],

    # H40-H42: Glaucoma
    ["Worldwide", ["high intraocular pressure", "genetic", "aging"], "degenerative", ["peripheral vision loss (tunnel vision)", "no early symptoms", "sudden eye pain (acute)", "halos around lights", "headache", "nausea (acute)"], "Glaucoma", "H40"],
    ["Worldwide", ["secondary to systemic disease", "steroid use", "inflammation"], "secondary", ["peripheral vision loss", "elevated eye pressure", "symptom of primary disease", "eye pain", "redness", "blurry vision"], "Secondary glaucoma", "H42"],

    # H43-H45: Disorders of vitreous body and globe
    ["Worldwide", ["aging", "PVD", "inflammation"], "degenerative", ["floaters (specks, cobwebs)", "flashes of light", "blurred vision", "vitreous hemorrhage", "vision loss", "no pain"], "Vitreous disorders (Floaters, Detachment)", "H43"],
    ["Worldwide", ["post-surgical infection", "trauma", "bacterial"], "bacterial", ["severe eye pain", "rapid vision loss", "redness", "swollen eyelid", "pus in anterior chamber", "light sensitivity"], "Disorders of globe (Endophthalmitis, Atrophy)", "H44"],
    ["Worldwide", ["secondary to systemic disease", "infection", "autoimmune"], "secondary", ["inflammation (uveitis)", "hemorrhage", "floaters", "vision loss", "symptom of primary disease", "eye pain"], "Vitreous/Globe disorder secondary to other disease", "H45"],

    # H46-H48: Disorders of optic nerve and visual pathways
    ["Worldwide", ["autoimmune (MS)", "idiopathic", "viral"], "autoimmune", ["vision loss in one eye", "pain with eye movement", "faded color vision", "flashing lights", "central scotoma", "headache"], "Optic neuritis", "H46"],
    ["Worldwide", ["vascular", "compressive (tumor)", "genetic"], "vascular", ["painless vision loss", "swollen optic disc (papilledema)", "peripheral vision loss", "headache", "visual field defects", "optic atrophy"], "Other optic nerve disorders (Ischemic Optic Neuropathy)", "H47"],
    ["Worldwide", ["secondary to systemic disease", "nutritional deficiency", "toxic"], "secondary", ["progressive vision loss", "visual field defects", "optic atrophy", "symptom of primary disease", "color vision loss", "central scotoma"], "Optic nerve disorder secondary to other disease", "H48"],

    # H49-H52: Disorders of ocular muscles, binocular movement, accommodation and refraction
    ["Worldwide", ["nerve palsy (CN III, IV, VI)", "trauma", "vascular (diabetes)"], "neurological", ["double vision (diplopia)", "eye misalignment", "head tilt", "dizziness", "inability to move eye", "eyelid droop (ptosis)"], "Paralytic strabismus", "H49"],
    ["Worldwide", ["congenital", "refractive error", "muscle imbalance"], "structural", ["crossed eyes", "eyes point different directions", "poor depth perception", "double vision", "head tilt", "eye strain"], "Non-paralytic strabismus (Esotropia, Exotropia)", "H50"],
    ["Worldwide", ["neurological", "congenital", "trauma"], "neurological", ["nystagmus (involuntary eye movement)", "dizziness", "vertigo", "blurred vision", "difficulty focusing", "gaze palsy"], "Other binocular movement disorders (Nystagmus)", "H51"],
    ["Worldwide", ["genetic predisposition", "environmental factors", "aging"], "structural", ["blurry distance vision (myopia)", "blurry near vision (hyperopia)", "blurry vision at all distances (astigmatism)", "eye strain", "headaches", "difficulty focusing (presbyopia)"], "Refractive errors (Myopia, Hyperopia, Astigmatism)", "H52"],

    # H53-H54: Visual disturbances and blindness
    ["Worldwide", ["neurological", "retinal", "idiopathic"], "symptomatic", ["visual field defects", "color vision deficiencies", "night blindness", "diplopia", "light sensitivity", "visual distortion"], "Visual disturbances (Amblyopia, Color blindness)", "H53"],
    ["Worldwide", ["cataract", "glaucoma", "macular degeneration"], "symptomatic", ["severe vision loss", "inability to see light", "legal blindness", "peripheral vision loss", "central vision loss", "poor visual acuity"], "Blindness and low vision", "H54"],

    # H55-H59: Other disorders of eye and adnexa
    ["Worldwide", ["congenital", "neurological", "inner ear disorder"], "neurological", ["involuntary rhythmic eye movements", "blurred vision", "dizziness", "oscillopsia (world appears to shake)", "poor depth perception", "head tilt"], "Nystagmus", "H55"],
    ["Worldwide", ["idiopathic", "traumatic", "vascular"], "idiopathic", ["eye pain", "redness", "pupil abnormalities", "foreign body sensation", "headache", "vision changes"], "Other unspecified eye disorders", "H57"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "infectious"], "secondary", ["eye pain", "vision changes", "symptom of primary disease", "redness", "pupil changes", "inflammation"], "Eye disorder secondary to other disease", "H58"],
    ["Worldwide", ["post-surgical complication", "iatrogenic", "inflammation"], "traumatic", ["post-operative pain", "vision loss after surgery", "inflammation", "infection", "high eye pressure", "corneal edema"], "Postprocedural eye disorder", "H59"],

    # H60-H62: Diseases of external ear
    ["Worldwide", ["bacterial", "fungal", "water exposure"], "bacterial", ["ear pain (otalgia)", "itchy ear canal", "redness/swelling of ear canal", "ear discharge", "muffled hearing", "pain on touching earlobe"], "Otitis externa (Swimmer's Ear)", "H60"],
    ["Worldwide", ["trauma", "impacted cerumen", "congenital"], "structural", ["earwax blockage", "hearing loss", "ear pain", "ear canal mass", "deformed pinna", "dizziness"], "Other external ear disorders (Impacted cerumen)", "H61"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "dermatological"], "secondary", ["rash on ear", "lesions in ear canal", "inflammation", "symptom of primary disease", "ear pain", "discharge"], "External ear disorder secondary to other disease", "H62"],

    # H65-H75: Diseases of middle ear and mastoid
    ["Worldwide", ["eustachian tube dysfunction", "viral URI", "allergic"], "inflammatory", ["muffled hearing", "feeling of fullness in ear", "popping/cracking sounds", "balance problems", "hearing loss (conductive)", "no pain or fever"], "Otitis media with effusion (Glue Ear)", "H65"],
    ["Worldwide", ["bacterial", "viral", "eustachian tube dysfunction"], "bacterial", ["severe ear pain", "fever", "hearing loss", "ear discharge (pus)", "irritability (infants)", "feeling of fullness"], "Acute otitis media (Ear Infection)", "H66"],
    ["Worldwide", ["secondary to systemic disease", "viral", "bacterial"], "secondary", ["ear pain", "fever", "hearing loss", "symptom of primary disease (e.g., flu)", "discharge", "fullness"], "Otitis media secondary to other disease", "H67"],
    ["Worldwide", ["inflammation", "allergy", "infection (URI)"], "inflammatory", ["ear fullness", "muffled hearing", "popping sounds", "difficulty equalizing pressure", "ear pain", "dizziness"], "Eustachian tube dysfunction", "H68"],
    ["Worldwide", ["congenital", "structural", "idiopathic"], "structural", ["patulous eustachian tube", "autophony (hearing own voice)", "ear fullness", "popping", "hearing own breathing", "muffled hearing"], "Other Eustachian tube disorders", "H69"],
    ["Worldwide", ["bacterial (complication of otitis media)", "untreated ear infection", "spread of infection"], "bacterial", ["pain behind ear", "swelling/redness behind ear", "fever", "headache", "ear discharge", "hearing loss"], "Mastoiditis", "H70"],
    ["Worldwide", ["eanglian tube dysfunction", "chronic ear infections", "skin cell accumulation"], "structural", ["painless, foul-smelling ear discharge", "progressive hearing loss", "dizziness", "earache", "facial muscle weakness", "fullness in ear"], "Cholesteatoma", "H71"],
    ["Worldwide", ["trauma (q-tip)", "barotrauma (pressure)", "infection"], "traumatic", ["sudden ear pain", "whistling sound from ear", "hearing loss", "ear discharge (clear or bloody)", "ringing in ear (tinnitus)", "dizziness"], "Perforated eardrum", "H72"],
    ["Worldwide", ["inflammation", "trauma", "chronic infection"], "inflammatory", ["hearing loss", "ear pain", "retracted eardrum", "feeling of fullness", "muffled hearing", "tinnitus"], "Other eardrum disorders (Tympanosclerosis)", "H73"],
    ["Worldwide", ["trauma", "congenital", "idiopathic"], "structural", ["conductive hearing loss", "ossicular chain dislocation", "ear pain", "tinnitus", "dizziness", "eardrum retraction"], "Other middle ear disorders (Ossicular discontinuity)", "H74"],
    ["Worldwide", ["secondary to systemic disease", "autoimmune", "congenital syndrome"], "secondary", ["hearing loss", "ear pain", "symptom of primary disease", "dizziness", "inflammation", "discharge"], "Middle ear disorder secondary to other disease", "H75"],

    # H80-H83: Diseases of inner ear
    ["Worldwide (more in Caucasians)", ["genetic", "hereditary", "unknown trigger"], "genetic", ["progressive conductive hearing loss", "tinnitus (ringing in ear)", "dizziness", "family history of hearing loss", "speaks quietly (own voice loud)", "paracusis willisii"], "Otosclerosis", "H80"],
    ["Worldwide", ["idiopathic", "fluid imbalance (endolymph)", "viral"], "idiopathic", ["episodic vertigo (spinning)", "tinnitus (roaring)", "fluctuating hearing loss", "aural fullness (pressure)", "nausea", "vomiting"], "Disorders of vestibular function (Meniere's, BPPV)", "H81"],
    ["Worldwide", ["secondary to systemic disease", "vascular", "neurological"], "secondary", ["vertigo", "dizziness", "symptom of primary disease", "nausea", "imbalance", "headache"], "Vertigo secondary to other disease", "H82"],
    ["Worldwide", ["viral", "autoimmune", "vascular"], "viral", ["sudden hearing loss", "tinnitus", "vertigo", "aural fullness", "imbalance", "nausea"], "Other inner ear diseases (Labyrinthitis, Vestibular Neuronitis)", "H83"],

    # H90-H95: Other disorders of ear
    ["Worldwide", ["noise exposure", "aging (presbycusis)", "genetic"], "degenerative", ["difficulty hearing speech", "muffled sounds", "tinnitus", "need to turn up volume", "difficulty in noisy places", "social withdrawal"], "Hearing loss (Conductive, Sensorineural)", "H90"],
    ["Worldwide", ["ototoxic drugs", "sudden idiopathic", "trauma"], "idiopathic", ["sudden deafness", "hearing loss after medication", "tinnitus", "muffled hearing", "aural fullness", "dizziness"], "Other hearing loss (Ototoxicity, Sudden Deafness)", "H91"],
    ["Worldwide", ["referred pain (dental, TMJ)", "infection", "inflammation"], "symptomatic", ["ear pain", "ear discharge", "hearing loss", "jaw pain", "headache", "fever"], "Otalgia (Ear pain)", "H92"],
    ["Worldwide", ["noise exposure", "hearing loss", "vascular"], "symptomatic", ["ringing in ears", "buzzing/hissing sound", "hearing loss", "dizziness", "hyperacusis (sound sensitivity)", "aural fullness"], "Tinnitus and other ear disorders", "H93"],
    ["Worldwide", ["secondary to systemic disease", "neurological", "autoimmune"], "secondary", ["hearing loss", "tinnitus", "dizziness", "symptom of primary disease", "ear pain", "inflammation"], "Ear disorder secondary to other disease", "H94"],
    ["Worldwide", ["post-surgical complication", "iatrogenic", "inflammation"], "traumatic", ["post-operative pain", "hearing loss after surgery", "dizziness", "infection", "ear discharge", "tinnitus"], "Postprocedural ear disorder", "H95"]
]

if __name__ == '__main__':
    # This part is just for demonstration, so you can run the file and see the data.
    # You can import the 'disease_data' list into your main script.
    print(f"Generated {len(disease_data)} rows for ICD-10 H00-H95 categories.")
    print("Example row (H00):")
    print(disease_data[0])
    print("\nExample row (H90):")
    print(disease_data[-6])
