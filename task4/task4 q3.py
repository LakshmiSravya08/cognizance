# creating the table to represent student records
n=int(input('Enter the number of students you want in the list : '))
x=[['Roll No','student Name','Marks',]]
for i in range(n):
    roll_no=input('Enter Roll No : ')
    stud_name=input('Enter Student Name : ')
    marks=int(input('Enter Marks : '))
    x.append([roll_no,stud_name,marks])
for i in range(len(x)):
    for j in range(len(x[i])):
        k=x[i][j]
        print(k,end='\t')
    print('\n')
a=int(input('Enter the row to be displayed: '))
for i in x[a]:
    print(i,end='\t')