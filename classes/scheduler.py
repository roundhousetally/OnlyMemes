#!/usr/bin/python3
""" Uses scheduler class to handle the posting of profiles. """

import sched, time, random, signal, sys
import classes

s = sched.scheduler(time.time, time.sleep)
running = True;

def postRandom():
    """ Posts to a random profile. """
    prof = random.choice(classes.storage.getProfile()) # Select random profile
    prof.post() # Post to it
    classes.storage.save()
    print('Profile {} has posted at {}'.format(prof.name, time.asctime())) # Log the post

def endSchedule(sig, frame):
    """ Ends the schedule loop. """
    print('Stopping schedule...')
    running = False;
    classes.storage.close()
    sys.exit(0)

if __name__ == "__main__":
    print('Starting post schedule...')
    signal.signal(signal.SIGINT, endSchedule) # Sets up interrupt catching
    s.enter(1, 1, print, argument=('Schedule started',)) # Log start of the schedule
    while (running):
        # First arg is 60 * n, where n is minutes
        s.enter(60 * random.randrange(5, 30), 1, postRandom) # Shedule a post
        s.run() # Start schedule
