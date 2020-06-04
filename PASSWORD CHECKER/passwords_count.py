def get_password_leaks_count(hashes,hash_to_check):
	hashes=(line.split(':') for line in hashes.text.splitlines())
	#print(hashes)
	for h,count in hashes:
		#print(h,count)
		if h==hash_to_check:
			return count

	return 0