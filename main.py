# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# 156 178 165 171 187 = 857
# output = 171.4 
height = 0
number_of_students = 0
for student in student_heights:
 
  height += student
  number_of_students += 1

print(round(height/number_of_students))



