n=int(input("enter a number:"))
if n==2:
    print("two is always prime and evennumber")
else:
    print("plese enter a valid number")
for i in range(2,n):
    if n%i==0 and n%n==0:
        print("this is  not  prime number thats you enter:",n)
        break
    else:
        print("this is  a prime prime number that you enterd:",n)
        break

        