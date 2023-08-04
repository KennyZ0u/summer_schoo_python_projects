#l
#:
user_input = (input("Please enter each of your grades to calculate your average. When you are done, enter 'q' : ")).lower()
sum_grade = int(0)
times = int(0)
average = int(0)
while user_input != "q" :
    try:
        user_input = int(user_input)
        if user_input < 0 :
            print("your grade can't be negative, ")
            user_input = (input("Please enter each of your grades to calculate your average. When you are done, enter 'q' : ")).lower()
        else:
            sum_grade = sum_grade + int(user_input)
            times = times + 1
            user_input = (input("Please enter each of your grades to calculate your average. When you are done, enter 'q' : ")).lower()
    except ValueError:
        print("it seems that you have entered an non-numerical value, or you entered nothing, ")
        user_input = (input("Please enter each of your grades to calculate your average. When you are done, enter 'q' : ")).lower()
try:
    sum_grade = int(sum_grade)
    average = sum_grade / times 
    print(f"Your grade point average is {average:0=2}")
except ZeroDivisionError:
    print("you entered nothing ")
