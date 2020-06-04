import requests

def request_api_data(query_char):
	url='https://api.pwnedpasswords.com/range/'+query_char
	res=requests.get(url)
	if res.status_code!=200:
		raise RuntimeError(f'error fetching : {res.status_code} check api and try again!!!!!!')
	return res

#request_api_data('123')