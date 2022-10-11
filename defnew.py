import datetime
amount=0
f=datetime.datetime.now()
print(50*" ","welcome to super market",25*" ",'Nellore',f)
print(80*" .")
print('''Today available provisions are shown below:
      bag  =50/-
      brush=100/-
      soup =50/-
      pen  =500/-''')
print(40*" ","Type the provision names followed by the quantity")
all={'bag':50,'brush':100,'soup':50,'pen':500,' ':0}
item=['bag','brush','soup','pen']
sel=[]
quan=[]
cal=[]
print("  ")
n=int(input("press 1  for provisions or press any key for exit:"))    
if n==1:
    for i in range(len(item)):
        w=input("item name:")
        if w in item:
         sel.append(w)
        else:
            continue
        k=int(input("quantity:"))
        quan.append(k)
    print(30*" ",">>>your selested items are shown below<<<")
    for i in range(len(sel)):
         print(30*" ",sel[i],":",quan[i])
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
print(50*" ",'than q',25*" ","total bill amount is:",amount)
print("X"*150) 

     

             
           

    
    