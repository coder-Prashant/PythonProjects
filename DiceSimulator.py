# Import the required modules
import random
import os

# Create a DICE art for pretty
DICE_ART = {
    1: ("[           ]",
        "[           ]",
        "[     0     ]",
        "[           ]",
        "[           ]"),
    2: ("[           ]",
        "[   0       ]",
        "[           ]",
        "[       0   ]",
        "[           ]"),
    3: ("[ 0         ]",
        "[     0     ]",
        "[         0 ]",
        "[           ]",
        "[           ]"),
    4: ("[           ]",
        "[  0     0  ]",
        "[           ]",
        "[  0     0  ]",
        "[           ]"),
    5: ("[  0     0  ]",
        "[           ]",
        "[     0     ]",
        "[           ]",
        "[  0     0  ]"),
    6: ("[           ]",
        "[  0     0  ]",
        "[  0     0  ]",
        "[  0     0  ]",
        "[           ]"),
}

while True:
    # Take the user input from command line
    user_input = input(f"[User Input]: Hello {os.getlogin().capitalize()}, how many dices do you want to roll: ")
    # Only proceed if user has selected to roll atleast 1 dice
    if user_input.isdigit():
        user_input = int(user_input)
        print(f"[ACTION]: Total {user_input} dices will be rolled, see result below:")
        if user_input>=1:
            roll_results = []
            # Loop over the total dices (user input)
            for _ in range(1, user_input+1):
                # Get random value between 1 to 6 and append each outcome in a list called roll_results
                roll = random.randint(1, 6)
                roll_results.append(roll)
            # Print the outcome and dice art for each rolled dice
            print('\n-----------------------RESULT------------------------')
            for idx, roll in enumerate(roll_results):
                idx += 1
                print(f"Number occured on the roll of dice-{idx}: {roll}")
                for line in DICE_ART[roll]:
                    print(line)
    elif user_input.lower() == 'done':
        print('[COMPLETED]: User asked to stop, exiting..')
        break
    elif (user_input.lower() != 'done') and (not user_input.isdigit()):
        print("[ERROR]: Invalid user input, expected input is integer value")
        print("Exiting..")
        break