bal=500
print("read the following otions carefully")
print('''
      
      1)cash diposit
      2)cash withdraw
      3)exit
      4)Balance enqiry
      '''
     )
c=int(input("please enter the number wich action you want to perform from the above: "))
if c==1:
      d=int(input("enter the diposited amount:")) 
      tot=bal+d
      print('available balece is:',bal)
      print('adding amount',d,'total amount after add:',tot)
      print('than q')
elif c==2:
      w=int(input("enter withdraw amount:"))
      tot=bal-w
      print('available balence is:',bal)
      print('withdravel',w,'total amount after deducting:',tot)
      print('than q')
elif c==4:
      print('your current balence is:',bal)      
      
else:
      print('''
            ###############sbi banking###############
            name:ram
            date:20-09-2022
            thanq 
            ''')
                  