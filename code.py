source=0
print("enter the destination")
destination=raw_input()
if (destination.isalpha()):
  print("invalid input")
elif not destination:
  print("enter something")
elif float(destination=='$'):
  print("invalid input")
elif float(destination=='@'):
  print("invalid input")
elif float(destination=='#'):
  print("invalid input")
elif float(destination)<=0:
	print("invalid destination")
elif float(destination)>=0:
  total=source+float(destination)
  print("enter the choice")
  print("1.auto...2.mini...3.micro....4.premium")
  ch=(raw_input())
  if (ch.isalpha()) :
		    print("invalid choice")
        
  elif float(ch)==2:
        fare=30*total
        print("the total fare =",fare)
  elif float(ch)==3:
        fare =45*total
        print("the total fare =",fare)
  elif float(ch)==4:
		    fare=60*total
		    print("the total fare =",fare)
  elif float(ch)==1:
        fare=15*total
        print("the total fare =",fare)
  else:
        print("invalid choice")

else:
        print("invalid") 
'''
print("*******************")
print("your destination is",destination)
print("your total fare is",fare)
print("*******************")
'''
