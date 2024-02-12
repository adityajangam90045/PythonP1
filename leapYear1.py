

#Project 

year = int(input("ENTER THE YRAR: "))

if(year % 400 == 0) and (year % 100 == 0):
    print(year,"This is leap year")
elif(year % 4 == 0) and (year % 100!=0):
        print(year,"This is leap year")
else:
    print("This is not leap year")
