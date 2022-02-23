# creating the table to represent student records
n=int(input('Enter the number of students you want in the list :'))
x=[['Roll No','student Name','Marks',]]
# inserting records into the table
for i in range(n):
    roll_no=input('Enter the Roll No : ')
    stud_name=input('Enter  the Student Name : ')
    marks=int(input('Enter  the Marks obtained: '))
    x.append([roll_no,stud_name,marks])
for i in range(len(x)):
    for j in range(len(x[i])):
        m=x[i][j]
        print(m,end='\t')
    print('\n')
# displaying the required row
a=int(input('Enter the row to be displayed: '))
for i in x[a]:
    print(i,end='\t')