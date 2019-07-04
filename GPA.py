#Grade Point Average
print("GPA = Grade Point Average")
import array

grades = array.array('I', [0])
points = array.array('I', [0])

i, sum1, sum2 = 1, 0, 0

while True:
    print("\nN" + str(i) + ".")
    g = int(input("Type the grade\n"))
    if g == 0: # can't have zero grade
        break
    p = int(input("Type the point (point credit)\n"))

    grades.append(g)
    points.append(p)
    i += 1

for i in grades:
    sum1 = sum1 + grades[i] * points[i]
    sum2 = sum2 + points[i]

try:
    div = sum1/sum2
except ZeroDivisionError:
    div = 0
    
print("GPA = " + str(div))
    
