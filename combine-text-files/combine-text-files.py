from pathlib import Path
import os

# READS THROUGH A LABEL FOLDER'S TXT FILE ANNOTATIONS
    # OUTPUTS THE File Name, Sign Type, AND Conf
    # INTO A FILE - combined-data.txt 
# IF THE TXT FILE IS EMPTY, OUTPUTS THE NAME AND ,, INSTEAD
# ADDS A TRAILING , AT THE END OF THE FILE DATA

def main():

    # PROMPT USER FOR DIRECTORY
    try:
        userInput = input(r'Type the directory path: ')
        userInput = userInput.replace('\\', '\\\\')
        testDir = Path(userInput)
        
    except:
        print('path went wrong')

    # GRAB CONTENTS FROM EACH FILE
    for item in testDir.iterdir():
        grab_contents(item)

# CREATES NEW FILE combined-data.csv 
def grab_name(file_name):
    try:
        with open('combined-data.txt', 'a') as file:
            file.write(file_name)
            file.write(',')

    except:
        print('ERROR - write file_name')

# OPENS EACH FILE TO GET CONTENTS - file name, label no., AND conf
def grab_contents(item):

    with open(item, 'r') as file:
        contents = file.read()
        contentsLines = [line.strip() for line in contents.splitlines()] # STRIP \n AND CREATE LIST contentsLines
        package = []
 
        if contentsLines:
            if len(contentsLines) != 1: # IF MORE THAN ONE BOUNDING BOX IN FILE
               for line in contentsLines:
                   package.append(item.name) # ADD File name
                   newContents = line.rsplit(' ', -1) # FORMAT SO HAS INDEXES
                   package.append(newContents[0]) # GRAB Sign Num
                   package.append(newContents[5]) # GRAB Conf
                   write_contents(package) # WRITE THE GOODS
                   package = [] # RESET package FOR NEXT line

            else: # IF ONLY ONE BOUNDING BOX
                package.append(item.name) # ADD File name
                contentsLinesString = contentsLines[0] # CONVERT List INTO A String
                newContents = contentsLinesString.rsplit(' ', -1) # FORMAT SO HAS INDEXES
                package.append(newContents[0]) # GRAB Sign Num
                package.append(newContents[5]) # GRAB Conf
                write_contents(package) # WRITE THE GOODS

# WRITE Label Class AND Conf TO combined-data.txt
def write_contents(package): # package = [File name, Sign, Conf]

    try:
        # CHECK IF FILE HAS BOUNDING BOX INFORMATION
        if len(package) == 3:
            sign = convert_sign_num(int(package[1]))

            with open('combined-data.txt', 'a') as file:
                file.write(package[0]) # WRITE File name 
                file.write(',')
                file.write(sign) # WRITE Sign
                file.write(',')
                file.write(package[2]) # WRITE Conf
                file.write(',') # THIS WILL LEAVE A TRAILING ',' AT THE END OF THE FILE

        # FILL WITH EMPTY COMMAS IF Label FILE IS EMPTY
        else:
            with open('combined-data.txt', 'a') as file:
                file.write(package[0]) # WRITE File name
                file.write(',')
                file.write('') # Sign PLACEHOLDER
                file.write(',')
                file.write('') # Conf PLACEHOLDER
                file.write(',') # THIS WILL LEAVE A TRAILING ',' AT THE END OF THE FILE

    except:
        print('ERROR - write_contents')
        print('THIS -> ', package)

# CONVERTS Sign Number INTO READABLE Sign Name
def convert_sign_num(package):
    sign = ''
    try:
        match package:
            case 0:
                sign = 'Chevron Left'
            case 1:
                sign = 'Chevron Right'
            case 2:
                sign = 'Curve Left'
            case 3:
                sign = 'Curve Right'
            case _:
                sign = 'Winding Road'

    except:
        print('ERROR - match case')

    return sign
#
#
#
# START THE PROGRAM
if __name__ == '__main__':
    main()


# Coded by Bill Bunkum
# END OF FILE
