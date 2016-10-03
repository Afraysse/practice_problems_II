
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
# with mode 'w' if there is a file called test.txt, it will be replaced
    # - if there is no test.txt, one will be created

""" READING FILES """

# open in mode 'r' - reading mode 
mynewhandle = open("test.txt", "r")
while True:                             # keep reading forever
    theline = mynewhandle.readline()    # try to read next line
    if len(theline) == 0:               # if there are no more lines
        break                           # break loop

    print(theline, end=" ")             # process what's been read

mynewhandle.close()