def count(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = i*i
    return dict
input_name = input("Enter your name: ")
print("My name: " + input_name)
print(count(int(len(input_name))))