import csv
import json

# Set the name of the csv file you are trying to convert and the output json file name that you would like
inputfile = 'example.csv'
outputfile = 'example.json'

# Get the csv file information and convert it to an array
def get_csv_array(filename):
    with open(filename, newline='') as csvfile:
        finalresults = []
        contents = csv.reader(csvfile)
        for row in contents:
            finalresults = finalresults + row
        return finalresults
    
# Save the array as a json file
def save_json_array(arraydata, output_file_name):
    with open(output_file_name, 'w') as file:
        json.dump(arraydata, file, indent=4)

# Main program
def main():
    save_json_array(get_csv_array(inputfile), outputfile)
    print('File is converted')

# Start the program when it is run
if __name__== "__main__":
    main()