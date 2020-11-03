""" Contains the storage object for other parts of the program to use. """

from classes.storage import Storage

# Prepare and initialise database storage object
storage = Storage()
storage.load()
