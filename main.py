name = input ("Please enter your full name: ")

mark_grade = int(input("What is your percentage mark: "))

if mark_grade >= 90:
    grade = "A*."
    print("Your mark: " ,mark_grade," Your grade: ",grade, " Excellent! Keep up the good work!")
    
elif mark_grade >= 80:
    grade = "A."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Aim for an A*!")
    
elif mark_grade >= 70: 
    grade = "B."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Good job.")
    
elif mark_grade >= 60: 
    grade = "C."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Okay, try harder.")
    
elif mark_grade >= 50:
    grade = "D."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Poor. I expect more.")

elif mark_grade >= 40:
    grade = "E."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Very poor")

elif mark_grade >= 0: 
    grade = "U."
    print("Your mark: " ,mark_grade," Your grade: ",grade, "Unacceptable")

target_mark = int(input("What is your target mark: "))

if target_mark > mark_grade:
  print("Apply yourself and you can achieve your target grade!")

if target_mark == mark_grade:
  print("You are achieving what is expected of you. Keep up the good work and you could achieve even higher!")

if target_mark < mark_grade:
  print("Congratulations on achieving a higher grade than expected, keep it up!!")
  