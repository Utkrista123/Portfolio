'''A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.'''

no_of_sweets = int(input("Enter the number of sweets you have: "))
no_of_students = int(input("Enter the number of students: "))

if no_of_sweets < no_of_students:
    print("!!! Not enought sweets !!!")

else:
    sweets_per_student = no_of_sweets // no_of_students
    remainder = no_of_sweets % no_of_students
    print(f"The students will get {sweets_per_student} number of sweets each and you will have {remainder} number of remaining sweets.")