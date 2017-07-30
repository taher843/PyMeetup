
def print_msg(msg, error="No Error", *args, **kwargs):
    print("Log: " + error + "\t" + msg)
    print(kwargs)
    print("Args", args)
    print("Kwargs", kwargs)

print("This will be logged", "File not found", "-13", "-1", "0")#,key_1="1,2,3,4,5", key_2="5,6,7,8")