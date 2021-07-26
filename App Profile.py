import os
import sys

while True:
    # Main folder path
    pathfile = sys.path[0] + '\\Path.mohz'
    try:
        fhandle = open(pathfile, 'r')
    except: # Create a Path.mohz folder if one does not exist
        fhandle = open(pathfile, 'w+') 
        fhandle.write(sys.path[0] + '\\Profiles')
    path = fhandle.read()
    fhandle.close()

    # Get folders list
    try:
        dirs = os.listdir(path)
    except: 
        dirs = list()
    folders = dict()

    # Remove folders with incorrect naming format and form dictionary with folder numbers as keys
    for folder in dirs:
        foldernum = ""
        folderdeleted = False
        dotpos = folder.find('.')
        
        if dotpos == -1: # File name has no '.'
            folderdeleted = True
        
        for charpos in range(0, dotpos): # File name has non-number before '.'
            if not folder[charpos].isdigit():
                folderdeleted = True
                break
            else:
                foldernum += folder[charpos]

        if not folderdeleted:
            folders[foldernum] = folder

    dirs = list(folders.values())
    dirs.sort()

    # Print folders list
    print('Modes: ')
    for folder in dirs:
        print(folder)
    print('\nC. To change Profiles path \nP. to open Profiles folder \nE. Exit')

    # Use mode
    while True:
        mode = input('Select mode number: ')
        
        if mode == 'c' or mode == 'C': # Change path mode
            newpath = input("Enter new path: ")
            fhandle = open(pathfile, 'w')
            fhandle.write(newpath)
            fhandle.close()
            break # Restarts the whole app with the new path
        
        elif mode == 'p' or mode == "P": # Open Profiles folder
            os.system(r'start %windir%\explorer.exe "' + path + '"')
            sys.exit(1)
        
        elif mode == 'e' or mode == "E": # Exit program
            sys.exit(1)

        else: # Execute mode
            try: # Launch all files in mode
                modepath = path + '\\' + folders[mode]
                dirs = os.listdir(modepath)
                for folder in dirs:
                    if '.' in folder:
                        os.system('"' + modepath + '\\' + folder + '"')
                    else:
                        os.system(r'start %windir%\explorer.exe "' + modepath + '\\' + folder + '"')
                sys.exit(1)
            except Exception:
                print('Incorrect format')
 