# This file contains 100 data rows for ICD-10 codes S00-S99 (Injuries).
# The data is structured as a list of lists.
# Each inner list represents a row with the following 6 columns:
# [Geography, Transmission (list), Disease Type, Symptoms (list), Label (Disease Name), ICD Code]

# Note on "Disease Type" and "Transmission":
# These categories are intended for infectious diseases. For injuries, they are
# marked 'N/A - Injury' unless the injury is an open wound (e.g., S01, S11)
# or amputation, where the primary complication *is* a 'Bacterial' infection
# transmitted via 'Contamination'.

icd_s_data = [
    # S00-S09: Injuries to the head
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion', 'Contusion'], 'Superficial injury of head', 'S00'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tissue damage'], 'Open wound of head', 'S01'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Swelling', 'Deformity', 'Loss of function', 'Bruising', 'Crepitus'], 'Fracture of skull and facial bones', 'S02'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Jaw pain', 'Difficulty opening mouth', 'Clicking sound', 'Joint locking', 'Headache', 'Neck pain'], 'Dislocation, sprain and strain of joints and ligaments of head', 'S03'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Loss of smell', 'Vision problems', 'Facial droop', 'Deafness', 'Dizziness', 'Difficulty swallowing'], 'Injury of cranial nerves', 'S04'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Vision loss', 'Eye pain', 'Double vision', 'Bleeding in eye', 'Swelling of eyelid', 'Foreign body sensation'], 'Injury of eye and orbit', 'S05'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Headache', 'Vomiting', 'Confusion', 'Loss of consciousness', 'Seizure', 'Drowsiness'], 'Intracranial injury', 'S06'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe tissue damage', 'Deformity', 'Massive swelling', 'Bleeding', 'Neurological deficit', 'Pain'], 'Crushing injury of head', 'S07'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of body part', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of head', 'S08'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Headache', 'Dizziness', 'Tenderness'], 'Other and unspecified injuries of head', 'S09'],

    # S10-S19: Injuries to the neck
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Redness', 'Superficial scratch', 'Contusion'], 'Superficial injury of neck', 'S10'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Hoarseness'], 'Open wound of neck', 'S11'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Neck pain', 'Swelling', 'Deformity', 'Difficulty swallowing', 'Limited motion', 'Crepitus'], 'Fracture of neck', 'S12'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Neck pain', 'Stiffness', 'Muscle spasm', 'Headache', 'Limited range of motion', 'Whiplash'], 'Dislocation, sprain and strain of joints and ligaments of neck', 'S13'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in arms', 'Tingling', 'Weakness', 'Paralysis', 'Loss of sensation', 'Loss of bladder control'], 'Injury of nerves and spinal cord at neck level', 'S14'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pulsating hematoma', 'Active bleeding', 'Bruit', 'Neurological deficit', 'Diminished pulse', 'Shock'], 'Injury of blood vessels at neck level', 'S15'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Stiffness', 'Weakness', 'Muscle spasm', 'Difficulty turning head', 'Swelling'], 'Injury of muscle, fascia and tendon at neck level', 'S16'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Airway obstruction', 'Difficulty breathing', 'Crushing deformity', 'Bruising'], 'Crushing injury of neck', 'S17'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Decapitation', 'Severe bleeding', 'Pain', 'Shock', 'Non-survivable', 'Risk of infection'], 'Traumatic amputation at neck level', 'S18'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain', 'Swelling', 'Bruising', 'Stiffness', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of neck', 'S19'],

    # S20-S29: Injuries to the thorax
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest wall pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion', 'Contusion'], 'Superficial injury of thorax', 'S20'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Sucking chest wound'], 'Open wound of thorax', 'S21'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe chest pain', 'Pain on breathing', 'Shortness of breath', 'Deformity of rib cage', 'Bruising', 'Crepitus'], 'Fracture of rib(s), sternum and thoracic spine', 'S22'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest pain', 'Back pain', 'Stiffness', 'Muscle spasm', 'Limited range of motion', 'Pain with twisting'], 'Dislocation, sprain and strain of joints and ligaments of thorax', 'S23'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in chest', 'Tingling', 'Weakness in legs', 'Paralysis', 'Loss of sensation below injury', 'Bowel/bladder dysfunction'], 'Injury of nerves and spinal cord at thorax level', 'S24'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Massive internal bleeding', 'Shock', 'Shortness of breath', 'Chest pain', 'Hemothorax', 'Diminished pulses'], 'Injury of blood vessels of thorax', 'S25'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with breathing', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle spasm', 'Difficulty twisting torso'], 'Injury of muscle, fascia and tendon at thorax level', 'S26'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Crushing deformity', 'Difficulty breathing', 'Flail chest', 'Internal organ damage', 'Shock'], 'Crushing injury of thorax and traumatic asphyxia', 'S27'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of arm at shoulder', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of thorax', 'S28'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Chest pain', 'Swelling', 'Bruising', 'Shortness of breath', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of thorax', 'S29'],

    # S30-S39: Injuries to the abdomen, lower back, lumbar spine and pelvis
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal pain', 'Back pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of abdomen, lower back and pelvis', 'S30'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Evisceration'], 'Open wound of abdomen, lower back and pelvis', 'S31'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe back pain', 'Pelvic pain', 'Inability to stand', 'Deformity', 'Bruising', 'Crepitus'], 'Fracture of lumbar spine and pelvis', 'S32'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Lower back pain', 'Stiffness', 'Muscle spasm', 'Sciatica', 'Limited range of motion', 'Pain with bending'], 'Dislocation, sprain and strain of joints and ligaments of lumbar spine and pelvis', 'S33'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in legs', 'Weakness', 'Paralysis', 'Loss of sensation', 'Bowel/bladder dysfunction', 'Cauda equina syndrome'], 'Injury of nerves and spinal cord at abdomen, lower back and pelvis level', 'S34'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Internal bleeding', 'Abdominal rigidity', 'Shock', 'Hypotension', 'Bruising', 'Pulsatile mass'], 'Injury of blood vessels at abdomen, lower back and pelvis level', 'S35'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal muscle pain', 'Back muscle strain', 'Tenderness', 'Swelling', 'Muscle spasm', 'Pain with movement'], 'Injury of muscle, fascia and tendon at abdomen, lower back and pelvis level', 'S36'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Internal organ damage', 'Internal bleeding', 'Shock', 'Pelvic instability'], 'Crushing injury of abdomen, lower back and pelvis', 'S37'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Traumatic dismemberment', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of part of abdomen, lower back and pelvis', 'S38'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Abdominal pain', 'Back pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of abdomen, lower back and pelvis', 'S39'],

    # S40-S49: Injuries to the shoulder and upper arm
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Shoulder pain', 'Arm pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of shoulder and upper arm', 'S40'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced arm mobility'], 'Open wound of shoulder and upper arm', 'S41'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe shoulder pain', 'Severe arm pain', 'Inability to lift arm', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of shoulder and upper arm', 'S42'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Shoulder joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Arm weakness'], 'Dislocation, sprain and strain of joints and ligaments of shoulder girdle', 'S43'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in arm', 'Tingling', 'Weakness', 'Wrist drop', 'Loss of sensation', 'Shooting pain'], 'Injury of nerves at shoulder and upper arm level', 'S44'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in wrist', 'Pale arm', 'Cold arm', 'Bruit'], 'Injury of blood vessels at shoulder and upper arm level', 'S45'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with movement', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle weakness', 'Rotator cuff tear symptoms'], 'Injury of muscle, fascia and tendon at shoulder and upper arm level', 'S46'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of shoulder and upper arm', 'S47'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of arm', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of shoulder and upper arm', 'S48'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Arm pain', 'Shoulder pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of shoulder and upper arm', 'S49'],

    # S50-S59: Injuries to the elbow and forearm
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Elbow pain', 'Forearm pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of elbow and forearm', 'S50'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced wrist/hand mobility'], 'Open wound of elbow and forearm', 'S51'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe elbow pain', 'Severe forearm pain', 'Inability to rotate forearm', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of elbow and forearm', 'S52'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Elbow joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Tennis elbow symptoms'], 'Dislocation, sprain and strain of joints and ligaments of elbow', 'S53'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in hand', 'Tingling', 'Weakness of grip', 'Claw hand', 'Loss of sensation in fingers', 'Shooting pain'], 'Injury of nerves at forearm level', 'S54'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in wrist', 'Pale hand', 'Cold hand', 'Bruit'], 'Injury of blood vessels at forearm level', 'S55'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with gripping', 'Muscle strain', 'Tenderness', 'Swelling', 'Muscle weakness', 'Pain on wrist movement'], 'Injury of muscle, fascia and tendon at forearm level', 'S56'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of elbow and forearm', 'S57'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of forearm/hand', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of elbow and forearm', 'S58'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Forearm pain', 'Elbow pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of elbow and forearm', 'S59'],

    # S60-S69: Injuries to the wrist, hand and fingers
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Wrist pain', 'Hand pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of wrist, hand and fingers', 'S60'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tendon exposure'], 'Open wound of wrist, hand and fingers', 'S61'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe wrist pain', 'Severe hand pain', 'Inability to grip', 'Finger deformity', 'Swelling', 'Crepitus'], 'Fracture at wrist and hand level', 'S62'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Wrist joint pain', 'Finger joint pain', 'Instability', 'Swelling', 'Limited range of motion', 'Jammed finger'], 'Dislocation, sprain and strain of joints and ligaments at wrist and hand level', 'S63'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in fingers', 'Tingling', 'Weakness of grip', 'Loss of sensation', 'Carpal tunnel symptoms', 'Clumsiness'], 'Injury of nerves at wrist and hand level', 'S64'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Poor capillary refill', 'Pale fingers', 'Cold fingers', 'Loss of pulse'], 'Injury of blood vessels at wrist and hand level', 'S65'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with gripping', 'Tendon rupture', 'Inability to extend/flex finger', 'Tenderness', 'Swelling', 'Trigger finger'], 'Injury of muscle, fascia and tendon at wrist and hand level', 'S66'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Crushing deformity', 'Mangling injury', 'Vascular compromise', 'Nerve damage'], 'Crushing injury of wrist, hand and fingers', 'S67'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of finger(s)/hand', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of wrist, hand and fingers', 'S68'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hand pain', 'Wrist pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of wrist, hand and fingers', 'S69'],

    # S70-S79: Injuries to the hip and thigh
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip pain', 'Thigh pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of hip and thigh', 'S70'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Reduced leg mobility'], 'Open wound of hip and thigh', 'S71'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe hip pain', 'Inability to bear weight', 'Shortened leg', 'Externally rotated leg', 'Severe thigh pain', 'Deformity'], 'Fracture of femur', 'S72'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip joint pain', 'Instability', 'Visible dislocation', 'Swelling', 'Limited range of motion', 'Groin pain'], 'Dislocation, sprain and strain of joint and ligaments of hip', 'S73'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in leg', 'Tingling', 'Weakness', 'Foot drop', 'Loss of sensation', 'Sciatic pain'], 'Injury of nerves at hip and thigh level', 'S74'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in foot', 'Pale leg', 'Cold leg', 'Shock'], 'Injury of blood vessels at hip and thigh level', 'S75'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with walking', 'Hamstring strain', 'Quadriceps strain', 'Tenderness', 'Swelling', 'Muscle weakness'], 'Injury of muscle, fascia and tendon at hip and thigh level', 'S76'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of hip and thigh', 'S77'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of leg', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of hip and thigh', 'S78'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Hip pain', 'Thigh pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of hip and thigh', 'S79'],

    # S80-S89: Injuries to the knee and lower leg
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee pain', 'Lower leg pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of knee and lower leg', 'S80'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Joint exposure'], 'Open wound of knee and lower leg', 'S81'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe knee pain', 'Severe leg pain', 'Inability to bear weight', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of lower leg, including ankle', 'S82'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee joint pain', 'Instability', 'Knee giving way', 'Swelling', 'Limited range of motion', 'Ligament tear (ACL/MCL)'], 'Dislocation, sprain and strain of joints and ligaments of knee', 'S83'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in foot', 'Tingling', 'Weakness', 'Foot drop', 'Loss of sensation', 'Shooting pain'], 'Injury of nerves at lower leg level', 'S84'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Diminished pulse in foot', 'Pale foot', 'Cold foot', 'Bruit'], 'Injury of blood vessels at lower leg level', 'S85'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Calf pain', 'Achilles tendon rupture', 'Inability to stand on toes', 'Tenderness', 'Swelling', 'Muscle weakness'], 'Injury of muscle, fascia and tendon at lower leg level', 'S86'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Compartment syndrome', 'Nerve damage', 'Vascular compromise', 'Crushing deformity'], 'Crushing injury of knee and lower leg', 'S87'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of lower leg/foot', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of knee and lower leg', 'S88'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Knee pain', 'Lower leg pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of knee and lower leg', 'S89'],

    # S90-S99: Injuries to the ankle and foot
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle pain', 'Foot pain', 'Swelling', 'Bruising', 'Redness', 'Abrasion'], 'Superficial injury of ankle, foot and toes', 'S90'],
    ['Global', ['Contamination', 'Direct contact', 'Poor hygiene'], 'Bacterial', ['Bleeding', 'Pain', 'Laceration', 'Puncture wound', 'Risk of infection', 'Tendon exposure'], 'Open wound of ankle, foot and toes', 'S91'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe ankle pain', 'Severe foot pain', 'Inability to bear weight', 'Deformity', 'Swelling', 'Crepitus'], 'Fracture of foot and ankle', 'S92'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle joint pain', 'Instability', 'Ankle giving way', 'Swelling', 'Limited range of motion', 'Ankle sprain'], 'Dislocation, sprain and strain of joints and ligaments of ankle, foot and toes', 'S93'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Numbness in foot', 'Tingling in toes', 'Weakness', 'Loss of sensation', 'Morton\'s neuroma symptoms', 'Burning pain'], 'Injury of nerves at ankle and foot level', 'S94'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Expanding hematoma', 'Active bleeding', 'Poor capillary refill', 'Pale toes', 'Cold toes', 'Loss of pulse'], 'Injury of blood vessels at ankle and foot level', 'S9Z'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Pain with walking', 'Tendon rupture', 'Plantar fasciitis', 'Tenderness', 'Swelling', 'Inability to stand on toes'], 'Injury of muscle, fascia and tendon at ankle and foot level', 'S96'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Severe pain', 'Massive swelling', 'Crushing deformity', 'Mangling injury', 'Vascular compromise', 'Nerve damage'], 'Crushing injury of ankle, foot and toes', 'S97'],
    ['Global', ['Contamination', 'Severe trauma', 'Poor hygiene'], 'Bacterial', ['Loss of foot/toes', 'Severe bleeding', 'Pain', 'Shock', 'Psychological trauma', 'Risk of infection'], 'Traumatic amputation of ankle, foot and toes', 'S98'],
    ['Global', ['N/A - Injury', 'N/A - Injury', 'N/A - Injury'], 'N/A - Injury', ['Ankle pain', 'Foot pain', 'Swelling', 'Bruising', 'Tenderness', 'Unspecified mechanism'], 'Other and unspecified injuries of ankle, foot and toes', 'S99']
]

if __name__ == '__main__':
    # Example of how to access the data
    print(f"Total rows generated: {len(icd_s_data)}")
    print("\n--- Example Row (S00) ---")
    print(f"Geography: {icd_s_data[0][0]}")
    print(f"Transmission: {icd_s_data[0][1]}")
    print(f"Disease Type: {icd_s_data[0][2]}")
    print(f"Symptoms: {icd_s_data[0][3]}")
    print(f"Label: {icd_s_data[0][4]}")
    print(f"ICD Code: {icd_s_data[0][5]}")

    print("\n--- Example Row (S01) ---")
    print(f"Geography: {icd_s_data[1][0]}")
    print(f"Transmission: {icd_s_data[1][1]}")
    print(f"Disease Type: {icd_s_data[1][2]}")
    print(f"Symptoms: {icd_s_data[1][3]}")
    print(f"Label: {icd_s_data[1][4]}")
    print(f"ICD Code: {icd_s_data[1][5]}")
