with open('assignment1.py',"r") as file:
  content = file.read()
with open('assignment.txt',"w") as file:
  file.write("Hello\n"+content)