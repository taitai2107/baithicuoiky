def isReversible(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False
input_name = input("Enter your name: ")
print("My name: " + input_name)
n = int(input("Enter a number "))
print("N is reversible ? : ", isReversible(n))
