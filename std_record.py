n=int(input("Number of Student record :"))
i=1
marksheet=[]
while(i<=n):
  print("----------Student--------- :",i)

  rollno=input("Enter Your roll number:")
  course=input("Enter Your Course :")
  name=input("Enter Your Name :")

  n1= int(input("enter your marks in First subject:"))
  n2=int(input("enter your marks in Second subject:"))
  n3=int(input("enter your marks in Third subject:"))
  per=(n1+n2+n3+n4+n5)//5
  std=[rollno,course,name,branch,Fname,Mname,sem,year,n1,n2,n3,n4,n5,per]
  marksheet.append(std)
  i+=1

while(True):
    
  print("\n")
  print(" 1 : All Student record. ")
  print(" 2 : Fail Student . ")
  print(" 3 : Search Student by Roll number. ")
  print(" 4 : Search Student by Name. ")
  print(" 5 : Student by percentage. ")
  print(" 6 : Search by Cource. ")
  print(" 7 : Search by Branch. ")    
  print(" 8 : Search Top student . ")
  print(" 9 : EXIT ")
  print("\n")
  chose=int(input("Enter your Choice: "))
  
  if(chose==1):

     for x in marksheet:
        print("\t\t\t\t\t\t\tRGPV-BHOPAL")
        print(" Roll No. \t: ",x[0],end="\t\t\t\t\t\t\t\t\t\t\tCourse : "+x[1])
        print("\n Name. \t\t: ",x[2],end="\t\t\t\t\t\t\t\t\t\t\tBranch : "+x[3])
        print("\n Father name \t : ",x[4],end="\t\t\t\t\t\t\t\t\t\tSem    : "+x[5])
        print(f"\n Mother name\t: {x[6]}\t\t\t\t\t\t\t\t\t\t\tYear   :{x[7]}")

        print("\n\n")

        print("\tSub-Code",end="\t\t\tSub-Name""\t\t\tMax-Marks""\t\t\tMin-Marks""\t\t\tObtain-Marks\n")

        print("\tME-101",end="\t\t\t\tTHE""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[8]}\n")
        print("\tME-102",end="\t\t\t\tSOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[9]}\n")
        print("\tME-103",end="\t\t\t\tTOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[10]}\n")
        print("\tME-104",end="\t\t\t\tDOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[11]}\n")
        print("\tME-105",end="\t\t\t\tED""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[12]}\n")
        print("\n")
        print("\t\t\t\t\t\tYour Total Percentage is :",x[13])
        print(" Press 9 for Exit : ")
       
    
  elif(chose==2):
      if(x[13]<33):
       for x in marksheet:
         print("\t\t\t\t\t\t\tRGPV-BHOPAL")
         print(" Roll No. \t: ",x[0],end="\t\t\t\t\t\t\t\t\t\t\tCourse : "+x[1])
         print("\n Name. \t\t: ",x[2],end="\t\t\t\t\t\t\t\t\t\t\tBranch : "+x[3])
         print("\n Father name \t : ",x[4],end="\t\t\t\t\t\t\t\t\t\tSem    : "+x[5])
         print(f"\n Mother name\t: {x[6]}\t\t\t\t\t\t\t\t\t\t\tYear   :{x[7]}")
         print("\n\n")
         print("\t\t\t\t\t\tYour Total Percentage is :",x[13])
         
      else:
         print("No one Fail.")

  elif(chose==3):

     for x in marksheet:
       j=input("Enter Roll Number of student : ")
       if(j==x[0]):
       
        print("\t\t\t\t\t\t\tRGPV-BHOPAL")
        print(" Roll No. \t: ",x[0],end="\t\t\t\t\t\t\t\t\t\t\tCourse : "+x[1])
        print("\n Name. \t\t: ",x[2],end="\t\t\t\t\t\t\t\t\t\t\tBranch : "+x[3])
        print("\n Father name \t : ",x[4],end="\t\t\t\t\t\t\t\t\t\tSem    : "+x[5])
        print(f"\n Mother name\t: {x[6]}\t\t\t\t\t\t\t\t\t\t\tYear   :x[7]")

        print("\n\n")

        print("\tSub-Code",end="\t\t\tSub-Name""\t\t\tMax-Marks""\t\t\tMin-Marks""\t\t\tObtain-Marks\n")

        print("\tME-101",end="\t\t\t\tTHE""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[8]}\n")
        print("\tME-102",end="\t\t\t\tSOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[9]}\n")
        print("\tME-103",end="\t\t\t\tTOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[10]}\n")
        print("\tME-104",end="\t\t\t\tDOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[11]}\n")
        print("\tME-105",end="\t\t\t\tED""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[12]}\n")
        print("\n")
        print("\t\t\t\t\t\tYour Total Percentage is :",x[13])
        print(" Press 9 for Exit : ")
       else:
        break
    
  elif(chose==4):

     for x in marksheet:
       j=input("Enter Name of student : ")
       if(j==x[2]):
       
        print("\t\t\t\t\t\t\tRGPV-BHOPAL")
        print(" Roll No. \t: ",x[0],end="\t\t\t\t\t\t\t\t\t\t\tCourse : "+x[1])
        print("\n Name. \t\t: ",x[2],end="\t\t\t\t\t\t\t\t\t\t\tBranch : "+x[3])
        print("\n Father name \t : ",x[4],end="\t\t\t\t\t\t\t\t\t\tSem    : "+x[5])
        print(f"\n Mother name\t: {x[6]}\t\t\t\t\t\t\t\t\t\t\tYear   :{x[7]}")

        print("\n\n")

        print("\tSub-Code",end="\t\t\tSub-Name""\t\t\tMax-Marks""\t\t\tMin-Marks""\t\t\tObtain-Marks\n")

        print("\tME-101",end="\t\t\t\tTHE""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[8]}\n")
        print("\tME-102",end="\t\t\t\tSOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[9]}\n")
        print("\tME-103",end="\t\t\t\tTOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[10]}\n")
        print("\tME-104",end="\t\t\t\tDOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[11]}\n")
        print("\tME-105",end="\t\t\t\tED""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[12]}\n")
        print("\n")
        print("\t\t\t\t\t\tYour Total Percentage is :",x[13])
        print(" Press 9 for Exit : ")
       else:
        break

  elif(chose==5):
     print("/t/tRoll No.\t\t\t\t\tName  \t\t\t\tPercentage ")
     for x in marksheet:
        
        marksheet[std[13]].sort()
        
        print("\t\tRoll No. : {x[0]}\t\t\t\t\t Name :{x[2]}\t\t\t\tPercentage :{x[13]}")
       
  elif(chose==8):

     for x in marksheet:
       top=max(x[13])
       if(top==x[13]):
       
        print("\t\t\t\t\t\t\tRGPV-BHOPAL")
        print(" Roll No. \t: ",x[0],end="\t\t\t\t\t\t\t\t\t\t\tCourse : "+x[1])
        print("\n Name. \t\t: ",x[2],end="\t\t\t\t\t\t\t\t\t\t\tBranch : "+x[3])
        print("\n Father name \t : ",x[4],end="\t\t\t\t\t\t\t\t\t\tSem    : "+x[5])
        print(f"\n Mother name\t: {x[6]}\t\t\t\t\t\t\t\t\t\t\tYear   :x[7]")

        print("\n\n")

        print("\tSub-Code",end="\t\t\tSub-Name""\t\t\tMax-Marks""\t\t\tMin-Marks""\t\t\tObtain-Marks\n")

        print("\tME-101",end="\t\t\t\tTHE""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[8]}\n")
        print("\tME-102",end="\t\t\t\tSOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[9]}\n")
        print("\tME-103",end="\t\t\t\tTOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[10]}\n")
        print("\tME-104",end="\t\t\t\tDOM""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[11]}\n")
        print("\tME-105",end="\t\t\t\tED""\t\t\t\t\t100""\t\t\t\t33"f"\t\t\t\t\t{x[12]}\n")
        print("\n")
        print("\t\t\t\t\t\tYour Total Percentage is :",x[13])
        print(" Press 9 for Exit : ")
       else:
        break
    
  elif(chose==9):
    break