-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-08 11:44:22 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create tables ************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_assessor 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_assessor
(
    id BIGINT NOT NULL,
    email VARCHAR(1000),
    name VARCHAR(1000),
    organisation VARCHAR(1000),
    phonenumber VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_assetdata
(
    id BIGINT NOT NULL,
    assettype VARCHAR(1000),
    category VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_building 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_building
(
    id BIGINT NOT NULL,
    buildingstate VARCHAR(1000),
    buildingusage VARCHAR(1000),
    climatezone VARCHAR(1000),
    location VARCHAR(1000),
    sribuildingtype VARCHAR(1000),
    usefulfloorarea VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_controllogic 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_controllogic
(
    id BIGINT NOT NULL,
    controlsystem VARCHAR(1000),
    controltype VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_cyberdevicedata
(
    id BIGINT NOT NULL,
    cyberdevicetype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_datacategorymeta 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_datacategorymeta
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    description VARCHAR(1000),
    designtype VARCHAR(1000),
    objectclass_id INTEGER,
    occupanttype VARCHAR(1000),
    other VARCHAR(1000),
    utilitygridtype VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_domain 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_domain
(
    id BIGINT NOT NULL,
    category VARCHAR(1000),
    description VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_energydata
(
    id BIGINT NOT NULL,
    enduse VARCHAR(1000),
    energysource VARCHAR(1000),
    scale VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_functionalitylevel 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_functionalitylevel
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    functionalitylevel INTEGER,
    id_1 VARCHAR(1000),
    name VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_indoorenvironmentalda
(
    id BIGINT NOT NULL,
    environmentaldatatype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_methodology
(
    id BIGINT NOT NULL,
    preferredservicecatalogue VARCHAR(1000),
    preferredweightings VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_onsiteenergygeneratio
(
    id BIGINT NOT NULL,
    nonrenewableenergy VARCHAR(1000),
    renewableenergy VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_operationaldata
(
    id BIGINT NOT NULL,
    systemdata VARCHAR(1000),
    systemtype VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_outdoorenvironmentald
(
    id BIGINT NOT NULL,
    environmentaldatatype VARCHAR(1000),
    other VARCHAR(1000),
    source VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriassessment
(
    id BIGINT NOT NULL,
    assessor_assessments_id BIGINT,
    dateofassessment TIMESTAMP WITH TIME ZONE,
    fullbuilding NUMERIC,
    methodology_assessments_id BIGINT,
    score INTEGER,
    sriservice_assessments_id BIGINT,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriservice
(
    id BIGINT NOT NULL,
    code VARCHAR(1000),
    domain VARCHAR(1000),
    impact VARCHAR(1000),
    name VARCHAR(1000),
    partofmethod NUMERIC,
    partofmethodb NUMERIC,
    preconditions VARCHAR(1000),
    servicegroup VARCHAR(1000),
    sriassessment_sriservices_id BIGINT,
    userdefined NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_usecase 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_usecase
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    title VARCHAR(1000),
    PRIMARY KEY (id)
);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create foreign keys ******************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_assessor 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_assessor ADD CONSTRAINT SRI_assessor_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_assetdata ADD CONSTRAINT SRI_assetdata_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_building 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_building ADD CONSTRAINT SRI_building_fk FOREIGN KEY (id)
REFERENCES building (id);

-- -------------------------------------------------------------------- 
-- SRI_controllogic 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_controllogic ADD CONSTRAINT SRI_controllogic_fk FOREIGN KEY (id)
REFERENCES SRI_datacategorymeta (id);

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_cyberdevicedata ADD CONSTRAINT SRI_cyberdevicedata_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_datacategorymeta 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_datacategorymeta ADD CONSTRAINT SRI_datacateg_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE SRI_datacategorymeta ADD CONSTRAINT SRI_datacategorymeta_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_domain 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_domain ADD CONSTRAINT SRI_domain_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_energydata ADD CONSTRAINT SRI_energydata_fk FOREIGN KEY (id)
REFERENCES SRI_datacategorymeta (id);

-- -------------------------------------------------------------------- 
-- SRI_functionalitylevel 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_functionalitylevel ADD CONSTRAINT SRI_functionalitylevel_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_indoorenvironmentalda ADD CONSTRAINT SRI_indoorenvironmental_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_methodology ADD CONSTRAINT SRI_methodology_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_onsiteenergygeneratio ADD CONSTRAINT SRI_onsiteenergygenerat_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_operationaldata ADD CONSTRAINT SRI_operationaldata_fk FOREIGN KEY (id)
REFERENCES SRI_datacategorymeta (id);

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_outdoorenvironmentald ADD CONSTRAINT SRI_outdoorenvironmenta_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriassessment_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriass_assess_asses_fk FOREIGN KEY (assessor_assessments_id)
REFERENCES SRI_assessor (id)
ON DELETE SET NULL;

ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriass_method_asses_fk FOREIGN KEY (methodology_assessments_id)
REFERENCES SRI_methodology (id)
ON DELETE SET NULL;

ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriass_sriser_asses_fk FOREIGN KEY (sriservice_assessments_id)
REFERENCES SRI_sriservice (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriservice_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_sriass_srise_fk FOREIGN KEY (sriassessment_sriservices_id)
REFERENCES SRI_sriassessment (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- SRI_usecase 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_usecase ADD CONSTRAINT SRI_usecase_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Indexes ************************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_datacategorymeta 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_datacateg_objectcl_fkx ON SRI_datacategorymeta
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriass_asses_asses_fkx ON SRI_sriassessment
    USING btree
    (
      assessor_assessments_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX SRI_sriass_metho_asses_fkx ON SRI_sriassessment
    USING btree
    (
      methodology_assessments_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX SRI_sriass_srise_asses_fkx ON SRI_sriassessment
    USING btree
    (
      sriservice_assessments_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriser_srias_srise_fkx ON SRI_sriservice
    USING btree
    (
      sriassessment_sriservices_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Sequences *********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
