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
        testDir = Path(userInput)
        
    except:
        print('path went wrong')

    #try:
    for item in testDir.iterdir():
        # GRAB DATA FROM EACH FILE
        grab_name(item.name)

        # GRAB CONTENTS FROM EACH FILE
        newContents = grab_contents(item)

        # PARSE CONTENTS AND WRITE INTO combined_data.txt
        write_contents(newContents)

    #except:
     #   print('ERROR: readin went wrong')

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
    try:
        with open(item, 'r') as file:
            contents = file.read()
            newContents = contents.rsplit(' ', -1)

#        print(newContents)

    except:
        print('ERROR - openFile')

    return newContents

# WRITE Label Class AND Conf TO combined-data.txt
def write_contents(newContents):
    try:
        # CHECK IF Label FILE IS EMPTY AND HAS conf
        #if newContents and len(newContents) == 5: # USE ONLY FOR TESTING FILES W/O Conf
        if newContents and len(newContents) == 6: 
            sign = convert_sign_num(int(newContents[0]))

            # WAIT FOR sign TO Return - MAYBE SUPERFLUOUS
            if sign:
                with open('combined-data.txt', 'a') as file:
                    file.write(sign)
                    file.write(',')
                    file.write(newContents[4])
                    file.write(',') # THIS WILL LEAVE A TRAILING ',' AT THE END OF THE FILE

        # FILL WITH EMPTY COMMAS IF Label FILE IS EMPTY
        else:
            with open('combined-data.txt', 'a') as file:
                file.write('')
                file.write(',')
                file.write('')
                file.write(',') # THIS WILL LEAVE A TRAILING ',' AT THE END OF THE FILE

    except:
        print('ERROR - write_contents')
        print('THIS -> ', newContents)

# CONVERTS Sign Number INTO READABLE Sign Name
def convert_sign_num(newContents):
    sign = ''
    try:
        match newContents:
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
