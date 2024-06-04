# Process_css.py
This Python script is designed to process a CSV file and separate it into two files: one for “clean” data and one for “unclean” data. The data is considered “clean” if the number of columns in a row matches the number of columns in the header row. If not, the data is considered “unclean”. Here’s a step-by-step breakdown:

Open Files: The script opens the input file in read mode and the two output files in write mode.
Read Header: The script reads the first line of the input file, which is assumed to be the header. It splits the header into parts (columns) based on the comma delimiter.
Initialize Counters: The script initializes counters for the total number of input rows, and the number of clean and unclean rows.

** Additional Functionality **

Write Headers to Output Files: The script writes the header line to both output files.

Process Input File: The script reads the input file line by line. For each line, it increments the total row counter. It then checks if the number of columns in the line matches the number of columns in the header. If it does, the line is written to the clean file and the clean row counter is incremented. If not, the line is written to the unclean file and the unclean row counter is incremented.

Define File Paths: The script first defines the paths for the input CSV file, the output file for clean data, and the output file for unclean data.
Print Results: Finally, the script prints the total number of rows in the input file, and the number of rows in the clean and unclean files.
Call Function: The process_csv function is called with the paths to the input file, clean file, and unclean file.

# Process_csv_pandas
Tried to do the same using pandas, but unable to read the csv becuase of uneven number of columns

# remove_special_characters.py
Data1.csv has unwanted characters in the phone number:
This Python script is designed to clean up a CSV file by removing special characters from specific columns. 

Define File Paths: The script first defines the paths for the input CSV file and the output file.
Read CSV File: The script reads the input CSV file into a pandas DataFrame. The file is assumed to be delimited by the pipe character (|).
Clean PhoneNumber Column: The script removes the +1  prefix and any non-numeric characters from the PhoneNumber column.
Clean Address Column: The script replaces comma-space (, ) and comma (,) with space ( ) in the Address column. Then it replaces space ( ) with comma-space (, ). This could be used to standardize the address format.
Write DataFrame to CSV: The cleaned DataFrame is written to the output CSV file, with the pipe character (|) as the delimiter.
Call Function: The remove_special_char function is called with the path to the input file.
