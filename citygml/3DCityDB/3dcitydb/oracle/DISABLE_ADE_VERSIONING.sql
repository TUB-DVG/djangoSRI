-- This document was automatically created by the ADE-Manager tool of 3DCityDB (https://www.3dcitydb.org) on 2025-04-10 16:18:54 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
-- *********************************** Disable Versioning ********************************* 
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

exec DBMS_WM.DisableVersioning('SRI_assessor,SRI_assetdata,SRI_building,SRI_controllogic,SRI_cyberdevicedata,SRI_datacategorymeta,SRI_domain,SRI_energydata,SRI_functionalitylevel,SRI_indoorenvironmentalda,SRI_methodology,SRI_onsiteenergygeneratio,SRI_operationaldata,SRI_outdoorenvironmentald,SRI_sriassessment,SRI_sriservice,SRI_usecase,',true, true);
