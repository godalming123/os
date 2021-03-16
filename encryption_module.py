import files
# base RSA encryption functions
def gcd(a, b):
 while b:
  a, b = b, a % b
 return a

def RSAEncrypt (message, public_key, prime_facter) :
   return "".join ([ chr (ord (letter)**public_key % prime_facter) for letter in message ])

class RsaCalcKeys :
	def __init__ (self, prime_1, prime_2) :
		self.prime_factor = prime_1 * prime_2
		totient = (prime_1 - 1) * (prime_2 - 1)
		# calculate the possible public keys where gcd(public_key, totient) == 1, then select the 5th one (this is abritary, any
		# of the public_keys could have been selected
		# (Note above link has an error that the gcd of public_key and totient must be 1, not public_key
		#  and the prime_factor as suggested in the article)
		public_keys = []
		for i in range(totient):
			if gcd(i, totient) == 1:
				public_keys.append(i)
		self.public_key = public_keys[4]
		# calculate the private key based on public key and totient when (public_key * private_key - 1) % totient == 0
		self.private_key = 0
		x = -1
		while x != 0:
			self.private_key += 1
			x = (self.public_key * self.private_key - 1) % totient
		
	def decrypt (self, message_encrypted) :
		return "".join([ chr (ord (letter)**self.private_key % self.prime_facter) for letter in message_encrypted])
	
	def encrypt (self, message) :
		return "".join ([ chr (ord (letter)**self.public_key % self.prime_facter) for letter in message ])

#code

def main () :
  ourEcryption = CalcKeys (13, 17)
  #with EncryptFile ("example encrypt.txt", "encrypt", "'your password'") as encrypted :
  #   print (encrypted.read ())
  while True :
    #RSAencrypted = ourEncryption.encrypt(input ("what do you want to encrypt: "))
    #RSAdecrypted = ourEncryption.decrypt(RSAencrypted)
    #print (RSAencrypted)
    #print (RSAdecrypted)
    #PassEncrypted = encrypt (b"password", b"my data")
    #PassDecrypted = decrypt (b"password", PassEncrypted)
    #print (PassEncrypted)
    #print (PassDecrypted)
    pass
if __name__ == "__main__" :
  main ()
