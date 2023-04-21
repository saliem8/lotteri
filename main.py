import os
import lotteri 

looping = True
lott = lotteri.Lotteri()



while looping:
    os.system('cls' if os.name == 'nt' else 'clear')
    antal_lotter = input("\n\t\tHur många lotter vill du ha? Max 3st: ")

    try:
        int_antal_lotter = int(antal_lotter)

        i = 0

        if (int_antal_lotter < 4):
            os.system('cls' if os.name == 'nt' else 'clear' )
            print("\n\t\tGrattis ni vann det här!")

            while i < int_antal_lotter:
                vinst = lott.get_vinst()
                print("\t\t" + vinst)
                i += 1
        elif int_antal_lotter > 3:
            print("Max 3 lotter var det! ")
                
    
    except ValueError:
        print("\n\t\tEndast siffror är tillåtna! ")


    fortsatt = input("Vill ni köra programmet en gång till? j/n: ")

    if (fortsatt == "n"):
        break 