from check_passsword import pwned_api_check
import sys

def main(args):
	for password in args:
		count=pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times ..You should change it....')
		else:
			print(f'{password} was NOt Found ...Carry on ')


main(sys.argv[1:])