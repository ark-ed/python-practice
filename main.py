# 3:02:04 - Classes
# Value Errors
try: # Telling python to try running this code
  a = int(input("What is your age? -->"))
  b = 8000/a
  print(b)
except ValueError: # Instead of crashing for non-integer values, perform action below instead.
  print("Invalid value")
except ZeroDivisionError:
  print("Undefined")