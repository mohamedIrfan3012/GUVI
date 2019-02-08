while True:
	try:
		d, b= raw_input().split( )
		d=int(d)
		b=int(b)
		break
	except:
		print("Invalid input")
		break
c=1
for x in range(b):
	c=c*d
print(c)
