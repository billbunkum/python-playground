from pathlib import Path
import shutil
import os

# COMPARES THE FILES WITHIN TWO DIRECTORIES WHICH SHOULD BE THE SAME BUT AREN'T
    # ASSUMES first_directory IS LARGER
    # OUTPUTS A results.txt FILE LIST OF THE FILES MISSING FROM second_directory

def main():
    print("yo")
    
        #first_directory = Path('../yolov8/datasets/chevron-turn-winding-project/annotations-labels-and-images-308-6100-and-batch-1-and-2/labels/')
        # 10,000 PHOTOS
    first_directory = Path('../../Dropbox (KTC)/downloaded_photos_URL_imagePathFront/')
    print('ok - first dir read in')

        #second_directory = Path('../yolov8/datasets/chevron-turn-winding-project/annotations-labels-and-images-308-6100-and-batch-1-and-2/images')
        # IMAGES ALREADY ADDED
    second_directory = Path('../yolov8/datasets/chevron-turn-winding-project/Labels-and-images-containing-batch1-batch2-308-to-6100/images/')
    print('ok - second dir read in')

        # CREATE DESTINATION DIR
    destination_dir = Path('../yolov8/datasets/chevron-turn-winding-project/Labels-and-images-containing-batch1-batch2-308-to-6100/Needed-images/')

        # GRAB THE CONTENTS OF BOTH DIRS AND RETURN unique_names FROM first_directory 
    results = readIn(first_directory, second_directory) # results[0] = unique_names; results[1] = first_contents
#    print(len(results[0]), len(results[1]) )

        # USE unique_names TO COPY REMAINING FILES INTO Needed-images/
    copyFiles(results[0], results[1], first_directory, destination_dir)

# READ IN BOTH DIRECTORIES AND THEIR CONTENTS
def readIn(first_directory, second_directory):
    # OPEN AND READ IN FIRST DIRECTORY
    try:
        first_contents = [item.name for item in first_directory.iterdir()]
        print('ok - first dir', first_directory)

    except FileNotFoundError:
        print(first_directory, ' not found')
    except PermissionError:
        print('Permissions denied')

    # OPEN AND READ IN SECOND DIRECTORY
    try:
        second_contents = [item.name for item in second_directory.iterdir()]
        print('ok - second dir', second_directory)

    except FileNotFoundError:
        print(second_directory, ' not found')
    except PermissionError:
        print('Permissions denied')
    
    return cleanContents(first_contents, second_contents), first_contents
   
# STRIP EXTENSION FROM FILE NAMES OF CONTENTS
def cleanContents(first_contents, second_contents):
    try:
        cleaned_first_contents = []
        for item in first_contents:
            cleaned_first_contents.append(item.rsplit('.', 1).pop(0))
        print('ok - cleaned first')
        print('First Folder has', len(cleaned_first_contents), ' files.')
#        print(cleaned_first_contents)

        cleaned_second_contents = []
        for item in second_contents:
            cleaned_second_contents.append(item.rsplit('.', 1).pop(0))
        print('ok - cleaned second')
        print('Second Folder has', len(cleaned_second_contents), ' files.')

    except:
        print('cleanContents - something went wrong!')

    return compareCleaned(cleaned_first_contents, cleaned_second_contents)

def compareCleaned(cleaned_first_contents, cleaned_second_contents):
    try:
        cleaned_first_contents_copy = cleaned_first_contents
        unique_names = []
        for image in cleaned_second_contents:
            for label in cleaned_first_contents_copy:
                if label == image:
                   cleaned_first_contents_copy.remove(label) 

        unique_names = cleaned_first_contents_copy

    except:
        print('compareCleaned - something went wrong!')

    displayResults(unique_names, cleaned_first_contents, cleaned_second_contents)

    # CREATE FILE AND WRITE RESULTS TO IT
    exportResults(unique_names)

    return unique_names

def displayResults(unique_names, cleaned_first_contents, cleaned_second_contents):
    try:
        # NUMBER OF FIRST CONTENTS
        print('There are ', len(cleaned_first_contents), ' label names.')
        # NUMBER OF SECOND CONTENTS
        print('There are ', len(cleaned_second_contents), ' image names.')
        # NUMBER OF UNIQUE NAMES
        print('There are ', len(unique_names), ' unique names.')

    except:
        print('displayResults - something went wrong!')

def exportResults(unique_names):
    try:
        # CREATE A FILE
        new_file = './results.txt' # THE FILE PATH AND NAME
        with open(new_file, 'w') as file: # 'with' CLOSES FILE WHEN FINISHED, 'w' WILL ALLOW FILE TO BE OVERWRITTEN

        # WRITE CONTENTS TO FILE
            for item in unique_names:
                file.write(item)
                file.write('\n')
    
    except:
        print('exportResults - something went wrong!')

def copyFiles(unique_names, first_contents, first_directory, destination_dir):
        # IF FILE MATCHES THEN COPY IT INTO needed_images/
    for file in first_contents:
        for name in unique_names:
            if name == file.rsplit('.', 1)[0]:
                source_file_path = os.path.join(first_directory, file)
                destination_file_path = os.path.join(destination_dir, file)
                    # COPY FROM source TO destination dir
                shutil.copy2(source_file_path, destination_file_path)

#
#
#
# START THE PROGRAM
if __name__ == "__main__":
    main()




# Coded by Bill Bunkum 
# END OF FILE
