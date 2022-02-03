name = input("Enter your name and surname: ")
number = int(input("Enter your student number: "))

lesson1 = input("Enter your first lesson: ")
l1_mid = float(input(f"Enter your {lesson1} mid-term exam result: "))
l1_final = float(input(f"Enter your {lesson1} final-exam result: "))

lesson2 = input("Enter your second lesson: ")
l2_mid = float(input(f"Enter your {lesson2} mid-term result: "))
l2_final = float(input(f"Enter your {lesson2} final-exam result: "))

lesson3 = input("Enter your third lesson: ")
l3_mid = float(input(f"Enter your {lesson3} mid-term result: "))
l3_final = float(input(f"Enter your {lesson3} final-exam result: "))

lesson4 = input("Enter your fourth lesson: ")
l4_mid = float(input(f"Enter your {lesson4} mid-term result: "))
l4_final = float(input(f"Enter your {lesson4} final-exam result: "))

l1_result = (l1_mid * 0.4) + (l1_final * 0.6)
l2_result = (l2_mid * 0.4) + (l2_final * 0.6)
l3_result = (l3_mid * 0.4) + (l3_final * 0.6)
l4_result = (l4_mid * 0.4) + (l4_final * 0.6)

if l1_result <50:
        print(f"You failed the {lesson1} lesson.")
else:
        print(f"Congratulations. you passed the {lesson1} lesson")

if l2_result <50:
        print(f"You failed the {lesson2} lesson.")
else:
        print(f"Congratulations. you passed the {lesson2} lesson")

if l3_result <50:
        print(f"You failed the {lesson3} lesson.")
else:
        print(f"Congratulations. you passed the {lesson3} lesson")

if l4_result <50:
        print(f"You failed the {lesson4} lesson.")
else:
        print(f"Congratulations. you passed the {lesson4} lesson")

list = [lesson1, lesson2, lesson3, lesson4]
for x in list:
        print(x)


