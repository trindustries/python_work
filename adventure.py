name = input("Type your name: ")
print("Welcome", name, "you're in a computer-generated reality created by artificially intelligent machines. They use it as a way to stimulate the brains of humans who are being programmed... You are about to embark on an adventure, if you chose to.")

answer = input(
    "[Takes out two pills, one of which is red, the other is blue] This is your last chance. After this there is no turning back. You take the blue pill, the story ends; you wake up in your bed and believe whatever you want to believe. Which will you choose? [Type continue to proceed, exit to leave] ".lower()
    )
if answer == "continue":
    answer = input("You are presented with two pills, one blue and one red. Which do you choose? (blue/red): ")

    if answer == "blue":
        print("You have decided to be a slave... [You wake up in your bed]")

    elif answer == "red":
        print("You have decided to find the truth... [You remain in Wonderland]")

    else:
        print('Not a valid option. [You wake up in your bed]')

elif answer == "exit":
    answer = input("Program terminated")
else:
    print('Not a valid option. [You wake up in your bed]')
