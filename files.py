
""" CREATE FILE """
# opening a file creates a 'file handle'

# myfile refers to the new handle object 
myfile = open("test.txt", "w")
myfile.write("I am writing a file. It is my first file.\n")
myfile.write("----------------------------------------\n")
myfile.write("Hello world!\n")
myfile.close()
# program calls methods on the handle, which makes changes to the actual file

# open(fileName, mode) - takes 2 arguments
# mode - there are different modes dependent upon functionality 
    # "w" - open the file for writing 
