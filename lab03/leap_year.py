
class Year:
    def __init__(self,year):
        self.year = year
        #self.n = ""
    def isLeapYear(self):
        if self.year>1582 and ((self.year%4==0 and self.year%100!=0)or(self.year%400==True)):
            self.print_leap()
        else:
            #print("Not a leap year")
            #self.n = "not"
            self.print_leap("not")
    def print_leap(self,n=""):
        print(str(self.year)+" is " +n+ " a leap year")

y = Year(1980)
y.isLeapYear()



##if year<1582:
##    if year%4==0:
##        print_leap()
##else:
##    if year%4==0:
##        if year%100!=0:
##            print_leap()
    
