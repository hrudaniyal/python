user_input = input("Enter some data to write to the file: ")
try:
    with open('./file/output.txt', 'w') as file:
        file.write(user_input + '\n')
except:
    print("file not found ")
additional_input = input("Enter additional data to append to the file: ")
try:
    with open('./file/output.txt', 'a') as file:
        file.write(additional_input + '\n')
except:
    print("file not found ")

print("\nFinal content of the file:")
try:
    with open('./file/output.txt', 'r') as file:
        content = file.read()
        print(content)
except:
    print("file not found ")