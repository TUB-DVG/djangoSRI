-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-06-20 01:49:58 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create tables ************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- sri_assessor 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_assessor
(
    id NUMBER(38) NOT NULL,
    email VARCHAR2(1000),
    name VARCHAR2(1000),
    organisation VARCHAR2(1000),
    phonenumber VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_assetdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_assetdata
(
    id NUMBER(38) NOT NULL,
    assettype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_building 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_building
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
-- sri_communicationprotocol 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_communicationprotocol
(
    id NUMBER(38) NOT NULL,
    protocoltype VARCHAR2(1000),
    protocolversion VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_controllogic 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_controllogic
(
    id NUMBER(38) NOT NULL,
    controlsystem VARCHAR2(1000),
    controltype VARCHAR2(1000),
    datascale VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_cyberdevicedata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_cyberdevicedata
(
    id NUMBER(38) NOT NULL,
    cyberdevicetype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_dataconnector 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_dataconnector
(
    id NUMBER(38) NOT NULL,
    documentationurl VARCHAR2(1000),
    modelschema VARCHAR2(1000),
    modeluri VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_datasource
(
    id NUMBER(38) NOT NULL,
    dataconnectort_documentation VARCHAR2(1000),
    dataconnectortyp_modelschema VARCHAR2(1000),
    dataconnectortype_modeluri VARCHAR2(1000),
    description VARCHAR2(1000),
    name VARCHAR2(1000),
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_designbasisdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_designbasisdata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    designtype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_energydata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_energydata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    enduse VARCHAR2(1000),
    energysource VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_ictequipment
(
    id NUMBER(38) NOT NULL,
    devicecategory VARCHAR2(1000),
    manufacturer VARCHAR2(1000),
    objectclass_id INTEGER,
    supportedaccesst_description VARCHAR2(1000),
    supportedaccesst_hasendpoint NUMBER,
    supportedaccessty_accesstype VARCHAR2(1000),
    supportedaccesstype_hasapi NUMBER,
    supportedprotcols VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_indoorenvironmentalda
(
    id NUMBER(38) NOT NULL,
    environmentaldatatype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_informationneed
(
    id NUMBER(38) NOT NULL,
    descriptioninformationneed VARCHAR2(1000),
    sriservice_needs_id NUMBER(38),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_informationneeddataca
(
    id NUMBER(38) NOT NULL,
    informationn_datarequirem_id NUMBER(38),
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_interface
(
    id NUMBER(38) NOT NULL,
    interfacetype VARCHAR2(1000),
    objectclass_id INTEGER,
    software VARCHAR2(1000),
    supportedaccesst_description VARCHAR2(1000),
    supportedaccesst_hasendpoint NUMBER,
    supportedaccessty_accesstype VARCHAR2(1000),
    supportedaccesstype_hasapi NUMBER,
    version VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_model 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_model
(
    id NUMBER(38) NOT NULL,
    aquisitionmethod VARCHAR2(1000),
    software VARCHAR2(1000),
    type VARCHAR2(1000),
    version VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_occupantdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_occupantdata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    occupanttype VARCHAR2(1000),
    other VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_onsiteenergygeneratio
(
    id NUMBER(38) NOT NULL,
    nonrenewableenergy VARCHAR2(1000),
    other VARCHAR2(1000),
    renewableenergy VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_operationaldata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_operationaldata
(
    id NUMBER(38) NOT NULL,
    datascale VARCHAR2(1000),
    other VARCHAR2(1000),
    systemdata VARCHAR2(1000),
    systemtype VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_outdoorenvironmentald
(
    id NUMBER(38) NOT NULL,
    environmentaldatatype VARCHAR2(1000),
    other VARCHAR2(1000),
    source VARCHAR2(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_servicecatalogue 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_servicecatalogue
(
    id NUMBER(38) NOT NULL,
    description VARCHAR2(1000),
    version INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_sriassessment
(
    id NUMBER(38) NOT NULL,
    assessor_id NUMBER(38),
    dateofassessment TIMESTAMP,
    methodology CLOB,
    score INTEGER,
    sriservice_isassessed_id NUMBER(38),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_sriservice
(
    id NUMBER(38) NOT NULL,
    code VARCHAR2(1000),
    descriptionfunctionalityleve VARCHAR2(1000),
    functionalitylevel INTEGER,
    impact VARCHAR2(1000),
    informationn_specifiesinf_id NUMBER(38),
    partofmethoda NUMBER,
    partofmethodb NUMBER,
    preconditions VARCHAR2(1000),
    servicecatal_ispartofcata_id NUMBER(38),
    servicegroup VARCHAR2(1000),
    servicename VARCHAR2(1000),
    sharefunctionalitylevel INTEGER,
    sriassessmen_ispartofasse_id NUMBER(38),
    sridomain VARCHAR2(1000),
    userdefined NUMBER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_supportedaccess 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_supportedaccess
(
    id NUMBER(38) NOT NULL,
    accesstype VARCHAR2(1000),
    description VARCHAR2(1000),
    hasapi NUMBER,
    hasendpoint NUMBER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_utilitygriddata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_utilitygriddata
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
-- sri_assetdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_assetdata ADD CONSTRAINT sri_assetdata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_building 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_building ADD CONSTRAINT sri_building_fk FOREIGN KEY (id)
REFERENCES building (id);

-- -------------------------------------------------------------------- 
-- sri_communicationprotocol 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_communicationprotocol ADD CONSTRAINT sri_communicationprotoc_fk FOREIGN KEY (id)
REFERENCES sri_ictequipment (id);

-- -------------------------------------------------------------------- 
-- sri_controllogic 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_controllogic ADD CONSTRAINT sri_controllogic_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_cyberdevicedata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_cyberdevicedata ADD CONSTRAINT sri_cyberdevicedata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_datasource ADD CONSTRAINT sri_datasourc_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE sri_datasource ADD CONSTRAINT sri_datasource_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- sri_designbasisdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_designbasisdata ADD CONSTRAINT sri_designbasisdata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_energydata ADD CONSTRAINT sri_energydata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_ictequipment ADD CONSTRAINT sri_ictequipm_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE sri_ictequipment ADD CONSTRAINT sri_ictequipment_fk FOREIGN KEY (id)
REFERENCES sri_datasource (id);

-- -------------------------------------------------------------------- 
-- sri_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_indoorenvironmentalda ADD CONSTRAINT sri_indoorenvironmental_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_informationneed ADD CONSTRAINT sri_informationneed_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE sri_informationneed ADD CONSTRAINT sri_inform_sriser_needs_fk FOREIGN KEY (sriservice_needs_id)
REFERENCES sri_sriservice (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_informationneeddataca ADD CONSTRAINT sri_informati_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE sri_informationneeddataca ADD CONSTRAINT sri_inform_inform_datar_fk FOREIGN KEY (informationn_datarequirem_id)
REFERENCES sri_informationneed (id);

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_interface ADD CONSTRAINT sri_interface_objectcla_fk FOREIGN KEY (objectclass_id)
REFERENCES objectclass (id);

ALTER TABLE sri_interface ADD CONSTRAINT sri_interface_fk FOREIGN KEY (id)
REFERENCES sri_datasource (id);

-- -------------------------------------------------------------------- 
-- sri_model 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_model ADD CONSTRAINT sri_model_fk FOREIGN KEY (id)
REFERENCES sri_datasource (id);

-- -------------------------------------------------------------------- 
-- sri_occupantdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_occupantdata ADD CONSTRAINT sri_occupantdata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_onsiteenergygeneratio ADD CONSTRAINT sri_onsiteenergygenerat_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_operationaldata ADD CONSTRAINT sri_operationaldata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_outdoorenvironmentald ADD CONSTRAINT sri_outdoorenvironmenta_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- -------------------------------------------------------------------- 
-- sri_servicecatalogue 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_servicecatalogue ADD CONSTRAINT sri_servicecatalogue_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_sriassessment ADD CONSTRAINT sri_sriassessment_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE sri_sriassessment ADD CONSTRAINT sri_sriassessm_assessor_fk FOREIGN KEY (assessor_id)
REFERENCES sri_assessor (id)
ON DELETE SET NULL;

ALTER TABLE sri_sriassessment ADD CONSTRAINT sri_sriass_sriser_isass_fk FOREIGN KEY (sriservice_isassessed_id)
REFERENCES sri_sriservice (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_sriservice ADD CONSTRAINT sri_sriservice_fk FOREIGN KEY (id)
REFERENCES cityobject (id);

ALTER TABLE sri_sriservice ADD CONSTRAINT sri_sriser_inform_speci_fk FOREIGN KEY (informationn_specifiesinf_id)
REFERENCES sri_informationneed (id)
ON DELETE SET NULL;

ALTER TABLE sri_sriservice ADD CONSTRAINT sri_sriser_sriass_ispar_fk FOREIGN KEY (sriassessmen_ispartofasse_id)
REFERENCES sri_sriassessment (id)
ON DELETE SET NULL;

ALTER TABLE sri_sriservice ADD CONSTRAINT sri_sriser_servic_ispar_fk FOREIGN KEY (servicecatal_ispartofcata_id)
REFERENCES sri_servicecatalogue (id)
ON DELETE SET NULL;

-- -------------------------------------------------------------------- 
-- sri_utilitygriddata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_utilitygriddata ADD CONSTRAINT sri_utilitygriddata_fk FOREIGN KEY (id)
REFERENCES sri_informationneeddataca (id);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Indexes ************************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_datasourc_objectcl_fkx ON sri_datasource (objectclass_id);

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_ictequipm_objectcl_fkx ON sri_ictequipment (objectclass_id);

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_inform_srise_needs_fkx ON sri_informationneed (sriservice_needs_id);

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_inform_infor_datar_fkx ON sri_informationneeddataca (informationn_datarequirem_id);

CREATE INDEX sri_informati_objectcl_fkx ON sri_informationneeddataca (objectclass_id);

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_interface_objectcl_fkx ON sri_interface (objectclass_id);

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_sriassess_assessor_fkx ON sri_sriassessment (assessor_id);

CREATE INDEX sri_sriass_srise_isass_fkx ON sri_sriassessment (sriservice_isassessed_id);

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_sriser_infor_speci_fkx ON sri_sriservice (informationn_specifiesinf_id);

CREATE INDEX sri_sriser_servi_ispar_fkx ON sri_sriservice (servicecatal_ispartofcata_id);

CREATE INDEX sri_sriser_srias_ispar_fkx ON sri_sriservice (sriassessmen_ispartofasse_id);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Sequences *********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

CREATE SEQUENCE sri_assessor_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE sri_informationneedda_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE sri_dataconnector_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

CREATE SEQUENCE sri_supportedaccess_seq INCREMENT BY 1 START WITH 1 MINVALUE 1 CACHE 10000;

