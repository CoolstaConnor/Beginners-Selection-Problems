BEGIN = input("You have finally awoken, in front of you you see that there are three doors with dangers behind each one. Behind these dangers are doors to escape to the next level, but you must make it through all the doors to survive. Use your common sense to make it through. Type 'BEGIN' to start your quest.")
if BEGIN == "BEGIN": 
    print("Firstly, behind the first door are thousands of venemous hornets, and upon stinging you, kill you in seconds.")
    print("Behind the second door is a sanctuary of Great White Sharks. They are so big that they won't chomp you, but swallow you whole.")
    print("Lastly, behind the third and final door are bundles of huge lethal Pythons that can wrap around you, and suffocate you to death.")
    door1 = int(input("Which animal are you picking, 1, 2, or 3? (You will need to rerun the level if you do not pick 1, 2, or 3)"))
    if door1 == 1:
            print("You Died! You were stung by the venemous hornets, rerun the level.")
    if door1 == 3:
        print("You Died! The Pythons suffocated you, rerun the level.")
    if door1 == 2:
        print("Good Choice! The water in the room came flowing out, and the sharks couldn't breathe, and died, you were free to pass.")
        print("The next 3 set of doors are not animals, but murderers that will kill you on sight.")
        print("The first door unveils a murderer with a sharp knife.")
        print("Behind the second door is a murderer with a loaded gun.")
        print("Finally, behind the third door is a murderer with a chainsaw.")
        door2 = int(input("Which murderer are you picking, 1, 2, or 3? (You will need to rerun the level if you do not pick 1, 2, or 3)"))
        if door2 == 1:
            print("You Died! You were stabbed by the murderer, rerun the level.")
        if door2 == 2:
            print("You Died! You were shot by the murderer, rerun the level.")
        if door2 == 3:
            print("Good Choice Again! The chainsaw needed to be plugged in for it to work, but there were no plugs.")
            print("You have one more sets of doors to get through.")
            print("Behind the next set of doors are liquids that you must drink half a litre of.")
            print("The first door will cleanse you of any viruses, bleach.")
            print("The second door may get you drunk, it showcases pure alcohol.")
            print("And the third door has boiling water.")
            door3 = int(input("Which dangerous liquid will you be choosing to drink, 1, 2, or 3?(You will need to rerun the level if you do not pick 1, 2, or 3)"))
            if door3 == 1:
                print("You Died! Bleach will clear out all toxins inside your body, including useful ones. Rerun the level.")
            if door3 == 3:
                print("You Died! Boiling water will burn you from the inside out, damaging and burning your limbs. Rerun the level.")
            if door3 == 2:
                print("Correct! Drinking pure alcohol is not safe, however you will LIKELY live after drinking it. Rerun the level.")
                print("Well Done! You completed your quest, I almost forgot your reward. Your reward is surviving, great job!")
else:
    print("Rerun the level, and type 'BEGIN' correctly to start the quest! It is case sensetive.")