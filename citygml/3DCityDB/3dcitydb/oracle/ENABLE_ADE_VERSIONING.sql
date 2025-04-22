-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-22 21:23:43 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Enable Versioning ********************************** 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

exec DBMS_WM.EnableVersioning('SRI_assessor,SRI_assetdata,SRI_building,SRI_controllogic,SRI_cyberdevicedata,SRI_datacategorymeta,SRI_dataconnector,SRI_datasource,SRI_device,SRI_energydata,SRI_functionalitylevel,SRI_indoorenvironmentalda,SRI_informationneed,SRI_interface,SRI_methodology,SRI_onsiteenergygeneratio,SRI_operationaldata,SRI_outdoorenvironmentald,SRI_servicecatalogue,SRI_sriassessment,SRI_sridomain,SRI_sriservice,SRI_supportedaccess,SRI_usecase,','VIEW_WO_OVERWRITE');
