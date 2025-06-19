-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-06-19 11:23:13 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create tables ************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- sri_assessor 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_assessor
(
    id BIGINT NOT NULL,
    email VARCHAR(1000),
    name VARCHAR(1000),
    organisation VARCHAR(1000),
    phonenumber VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_assetdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_assetdata
(
    id BIGINT NOT NULL,
    assettype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_building 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_building
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
-- sri_communicationprotocol 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_communicationprotocol
(
    id BIGINT NOT NULL,
    protocoltype VARCHAR(1000),
    protocolversion VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_controllogic 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_controllogic
(
    id BIGINT NOT NULL,
    controlsystem VARCHAR(1000),
    controltype VARCHAR(1000),
    datascale VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_cyberdevicedata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_cyberdevicedata
(
    id BIGINT NOT NULL,
    cyberdevicetype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_dataconnector 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_dataconnector
(
    id BIGINT NOT NULL,
    documentationurl VARCHAR(1000),
    modelschema VARCHAR(1000),
    modeluri VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_datasource
(
    id BIGINT NOT NULL,
    dataconnectort_documentation VARCHAR(1000),
    dataconnectortyp_modelschema VARCHAR(1000),
    dataconnectortype_modeluri VARCHAR(1000),
    description VARCHAR(1000),
    name VARCHAR(1000),
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_designbasisdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_designbasisdata
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    designtype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_energydata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_energydata
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    enduse VARCHAR(1000),
    energysource VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_functionalitylevel 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_functionalitylevel
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    functionalitylevel INTEGER,
    name VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_ictequipment
(
    id BIGINT NOT NULL,
    devicecategory VARCHAR(1000),
    manufacturer VARCHAR(1000),
    objectclass_id INTEGER,
    supportedaccesst_description VARCHAR(1000),
    supportedaccesst_hasendpoint NUMERIC,
    supportedaccessty_accesstype VARCHAR(1000),
    supportedaccesstype_hasapi NUMERIC,
    supportedprotcols VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_indoorenvironmentalda
(
    id BIGINT NOT NULL,
    environmentaldatatype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_informationneed
(
    id BIGINT NOT NULL,
    descriptioninformationneed VARCHAR(1000),
    sriservice_needs_id BIGINT,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_informationneeddataca
(
    id BIGINT NOT NULL,
    informationn_datarequirem_id BIGINT,
    objectclass_id INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_interface
(
    id BIGINT NOT NULL,
    interfacetype VARCHAR(1000),
    objectclass_id INTEGER,
    supportedaccesst_description VARCHAR(1000),
    supportedaccesst_hasendpoint NUMERIC,
    supportedaccessty_accesstype VARCHAR(1000),
    supportedaccesstype_hasapi NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_model 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_model
(
    id BIGINT NOT NULL,
    aquisitionmethod VARCHAR(1000),
    software VARCHAR(1000),
    type VARCHAR(1000),
    version VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_occupantdata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_occupantdata
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    occupanttype VARCHAR(1000),
    other VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_onsiteenergygeneratio
(
    id BIGINT NOT NULL,
    nonrenewableenergy VARCHAR(1000),
    other VARCHAR(1000),
    renewableenergy VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_operationaldata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_operationaldata
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    other VARCHAR(1000),
    systemdata VARCHAR(1000),
    systemtype VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_outdoorenvironmentald
(
    id BIGINT NOT NULL,
    environmentaldatatype VARCHAR(1000),
    other VARCHAR(1000),
    source VARCHAR(1000),
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_servicecatalogue 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_servicecatalogue
(
    id BIGINT NOT NULL,
    description VARCHAR(1000),
    version INTEGER,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_sriassessment
(
    id BIGINT NOT NULL,
    assessor_id BIGINT,
    dateofassessment TIMESTAMP WITH TIME ZONE,
    methodology VARCHAR(1000),
    score INTEGER,
    sriservice_isassessed_id BIGINT,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_sriservice
(
    id BIGINT NOT NULL,
    code VARCHAR(1000),
    descriptionfunctionalityleve VARCHAR(1000),
    functionalitylevel INTEGER,
    impact VARCHAR(1000),
    informationn_specifiesinf_id BIGINT,
    partofmethoda NUMERIC,
    partofmethodb NUMERIC,
    preconditions VARCHAR(1000),
    servicecatal_ispartofcata_id BIGINT,
    servicegroup VARCHAR(1000),
    servicename VARCHAR(1000),
    sharefunctionalitylevel INTEGER,
    sriassessmen_ispartofasse_id BIGINT,
    sridomain VARCHAR(1000),
    userdefined NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_supportedaccess 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_supportedaccess
(
    id BIGINT NOT NULL,
    accesstype VARCHAR(1000),
    description VARCHAR(1000),
    hasapi NUMERIC,
    hasendpoint NUMERIC,
    PRIMARY KEY (id)
);

-- -------------------------------------------------------------------- 
-- sri_utilitygriddata 
-- -------------------------------------------------------------------- 
CREATE TABLE sri_utilitygriddata
(
    id BIGINT NOT NULL,
    datascale VARCHAR(1000),
    other VARCHAR(1000),
    utilitygridtype VARCHAR(1000),
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
REFERENCES sri_datasource (id);

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
CREATE INDEX sri_datasourc_objectcl_fkx ON sri_datasource
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_ictequipm_objectcl_fkx ON sri_ictequipment
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_inform_srise_needs_fkx ON sri_informationneed
    USING btree
    (
      sriservice_needs_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_inform_infor_datar_fkx ON sri_informationneeddataca
    USING btree
    (
      informationn_datarequirem_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX sri_informati_objectcl_fkx ON sri_informationneeddataca
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_interface_objectcl_fkx ON sri_interface
    USING btree
    (
      objectclass_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_sriassess_assessor_fkx ON sri_sriassessment
    USING btree
    (
      assessor_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX sri_sriass_srise_isass_fkx ON sri_sriassessment
    USING btree
    (
      sriservice_isassessed_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
CREATE INDEX sri_sriser_infor_speci_fkx ON sri_sriservice
    USING btree
    (
      informationn_specifiesinf_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX sri_sriser_servi_ispar_fkx ON sri_sriservice
    USING btree
    (
      servicecatal_ispartofcata_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

CREATE INDEX sri_sriser_srias_ispar_fkx ON sri_sriservice
    USING btree
    (
      sriassessmen_ispartofasse_id ASC NULLS LAST
    )   WITH (FILLFACTOR = 90);

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Create Sequences *********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

CREATE SEQUENCE sri_assessor_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE sri_informationneedda_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE sri_dataconnector_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE sri_functionalityleve_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


CREATE SEQUENCE sri_supportedaccess_seq
INCREMENT BY 1
MINVALUE 0
MAXVALUE 9223372036854775807
START WITH 1
CACHE 1
NO CYCLE
OWNED BY NONE;


