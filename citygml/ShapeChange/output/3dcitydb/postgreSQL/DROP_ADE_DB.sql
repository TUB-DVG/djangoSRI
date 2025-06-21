-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-06-21 16:07:32 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop foreign keys ********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- sri_assetdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_assetdata
    DROP CONSTRAINT sri_assetdata_fk;

-- -------------------------------------------------------------------- 
-- sri_building 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_building
    DROP CONSTRAINT sri_building_fk;

-- -------------------------------------------------------------------- 
-- sri_communicationprotocol 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_communicationprotocol
    DROP CONSTRAINT sri_communicationprotoc_fk;

-- -------------------------------------------------------------------- 
-- sri_controllogic 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_controllogic
    DROP CONSTRAINT sri_controllogic_fk;

-- -------------------------------------------------------------------- 
-- sri_cyberdevicedata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_cyberdevicedata
    DROP CONSTRAINT sri_cyberdevicedata_fk;

-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_datasource
    DROP CONSTRAINT sri_datasourc_objectcla_fk;

ALTER TABLE sri_datasource
    DROP CONSTRAINT sri_datasource_fk;

-- -------------------------------------------------------------------- 
-- sri_designbasisdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_designbasisdata
    DROP CONSTRAINT sri_designbasisdata_fk;

-- -------------------------------------------------------------------- 
-- sri_energydata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_energydata
    DROP CONSTRAINT sri_energydata_fk;

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_ictequipment
    DROP CONSTRAINT sri_ictequipm_objectcla_fk;

ALTER TABLE sri_ictequipment
    DROP CONSTRAINT sri_ictequipment_fk;

-- -------------------------------------------------------------------- 
-- sri_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_indoorenvironmentalda
    DROP CONSTRAINT sri_indoorenvironmental_fk;

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_informationneed
    DROP CONSTRAINT sri_informationneed_fk;

ALTER TABLE sri_informationneed
    DROP CONSTRAINT sri_inform_sriser_needs_fk;

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_informationneeddataca
    DROP CONSTRAINT sri_informati_objectcla_fk;

ALTER TABLE sri_informationneeddataca
    DROP CONSTRAINT sri_inform_inform_datar_fk;

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_interface
    DROP CONSTRAINT sri_interface_objectcla_fk;

ALTER TABLE sri_interface
    DROP CONSTRAINT sri_interface_fk;

-- -------------------------------------------------------------------- 
-- sri_model 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_model
    DROP CONSTRAINT sri_model_fk;

-- -------------------------------------------------------------------- 
-- sri_occupantdata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_occupantdata
    DROP CONSTRAINT sri_occupantdata_fk;

-- -------------------------------------------------------------------- 
-- sri_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_onsiteenergygeneratio
    DROP CONSTRAINT sri_onsiteenergygenerat_fk;

-- -------------------------------------------------------------------- 
-- sri_operationaldata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_operationaldata
    DROP CONSTRAINT sri_operationaldata_fk;

-- -------------------------------------------------------------------- 
-- sri_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_outdoorenvironmentald
    DROP CONSTRAINT sri_outdoorenvironmenta_fk;

-- -------------------------------------------------------------------- 
-- sri_servicecatalogue 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_servicecatalogue
    DROP CONSTRAINT sri_servicecatalogue_fk;

-- -------------------------------------------------------------------- 
-- sri_sri_sriasses_building 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_sri_sriasses_building
    DROP CONSTRAINT sri_sri_sriasse_buildin_fk;

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_sriassessment
    DROP CONSTRAINT sri_sriassessment_fk;

ALTER TABLE sri_sriassessment
    DROP CONSTRAINT sri_sriassessm_assessor_fk;

ALTER TABLE sri_sriassessment
    DROP CONSTRAINT sri_sriass_sriser_isass_fk;

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_sriservice
    DROP CONSTRAINT sri_sriservice_fk;

ALTER TABLE sri_sriservice
    DROP CONSTRAINT sri_sriser_inform_speci_fk;

ALTER TABLE sri_sriservice
    DROP CONSTRAINT sri_sriser_sriass_ispar_fk;

ALTER TABLE sri_sriservice
    DROP CONSTRAINT sri_sriser_servic_ispar_fk;

-- -------------------------------------------------------------------- 
-- sri_utilitygriddata 
-- -------------------------------------------------------------------- 
ALTER TABLE sri_utilitygriddata
    DROP CONSTRAINT sri_utilitygriddata_fk;

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop tables *************************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- -------------------------------------------------------------------- 
-- sri_assessor 
-- -------------------------------------------------------------------- 
DROP TABLE sri_assessor;

-- -------------------------------------------------------------------- 
-- sri_assetdata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_assetdata;

-- -------------------------------------------------------------------- 
-- sri_building 
-- -------------------------------------------------------------------- 
DROP TABLE sri_building;

-- -------------------------------------------------------------------- 
-- sri_communicationprotocol 
-- -------------------------------------------------------------------- 
DROP TABLE sri_communicationprotocol;

-- -------------------------------------------------------------------- 
-- sri_controllogic 
-- -------------------------------------------------------------------- 
DROP TABLE sri_controllogic;

-- -------------------------------------------------------------------- 
-- sri_cyberdevicedata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_cyberdevicedata;

-- -------------------------------------------------------------------- 
-- sri_dataconnector 
-- -------------------------------------------------------------------- 
DROP TABLE sri_dataconnector;

-- -------------------------------------------------------------------- 
-- sri_datasource 
-- -------------------------------------------------------------------- 
DROP TABLE sri_datasource;

-- -------------------------------------------------------------------- 
-- sri_designbasisdata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_designbasisdata;

-- -------------------------------------------------------------------- 
-- sri_energydata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_energydata;

-- -------------------------------------------------------------------- 
-- sri_ictequipment 
-- -------------------------------------------------------------------- 
DROP TABLE sri_ictequipment;

-- -------------------------------------------------------------------- 
-- sri_indoorenvironmentalda 
-- -------------------------------------------------------------------- 
DROP TABLE sri_indoorenvironmentalda;

-- -------------------------------------------------------------------- 
-- sri_informationneed 
-- -------------------------------------------------------------------- 
DROP TABLE sri_informationneed;

-- -------------------------------------------------------------------- 
-- sri_informationneeddataca 
-- -------------------------------------------------------------------- 
DROP TABLE sri_informationneeddataca;

-- -------------------------------------------------------------------- 
-- sri_interface 
-- -------------------------------------------------------------------- 
DROP TABLE sri_interface;

-- -------------------------------------------------------------------- 
-- sri_model 
-- -------------------------------------------------------------------- 
DROP TABLE sri_model;

-- -------------------------------------------------------------------- 
-- sri_occupantdata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_occupantdata;

-- -------------------------------------------------------------------- 
-- sri_onsiteenergygeneratio 
-- -------------------------------------------------------------------- 
DROP TABLE sri_onsiteenergygeneratio;

-- -------------------------------------------------------------------- 
-- sri_operationaldata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_operationaldata;

-- -------------------------------------------------------------------- 
-- sri_outdoorenvironmentald 
-- -------------------------------------------------------------------- 
DROP TABLE sri_outdoorenvironmentald;

-- -------------------------------------------------------------------- 
-- sri_servicecatalogue 
-- -------------------------------------------------------------------- 
DROP TABLE sri_servicecatalogue;

-- -------------------------------------------------------------------- 
-- sri_sri_sriasses_building 
-- -------------------------------------------------------------------- 
DROP TABLE sri_sri_sriasses_building;

-- -------------------------------------------------------------------- 
-- sri_sriassessment 
-- -------------------------------------------------------------------- 
DROP TABLE sri_sriassessment;

-- -------------------------------------------------------------------- 
-- sri_sriservice 
-- -------------------------------------------------------------------- 
DROP TABLE sri_sriservice;

-- -------------------------------------------------------------------- 
-- sri_supportedaccess 
-- -------------------------------------------------------------------- 
DROP TABLE sri_supportedaccess;

-- -------------------------------------------------------------------- 
-- sri_utilitygriddata 
-- -------------------------------------------------------------------- 
DROP TABLE sri_utilitygriddata;

-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Drop Sequences ************************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

DROP SEQUENCE sri_assessor_seq;

DROP SEQUENCE sri_informationneedda_seq;

DROP SEQUENCE sri_dataconnector_seq;

DROP SEQUENCE sri_supportedaccess_seq;
