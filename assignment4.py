with open('assignment1.py',"r") as file:
  content = file.read()
with open('assignment.txt',"w") as file:
  file.write("Hello\n"+content)
# User prompt
file1 = input("File to rad from:")
file2 = input("File to write to:")
with open(file1,"r") as file:
  content = file.read()
with open(file2,"w") as file:
  file.write("Hello\n"+content)