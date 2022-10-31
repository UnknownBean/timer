//Description
This is a shitty timer/alarm  program I wrote in python3 to alert me when to leave work for class.

//Usage
using the timer is pretty simple but not super intuitive. 
call it with "python3 timer.py" 
it will prompt you for a time to alert you at. the program currently only accepts 12 hour time format but 2 levels of precision. [hour minute am/pm] (%I%M%p) or  [hour minute seconds am/pm] (%I%M%S%p). Input is to be entered as a string of numbers with no seperator followed by an am/pm

python3 timer.py 

input: 237am 
result: alarm set at 02:37:00AM

input: 23705am
result: alarm set forr 02:37:05AM

