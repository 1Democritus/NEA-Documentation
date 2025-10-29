# This file contains dataset rows for ICD-10 codes V01-V99 (Transport Accidents)
# as requested. The features have been adapted from "disease" metrics
# to "injury/accident" metrics to match the code range.

# --- Define common feature sets ---

# "Symptoms" for transport accidents are physical injuries
trauma_symptoms = ["Fracture", "Laceration", "Contusion", "Abrasion", "Concussion", "Internal injury"]
head_trauma_symptoms = ["Head injury", "Fracture", "Laceration", "Concussion", "Traumatic brain injury", "Contusion"]
multi_trauma_symptoms = ["Multiple trauma", "Fracture", "Internal bleeding", "Head injury", "Laceration", "Spinal injury"]
water_symptoms_drown = ["Asphyxiation", "Hypoxia", "Water inhalation", "Hypothermia", "Cardiac arrest", "Loss of consciousness"]
water_symptoms_injury = ["Fracture", "Laceration", "Hypothermia", "Contusion", "Head injury", "Sprain"]
unspecified_symptoms = ["Trauma (unspecified)", "Pain", "Laceration", "Fracture", "Head injury", "Contusion"]

# "Transmission" for transport accidents relates to the mechanism of injury
land_transport_mechanism = ["Collision", "Physical impact", "Kinetic energy transfer"]
water_transport_mechanism = ["Submersion", "Impact", "Environmental exposure"]
air_transport_mechanism = ["High-velocity impact", "Deceleration trauma", "Gravitational force"]
unspecified_mechanism = ["Physical impact", "Trauma", "Unspecified event"]


# --- Generate the dataset ---

icd_v_code_data = [
    # V01-V09: Pedestrian injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with pedal cycle",
        "ICD_Code": "V01"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V02"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with car, pick-up truck or van",
        "ICD_Code": "V03"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V04"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedestrian injured in collision with railway train or railway vehicle",
        "ICD_Code": "V05"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedestrian injured in collision with other nonmotor vehicle",
        "ICD_Code": "V06"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Pedestrian injured in other and unspecified transport accidents",
        "ICD_Code": "V09"
    },

    # V10-V19: Pedal cyclist injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with pedestrian or animal",
        "ICD_Code": "V10"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with other pedal cycle",
        "ICD_Code": "V11"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V12"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with car, pick-up truck or van",
        "ICD_Code": "V13"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V14"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with railway train or railway vehicle",
        "ICD_Code": "V15"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with other nonmotor vehicle",
        "ICD_Code": "V16"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Pedal cyclist injured in collision with fixed or stationary object",
        "ICD_Code": "V17"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Pedal cyclist injured in noncollision transport accident",
        "ICD_Code": "V18"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Pedal cyclist injured in other and unspecified transport accidents",
        "ICD_Code": "V19"
    },

    # V20-V29: Motorcycle rider injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with pedestrian or animal",
        "ICD_Code": "V20"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with pedal cycle",
        "ICD_Code": "V21"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V22"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with car, pick-up truck or van",
        "ICD_Code": "V23"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V24"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with railway train or railway vehicle",
        "ICD_Code": "V25"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with other nonmotor vehicle",
        "ICD_Code": "V26"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": head_trauma_symptoms,
        "Label": "Motorcycle rider injured in collision with fixed or stationary object",
        "ICD_Code": "V27"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Motorcycle rider injured in noncollision transport accident",
        "ICD_Code": "V28"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Motorcycle rider injured in other and unspecified transport accidents",
        "ICD_Code": "V29"
    },

    # V30-V39: Occupant of three-wheeled motor vehicle injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with pedestrian or animal",
        "ICD_Code": "V30"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with pedal cycle",
        "ICD_Code": "V31"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V32"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with car, pick-up truck or van",
        "ICD_Code": "V33"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V34"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with railway train or railway vehicle",
        "ICD_Code": "V35"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with other nonmotor vehicle",
        "ICD_Code": "V36"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in collision with fixed or stationary object",
        "ICD_Code": "V37"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in noncollision transport accident",
        "ICD_Code": "V38"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of three-wheeled motor vehicle injured in other and unspecified transport accidents",
        "ICD_Code": "V39"
    },

    # V40-V49: Car occupant injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with pedestrian or animal",
        "ICD_Code": "V40"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with pedal cycle",
        "ICD_Code": "V41"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V42"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with car, pick-up truck or van",
        "ICD_Code": "V43"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Car occupant injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V44"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Car occupant injured in collision with railway train or railway vehicle",
        "ICD_Code": "V45"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with other nonmotor vehicle",
        "ICD_Code": "V46"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in collision with fixed or stationary object",
        "ICD_Code": "V47"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Car occupant injured in noncollision transport accident",
        "ICD_Code": "V48"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Car occupant injured in other and unspecified transport accidents",
        "ICD_Code": "V49"
    },

    # V50-V59: Occupant of pick-up truck or van injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with pedestrian or animal",
        "ICD_Code": "V50"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with pedal cycle",
        "ICD_Code": "V51"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V52"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with car, pick-up truck or van",
        "ICD_Code": "V53"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V54"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with railway train or railway vehicle",
        "ICD_Code": "V55"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with other nonmotor vehicle",
        "ICD_Code": "V56"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in collision with fixed or stationary object",
        "ICD_Code": "V57"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of pick-up truck or van injured in noncollision transport accident",
        "ICD_Code": "V58"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of pick-up truck or van injured in other and unspecified transport accidents",
        "ICD_Code": "V59"
    },

    # V60-V69: Occupant of heavy transport vehicle injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with pedestrian or animal",
        "ICD_Code": "V60"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with pedal cycle",
        "ICD_Code": "V61"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V62"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with car, pick-up truck or van",
        "ICD_Code": "V63"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V64"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with railway train or railway vehicle",
        "ICD_Code": "V65"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with other nonmotor vehicle",
        "ICD_Code": "V66"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in collision with fixed or stationary object",
        "ICD_Code": "V67"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in noncollision transport accident",
        "ICD_Code": "V68"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Occupant of heavy transport vehicle injured in other and unspecified transport accidents",
        "ICD_Code": "V69"
    },

    # V70-V79: Bus occupant injured in transport accident
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with pedestrian or animal",
        "ICD_Code": "V70"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with pedal cycle",
        "ICD_Code": "V71"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with two- or three-wheeled motor vehicle",
        "ICD_Code": "V72"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with car, pick-up truck or van",
        "ICD_Code": "V73"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Bus occupant injured in collision with heavy transport vehicle or bus",
        "ICD_Code": "V74"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Bus occupant injured in collision with railway train or railway vehicle",
        "ICD_Code": "V75"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with other nonmotor vehicle",
        "ICD_Code": "V76"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in collision with fixed or stationary object",
        "ICD_Code": "V77"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Bus occupant injured in noncollision transport accident",
        "ICD_Code": "V78"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Bus occupant injured in other and unspecified transport accidents",
        "ICD_Code": "V79"
    },

    # V80-V89: Other land transport accidents
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Animal-rider or occupant of animal-drawn vehicle injured in transport accident",
        "ICD_Code": "V80"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Occupant of railway train or railway vehicle injured in transport accident",
        "ICD_Code": "V81"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of streetcar injured in transport accident",
        "ICD_Code": "V82"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special vehicle mainly used on industrial premises injured in transport accident",
        "ICD_Code": "V83"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special vehicle mainly used in agriculture injured in transport accident",
        "ICD_Code": "V84"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special construction vehicle injured in transport accident",
        "ICD_Code": "V85"
    },
    {
        "Geography": "Global",
        "Transmission": land_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": trauma_symptoms,
        "Label": "Occupant of special all-terrain or other motor vehicle designed primarily for off-road use, injured in transport accident",
        "ICD_Code": "V86"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Traffic accident of specified type but victim's mode of transport unknown",
        "ICD_Code": "V87"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Nontraffic accident of specified type but victim's mode of transport unknown",
        "ICD_Code": "V88"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Motor- or nonmotor-vehicle accident, type of vehicle unspecified",
        "ICD_Code": "V89"
    },

    # V90-V94: Water transport accidents
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_drown,
        "Label": "Drowning and submersion due to accident to watercraft",
        "ICD_Code": "V90"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_injury,
        "Label": "Other injury due to accident to watercraft",
        "ICD_Code": "V91"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_drown,
        "Label": "Drowning and submersion due to fall overboard",
        "ICD_Code": "V92"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": water_symptoms_injury,
        "Label": "Accident on board watercraft without accident to watercraft, not causing drowning and submersion",
        "ICD_Code": "V93"
    },
    {
        "Geography": "Global",
        "Transmission": water_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other and unspecified water transport accidents",
        "ICD_Code": "V94"
    },

    # V95-V97: Air and space transport accidents
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Accident to powered aircraft causing injury to occupant",
        "ICD_Code": "V95"
    },
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": multi_trauma_symptoms,
        "Label": "Accident to nonpowered aircraft causing injury to occupant",
        "ICD_Code": "V96"
    },
    {
        "Geography": "Global",
        "Transmission": air_transport_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other specified air transport accidents",
        "ICD_Code": "V97"
    },

    # V98-V99: Other and unspecified transport accidents
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Other specified transport accidents",
        "ICD_Code": "V98"
    },
    {
        "Geography": "Global",
        "Transmission": unspecified_mechanism,
        "Disease_Type": "Injury/Trauma",
        "Symptoms": unspecified_symptoms,
        "Label": "Unspecified transport accident",
        "ICD_Code": "V99"
    }
]

# Example of how to use this data (e.g., to write to a CSV)
if __name__ == "__main__":
    import csv

    print(f"Total rows generated: {len(icd_v_code_data)}")
    
    # Get the headers from the first item's keys
    if icd_v_code_data:
        headers = icd_v_code_data[0].keys()
        
        try:
            with open("icd_v_code_dataset.csv", "w", newline="", encoding="utf-8") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(icd_v_code_data)
            
            print("Successfully saved data to 'icd_v_code_dataset.csv'")
            
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print("No data was generated.")
