import datetime
amount=0
t=0
f=datetime.datetime.now()
print(50*" ","welcome to super market",25*" ",'Nellore',f)
print(80*" .")
print('''Today available provisions are shown below:
      bag  =300/-
      brush=20/-
      soup =30/-
      pen  =10/-
      pencil=15/-
      bucket=200/-
      fant=500/-
      chocolate=40/-''')
print(40*" ","Type the provision names followed by the quantity")
all={'bag':300,'brush':20,'soup':30,'pen':10,'pencil':15,'bucket':15,'fant':500,'chocolate':40}
item=['bag','brush','soup','pen','pencil','bucket','fant','chocolate']
sel=[]
quan=[]
cal=[]
print("  ")
n=(input("press 1  for provisions or press any key for exit:"))    
if n=='1':
    for i in range(len(item)):
        w=input("item name:")
        if w in item:
         sel.append(w)
        else:
            break
        k=int(input("quantity:"))
        quan.append(k)
        a=(all[sel[i]])*quan[i]
        t=a+t
        print(15*" ","current your total bill is:",t,'/-',"(item:",sel[i],"  ","quantity:",quan[i],' ',"tot:", a,'/-',")")
    print(30*" ",">>>your selested items are shown below<<<")
    for i in range(len(sel)):
         print(34*" ",sel[i],":",quan[i]) 
else:
    print("  ")
    print(20*" ","sorry you choose wrong number")         
l=int(input("press  1 for bill or prss 2 for exit "))
if l!=1:
    print(20*" ","you are not purchased  any thing from my shop,than q")    
else:
    for i in range(0,len(sel)):
     a=(all[sel[i]])*quan[i]
     amount=amount+a
print(80*" .")  
print(50*" ",'than q',25*" ","total bill amount is:",amount,10*" ",f)
print("X"*150) 

     

             
           

    
    