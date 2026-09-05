'''movies = []
mov= input("enter the first movie:")
movies.append(mov)
mov1= input("enter the second movie:")
movies.append(mov1)
print(movies)'''

# check list contain palindrome r not
list1 = [1,"abc","abc",1]
temp = list1.copy()
temp.reverse()
if list1 == temp:
    print("palindrome")
else:
    print("not palindrme")

print(list1)

#tuples 
grade = ["C","D","B","A","A","B","A"]
grade.sort()
print(grade)

