import os

def write_file(path) :
    
    isfile = os.path.isfile(path)
    
    if isfile != True:
        print("file not found")
        
    return isfile