
def print_msg(msg, error="No Error", *kwargs):
    print("Log: " + error + "\t" + msg)
    print(kwargs)

print_msg("This will be logged", "File not found", "1","2")



def print_msg(msg, error="No Error", **kwargs):
    print("Log: " + error + "\t" + msg)
    print(kwargs)

print_msg("This will be logged", "File not found", Key1 ="1 , 2")