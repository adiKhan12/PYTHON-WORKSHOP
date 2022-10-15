
#try:
    # Code to try

#except (RuntimeError, TypeError, NameError):
    # Code to run if one of these exceptions is hit

#A try statement can also have more than one except clause:

#try:
    # Code to try

#except RuntimeError:
    # Code to run if there's a RuntimeError

#except TypeError:
    # Code to run if there's a TypeError

#except NameError:
    # Code to run if there's a NameError




# int ("a") this will throw an exception

try:  # try to execute this code
    print(int("a"))
except ValueError: # if the code throws an exception of type ValueError, then execute this code
    print("An exception was thrown")


# to catch multiple exceptions not specific to one type

try:
    d = {}
    d["a"]
except KeyError:
    print("KeyError")

#to catch all exceptions specificaly

try:
    d = {}
    d["a"]
    print(int("a"))

except (KeyError, ValueError):
    print("KeyError or ValueError")

try:
    number1 = int(input("Enter a number: "))
except ValueError:
    print("You did not enter a number")

print("end of program")