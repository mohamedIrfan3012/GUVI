def main():
 m=int(input(""))
 tempe=m
 rev=0
 while(m>0):
    dig=m%10
    rev=rev*10+dig
    m=m//10
 if(tempe==rev):
    print("yes")
 else:
    print("no")

if __name__ == '__main__':
    main()
