-- create the relational database tables

-- Patients Table

CREATE TABLE Patients(
    patient_id INT PRIMARY KEY,
    name_first VARCHAR(20),
    name_last VARCHAR(20),
    date_of_intake DATE,
    weight INT,
    height INT,

    date_of_birth DATE,
    sex VARCHAR(10),
    diagnosis VARCHAR(100),
    current_occupation VARCHAR(100),
    area_of_residence VARCHAR(100),
    email VARCHAR(100),
    phone int

);

-- PediatricIntakeVisits table - should initialize a patient into the Patients relation and contain extra visit information

CREATE TABLE PediatricIntakeVisits(
    patient_id PRIMARY KEY FOREIGN KEY REFERENCES Patients.patient_id,          -- TODO: is this allowed / correct synatx for a forign primary key? *?/
    date_of_intake DATE,

-- General health/diagnostic information
    weight FLOAT,
    height FLOAT,
    temp FLOAT,
    head_circumference FLOAT,
    date_of_birth DATE,
    age INT,
    address VARCHAR(100),
    district VARCHAR(100),
    next_of_kin_relationship VARCHAR(50),
    primary_phone_number INT,
    secondary_phone_number INT,
    tertiary_phone_number INT,
    referral_source VARCHAR(100),
    nearest_health_center VARCHAR(100),

--Patient History

    fam_history_febrile_seizures BOOLEAN,
    fam_history_epilepsy BOOLEAN,
    fam_history_epilepsy_side BOOLEAN,       -- TRUE is maternal, FALSE is paternal
    other_siblings_with_epilepsy BOOLEAN,
    antenatal_problems BOOLEAN,
    antenatal_problems_description VARCHAR(100),
    immediate_postnatal_problems BOOLEAN,
    suckle_immediately_after_birth BOOLEAN,
    breathing_difficulties BOOLEAN,
    seizures_in_newborn_period BOOLEAN,
    fam_history_jaundice BOOLEAN,            -- I'm assuming Jondis in the form means Jaundice?
    past_med_history_admission BOOLEAN,
    diagnosis_at_admission VARCHAR(100),
    vaccination_status_card_seen BOOLEAN,
    history_of_neurosurgery BOOLEAN,
    chronic_medical_conditions VARCHAR(100),
    animals_kept_at_home VARCHAR(50),

--Semiology (description of how symptoms developed)
    semiology TEXT(250),
    epileptic_events BOOLEAN,
    non_epileptic_events BOOLEAN,

--Types of Seizures
    --Generalized Seizures
    generalized_tonic_clonic_seizures BOOLEAN,
    tonic_clonic_seizures_onset_date DATE,
    tonic_seizures BOOLEAN,
    tonic_seizures_onset_date DATE,
    clonic_seizures BOOLEAN,
    clonic_seizures_onset_date DATE,
    myoclonic_seizures BOOLEAN,
    myoclonic_seizures_onset_date DATE,
    atonic_seizures BOOLEAN,
    atonic_seizures_onset_date DATE,
    drop_attack_seizures BOOLEAN,
    drop_attack_seizures_onset_date DATE,
    absence_typical_seizures BOOLEAN,
    absence_atypical_seizures BOOLEAN,
    absence_seizures_onset_date DATE,
    epileptic_spasms BOOLEAN,
    epileptic_spasms_onset_date DATE,

    --Focal Seizures
    motor_seizures BOOLEAN,
    motor_seizures_onset_date DATE,
    non_motor_seizures VARCHAR(25), CHECK (non_motor_seizures IN ('automatic', 'behavioral arrest', 'cognitive', 'emotional','sensory')),  --TODO: is this the right syntax for this?
    non_motor_seizures_onset_date DATE,
    focal_seizure_aware BOOLEAN,
    focal_seizure_aware_onset_date DATE,
    focal_seizure_loss_of_awareness BOOLEAN,
    focal_seizure_loss_of_awareness_onset_date DATE,

    seizure_frequency INT,
    seizure_frequency_time_frame VARCHAR(8), CHECK (seizure_frequency_time_frame IN ('daily','weekly','monthly','annually')),
    duration_of_seizure VARCHAR(12), CHECK (duration_of_seizure IN ('<3 minutes','<5 minutes','<15 minutes', '> 1 hour')),
    epilepsy_syndrome VARCHAR(35),

--EEGs / Previous Diagnostic Investigations
    any_laboratory_investigations BOOLEAN,
    laboratory_investigations VARCHAR(50),
    eeg_done BOOLEAN,
    eeg_result VARCHAR(25),
    eeg_date DATE,
    type_of_study BOOLEAN,              -- TRUE is Asleep, FALSE is Awake
    routine_study BOOLEAN,
    non_routine_study BOOLEAN,
    non_routine_study_specification VARCHAR(50),
    eeg_outcome VARCHAR(35), CHECK (eeg_outcome IN ('normal','epileptiform','abnormalities','non-epileptiform abnormalities', 'not done')),             -- TODO: double check that this is what this means
    telemetry_done BOOLEAN,
    telemetry_date DATE,
    generalized_spike_wave VARCHAR(11), CHECK (generalized_spike_wave IN ('<2.5Hz slow', '2.5-3.5Hz','>3.5Hz')),
    focal_spikes VARCHAR(15), CHECK (focal_spikes IN ('temporal', 'extra temporal', 'multifocal')),
    nonepileptiform_abnormalities_focal_slowing VARCHAR(50),

    aetiology VARCHAR(10), CHECK (aetiology IN ('unknown','hereditary','structural','metabolic','infectious','immune')),

--Neuroimaging
    ct_done BOOLEAN,
    ct_normal BOOLEAN,      --TRUE is normal, FALSE is abnormal
    ct_abnormality TEXT(1000),
    mri_done BOOLEAN,
    mri_normal BOOLEAN,      --TRUE is normal, FALSE is abnormal
    mri_abnormality TEXT(1000),

--Comorbidities
    --Developmental Assessment
    cognitive_dq_score VARCHAR(10),         --CDQ static or CDQ regression score
    behavioral_problems TEXT(500),
    --Schooling
    current_class INT,                      --TODO: check if this is an int for grade, or some other data type
    position_in_class INT,                  -- 1 is 1st quarter, 2 is 2nd quarter, 3 is 3rd quarter, 4 is 4th quarter
    class_performance VARCHAR(100),
    missed_school_days BOOLEAN,
    num_missed_school_days INT,
    --Physical Exam
    has_dysmorphic_features BOOLEAN,
    dysmorphic_features VARCHAR(100),
    has_microcephaly BOOLEAN,
    has_macrocephaly BOOLEAN,
    has_cerebral_palsy BOOLEAN,
    cerebral_palsy_specification VARCHAR(50),
    has_cranial_nerve_palsy BOOELAN,
    cranial_nerve_palsy_specification VARCHAR(50),


--Treatment
    previous_treatment_sought BOOLEAN,
    previously_sought_herbal_treatment BOOLEAN,
    previously_sought_medical_treatment BOOLEAN,
    previously_sought_spiritual_treatment BOOLEAN,
    medications_prescribed BOOLEAN,
    medication_prescribed_type VARCHAR(25),
    source_of_medical_treatment VARCHAR(25),

--Clinical Progress
    medically_refractory BOOLEAN,
    surgical_treatment BOOLEAN,
    activity_restriction BOOLEAN,
    activity_restriction_description VARCHAR(100),
    need_for_other_specialist BOOLEAN,
    other_specialist_specification VARCHAR(100),
    dietary_recommendations BOOLEAN,
    dietary_recommendations_description TEXT(500),

--Support services while at the epilepsy clinic
    education_on_epilepsy BOOLEAN,
    education_on_epilepsy_provider VARCHAR(35),
    psychological_counseling BOOLEAN,
    psychological_counseling_provider VARCHAR(35),
    antiepileptic_drug_counseling BOOLEAN,
    antiepileptic_drug_counseling_provider VARCHAR(35),
    education_on_emergency_seizures BOOLEAN,
    education_on_emergency_seizures_provider VARCHAR(35),

--Administrative
    review_date DATE,
    review_site VARCHAR(50),
    clinician INT FOREIGN KEY REFERENCES Doctors.doctor_id,
    clinician_title VARCHAR(25),            -- how to import this from Doctors table?:
    emergency_contacts TEXT(150)

);

-- AdultIntakeVisit - should initialize a patient into the Patients relation and contain extra visit information

CREATE TABLE AdultIntakeVisits(
    patient_id PRIMARY KEY FOREIGN KEY REFERENCES Patients.patient_id,          -- TODO: is this allowed / correct synatx for a forign primary key? *?/
    date_of_assessment DATE,

-- General health/diagnostic information
    history_obtained_from VARCHAR(10),
    has_family_member_with_epilepsy BOOLEAN,
    family_member_
    weight FLOAT,
    height FLOAT,
    temp FLOAT,
    head_circumference FLOAT,
    date_of_birth DATE,
    age INT,
    address VARCHAR(100),
    district VARCHAR(100),
    next_of_kin_relationship VARCHAR(50),
    primary_phone_number INT,
    secondary_phone_number INT,
    tertiary_phone_number INT,
    referral_source VARCHAR(100),
    nearest_health_center VARCHAR(100),
