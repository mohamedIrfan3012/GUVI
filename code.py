source=0
print("enter the destination")
destination=int(input())
if destination<1:
	print("invalid destination")
  
else:
  total=source+destination
  print("enter the choice")
  print("1.auto...2.mini...3.micro....4.premium")
  ch=int(input())
  if ch==1:
        fare=15*total
        print("the total fare =",fare)
  elif ch==2:
        fare=30*total
        print("the total fare =",fare)
  elif ch==3:
        fare =45*total
        print("the total fare =",fare)
  elif ch==4:
		    fare=60*total
		    print("the total fare =",fare)
  else :
		    print("invalid choice")
