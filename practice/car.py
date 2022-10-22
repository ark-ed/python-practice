# Car Game
# Python Tutorial - Python Full Course for Beginners by Programming with Mosh

print("Type 'help' to view all commands")
cu_i = "stop"

while True:
    u_i = input(">")
    
    if u_i.lower() == "help":
        print("""Commands are:
    > start: starts the vehicle
    > stop: stops the vehicle
    > quit: exit the program    
    """)

    #---------------------------------------------
    # Start
    elif u_i == "start" and cu_i == "stop":
      print("Started the vehicle")
      cu_i = "start"
    elif u_i == "start" and cu_i == "start":
      print("Vehicle is already on")
  
    # Stop
    elif u_i.lower() == "stop" and cu_i.lower() == "start":
      print("Stopped the vehicle")
      cu_i = "stop"
    elif u_i.lower() == "stop" and cu_i == "stop":
      print("Vehicle is already off")

    elif u_i.lower() == "quit":
        exit()

    else:
      print("Sorry, I don't understand")