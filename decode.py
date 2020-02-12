from os import urandom
from ctypes import CDLL
import string
out=input()
global key
key = ""
c = urandom(1)
if len(key)!=5:
    key += str(c)      
global ciphertext
hex_key = key.encode("utf-8").hex()
key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
ciphertext=bytearray.fromhex(out).decode()
ordd=0
for i in range(len(ciphertext)):
	main=(ord(ciphertext[i])^int(key_list[i%5], 16))
	ordd+=(main)
print(ordd)