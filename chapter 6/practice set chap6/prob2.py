marks1=int(input("enter your marks1: "))
marks2=int(input("enter your marks2: "))
marks3=int(input("enter your marks3: "))

total_percentage=(100*(marks1 + marks2 + marks3))/300

if(total_percentage>=33):
    print("congratulation you are pass:",total_percentage)

else:
    print("better luck next time:",total_percentage)








