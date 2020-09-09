import files as f
import encryption_module as encryption
def CreateUser (username, password):
  DirectoryName = username
  f.mkdir (f.JoinPath (f.DirectoryForUsers, DirectoryName) )
  f.mkdir (f.JoinPath (f.DirectoryForUsers, DirectoryName))
  open (DirectoryForUsers + "/" + DirectoryName + "/settings.ini","w+")
  #ove  this file and create a sign in file
  PrevStartupNameAndLoc = r"startup.txt"
  NewStartupNameAndLoc = r"startup.py"
  f.rename (PrevStartupNameAndLoc ,NewStartupNameAndLoc)

def SignInUser (username, PrivateKey, PrimeFactor) :
  encryption.DecryptFile (DirectoryForUsers + "/" + username, "encyption.RSADecrypt", PrivateKey, PrimeFactor)

def SignOutUser (username, PublicKey, PrimeFactor) :
  encryption.EncryptFile (DirectoryForUsers + "/" + username, "encryption.RSaEncrypt", PublicKey, PrimeFactor)
