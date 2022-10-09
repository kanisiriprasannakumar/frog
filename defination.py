import datetime
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
items=['bag','brush','soup','pen']
selected=[]
quantity=[]
cal=[]
print("  ")
n=int(input("press 1  for provisions or press any key for exit:"))    
if n==1:
    for i in range(len(items)):
        w=input("item name:")
        if w in items:
         selected.append(w)
        else:
            continue
        k=int(input("quantity:"))
        quantity.append(k)
    print(40*" ","your selested items are shown below")
    if len(selected)==0:
        print("you are selected none,than q")
    else:   
     for i in range(len(selected)):
         print(40*" ",selected[i],":",quantity[i])
         l=int(input("press  5 for bill or prss 6 for exit "))
else:
        print("you are not selected any thing,than q")    
if l==5:
    for i in range(0,len(selected)):
     amount=(all[selected[i]])*quantity[i]
     print(80*" .")  
     print(50*" ",'than q',25*" ","total bill amount is:",amount)
     print("X"*150) 
else:
    print("you are not buy any items,than q")     

             
           

    
    