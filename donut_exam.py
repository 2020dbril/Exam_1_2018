# Conditions
## If the class average is an A, every student gets a donut
## If the class average is a B, every student gets a half donut. Make sure not to round half donuts up. Return the float.
## If the class average is a C, every student gets 1/3 of a donut. Make sure not to round up, but to return the float
## If the class average is a D, every student will give Mr. James a half donut.
#print('type in the 10 scores of the class')

#line 10-28 even numbers get the user to enter the grades required to run the program
#line 10-28 odd numbers store the grade in a variable which is an input, the users response, and wraps it into an integer so that there wont be a string int error
print('enter score 1')
score_1=int(input())
print('enter score 2')
score_2=int(input())
print('enter score 3')
score_3=int(input())
print('enter score 4')
score_4=int(input())
print('enter score 5')
score_5=int(input())
print('enter score 6')
score_6=int(input())
print('enter score 7')
score_7=int(input())
print('enter score 8')
score_8=int(input())
print('enter score 9')
score_9=int(input())
print('enter score 10')
score_10=int(input())
#the array below stores all user responses of the 10 grades
array=(score_1,score_2,score_3, score_4, score_5, score_6, score_7, score_8, score_9, score_10)
#the lines 33-37 is a for loop that increases the added count by looping a through the array. It also finds the average by divinding it by 10
def average(score):
    added = 0
    for a in array:
         added = added + a
         average_score=(added)/10
#line 39 to 46 is the comparing the average of the array to different conditions to determine which conditions are printed.
    if average_score >= 95:
        print("every student gets one donut")
    if 95 >= average_score >= 90:
        print("every student gets half a donut")
    if 90 >= average_score >= 80:
        print('every student gets 1/3 of a donut')
    if 80 >= average_score:
        print("every student gives Mr James half a donut")
average(array)
#line 47 calls the function so that the function is completed
