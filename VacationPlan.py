#It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is Saturday.
#If you go on a wonderful holiday leaving on day 3 (a Wednesday) and you return home after 10 nights,
#you arrive home on day 6 (a Saturday).

#Write a general version of the program which asks for the day number that your vacation starts on
#and the length of your holiday, and then tells you the number of the day of the week you will return
#on.

#Get start day from user, convert to int, assign to a variable
vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, etc.) '))

#Get length of vacation from user, convert to int, assign to a variable 
vacationLength=int(input('How many days will your vacation be? '))

#Take the vacation length add to the vacation start
#Use modulus operator to get the remainder of the reaminder of this value divided by 7(for 7 days of week)
returnDay=(vacationLength+vacationStart)%7

print(returnDay)
