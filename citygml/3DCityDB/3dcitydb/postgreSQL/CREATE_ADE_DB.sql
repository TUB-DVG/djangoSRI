-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-22 21:23:43 
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
    sridescription VARCHAR(1000),
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
    designtype VARCHAR(1000),
    objectclass_id INTEGER,
    occupanttype VARCHAR(1000),
    other VARCHAR(1000),
    utilitygridtype VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_dataconnector 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_dataconnector
(
    id BIGINT NOT NULL,
    modelschema VARCHAR(1000),
    urlmodelschema VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_datasource
(
    id BIGINT NOT NULL,
    aquisitionmethod VARCHAR(1000),
    dataconnectort_urlmodelschem VARCHAR(1000),
    dataconnectortyp_modelschema VARCHAR(1000),
    description VARCHAR(1000),
    name VARCHAR(1000),
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_device
(
    id BIGINT NOT NULL,
    manufacturer VARCHAR(1000),
    objectclass_id INTEGER,
    supportedaccesst_description VARCHAR(1000),
    supportedaccesst_hasendpoint NUMERIC,
    supportedaccesstype_hasapi NUMERIC,
    supportedprotcolls TEXT,
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
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_informationneed
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    objectclass_id INTEGER,
    usecase_informationneed_id BIGINT,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_interface 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_interface
(
    id BIGINT NOT NULL,
    supportedaccesst_description VARCHAR(1000),
    supportedaccesst_hasendpoint NUMERIC,
    supportedaccesstype_hasapi NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_methodology
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
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
-- SRI_servicecatalogue 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_servicecatalogue
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    version INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriassessment
(
    id BIGINT NOT NULL,
    assessor_id BIGINT,
    dateofassessment TIMESTAMP WITH TIME ZONE,
    methodology VARCHAR(1000),
    score INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sridomain 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sridomain
(
    id BIGINT NOT NULL,
    category VARCHAR(1000),
    description VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriservice
(
    id BIGINT NOT NULL,
    building_sriservice_id BIGINT,
    code VARCHAR(1000),
    descriptionfunctionalityleve VARCHAR(1000),
    functionalitylevel INTEGER,
    impact VARCHAR(1000),
    name VARCHAR(1000),
    partofmethod NUMERIC,
    partofmethodb NUMERIC,
    preconditions VARCHAR(1000),
    servicecatalog_sriservice_id BIGINT,
    servicegroup VARCHAR(1000),
    sharefunctionalitylevel INTEGER,
    sriassessment_sriservice_id BIGINT,
    sridomain VARCHAR(1000),
    userdefined NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_supportedaccess 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_supportedaccess
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    hasapi NUMERIC,
    hasendpoint NUMERIC,
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
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_assetdata ADD CONSTRAINT SRI_assetdata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

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
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_datacategorymeta 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_datacategorymeta ADD CONSTRAINT SRI_datacategorymeta_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

ALTER TABLE SRI_datacategorymeta ADD CONSTRAINT SRI_datacateg_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_datasource ADD CONSTRAINT SRI_datasource_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE SRI_datasource ADD CONSTRAINT SRI_datasourc_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_device ADD CONSTRAINT SRI_device_fk FOREIGN KEY (id)
REFERENCES SRI_datasource (id);

ALTER TABLE SRI_device ADD CONSTRAINT SRI_device_objectclass_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_energydata ADD CONSTRAINT SRI_energydata_fk FOREIGN KEY (id)
REFERENCES SRI_datacategorymeta (id);

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_indoorenvironmentalda ADD CONSTRAINT SRI_indoorenvironmental_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_informationneed ADD CONSTRAINT SRI_informati_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE SRI_informationneed ADD CONSTRAINT SRI_inform_usecas_infor_fk FOREIGN KEY (usecase_informationneed_id)
REFERENCES SRI_usecase (id);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_methodology ADD CONSTRAINT SRI_methodology_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_onsiteenergygeneratio ADD CONSTRAINT SRI_onsiteenergygenerat_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_operationaldata ADD CONSTRAINT SRI_operationaldata_fk FOREIGN KEY (id)
REFERENCES SRI_datacategorymeta (id);

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_outdoorenvironmentald ADD CONSTRAINT SRI_outdoorenvironmenta_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_servicecatalogue 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_servicecatalogue ADD CONSTRAINT SRI_servicecatalogue_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriassessment_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE SRI_sriassessment ADD CONSTRAINT SRI_sriassessm_assessor_fk FOREIGN KEY (assessor_id)
REFERENCES SRI_assessor (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_buildi_srise_fk FOREIGN KEY (building_sriservice_id)
REFERENCES SRI_building (id);

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_sriass_srise_fk FOREIGN KEY (sriassessment_sriservice_id)
REFERENCES SRI_sriassessment (id);

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_servic_srise_fk FOREIGN KEY (servicecatalog_sriservice_id)
REFERENCES SRI_servicecatalogue (id);

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
-- SRI_datasource 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_datasourc_objectcl_fkx ON SRI_datasource
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_device_objectclass_fkx ON SRI_device
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_informati_objectcl_fkx ON SRI_informationneed
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX SRI_inform_useca_infor_fkx ON SRI_informationneed
    USING btree
    (
      usecase_informationneed_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriassess_assessor_fkx ON SRI_sriassessment
    USING btree
    (
      assessor_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriser_build_srise_fkx ON SRI_sriservice
    USING btree
    (
      building_sriservice_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX SRI_sriser_servi_srise_fkx ON SRI_sriservice
    USING btree
    (
      servicecatalog_sriservice_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX SRI_sriser_srias_srise_fkx ON SRI_sriservice
    USING btree
    (
      sriassessment_sriservice_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Sequences *********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

CREATE SEQUENCE SRI_sriservice_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_assessor_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_informationneed_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_dataconnector_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_supportedaccess_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_functionalityleve_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE SRI_sridomain_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


