import os.path

def process_csv(input_file, clean_file, unclean_file):

    with open(input_file, mode = 'r') as inputFile, open(clean_file, mode = 'w') as cleanFile, open(unclean_file, mode = 'w') as uncleanFile:
        # We need to read the first header line from the input csv file
        header = inputFile.readline().strip()
        header_parts = header.split(',') # here specify the delimiter

        expected_parts = len(header_parts) #here we get the number of columns based on the header

        input_rows = 0
        clean_rows = 0
        unclean_rows = 0

        # writing the header to both output files
        cleanFile.write(header + '\n')
        uncleanFile.write(header + '\n')

        for line in inputFile:
            line = line.strip()
            parts = line.split(',')
            input_rows += 1

            if len(parts) == expected_parts:
                cleanFile.write(line + '\n')
                clean_rows += 1
            else:
                uncleanFile.write(line + '\n')
                unclean_rows += 1
        print(f"Number of rows in Input file: {input_rows}")
        print(f"Number of rows in Clean file: {clean_rows}")
        print(f"Number of rows in Unclean file: {unclean_rows}")

#path for input file
input_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Input_data_file\data.csv')
# paths for cleanfile and uncleanfile
clean_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Output_data_file\cleanfile.csv')
unclean_file = os.path.expanduser(r'C:\Users\Sukumar\Desktop\DE\Python\Project_1\processing_csv\Output_data_file\uncleanfile.csv')

process_csv(input_file, clean_file, unclean_file)

