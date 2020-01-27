class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self._age = 0
        else:
            self._age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self._age < 13:
            print("You are young.")
        elif (13 <= self._age) and (self._age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self._age += 1
        # Increment the age of the person in here

