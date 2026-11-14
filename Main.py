print("===TAITA TAVETA UNIVERSITY===")
print("Student Grade Calculator")
print("------------------------------")

name = input("Enter Student Number: ")
reg_no = input("Enter reg_no")

try:
    marks = float(input("Enter marks (0-100: )"))

    if marks >=70:
        grade= "A - First Class"
    elif marks >=60:
        grade= "B - Second Upper"
    elif marks >=50:
        grade= "C - Second Lower"
    elif marks >=40:
        grade= "D - Pass"

    else:
        grade= "F - Fail"

    print("/n---RESULT---")
    print(f"Name: {name}")
    print(f"Reg No: {reg_no}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

except ValueError:
    print("Please enter numbers only for marks!")
