from prettytable import PrettyTable
t=PrettyTable(['Particulars','Quantity','Rate'])
amount=int(input("Enter the amount : "))
a=amount 
if a>999:
   b=a//1000
   c=1000*b
   t.add_row([1000,b,c])
   a=a-c
if a>499:
   t.add_row([500,1,500])
   a=a-500
if a>99:
   b=a//100
   c=100*b
   t.add_row([100,b,c])
   a=a-c
if a>49:
   t.add_row([50,1,50])
   a=a-50
if a>19:
   b=a//20
   c=20*b
   t.add_row([20,b,c])
   a=a-c
if a>9:
   t.add_row([10,1,10])
   a=a-10
if a>4:
   t.add_row([5,1,5])
   a=a-5
if a>1:
   b=a//2
   c=b*2
   t.add_row([2,b,c])
   a=a-c
if a>0:
   t.add_row([1,a,a])

print t
print ("TOTAL : {}".format(amount).rjust(30))

