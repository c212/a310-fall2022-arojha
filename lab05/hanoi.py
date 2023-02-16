

def hanoi(n,source,destination,auxiliary):
    if n==1: # exit condition
        print("Moving "+str(n)+" "+source+" to "+destination)
        return
    hanoi(n-1,source,auxiliary,destination)
        #  3   "A"    "C"          "B"
        #  2   "A"    "B"          "C"
    print("moving "+str(n)+" "+source+" to "+destination)
    hanoi(n-1,auxiliary,destination,source)
        #  3    "C"         "B"      "A"
        #  2    "A"         "B"      "C"  
n=4
hanoi(n,"A","B","C")
