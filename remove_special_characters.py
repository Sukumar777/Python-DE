import pandas as pd
import os.path


def remove_special_char(input_file):
    df = pd.read_csv(input_file, delimiter='|')
    # Remove the special characters from the PhoneNumber
    df['PhoneNumber'] = df['PhoneNumber'].str.replace('+1 ', '')
    df["PhoneNumber"] = df["PhoneNumber"].str.replace(r'[^0-9]', '', regex=True)

    df["Address"] = df["Address"].str.replace(", ", " ")
    df["Address"] = df["Address"].str.replace(",", " ")
    df["Address"] = df["Address"].str.replace(" ", ", ")

    df.to_csv(output_file, index=False, sep="|")


input_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Input_data_file\data1.csv')
output_file = os.path.expanduser(
    r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Output_data_file\cleaned_unwanted_char.csv')
remove_special_char(input_file)
