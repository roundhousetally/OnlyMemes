#!/usr/bin/python3
""" Uses scheduler class to handle posting to profiles on a randomized timer. """

import sched, time, random, signal, sys
import classes

s = sched.scheduler(time.time, time.sleep)


def postRandom():
    """ Posts to a random profile. """
    prof = random.choice(classes.storage.getProfile())  # Select random profile
    prof.post()  # Post to it
    classes.storage.save()
    print('Profile {} has posted at {}'.format(prof.name, time.asctime()))  # Log the post


def endSchedule(sig, frame):
    """ SIGINT handler to end the schedule loop. """
    print('Stopping schedule...')
    classes.storage.close()  # Ends the database session
    sys.exit(0)  # Ends the program

# Runs only if this file is run as the main file
if __name__ == "__main__":
    print('Starting post schedule...')
    signal.signal(signal.SIGINT, endSchedule)  # Sets up interrupt catching
    s.enter(1, 1, print, argument=('Schedule started',))  # Log start of the schedule

    # Infinite loop to keep the scheduler running
    while (True):
        # First arg is 60 * n, where n is minutes
        s.enter(60 * random.randrange(5, 30), 1, postRandom)  # Shedule a post
        s.run()  # Start schedule
