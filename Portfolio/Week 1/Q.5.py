'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group.'''

total_students = 113 + 175 + 12

full_groups = total_students // 24
left_over = total_students % 24
print(f"There will be {full_groups} full groups.")
print(f"There will be {left_over} left over students")