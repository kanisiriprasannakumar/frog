import datetime
k=datetime.datetime.now()
print(50*"=",k,58*".","pro:Prasannakumar")
print(50*"=","welcome to Big bujar",75*"=")
print(50*" ",75*" ")
print('''Today available provisions are shown below:
      Brush =20/-
      Tea   =10/-
      Mirchi=50/-''')
l={'brush':20,'tea':10,'mirchi':50}
np=[]
print(50*" ",75*" ")
print(50*"" ,75*" ")
print("NOTE-select the provisions from top to bottom only(random selection not possible)")
print(50*".",75*".")
pro=input("Enter the provision NAME wich you want:")
np.append(pro)
t=int(input("Plese enter the QUANTITY of the above provision:"))
np.append(t)
pro=input("Enter the second provision NAME :")
np.append(pro)
t=int(input("Plese enter the QUANTITY for second provision:"))
np.append(t)
pro=input("Enter the  third provision NAME wich you want:")
np.append(pro)
t=int(input("Plese enter the quantity for third provision:"))
np.append(t)
print("Your selected materials from BIG bujar are:")
print(40*"-",np)
n=int(input("presse 1 for total bill or press 2 to exit::"))
if n==1:
     total=l['brush']*np[1]+l['tea']*np[3]+l['mirchi']*np[5]
     print(75*"=",'your total bill amount is:',total,'/-')
     print(75*"=",'than q--visit again',50*"=")
     print(75*"=",k,50*"=")
     print(75*"=",'Magunta laout,Nellore',50*"=")
elif n!=1:
     print(75*"=",'DONT COME HERE Again for time pass')
     print(75*"=",'than q',50*"=")
     print(75*"=",k,50*"=")
     print(75*"=",'Magunta laout,Nellore',50*"=")
else:
     print("orey one press chey bill kanipistundi")
