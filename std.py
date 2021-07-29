def std():
    
    # infinite loop
    while True:
        myname = input("What's your name? ")
        try:
            if myname == ("Shae"):
             print(" That's a gay ass name just fyi...")
            bitches = int(input("So how many bitches have you fucked? " ))
            
        # Check if value is an int.
        except ValueError:
            print("That's not a number.")
            continue
            
        if bitches >= 100:
            print("You're not man enough to have reached that number, try again.")
        
        elif bitches <= 0:
            print("Sorry, no numbers below zero you fucking virgin.")
            

        
        # end of loop upon user input.
        else:
            print("Holy shit,", myname, "! You have about a", bitches/2,"out of", bitches/2*8, "% chance of getting aids!")
            break

std()
