""" This software implements command line calendar
Users can choose to:
1) View the calendar
2) Add an event to the calendar
3) Update an existing event
4) Delete an existing event """

from time import sleep, strftime

""" Data Declaration"""
firstName = "Anil"
calendar = {}

""" Function for Welcome Message """
def welcome():
  print "Welcome to the Calendar software " + firstName
  print "Calendar program is starting...."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y") 
  print "Current time is: " + strftime("%H:%M:%S")
  print "What would you like to do?"

""" Function for Calendar """
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter V for view or U for update or A for add or D for delete or X for exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("what date: ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Your update was successfull!..."
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "You have entered and invalid date!!"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Your event was successfully added!..."
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print " Event was successfully deleted!..."
            print calendar
          else:
            print "You have entered an incorrect event!"
    elif user_choice == "X":
        start = False
    else:
      print "You have entered an invalid command!!!"

""" Runs the calendar """
start_calendar()
    





