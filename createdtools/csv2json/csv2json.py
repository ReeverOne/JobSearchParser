import csv
import json

# Get the csv file information and convert it to an array
def get_csv_array(filename): # Input the name of the file
    with open(filename, newline='') as csvfile:
        finalresults = []
        contents = csv.reader(csvfile)
        for row in contents: # Iterate through the row, adding each to the new array
            finalresults = finalresults + row
        return finalresults # Returns the new object as an array
    
# Save the array as a json file
def save_json_array(arraydata, output_file_name):
    with open(output_file_name, 'w') as file:
        json.dump(arraydata, file, indent=4)

# Set the name of the csv file you are trying to convert
inputfile = 'example.csv'
# Set the name of the json file you are saving to
outputfile = 'example.json'

# Main program
def main():
    save_json_array(get_csv_array(inputfile), outputfile)
    print('File is converted')

# Start the program when it is run
if __name__== "__main__":
    main()