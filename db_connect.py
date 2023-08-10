from CRUD import db_fun as sl

def DB_show():
    rec=db.fetchall()
    print("-------------------------------------------")
    print("ID \t NAME \t\t YEAR \t RATING")
    print("-------------------------------------------")
    for x in rec:   
        print(x[0],"\t",x[1],"\t",x[2],"\t",x[3])

import mysql.connector as mysql
con=mysql.connect(host="localhost",user="root",password="root",database="")
mc=con.cursor()
mc.execute("Show databases")
for j in mc:  
  print(j)

data_B=input("Enter Your Database Name:")

con=mysql.connect(host="localhost",user="root",password="root",database=data_B)

data_tb=input("Enter Table Name:")


while (True):
  print("\n")
  print("Press 1 : For Show All Record of Table:")
  print("Press 2 : For Show of Even ID Record of Table:")
  print("Press 3 : For Show of Odd ID Record of Table:")
  print("Press 4 : For Show By Name :")
  print("Press 5 : For Show By Rating:")
  print("Press 6 : For Show By Year:")
  print("Press 7 : For Show All Record Of ID:")
  print("Press 8 : For Show All Record of Name:")
  print("Press 9 : For Show All Record of Year:")
  print("Press 10 : For Show All Record ORDER by year:")
  print("Press 11 : For Show All Total Number of Record:")
  print("Press 12 : For Show All Record of Table:")
  print("Press 0 : EXIT:")
  print("\n")
  
  ch=int(input("Enter Your Choice:- "))
  if (ch==1):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   DB_show()
   
  elif(ch==2):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:
     if ((x[0]%2)==0):
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3])  
      
  elif(ch==3):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:
     if ((x[0]%2)!=0):
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3]) 
      
  elif(ch==4):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   nm=input("Enter Name of data in Name Field: ")
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:
     if (x[1]==nm):
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3]) 
      
  elif(ch==5):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   nm=input("Enter Rating of data in Name Field: ")
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:
     if (x[1]==nm):
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3])
      
  elif(ch==6):
   sql="select * from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   yr=input("Enter Year of data in Name Field: ")
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:
     if (x[2]==yr):
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3]) 
      
  elif (ch==7):
   sql="select id from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("----------------")
   print(" ID :")
   print("----------------")
   for r in rec:
    print(r[0])
    
  elif (ch==8):
   sql="select name from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("----------------")
   print(" NAME :")
   print("----------------")
   for r in rec:
    print(r[0])
    
  elif (ch==9):
   sql="select year from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("----------------")
   print(" YEAR :")
   print("----------------")
   for r in rec:
    print(r[0])
    
  elif (ch==10):
   sql="select * from "+data_tb+" order by year"
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print("-------------------------------------------")
   print("ID \t NAME \t\t YEAR \t RATING")
   print("-------------------------------------------")
   for x in rec:   
      print(x[0],"\t",x[1],"\t",x[2],"\t",x[3])

  elif (ch==11):
   sql="select count(*) from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   print(rec)
   
  elif (ch==14):
   sql="delete from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()
   
  
   
  elif (ch==12):
   sql="select max(rating) from "+data_tb
   db=con.cursor()
   db.execute(sql)
   rec=db.fetchall()

   print(rec)
    
  elif(ch==0):
      break
    

