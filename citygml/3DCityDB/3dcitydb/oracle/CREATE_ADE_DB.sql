-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-25 18:11:09 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create tables ************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_assessor 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_assessor
(
    id NUMBER(38) NOT NULL,
    email VARCHAR2(1000),
    name VARCHAR2(1000),
    organisation VARCHAR2(1000),
    phonenumber VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_assetdata
(
    id NUMBER(38) NOT NULL,
    assettype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_building 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_building
(
    id NUMBER(38) NOT NULL,
    buildingstate VARCHAR2(1000),
    buildingusage VARCHAR2(1000),
    climatezone VARCHAR2(1000),
    location VARCHAR2(1000),
    sribuildingtype VARCHAR2(1000),
    sridescription VARCHAR2(1000),
    usefulfloorarea VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_controllogic 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_controllogic
(
    id NUMBER(38) NOT NULL,
    controlsystem VARCHAR2(1000),
    controltype VARCHAR2(1000),
    datascale VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_cyberdevicedata
(
    id NUMBER(38) NOT NULL,
    cyberdevicetype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_dataconnector 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_dataconnector
(
    id NUMBER(38) NOT NULL,
    modelschema VARCHAR2(1000),
    urlmodelschema VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_datasource
(
    id NUMBER(38) NOT NULL,
    aquisitionmethod VARCHAR2(1000),
    dataconnectort_urlmodelschem VARCHAR2(1000),
    dataconnectortyp_modelschema VARCHAR2(1000),
    description VARCHAR2(1000),
    name VARCHAR2(1000),
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_designbasisdata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_designbasisdata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    designtype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_device
(
    id NUMBER(38) NOT NULL,
    manufacturer VARCHAR2(1000),
    objectclass_id INTEGER,
    supportedaccesst_description VARCHAR2(1000),
    supportedaccesst_hasendpoint NUMBER,
    supportedaccesstype_hasapi NUMBER,
    supportedprotcolls CLOB,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_energydata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    enduse VARCHAR2(1000),
    energysource VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_functionalitylevel 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_functionalitylevel
(
    id NUMBER(38) NOT NULL,
    description VARCHAR2(1000),
    functionalitylevel INTEGER,
    name VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_indoorenvironmentalda
(
    id NUMBER(38) NOT NULL,
    environmentaldatatype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_informationneed
(
    id NUMBER(38) NOT NULL,
    descriptioninformationneed VARCHAR2(1000),
    objectclass_id INTEGER,
    sriservice_needs_id NUMBER(38),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_interface 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_interface
(
    id NUMBER(38) NOT NULL,
    supportedaccesst_description VARCHAR2(1000),
    supportedaccesst_hasendpoint NUMBER,
    supportedaccesstype_hasapi NUMBER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_methodology
(
    id NUMBER(38) NOT NULL,
    description VARCHAR2(1000),
    preferredservicecatalogue VARCHAR2(1000),
    preferredweightings VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_occupantdata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_occupantdata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    occupanttype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_onsiteenergygeneratio
(
    id NUMBER(38) NOT NULL,
    nonrenewableenergy VARCHAR2(1000),
    other VARCHAR2(1000),
    renewableenergy VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_operationaldata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    other VARCHAR2(1000),
    systemdata VARCHAR2(1000),
    systemtype VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_outdoorenvironmentald
(
    id NUMBER(38) NOT NULL,
    environmentaldatatype VARCHAR2(1000),
    other VARCHAR2(1000),
    source VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_servicecatalogue 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_servicecatalogue
(
    id NUMBER(38) NOT NULL,
    description VARCHAR2(1000),
    version INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriassessment
(
    id NUMBER(38) NOT NULL,
    assessor_id NUMBER(38),
    dateofassessment TIMESTAMP,
    methodology VARCHAR2(1000),
    score INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_sriservice
(
    id NUMBER(38) NOT NULL,
    building_sriservice_id NUMBER(38),
    code VARCHAR2(1000),
    descriptionfunctionalityleve VARCHAR2(1000),
    functionalitylevel INTEGER,
    impact VARCHAR2(1000),
    informationneed_services_id NUMBER(38),
    partofmethoda NUMBER,
    partofmethodb NUMBER,
    preconditions VARCHAR2(1000),
    servicecatalog_sriservice_id NUMBER(38),
    servicegroup VARCHAR2(1000),
    servicename VARCHAR2(1000),
    sharefunctionalitylevel INTEGER,
    sriassessment_sriservice_id NUMBER(38),
    sridomain VARCHAR2(1000),
    userdefined NUMBER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_supportedaccess 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_supportedaccess
(
    id NUMBER(38) NOT NULL,
    description VARCHAR2(1000),
    hasapi NUMBER,
    hasendpoint NUMBER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- SRI_utilitygriddata 
-- -------------------------------------------------------------------- 
CREATE TABLE SRI_utilitygriddata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    other VARCHAR2(1000),
    utilitygridtype VARCHAR2(1000),
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
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_cyberdevicedata ADD CONSTRAINT SRI_cyberdevicedata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_datasource ADD CONSTRAINT SRI_datasourc_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE SRI_datasource ADD CONSTRAINT SRI_datasource_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_designbasisdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_designbasisdata ADD CONSTRAINT SRI_designbasisdata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_device ADD CONSTRAINT SRI_device_objectclass_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE SRI_device ADD CONSTRAINT SRI_device_fk FOREIGN KEY (id)
REFERENCES SRI_datasource (id);

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_energydata ADD CONSTRAINT SRI_energydata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

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

ALTER TABLE SRI_informationneed ADD CONSTRAINT SRI_inform_sriser_needs_fk FOREIGN KEY (sriservice_needs_id)
REFERENCES SRI_sriservice (id);

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_methodology ADD CONSTRAINT SRI_methodology_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- SRI_occupantdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_occupantdata ADD CONSTRAINT SRI_occupantdata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_onsiteenergygeneratio ADD CONSTRAINT SRI_onsiteenergygenerat_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_operationaldata ADD CONSTRAINT SRI_operationaldata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

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

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_inform_servi_fk FOREIGN KEY (informationneed_services_id)
REFERENCES SRI_informationneed (id);

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_sriass_srise_fk FOREIGN KEY (sriassessment_sriservice_id)
REFERENCES SRI_sriassessment (id);

ALTER TABLE SRI_sriservice ADD CONSTRAINT SRI_sriser_servic_srise_fk FOREIGN KEY (servicecatalog_sriservice_id)
REFERENCES SRI_servicecatalogue (id);

-- -------------------------------------------------------------------- 
-- SRI_utilitygriddata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_utilitygriddata ADD CONSTRAINT SRI_utilitygriddata_fk FOREIGN KEY (id)
REFERENCES SRI_informationneed (id);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Indexes ************************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_datasourc_objectcl_fkx ON SRI_datasource (objectclass_id);

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_device_objectclass_fkx ON SRI_device (objectclass_id);

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_informati_objectcl_fkx ON SRI_informationneed (objectclass_id);

CREATE INDEX SRI_inform_srise_needs_fkx ON SRI_informationneed (sriservice_needs_id);

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriassess_assessor_fkx ON SRI_sriassessment (assessor_id);

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
CREATE INDEX SRI_sriser_build_srise_fkx ON SRI_sriservice (building_sriservice_id);

CREATE INDEX SRI_sriser_infor_servi_fkx ON SRI_sriservice (informationneed_services_id);

CREATE INDEX SRI_sriser_servi_srise_fkx ON SRI_sriservice (servicecatalog_sriservice_id);

CREATE INDEX SRI_sriser_srias_srise_fkx ON SRI_sriservice (sriassessment_sriservice_id);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Sequences *********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

CREATE SEQUENCE SRI_sriservice_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE SRI_assessor_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE SRI_informationneed_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE SRI_dataconnector_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE SRI_supportedaccess_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE SRI_functionalityleve_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

