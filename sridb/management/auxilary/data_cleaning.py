import pandas as pd


def clean_data(df):
    # Function removes all data, where not relevant content is given
     # clean data codes is not 0 or na 
    # Service ready service does not containt ' User defined smart ready service'
    df = df[df['Code'].notna()]
    df = df[df['Code'] != 0]
    df = df[~df['Smart ready service'].str.contains('User defined smart ready service')]
    return df



def load_building_data(df):

    # Loads and processes the Building Information Sheet
        
    # Check if the Excel file follows the expected schema
    # Import Schema is based on excel sheet version 4.5
    # Simple check if the correct file is used
    if df.loc[3, "Unnamed: 2"] == "ASSESSOR INFORMATION":
           # Create a dictionary to store all the building information
        building_info_dict = {
            'Building State': df.loc[23, "Unnamed: 6"],
            'Building Type': df.loc[16, "Unnamed: 6"],
            'Building Usage': df.loc[17, "Unnamed: 6"],
            'Climate Zone': df.loc[19, "Unnamed: 6"],
            'Location': df.loc[18, "Unnamed: 6"],
            'Useful Floor Area': df.loc[21, "Unnamed: 6"],
            'Description': df.loc[25, "Unnamed: 6"],
            "Assessor Name": df.loc[5, "Unnamed: 6"],
            "Assessor Organisation": df.loc[6, "Unnamed: 6"],
            "Assessor Email": df.loc[7, "Unnamed: 6"],
            "Assessor Phone": df.loc[9, "Unnamed: 6"],
            "Date of Assessment": df.loc[59, "Unnamed: 6"] + " " + df.loc[60, "Unnamed: 6"] + " " + df.loc[61, "Unnamed: 6"],
            "Preffered Methodology": df.loc[35, "Unnamed: 6"],
            "Preffered Service Catalogue": df.loc[37, "Unnamed: 6"]
        }
        return building_info_dict
    elif df.loc[1, "Unnamed: 2"] == "ASSESSOR INFORMATION":
        
        # Create a dictionary to store all the building information
        building_info_dict = {
            'Building State': df.loc[23, "Unnamed: 6"],
            'Building Type': df.loc[14, "Unnamed: 6"],
            'Building Usage': df.loc[15, "Unnamed: 6"],
            'Climate Zone': df.loc[17, "Unnamed: 6"],
            'Location': df.loc[16, "Unnamed: 6"],
            'Useful Floor Area': df.loc[19, "Unnamed: 6"],
            'Description': df.loc[25, "Unnamed: 6"],
            "Assessor Name": df.loc[5, "Unnamed: 6"],
            "Assessor Organisation": df.loc[4, "Unnamed: 6"],
            "Assessor Email": df.loc[7, "Unnamed: 6"],
            "Assessor Phone": df.loc[8, "Unnamed: 6"],
            "Date of Assessment": str(df.loc[57, "Unnamed: 6"]) + " " + str(df.loc[58, "Unnamed: 6"]) + " " + str(df.loc[59, "Unnamed: 6"]),
            "Preffered Methodology": df.loc[35, "Unnamed: 6"],
            "Preffered Service Catalogue": df.loc[37, "Unnamed: 6"]
        }

        return building_info_dict
    else:
        raise ValueError("Different Schema, please update the import function or verify the version of the SRI excel sheet.")
