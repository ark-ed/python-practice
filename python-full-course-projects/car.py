# Car Game
# Python Tutorial - Python Full Course for Beginners by Programming with Mosh
# Attempt 1

print("Type 'help' to view all commands")

while True:
    u_i = input(">")
    
    if u_i.lower() == "help":
        print("""Commands are:
    > start: starts the vehicle
    > stop: stops the vehicle
    > quit: exit the program    
    """)

    elif u_i.lower() == "start":
        print("Started the vehicle")
    
    elif u_i.lower() == "stop":
        print("Stopped the vehicle")

    elif u_i.lower() == "quit":
        exit()