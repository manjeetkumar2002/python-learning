#file_obj = open("file_1.txt","x") # x mode means file_1 will create
# if you run this command again then it give error because file already exist now
# use x mode only when you want to create a file which not exist

# how to read from file
# r is by default no need to write it , if file not exist it give error
# file_obj = open("file_1.txt","r")
# data=file_obj.read()
# print(data)
# print(type(data))

# how to write in a file (it override the new content)
# it file not exist it create that file
# file_obj = open("file_1.txt","w")
# file_obj.write("write the new content here...")
#print(file_obj.read()) #io.UnsupportedOperation: not readable

# how to open in both mode in read as well in write
# first process should be read then write

file_obj = open("file_1.txt","r+")
data = file_obj.read()
print(data)
file_obj.write("hello")

