### This file loads the data from the SRI calculation sheet and transforms it into the model sheet for the Archetype

import pandas as pd
import os

PATH_SRI_CALCULATION = r"C:\Users\felix\Nextcloud\Back Up\03_Rehmann\04_Paper\11_InformationsSystems\SRI_Version45\SRI3_calculation-sheet_v4.5.xlsx"
SHEET_NAME_SRI_CALCULATION = "overview_of_services"
PATH_ARCHETYPE = r"C:\Users\felix\Nextcloud\Back Up\03_Rehmann\04_Paper\11_InformationsSystems\DigitalArchetypes.xlsx"
SHEET_NAME_ARCHETYPE = "overview_of_archetypes"
# Load the SRI calculation sheet
sri_data = pd.read_excel(PATH_SRI_CALCULATION, sheet_name=SHEET_NAME_SRI_CALCULATION, skiprows=[1,2])
archetype_data = pd.read_excel(PATH_ARCHETYPE, sheet_name=SHEET_NAME_ARCHETYPE)

print(sri_data.columns)
print(archetype_data.head())

FUNCTIONALITY_LEVELS = ["Functionality level 0 (as non-smart default)", "Functionality level 1", "Functionality level 2", "Functionality level 3", "Functionality level 4"]

ARCHETYPE_COLUMNS = ["Energy data",
                    "Indoor environmental data",
                    "Outdoor envionmental data",
                    "System and equipment operational data",
                    "Control setting and logic data",
                    "Occupant data",
                    "Desing basis data",
                    "Building and system asset data",
                    "Utility and grid signal data",
                    "Onsite energy generation data",
                    "Cyber (IoT) device data", "Use Cases"]


# Load the data and split it into different service groups ( Functionality level 0 (as non-smart default)	Functionality level 1	Functionality level 2	Functionality level 3	Functionality level 4) together with the rest of the columns
# Add the text of this service group to the archetype description
# Add the column level and add the value based on the functionality level
# Merge the different dataframes together
# Sort by the value

# Filter all data that has 
# "User defined smart ready service n" and drop it


sri_data = sri_data[~sri_data["Smart ready service"].str.contains("User defined smart ready service")]


list_of_reduced_data = []
for i, functionality_level in enumerate(FUNCTIONALITY_LEVELS):
    columns_to_keep = [col for col in sri_data.columns if col not in FUNCTIONALITY_LEVELS]
    columns_to_keep.append(functionality_level)

    reduced_data = sri_data[columns_to_keep]
    reduced_data.loc[:, "FunctionalityLevel"] = i
    reduced_data.loc[:, "FunctionalityDescription"] = reduced_data.loc[:, functionality_level]
    list_of_reduced_data.append(reduced_data)
    


df_merged = pd.concat(list_of_reduced_data, ignore_index=True)

NEW_NAMES = {"Domain" :"SRIDomain", 
             "Code" : "SRIService",
             "Service Group" : "ServiceGroup",
             "part of the method A: 1 - YES; 0 - NO" : "PartOfMethodA",
             "part of the method B: 1 - YES; 0 - NO" : "PartOfMethodB",
             "part of the custom services list?:  1 - YES; 0 - NO" : "PartOfCustomServicesList",
             "Preconditions / Dependency on other services or building types" : "Preconditions",
             "TRIAGE: 1 - This service affects maximum obtainable score, even if service is not applicable in this building;  0 - This service does not affect maximum obtainable score when not present in building" : "AffectsMaxScore", 
             }
df_merged = df_merged.rename(columns=NEW_NAMES)

# In version 4.5 of the SRI ADE sheet are stated, but hidden in the sheet
# Drop them, as the are not needed for the information modeling sheet
HIDDEN_COLUMNS = [15, "Service included in the selected method (A/B/custom): 0 - not included, 1 - included",
                   	"1 - This domain is present; 2 - This domain is absent but mandatory; 0 - This domain is absent and not mandatory"]

df_merged = df_merged.drop(columns=HIDDEN_COLUMNS)

df_merged = df_merged.drop(columns=FUNCTIONALITY_LEVELS)

df_merged["Preconditions"] = df_merged["Preconditions"].str.replace("Please define your preconditions for this service", "")
df_merged = df_merged.sort_values(by=["SRIService", "FunctionalityLevel"])
df_merged.dropna(subset=["FunctionalityDescription"], inplace=True)
df_merged[ARCHETYPE_COLUMNS] = ""
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
df_merged.to_excel(os.path.join(BASE_PATH, "DigitalArchetypes_BasiscSheet.xlsx"), index=False)


