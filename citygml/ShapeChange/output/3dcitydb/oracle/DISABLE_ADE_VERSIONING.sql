-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-06-20 01:49:58 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Disable Versioning ********************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

exec DBMS_WM.DisableVersioning('sri_assessor,sri_assetdata,sri_building,sri_communicationprotocol,sri_controllogic,sri_cyberdevicedata,sri_dataconnector,sri_datasource,sri_designbasisdata,sri_energydata,sri_ictequipment,sri_indoorenvironmentalda,sri_informationneed,sri_informationneeddataca,sri_interface,sri_model,sri_occupantdata,sri_onsiteenergygeneratio,sri_operationaldata,sri_outdoorenvironmentald,sri_servicecatalogue,sri_sriassessment,sri_sriservice,sri_supportedaccess,sri_utilitygriddata',true, true);
