print("Hello in 'The Quiz' !")
print("Answer with 'Yes' or 'No'.")
print()

y = ["Yes" and 1]
n = ["No" and 2]

# Question 1
q1 = print("One Piece is trash or not ?")
a1 = str(input("Answer 1 : "))
if a1 == n :
 p1 = 5
elif a1 == y :
 p1 = -1
else :
 print("FAUX !")
print()
# Question 2
q2 = print("Game of Thrones is the best series in the world ?")
a2 = str(input("Answer 2 : "))
if a2 == y :
 p2 = 5
elif a2 == n :
 p2 = -1
else :
 print("FAUx !")
print()
# Question 3
q3 = print("The WORLD IS Good  ?")
a3 = str(input("Answer 3 : "))
if a3 == y :
 p3 = 5
elif a3 == n :
 p3 = -1
else :
 print("FAux !")
print()
# Question 4
q4 = print("PYthon EASY  ?")
a4 = str(input("Answer 4 : "))
if a4 == y :
 p4 = 5
elif a4 == n :
 p4 = -1
else :
 print("FAUX !")
print()

points = p1+p2+p3+p4
print("Tu as obtenu", points, "points.")