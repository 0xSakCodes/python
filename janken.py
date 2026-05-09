# casa janken game:
import random

name = input("Player please input your NAME:")
paper = 1
scissor = 2
rock = 3
doYouWantToPlay = True
# 1 = paper; 2 = scissor; 3 = rock

# certifies:
# paper (1) < scissor (2);
# paper (1) > rock (3)
# paper (1) = paper (1)

# scissor (2) > paper (1)
# scissor (2) < rock (3)
# scissor (2) = scissor (2)

# rock (3) > scissor (2)
# rock (3) < paper (1)
# rock (3) = rock (3)

# module:
"""
storing players & jankie's win and losses 
"""
playersWin = 0
jankieWin = 0

while doYouWantToPlay:
    inpVal = input("Enter rock/paper/scissor:\n>>")
    random_num = random.randint(1, 3)
    updatedVal = inpVal.lower()

    if updatedVal == "rock":
        if random_num == rock:
            print("JANKIE: 🪨")
            print("PLAYER: 🪨")
            print("\n🤖 It's a tie!")
            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
        else:
            if random_num == scissor:
                print("JANKIE: ✂️")
                print("PLAYER: 🪨")
                playersWin += 1
                print("\n🎉 Congrats! %s won!" % (name))

                replay = input("\nDo you want to play again?\n>> yes/no:")
                if replay.lower() == "no":
                    doYouWantToPlay = False
                elif replay.lower() == "yes":
                    print("Jankie: Let's play again!\n")
                else:
                    print("Error: Unexpected Input!")
                    break
            else:
                if random_num == paper:
                    print("JANKIE: 📜")
                    print("PLAYER: 🪨")
                    jankieWin += 1
                    print("\n🙊 Oops! %s lost!" % (name))

                    replay = input("\nDo you want to play again?\n>> yes/no:")
                    if replay.lower() == "no":
                        doYouWantToPlay = False
                    elif replay.lower() == "yes":
                        print("Jankie: Let's play again!\n")
                    else:
                        print("Error: Unexpected Input!")
                        break
    elif updatedVal == "paper":
        if random_num == paper:
            print("JANKIE: 📜")
            print("PLAYER: 📜")
            print("\n🤖 It's a tie.")

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
        elif random_num == scissor:
            print("JANKIE: ✂️")
            print("PLAYER: 📜")
            jankieWin += 1
            print("\n🙊 Oops! %s lost!" % (name))

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
        elif random_num == rock:
            print("JANKIE: 🪨")
            print("PLAYER: 📜")
            playersWin += 1
            print("\n🎉 Congrats! %s won!" % (name))

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
    elif updatedVal == "scissor" or updatedVal == "scissors":
        if random_num == scissor:
            print("JANKIE: ✂️")
            print("PLAYER: ✂️")
            print("\n🤖 It's a tie.")

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
        elif random_num == paper:
            print("JANKIE: 📜")
            print("PLAYER: ✂️")
            playersWin += 1
            print("\n🎉 Congrats! %s won!" % (name))

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
        elif random_num == rock:
            print("JANKIE: 🪨")
            print("PLAYER: ✂️")
            jankieWin += 1
            print("\n🙊 Oops! %s lost!" % (name))

            replay = input("\nDo you want to play again?\n>> yes/no:")
            if replay.lower() == "no":
                doYouWantToPlay = False
            elif replay.lower() == "yes":
                print("Jankie: Let's play again!\n")
            else:
                print("Error: Unexpected Input!")
                break
    else:
        print("CasaJanken: Quitted (Unexpected Input)")
        print("made with ❤️  by SakCodes!")
else:
    print()
    print("%s: won %s times!" % (name.title(), playersWin))
    print("Jankie: won %s times!" % (jankieWin))
    print()
    print("Jankie: Thankyou for playing!")
    print("made with ❤️  by SakCodes!")
