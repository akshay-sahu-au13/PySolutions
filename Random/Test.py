A = int(input("Enter you marks in Maths:"))
B = int(input("Enter you marks in Science:"))
C = int(input("Enter you marks in English:"))
D = int(input("Enter you marks in Hindi:"))
E = int(input("Enter you marks in Social Science:"))

Perc = (A+B+C+D+E)/5

if Perc >= 90:
    print("Grade: A")
elif 70 <= Perc < 89:
    print("Grade: B")
elif 50 <= Perc < 69:
    print("Grade: C")
elif 30 <= Perc < 49:
    print("Grade: D")
else:
    print("Grade: E")
