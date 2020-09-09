import files
# base RSA encryption functions
def gcd(a, b):
 while b:
  a, b = b, a % b
 return a

def RSAEncrypt (message, public_key, prime_facter) :
   return "".join ([ chr (ord (letter)**public_key % prime_facter) for letter in message ])

def RSADecrypt (message_encrypted, private_key, prime_facter) :
 return "".join([ chr (ord (letter)**private_key % prime_facter) for letter in message_encrypted])

def CalcKeys (prime_1, prime_2) :
 prime_factor = prime_1 * prime_2
 totient = (prime_1 - 1) * (prime_2 - 1)
 # calculate the possible public keys where gcd(public_key, totient) == 1, then select the 5th one (this is abritary, any
 # of the public_keys could have been selected
 # (Note above link has an error that the gcd of public_key and totient must be 1, not public_key
 #  and the prime_factor as suggested in the article)
 public_keys = []
 for i in range(totient):
   if gcd(i, totient) == 1:
    public_keys.append(i)
 public_key = public_keys[4]
 # calculate the private key based on public key and totient when (public_key * private_key - 1) % totient == 0
 private_key = 0
 x = -1
 while x != 0:
   private_key += 1
   x = (public_key * private_key - 1) % totient
 return prime_factor, public_key, private_key

#base file encryption functions

def OperateOnFile (filename, Function, *Propertyes) :
   file = files.write (filename, Function (files.read (filename),  Propertyes) ))
   return file

#code

def main () :
  prime_factor, public_key, private_key = CalcKeys (13, 17)
  #with EncryptFile ("example encrypt.txt", "encrypt", "'your password'") as encrypted :
  #   print (encrypted.read ())
  while True :
    #RSAencrypted = RSAEncrypt (input ("what do you want to encrypt: "), public_key, prime_factor)
    #RSAdecrypted = RSADecrypt (RSAencrypted, private_key, prime_factor)
    #print (RSAencrypted)
    #print (RSAdecrypted)
    #PassEncrypted = encrypt (b"password", b"my data")
    #PassDecrypted = decrypt (b"password", PassEncrypted)
    #print (PassEncrypted)
    #print (PassDecrypted)
    pass
if __name__ == "__main__" :
  main ()
