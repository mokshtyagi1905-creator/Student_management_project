def menu():

   while True:
    print("-------------------------------------------")
    print("          Student Management V1.0          ")
    print("-------------------------------------------")
    print()
    print("1. Add Student ")
    print("2. View All Students")
    print("3. View Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print()

    choice = input("Enter Your Choice (1-6): ")

    if choice in ["1","2","3","4","5","6"]:
        return choice
    else:
        print("invalid Input! PLease Enter The Number From 1 To 6\n ")

def add_students():

    print("---------------Add Student----------------")

    roll=input("Enter the student's roll number: ")
    print()

    name=input("Enter the student name: ")
    print()

    age=input("Enter the age: ")
    print()

    branch=input("Enter the student's branch: ")
    print()

    marks=input("Enter the student's marks: ")
    print()

    print("-------------------------------------------")
    print()
    print("   Student Details Added Successfully!!")

    student={
    "roll":roll,
    "name":name,
    "age":age,
    "branch":branch,
    "marks":marks
    }

    return student

students=[]

def view_students(students):

  if len(students)==0:
   print("There is no student record yet!! ")
  else:  
   print("---------------------------")
   print("Total Students: ",len(students)) 
   print("---------------------------")
   print()

   for student in students:
      print("------------------------")
      print("Roll: ",student["roll"])
      print("Name: ",student["name"])
      print("Age: ",student["age"])
      print("Branch: ",student["branch"])
      print("Marks: ",student["marks"])
      print()

   print("---------------------------")

def search_student(students):
   print("---------------------------")
   user_roll=input("Enter The Roll Number: ")
   print("---------------------------")
   found=0

   for student in students:
      if user_roll==student["roll"]:
         found+=1
         print("Student Found")
         print()
         print("Roll: ",student["roll"])
         print("Name: ",student["name"])
         print("Age: ",student["age"])
         print("Branch: ",student["branch"])
         print("Marks: ",student["marks"])
         print()
         print("---------------------------")
         break

   if found==0:     
      print("Student Not Found!!") 

def update_student(students):
   print("--------------Update_Student---------------")
   user_roll=input("Enter The Roll Number")
   print("-------------------------------------------")
   print()

   found=0

   for student in students:
      if user_roll==student["roll"]:
         found+=1

         print("Student Found")
         print()
         print("Roll: ",student["roll"])
         print("Name: ",student["name"])
         print("Age: ",student["age"])
         print("Branch: ",student["branch"])
         print("Marks: ",student["marks"])
         print()

         while True:
          print("---------------------------")          
          print("1. Name")
          print("2. Age")
          print("3. Branch")
          print("4. Marks")
          print("5. Cancel")
          print()

          number=input("Enter The Number of Field To Update: ")
          print("---------------------------")

          if number=="1":
            student["name"]=input("Enter The Updated Name: ")
            break
          elif number=="2":
            student["age"]=input("Enter The Updated Age: ")
            break 
          elif number=="3":
            student["branch"]=input("Enter The Updated Branch: ")
            break
          elif number=="4":
            student["marks"]=input("Enter The Updated Marks: ")
            break
          elif number=="5":
            return
          else:
            print("Invalid Choice!!")

         print()
         print("---------------------------")
         print("Updated Record")
         print()
         print("Roll: ",student["roll"])
         print("Name: ",student["name"])
         print("Age: ",student["age"])
         print("Branch: ",student["branch"])
         print("Marks: ",student["marks"])
         print()
         print("---------------------------")
         print("Student Data Updated Successfully!!")
         print()
         break

   if found==0:
      print("Student Not Found!!")            

def del_student(students):
  print("-----------------------------")
  user_roll=input("Enter The Roll Number To Delete Student: ")
  print("-----------------------------")
  print()
  found=0
  for i in range(len(students)):
    if user_roll==students[i]["roll"]:
      found+=1
      deleted=students.pop(i)
      print("----------------------------")
      print()
      print("Roll: ",deleted["roll"])
      print("Name: ",deleted["name"])
      print("Age: ",deleted["age"])
      print("Branch: ",deleted["branch"])
      print("Marks: ",deleted["marks"])
      print()
      print("---------------------------")
      print("This Record Has Been Deleted From Students!!")
      print()
      break

  if found==0:
    print("Student Not Found!!")

def load_student():
  students=[]
  file= open("student.txt","r")
  for line in file:
    line=line.strip()
    student=line.split(",")
    dic={
      "roll":student[0],
      "name":student[1],
      "age":student[2],
      "branch":student[3],
      "marks":student[4]
    }
    students.append(dic)
  file.close()  

  return students

def save_student(students):
  file=open("student.txt","w")
  for student in students:
    line=student["roll"]+","+student["name"]+","+student["age"]+","+student["branch"]+","+student["marks"]+"\n"
    file.write(line)
  file.close()          

students=load_student()
while True:
   choice=menu()
   if choice=="1":
      student=add_students()
      students.append(student)
      save_student(students)
   elif choice=="2":
      view_students(students)
   elif choice=="3":
      search_student(students)
   elif choice=="4":
      update_student(students)
      save_student(students)
   elif choice=="5":
      del_student(students)
      save_student(students)
   elif choice=="6":
      print("Thank You For Using Student Management V1.0")
      break
