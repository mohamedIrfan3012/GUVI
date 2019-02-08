def main():
   
 numbe = int(input())
 sum = 0
 temp = numbe
 while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
 if numbe == sum:
   print("yes")
 else:
   print("no")

if __name__ == '__main__':
    main()
