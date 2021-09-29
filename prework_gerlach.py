#Question 1 Greeting USERNAME (complete)
def hello_name(user_name):
     """prints "hello_USERNAME!" USERNAME is the input of the function"""
     user_name=input("Please enter your user name: ").upper
     print("Hello, "+user_name()+"!")
hello_name(user_name=input)


#Question 2 (complete)
print(list(range(1,101,2)))

#Question 3 Max Number in List (complete)
def max_num_in_list(a_list):
    """finds the max number in a list"""
    print(max(a_list))
Next line is invalid syntax no matter what I put there.
a_list = list(range(1,16))
max_num_in_list(a_list)


#Question 4 Leap Year (complete)
def is_leap_year(a_year):
    """answers whether input year is a leap year""" 
    if (int(a_year)%4==0) and ((int(a_year)%100!=0) or (int(a_year) % 400==0)):
        print('leap year')
    else:
        print('not a leap year')
a_year=input('Enter a year: ')
is_leap_year(a_year)

#Question 5 consecutive numbers (not functional)
def is_consecutive(b_list):
    """finds if numbers in a list are consecutive"""
    if sorted(b_list)==range(min(b_list), max(b_list)+1):
        print('Consecutive')
    else:
        print('Not Consecutive')

b_list=input('Enter a list of numbers: ')
is_consecutive(b_list)