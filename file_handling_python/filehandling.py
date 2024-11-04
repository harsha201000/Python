# Python File Handling

# Read a file
# step 1: open a file
file = open("file.txt",mode= "r",encoding="utf-8")
# step 2: operation
text = file.read()
print(text)
# step 3: close a file
file.close()

# Write a File
# step 1: open a file
file1 = open("hello.txt",mode= "w",encoding="utf-8")
# step 2: operation
file1.write("Hello World, My name is Harsha Malipeddi.")
# step 3: close a file
file1.close()

program = open("output.txt",mode="w",encoding="utf-8")
name = input("Enter your name: ")
age = input("Enter your age: ")
info = [name, age]
program.writelines(info)
program.close()

try:
  prog = open("numbers.txt",mode="w",encoding="utf-8")
  for i in range(0,10):
    prog.writelines(str(i)+"\n")
finally:
  prog.close()
  
 