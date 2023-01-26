
        


print("enter a number")
#grade=0.0
try:
    grade = float(input())
    if grade>4.0:
        print("Useless")
    elif grade>3.67:
        print("A")
    elif grade>3.33:
        print("A-")
    elif grade>3.00:
        print("B+")
    elif grade>2.67:
        print("B")
    elif grade>2.33:
        print("B-")
    elif grade>2.0:
        print("C+")
    elif grade>1.0:
        print("C")
    elif grade==0.00:
        print("D")
    else:
        print("Too small")
except NameError:
    print("invalid")
except ValueError:
    print("value issue")



