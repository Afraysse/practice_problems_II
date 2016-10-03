
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
    theline = mynewhandle.readlines()    # try to read next line
    if len(theline) == 0:               # if there are no more lines
        break                           # break loop

    print(theline, end=" ")             # process what's been read

mynewhandle.close()

# for bigger programs, add more logic to body after loop, including parsing through info
# line 28 - surpress the newline character that print usually appends to strings
# because the string already has its own newline: the readline() returns everything up to 
# and including the newline character.

# try to open a file that doesn't, exist; get an error:
>>> mynewhandle = open("whatsup.txt", "r")
IOError: [Errno 2] No such file or directory: "whatsup.txt"

""" FILE INTO A LIST OF LINES """
# to handle incoming information, read everything into list of lines, sort list,
# then write the sorted list back to another file:

f = open("friends.txt", "r")
xs = f.readline()  # reads all lines and returns a list of strings
f.close() 

xs.sort()

g = open("sortedfriends.txt", "w")      # creates new file 
for v in xs:        # iterates through the sorted xs lines
    g.write()       # write sorted list back into new file
g.close()           # close file

""" READING WHOLE FILES AT ONCE """

# another way is to read complete contents of the file into a string 
# then, use string-processing to work with the contents 

# normally use this method if not interested in line structure of file

# count number of words in a file 

# assuming file is in same directory as Python source code
# may need to provide full or relative path to file 
f = open("/home/desktop/somefile.txt")       # no mode: by default, assumes "r" - reading
content = f.read()
f.close()

words = content.split()
print("There are {0} words in the file.").format(len(words))

""" WORKING WITH BINARY FILES """

# files that hold photos, video, zip files, executable programs are
# call 'binary files'

# binary files are not organized into lines and cannot be opened in a normal text editor 
# when read from binary file, you get bytes back - not a string 

# copy one binary file to another
f = open("somefile.txt", "rb")      # 'b' is added to 'rb' to specify binary
g = open("thecopy.txt", "wb")

while True:
    buf = f.read(1024)      # arg: how many bytes to read from file
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()

""" FILTER PROGRAMS """

# alters the context of the file in some way 

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break 
        if text[0] == "#":
            continue            # skips over remaining lines in current iteration of loop, but the loop will still iterate

        # put anymore processing logic here
        outfile.write(text)

    infile.close()
    outfile.close()

""" DIRECTORIES """

# file system: set of rules that organize files on non-volatile storage media
# file systems are made up of file and directories, which are containers for both files and other directories 

# when create a new file and begin writing, the file goes in the current directory (wherever ran the program)
# to find a file elsewhere, have to specify the path - the name of hte directory where file is located

wordsfile = open("/usr/share/dict/words", "r")
wordlist = wordsfile.readlines()
print(wordlist[:6])

>>> ['\n', 'A\n', "A's\n", 'AOL\n', "AOL's\n", 'Achen\n']

# opens a file call words residing in a directory named dict, resides in share, ect. 
# reads in each line into a list using readlines and prints out first 5 elements in that list

""" FETCHING FROM THE WEB """

# copy a URL into a local file 

import urllib.request

url = "http://xml.resource.org/public/rfc/txt/rfc793.txt"
destination_file = "rfc793.txt"

urllib.request.urlretrieve(url, destination_file)

# urlretrieve() can be used to download any kind of content from the internet

# to get right, make sure resource to fetch exists
# need permission to write to the destination filename, and the file will be created in "current directory"
# if behind a proxy server that requires authentication, may require more special handling

# OR rather than save web resource to local disk, read it directly into a string and return it 

import urllib.request

def retrieve_page(url):
    """
    Retrieve contents of this web page.
    Convert contents into a string before returning it.
    """

    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta 

the_text = retrieve_page("http://xml.resource.org/public/rfc/txt/rfc793.txt")
print(the_text)

# opening a remote url returns a socket 
# a socket handles our end of connection between our program and remote web server
# can then call read, write, and close methods on the socket object in the same way with a file handle

################################################################################
""" EXERCISES """

"""
1. Write a program that reads a file and writes out a new file with the lines in reverse order (ie: the first line
    in the old file becomes the last line in a new file).

"""
def reverse_lines(oldfile, newfile):
    f = open("oldfile", "r")
    xs = f.readlines()
    f.close()

    xs.reverse()

    g = open("newfile", "w")
    for v in xs:
        g.write(v)
    g.close()

# OR 

def reverse_lines(oldfile, newfile):
    f = open(oldfile, "r")
    g = open(newfile, "w")

    for line in reversed(f.readlines()):
        g.write(line)

    f.close()
    g.close()

"""
2. Write a program that reads a text file and prints only those lines that containers
the substring 'snake.'
"""

def find_snake(givenFile):
    f = open(givenFile, "r")
    while True:
        text = f.readline()
        if len(text) == 0:
            break 
        if "snake" not in text:
            continue

# OR 

def find_snake(givenFile):
    while True:
        if 'snake' not in open(givenFile).readline():
            continue 
        if len(givenFile.readline()) == 0:
            break 

# OR 

# for better memory conservation 
import mmap 
def find_snake(givenFile):
    f = open(givenFile, "r")
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find('snake') == -1:
        continue
# NOTE: in Python 3, mmaps behave like bytearray objects rather than strings
# so the subseqnece you look for with find as to be in bytes, ie: s.find(b'snake')

""" 
3. Write a program that reads a text file and produces an output file, which is a copy
of the file, except the first five columns of each line contain a four digit line number, 
followed by a space. Start numbering the first line in the output file at 1. Ensure that every
line number is formatted to the same width in the output file. 
"""

def numbered_output(filename):

    # need to improve counter
    g = open("outputfile", "w")

    with open(filename, "r") as f:
        counted = [f.insert(0, ' ' * 5) for line in f.readline()]
    g.write(counted)

    f.close()
    g.close()

"""
4. Look up a term in a file and return the number line. Then write the new line in a new text file. 
"""
def find_term(filename):
    lookup = "hello world"
    with open(filename, "r") as f:
        for num, line in enumerate(f, 1):
            if lookup in line:
                found = 'found at line': num 
    f.close()

    with open("newFile.txt", "w") as g:
        g.write(found)

    g.close()
