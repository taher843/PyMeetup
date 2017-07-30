file_name = 'file.txt'

def write():
    with open(file_name,'w') as f:
        f.write("1. Attend the meetup \n")
        f.write("2. Go home and get sleep \n")
        f.write("3. make sure to have lunch before going to bed \n")
    print("File Written successfully")

def append():
    with open(file_name,'a') as d:
        d.write("2. Go home and get sleep \n")
        d.write("3. make sure to have lunch before going to bed \n")
        d.seek(12)
        d.write("This is after seek")
    print("File Written successfully")

append()



