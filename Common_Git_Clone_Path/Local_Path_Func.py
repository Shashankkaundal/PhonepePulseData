def Local_Path_Func():
    filename = r"/Users/shashankkaundal/Downloads/PhonepePulseData/Common_Git_Clone_Path/Local_Path.txt"
    with open(filename,"rt") as f:
        text = f.readline()
    local_path = text.strip().split()
    return str(*local_path)
x=Local_Path_Func()
print(x)