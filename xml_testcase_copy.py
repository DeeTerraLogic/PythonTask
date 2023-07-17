import os
import shutil
import argparse

def copy_xml_testcase_files(search_path):
    home_directory = '/home/'
    
    # Walk through all directories and files in the search path
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                
                # Check if the file contains 'Testcase' string
                with open(file_path, 'r') as f:
                    if 'Testcase' in f.read():
                        # Copy the file to the home directory
                        shutil.copy(file_path, home_directory)
                        print(f"Copied {file} to {home_directory}")
    
    print("Copying completed!")

if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Copy XML Testcase files.')
    
    # Add the '--search' argument
    parser.add_argument('--search', type=str, help='Path to search for XML files.')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Check if the '--search' argument is provided
    if args.search:
        search_path = args.search
        
        # Call the function to copy XML Testcase files
        copy_xml_testcase_files(search_path)
    else:
        print("Please provide the '--search' argument.")
