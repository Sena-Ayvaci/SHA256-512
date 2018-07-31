from hashlib import sha256
from hashlib import sha512
import argparse

def sha256_en (string256):
	return sha256(string256.encode('UTF-8')).hexdigest()
	
def sha512_en (string512):
	return sha512(string512.encode('UTF-8')).hexdigest()
	
def sha_decode (hashObject, filepath):
	try:
		file = open(filepath, "r")
	except Exception as e:
		print("ERROR: ", str(e))
		exit(1)
		
	for object in file:
		sha256_de = sha256_en(object.strip())
		sha512_de = sha512_en(object.strip())
		if hashObject == sha256_de:
			print("DECODED OBJECT (SHA256): ", hashObject, "RESULT: ", object)
			break
		elif hashObject == sha512_de:
			print("DECODED OBJECT (SHA512): ", hashObject, "RESULT: ", object)
			break
	else:
		print("DID NOT FOUND IN YOUR WORD LIST!")
	file.close()
	
def Main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("-hs","--hashobject",help="use as : -hs [string] or --hashobject [string]",action="store")
	parser.add_argument("-p","--filepath",help="use as : -p [filepath] or --filepath [filepath]",action="store")
	group.add_argument("-e","--encode",help="use as:-hs [object] -e",action="store_true")
	group.add_argument("-d","--decode",help="use as: -hs [object] -p [path] -d",action="store_true")
	args = parser.parse_args()
	
	if args.encode:
		if args.hashobject:
			encode_sha256 = sha256_en(args.hashobject)
			encode_sha512 = sha512_en(args.hashobject)
			print("ENCODED OBJECT (SHA256): ", encode_sha256)
			print("ENCODED OBJECT (SHA512): ", encode_sha512)
	elif args.decode:
		if args.hashobject and args.filepath:
			sha_decode(args.hashobject, args.filepath)
	else:
		print(parser.format_help())
		
if __name__ == '__main__':
	try:
		Main()
	except:
		print("Fail")
		exit(1)