# Importing the 'time' module to use the sleep function, which adds delay.
import time

# Define a function 'countdown' that takes one argument 't' (time in seconds)
def countdown(t):
  # Loop continues until t becomes 0
  while t: 
    # Convert total seconds into minutes and seconds using divmod
    mins, secs = divmod(t, 60)
    
    # Format the time as MM:SS (e.g., 01:30)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    
    # Print the formatted time, using '\r' to overwrite the previous line
    print(timer, end="\r")
    
    # Pause the loop for 1 second
    time.sleep(1)
    
    # Decrease time by 1 second
    t -= 1

  # Once the loop ends, print that the time is up
  print('Time’s up!')

# Ask the user to input the countdown time in seconds
t = input('Enter your time in seconds: ')

# Convert the input to an integer and call the countdown function
countdown(int(t))
