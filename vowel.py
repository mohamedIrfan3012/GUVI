list=['a','e','i','o','u','A','E','I','O','U']
a=raw_input()
if(a in list):
	print('Vowel')
elif(a!=list):
	print('Consonant')
else:
	print('invalid')
