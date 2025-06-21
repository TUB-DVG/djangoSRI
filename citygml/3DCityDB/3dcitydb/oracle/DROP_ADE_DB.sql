-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-25 18:11:09 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop foreign keys ********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_assetdata
    DROP CONSTRAINT SRI_assetdata_fk;

-- -------------------------------------------------------------------- 
-- SRI_building 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_building
    DROP CONSTRAINT SRI_building_fk;

-- -------------------------------------------------------------------- 
-- SRI_controllogic 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_controllogic
    DROP CONSTRAINT SRI_controllogic_fk;

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_cyberdevicedata
    DROP CONSTRAINT SRI_cyberdevicedata_fk;

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_datasource
    DROP CONSTRAINT SRI_datasourc_objectcla_fk;

ALTER TABLE SRI_datasource
    DROP CONSTRAINT SRI_datasource_fk;

-- -------------------------------------------------------------------- 
-- SRI_designbasisdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_designbasisdata
    DROP CONSTRAINT SRI_designbasisdata_fk;

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_device
    DROP CONSTRAINT SRI_device_objectclass_fk;

ALTER TABLE SRI_device
    DROP CONSTRAINT SRI_device_fk;

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_energydata
    DROP CONSTRAINT SRI_energydata_fk;

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_indoorenvironmentalda
    DROP CONSTRAINT SRI_indoorenvironmental_fk;

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_informationneed
    DROP CONSTRAINT SRI_informati_objectcla_fk;

ALTER TABLE SRI_informationneed
    DROP CONSTRAINT SRI_inform_sriser_needs_fk;

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_methodology
    DROP CONSTRAINT SRI_methodology_fk;

-- -------------------------------------------------------------------- 
-- SRI_occupantdata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_occupantdata
    DROP CONSTRAINT SRI_occupantdata_fk;

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_onsiteenergygeneratio
    DROP CONSTRAINT SRI_onsiteenergygenerat_fk;

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_operationaldata
    DROP CONSTRAINT SRI_operationaldata_fk;

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_outdoorenvironmentald
    DROP CONSTRAINT SRI_outdoorenvironmenta_fk;

-- -------------------------------------------------------------------- 
-- SRI_servicecatalogue 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_servicecatalogue
    DROP CONSTRAINT SRI_servicecatalogue_fk;

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriassessment
    DROP CONSTRAINT SRI_sriassessment_fk;

ALTER TABLE SRI_sriassessment
    DROP CONSTRAINT SRI_sriassessm_assessor_fk;

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_sriservice
    DROP CONSTRAINT SRI_sriser_buildi_srise_fk;

ALTER TABLE SRI_sriservice
    DROP CONSTRAINT SRI_sriser_inform_servi_fk;

ALTER TABLE SRI_sriservice
    DROP CONSTRAINT SRI_sriser_sriass_srise_fk;

ALTER TABLE SRI_sriservice
    DROP CONSTRAINT SRI_sriser_servic_srise_fk;

-- -------------------------------------------------------------------- 
-- SRI_utilitygriddata 
-- -------------------------------------------------------------------- 
ALTER TABLE SRI_utilitygriddata
    DROP CONSTRAINT SRI_utilitygriddata_fk;

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop tables *************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- SRI_assessor 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_assessor;

-- -------------------------------------------------------------------- 
-- SRI_assetdata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_assetdata;

-- -------------------------------------------------------------------- 
-- SRI_building 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_building;

-- -------------------------------------------------------------------- 
-- SRI_controllogic 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_controllogic;

-- -------------------------------------------------------------------- 
-- SRI_cyberdevicedata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_cyberdevicedata;

-- -------------------------------------------------------------------- 
-- SRI_dataconnector 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_dataconnector;

-- -------------------------------------------------------------------- 
-- SRI_datasource 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_datasource;

-- -------------------------------------------------------------------- 
-- SRI_designbasisdata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_designbasisdata;

-- -------------------------------------------------------------------- 
-- SRI_device 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_device;

-- -------------------------------------------------------------------- 
-- SRI_energydata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_energydata;

-- -------------------------------------------------------------------- 
-- SRI_functionalitylevel 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_functionalitylevel;

-- -------------------------------------------------------------------- 
-- SRI_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_indoorenvironmentalda;

-- -------------------------------------------------------------------- 
-- SRI_informationneed 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_informationneed;

-- -------------------------------------------------------------------- 
-- SRI_interface 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_interface;

-- -------------------------------------------------------------------- 
-- SRI_methodology 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_methodology;

-- -------------------------------------------------------------------- 
-- SRI_occupantdata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_occupantdata;

-- -------------------------------------------------------------------- 
-- SRI_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_onsiteenergygeneratio;

-- -------------------------------------------------------------------- 
-- SRI_operationaldata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_operationaldata;

-- -------------------------------------------------------------------- 
-- SRI_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_outdoorenvironmentald;

-- -------------------------------------------------------------------- 
-- SRI_servicecatalogue 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_servicecatalogue;

-- -------------------------------------------------------------------- 
-- SRI_sriassessment 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_sriassessment;

-- -------------------------------------------------------------------- 
-- SRI_sriservice 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_sriservice;

-- -------------------------------------------------------------------- 
-- SRI_supportedaccess 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_supportedaccess;

-- -------------------------------------------------------------------- 
-- SRI_utilitygriddata 
-- -------------------------------------------------------------------- 
DROP TABLE SRI_utilitygriddata;

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop Sequences ************************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

DROP SEQUENCE SRI_sriservice_seq;

DROP SEQUENCE SRI_assessor_seq;

DROP SEQUENCE SRI_informationneed_seq;

DROP SEQUENCE SRI_dataconnector_seq;

DROP SEQUENCE SRI_supportedaccess_seq;

DROP SEQUENCE SRI_functionalityleve_seq;

PURGE RECYCLEBIN;
