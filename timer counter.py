#timer counter 
#import the time module
import time

#define the counter function.
def countdown(t):

    while t:
        mins,secs=divmod(t, 60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1

    print('Fire in the hole !!')

    #input time in seconds
t=input("Enter the time in second :")

#function call
countdown(int(t))