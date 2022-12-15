import os

       

def check_for_file(path) :
    
    isfile = os.path.isfile(path)
    
    if isfile == True:
        print("file found")

    return isfile
    
    