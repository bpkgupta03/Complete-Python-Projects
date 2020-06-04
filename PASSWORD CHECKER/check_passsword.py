import requests
import hashlib
import request_api_modules
from read_response_text import read_res
from passwords_count import get_password_leaks_count

def pwned_api_check(passsword):

	#print(hashlib.sha1(passsword.encode('utf-8')).hexdigest().upper())
	sha1password=hashlib.sha1(passsword.encode('utf-8')).hexdigest().upper()
	first5_char,tail=sha1password[:5],sha1password[5:]
	#print(first5_char,tail)
	response=request_api_modules.request_api_data(first5_char)
	#read_response=read_res(response)
	#print(response)
	#return read_response
	return get_password_leaks_count(response,tail)

#pwned_api_check('12345678')