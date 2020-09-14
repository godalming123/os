from os import *
DirectoryForUsers = "user data/users"#this is refrenced in over files
def JoinPath (*paths) :
  output = ""
  for path in paths :
    output += path
    output += "/"
  print (output)
  
def read (filename):
  with open (filename, "rb").read() as output :
    return output
    
def write (filename, data):
  with open (filename, "wb") as toWrite :
    toWrite.write(data)
    return ToWrite

def OperateOnFile (filename, Function, *Propertyes) :
   file = write (filename, Function (files.read (filename),  Propertyes) ))
   return file
