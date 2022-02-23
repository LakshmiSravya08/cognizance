# printing letters on the even indexes of a given string
given_str=input("please enter a string:")
for index in range(len(given_str)):
    if index % 2 == 0:
       print(given_str[index], end='')