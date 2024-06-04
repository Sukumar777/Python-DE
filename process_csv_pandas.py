import os.path
import pandas as pd

def process_csv_pandas(input_file, clean_file_p, unclean_file_p):
    with open(input_file, mode='r') as inputFile:
        # We need to read the first header line from the input csv file
        header = inputFile.readline().strip()
        sections = len(header.split(','))
        df = pd.read_csv(input_file, sep =',')
        """ Tried using pandas, unable to load the csv file dues to uneven  number of columns"""


# Paths for input file
input_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Input_data_file\data.csv')
# paths for cleanfile and uncleanfile
clean_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Output_data_file\cleanfile.csv')
unclean_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Output_data_file\uncleanfile.csv')

process_csv_pandas(input_file, clean_file_p, unclean_file_p)
