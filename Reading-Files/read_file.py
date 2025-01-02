#inputFile.txt contains the data of driving test - name, age, and P or F
inputFile=open("inputFile.txt","r")
print(inputFile.read())
inputFile.close() 

print("*"*45)
# built-in function to count the number of lines in inputFile
inputFile=open("inputFile.txt","r")
print(len(inputFile.readlines()))
inputFile.close() 

print("*"*45)
#Print only the passed students
inputFile=open("inputFile.txt","r")
for line in inputFile:
    line_split=line.split()
    if line_split[2]=="P":
        print(line)
inputFile.close() 