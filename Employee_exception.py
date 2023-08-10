n=int(input("Enter number of field reqired to print : "))
cmp=[]

i=1
while(i<=n):
    print("Employee: ",i)
    try:
      empname=input("Enter Emplyee Name :")
      empid=int(input("Enter Employee ID :"))
      dgn=input("Enter Emplyee Designation :")
      slr=int(input("Enter Emplyee Salary : "))
      emp=[empname,empid,dgn,slr]
      cmp.append(emp)
      i+=1
    except ValueError:
        print("Please Enter valid Value")
print("\n")
print(" 1 : All Emplyee record. ")
print(" 2 : Emplyee salary greater then 16000. ")
print(" 3 : Emplyee salary less then 7000. ")
print(" 4 : Emplyee salary between 10,000 - 13,000. ")
print(" 5 : Even Id Records. ")
print(" 6 : Odd Id Records. ")
print(" 7 : Designation is Manager. ")    
print(" 8 : Total salary of clerk. ")
print(" 9 : EXIT ")
print("\n")

while(True):
  
  chose=int(input("Enter your choice :"))

  if(chose==1):
   print("\t Name \t\t Emplyee ID \t\t\t Designamtion \t\t\t Salary")
   for x in cmp:
     print("\t",x[0],"\t\t",x[1],"\t\t\t\t\t",x[2],"\t\t\t\t",x[3])
   
  elif(chose==2):
    print("\tName\t\tEmplyee ID\t\t\tDesignamtion\t\tSalary")
    flag=0
    for x in cmp:
     if (x[3]>=15000):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
     elif flag==1:
         print("Record not found:")
         break
         
  elif(chose==3):
    print("\tName\t\tEmplyee ID\t\t\tDesignamtion\t\tSalary")
    flag=0
    for x in cmp:
     if (x[3]<=7000):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
     elif flag==1:
         print("Record not found:")     
         
  elif(chose==4):
    print("\tName \t\t Emplyee ID \t\t\t Designamtion \t\t Salary")
    flag=0
    for x in cmp:
     if (x[3]>=10000 and x[3]<=13000):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
       flag=1
     elif flag==0:
         print("Record not found:") 
         break
  elif(chose==5):
    print("\t Name \t\t Emplyee ID \t\t\t Designamtion \t\t Salary")
    flag=0
    for x in cmp:
     if (x[1]%2==0):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
       flag=1
     elif flag==0:
         print("Record not found:") 
         break

  elif(chose==6):
    print("\t Name \t\t Emplyee ID \t\t\t Designamtion \t\t Salary")
    flag=0
    for x in cmp:
     if (x[1]%2!=0):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
       flag=1
     elif flag==0:
         print("Record not found:") 
         break
     
  elif(chose==7):
    print("\t Name \t\t Emplyee ID \t\t\t Designamtion \t\t Salary")
    flag=0
    for x in cmp:
     if (x[2]=="manager"):
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
       flag=1
     elif flag==0:
         print("Record not found:") 
         break
     
  elif(chose==8):
    print("\t Name \t\t Emplyee ID \t\t\t Designamtion \t\t Salary")
    
    sum=0
    for x in cmp:
     if (x[2]=="clerk"): 
       print("\t",x[0],"\t\t",x[1],"\t\t\t",x[2],"\t\t\t\t",x[3])
       
       sum=sum+x[3]
     elif flag==0:
         print("Record not found:") 
         break
    print("total Salary of clerk :",sum)
    
  elif(chose==9):
      break
  
    
  
    
  
    
  