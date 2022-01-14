def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total
def nameToNumber(name):
    arr = name.split()
    num = ""
    for i in arr:
        num = num + str(len(i))
    return num
input_name = input("Enter your name: ")
print("My name: " + input_name)
nameToNumber(input_name)
n = int(nameToNumber(input_name))
print("Sum", n , "is", totalDigitsOfNumber(n))
