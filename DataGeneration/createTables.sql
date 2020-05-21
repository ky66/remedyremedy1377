-- Table: public."Doctors"

-- DROP TABLE public."Doctors";

CREATE TABLE public.doctors
(
    id integer NOT NULL DEFAULT nextval('user_id_seq'::regclass),
    username character varying(50) COLLATE pg_catalog."default",
    password character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (id)
)

CREATE TABLE public.history
(
    id integer NOT NULL DEFAULT nextval('history_id_seq'::regclass),
    patientid integer NOT NULL,
    medical_history character varying(1500) COLLATE pg_catalog."default",
    treatment character varying(1500) COLLATE pg_catalog."default",
    CONSTRAINT "hasHistory" FOREIGN KEY (patientid)
        REFERENCES public.patients (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE public.patients
(
    id integer NOT NULL DEFAULT nextval('patients_id_seq'::regclass),
    name_first character varying(35) COLLATE pg_catalog."default" NOT NULL,
    name_last character varying(35) COLLATE pg_catalog."default" NOT NULL,
    dob date NOT NULL,
    email character varying(254) COLLATE pg_catalog."default",
    address character varying(95) COLLATE pg_catalog."default",
    phone character varying(13) COLLATE pg_catalog."default",
    CONSTRAINT patients_pkey PRIMARY KEY (id)
)

CREATE TABLE public.medication
(
    id integer NOT NULL DEFAULT nextval('medication_id_seq'::regclass),
    patientid integer NOT NULL,
    med_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    startdate date,
    enddate date,
    dose double precision,
    frequency double precision,
    CONSTRAINT medication_pkey PRIMARY KEY (id),
    CONSTRAINT "MedicationToPatient" FOREIGN KEY (patientid)
        REFERENCES public.patients (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE public.visits
(
    id integer NOT NULL DEFAULT nextval('visits_id_seq'::regclass),
    patientid integer NOT NULL,
    visitdate date NOT NULL,
    weight double precision,
    height double precision,
    symptoms character varying(500) COLLATE pg_catalog."default",
    diagnostics character varying(500) COLLATE pg_catalog."default",
    comorbidities character varying(500) COLLATE pg_catalog."default",
    treatment character varying(500) COLLATE pg_catalog."default",
    clinical_progress character varying(500) COLLATE pg_catalog."default",
    support_services character varying(500) COLLATE pg_catalog."default",
    doctor_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT visits_pkey PRIMARY KEY (id),
    CONSTRAINT "VisitsToPatient" FOREIGN KEY (patientid)
        REFERENCES public.patients (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)