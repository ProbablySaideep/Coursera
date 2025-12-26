def simulator():
    name=input("Enter your passenger princess: ")
    like="Madhura"

    if name.lower() == like.lower():
        print("\nYES SHE IS MY PASSENGER PRINCESS!\n")

    else:
        print("Nah idk who that is")


while True:
    print("\n\nWELCOME TO SAIDEEP'S PASSENGER PRINCESS SIMULATOR\n")
    cond=int(input("Press 1: To start\nPress 2: to Discontinue/Exit\n"))

    if cond==1:
        simulator()
        wish=int(input("\nDo you want to continue again? Press 1 for yes and 2 for no:\n"))
        if wish==1:
            continue
        elif wish == 2:
            break
        else:
            print("Error try again!")
    

    elif cond==2:
        break

    else:
        print("Error Try Again!")




