""" this file uses pure python to generate a has and convert it to binary"""
import random
from werkzeug.security import generate_password_hash


# generate a random number to encrypt
def randGenerator():
    rand_num = random.randint(1, 100)
    print('Random number generated is: ' + str(rand_num))
    return str(rand_num)


# encrypt the number that was generated above
def numEncrypt():
    cipher_num = generate_password_hash(
        randGenerator()
    )
    print("Hash of the number: " + str(cipher_num))

    return cipher_num


# generate it's binary value
def binaryConvert():
    return ' '.join(format(ord(x), 'b') for x in numEncrypt())


print(binaryConvert())
