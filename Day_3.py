'''
Write a program to read firstname lastname of the user, take last two characters from firstname , 
and first two character of last name , joiuning those two characters gives a new name, 
return that new name as alien name
'''

def alien():
    first_name = input("Enter the first name: ")
    if first_name.isalpha() and len(first_name) >= 4:
        last_name = input("Enter the last name: ")
        if last_name.isalpha() and len(last_name) >= 4:
            alien_name = first_name[-2:] + last_name[0:2]
            print(f"The Alien Name is: {alien_name}")
        else:
            print("Last Name should have letters only or it should have length of 4.")
    else:
        print("First Name should have letters only / it should have length of 4.")
alien()

