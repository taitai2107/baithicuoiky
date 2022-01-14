def nameAndID(name):
    nai = name.split(",")
    nai2 = ""
    for i in nai:
        nai2 = nai2 + str(i)
    nai3 = nai2.split(" ")
    nai4 = ""
    for i in nai3:
        nai4 = nai4 + str(i)
    return nai4
    
def nameToTuples(name):
    tup = ()
    li = list(tup)
    for i in name:
        li.append(i)
    return tuple(li)
    
input_name = input("Enter your name: ")
print(nameAndID(input_name))
nai = nameAndID(input_name)
print(nameToTuples(nai))