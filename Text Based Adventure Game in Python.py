import random
import time
import sys

man = [1000, 650]  # [power,health]
woman = [600, 1500]
monsters = ["dwarfs", "snakes", "giants"]
congratulations = ["Nice job!", "Nice going!", "Great work!",
                   "Keep it up!", "Great improvement!"]


# the main function that contain all of code
#  to start the game and restart it
def playing_again():
    global the_health, the_power

    # this function just print the sentences
    # but it set the time to make it more easier to read
    def print_pause(string, time_of_sleeping):
        print(string)
        time.sleep(time_of_sleeping)

    # attacking function it gets the type of monsters
    #  and num of monsters to start simulate the attack
    def attacking(monster, num):
        giants_health = 1100
        if gender2 == "man":
            gender_health = man[1]
            gender_power = man[0]
        else:
            gender_health = woman[1]
            gender_power = woman[0]
        print_pause("start your attack", 1)
        attacking_stle = input("aggressive(1)/defensive(2)")
        while attacking_stle != "1" and attacking_stle != "2":
            print('please,enter 1 or 2')
            attacking_stle = input("")
            if attacking_stle == '1' or attacking_stle == '2':
                break
        if attacking_stle == '1':
            i = 1
        else:
            i = 1 / 10
        if monster == "dwarfs":
            gender_health -= (num * 10 * i)
            print_pause(f"{random.choice(congratulations)}"
                        f" you killed them", 2)
            if gender_health <= 0:
                gender_health = 0
            print_pause(f"but you are attacked,"
                        f"your health is {gender_health}pt", 2)
            if gender2 == "man":
                man[1] = gender_health
                man[0] = gender_power
            else:
                woman[1] = gender_health
                woman[0] = gender_power
            if gender_health <= 0:
                print_pause("Game Over", 1)
                print_pause(" you are killed", 1)
                print_pause("do you wanna play again??", 1)
                pla_again = input("yes(1)/no(2)")
                while pla_again != '1' and pla_again != '2':
                    print_pause('please,enter 1 or 2', 1)
                    pla_again = input("")
                    if pla_again == '1' or pla_again == '2':
                        break
                if pla_again == '1':
                    playing_again()
                if pla_again == '2':
                    sys.exit("okay, see you in another invasion")

        elif monster == "giants":
            while True:
                gender_health = gender_health - (num * 60 * i)
                giants_health = giants_health - (gender_power * i)
                if gender_health < 0:
                    gender_health = 0
                if giants_health < 0:
                    giants_health = 0
                print_pause(f"{random.choice(congratulations)} you decreased "
                            f"the giants health to {giants_health}pt", 2)
                print_pause(f"but you are attacked,"
                            f"your health is {gender_health}pt", 1)
                print_pause("                                      ", 0)
                if gender2 == "man":
                    man[1] = gender_health
                    man[0] = gender_power
                else:
                    woman[1] = gender_health
                    woman[0] = gender_power
                if giants_health <= 0 or gender_health <= 0:
                    break
            if giants_health <= 0:
                print_pause(f"{random.choice(congratulations)} "
                            f"you killed all of them", 1)
            if gender_health <= 0:
                print_pause("Game Over", 1)
                print_pause(" you are killed", 2)
                print_pause("do you wanna play again??", 1)
                play_agan = input("yes(1)/no(2)")
                while play_agan != '1' and play_agan != '2':
                    print_pause('please,enter 1 or 2', 1)
                    play_agan = input("")
                    if play_agan == '1' or play_agan == '2':
                        break
                if play_agan == '1':
                    playing_again()
                if play_agan == '2':
                    sys.exit("okay, see you in another invasion")
        else:
            if i == 1 / 10:
                print_pause(" you are killed", 2)
                print_pause("do you wanna play again??", 1)
                play_agai = input("yes(1)/no(2)")
                while play_agai != '1' and play_agai != '2':
                    print_pause('please,enter 1 or 2', 1)
                    play_agai = input("")
                    if play_agai == '1' or play_agai == '2':
                        break
                if play_agai == '1':
                    playing_again()
                if play_agai == '2':
                    sys.exit("okay, see you in another invasion")
            else:
                print_pause(f"{random.choice(congratulations)}"
                            f" you killed them", 1)
                print_pause(f"your health is still "
                            f"{gender_health}pt", 1)

    # round function that organizes the round
    # and determines type and num of monsters
    def round_1():
        monster = random.choice(monsters)
        if monster == "dwarfs":
            num = random.randint(2, 100)
            print_pause(f"OMG,there are {num} {monster}", 2)
        else:
            num = random.randint(3, 6)
            print_pause(f"OMG,there are {num} {monster}", 2)
        attacking(monster, num)
        monsters.remove(monster)

    print_pause("hello", 1)
    print_pause("before starting "
                "the game", 1)
    print_pause("do you wanna be man"
                " or woman??", 1)
    print_pause("by the way,the man has"
                " power more than woman", 2)
    print_pause("But in some cases,the woman "
                "is useful than man ", 2)
    print_pause("because woman has incredible "
                "health,it's reach about 1500pt", 1)
    gender = input("so what do you will"
                   " choose??(m(1)/w(2))")
    while gender != "1" and gender != "2":
        print_pause('please,enter 1 or 2', 1)
        gender = input("")
        if gender == '1' or gender == '2':
            break

    if gender == '1':
        print_pause(f"your power={man[0]}pt", 2)
        print_pause(f"your health={man[1]}pt", 2)
        gender2 = "man"
    else:
        print_pause(f"your power={woman[0]}pt", 2)
        print_pause(f"your health={woman[1]}pt", 2)
        gender2 = "woman"
    print_pause("the story start with green monsters", 2)
    print_pause("these organisms wanna invade the earth ", 2)
    print_pause("but we were so lucky", 2)
    print_pause("because we discovered these monsters"
                " have a great mother", 2)
    print_pause("if we can defeat the great mother all "
                "of them will be killed", 2)
    print_pause("so you must defeat those green "
                "killers and save the world ", 2)
    additional_info = input("if you wanna read more "
                            "enter(1) or for skipping enter(2)")
    while additional_info != '1' and additional_info != '2':
        print_pause('please,enter 1 or 2', 1)
        additional_info = input("")
        if additional_info == '1' or additional_info == '2':
            break
    if additional_info == '1':
        print_pause('ok,there are three types from '
                    'green monsters', 2)
        print_pause('first type is called dwarfs', 2)
        print_pause("those are very short and thin ", 2)
        print_pause("they attack as a group, they are so fast", 2)
        print_pause("and only one hit decreases your health about 10pt "
                    "and they have health about 50pt", 2)
        print_pause('second type is called green snakes', 2)
        print_pause('this type is very weak but has a strong hit', 2)
        print_pause("its can decrease your health about 2000pt", 2)
        print_pause("but they can't hurt you if you are attacking "
                    "from close "
                    "area like in aggressive attack", 2)
        print_pause("except that,actually you will die", 2)
        print_pause('third type is called giants ', 2)
        print_pause('those are tall and huge', 2)
        print_pause("they are so strong,their health about 1100 "
                    "and their hit,its about 60pt", 2)
        print_pause("in the end,you will meet the great mother", 2)
        print_pause("she is stronger than giants", 2)
        print_pause("she has a hit stronger than snakes", 2)
        print_pause("her health is 4000", 2)
        print_pause("and her power is 2500", 2)
        print_pause("and we well move to the important"
                    " part is the attack style", 2)
        print_pause("there are two types of attacks defensive"
                    " attack and aggressive attack", 2)
        print_pause("aggressive attack when you attack with "
                    "all power you have", 2)
        print_pause("defensive attack when you attack"
                    " with only 10% from your power", 2)
        print_pause("and also the hit of your opponent is"
                    " decreased to 10%", 2)
        print_pause("but that is useful in some cases", 2)
        print_pause("now, you are ready to play", 2)

    print_pause("now, you are going to defeat the"
                " great mother", 2)
    print_pause("so be careful because these"
                " organisms are so sly", 2)
    print_pause("you entered the great mother's building ", 2)
    print_pause("what's that,all of lights are turned off"
                ",i think they knew that you are here ", 2)
    round_1()
    print_pause("please,take care! you are only one that"
                " can save us ", 2)
    print_pause("you are going to the great mother", 2)
    round_1()
    print_pause("you are very close to reach to your"
                " target ", 2)
    round_1()
    z = random.randint(1000, 3000)
    print_pause(f"ooh, we found the additional health and"
                f" power about {z}pt", 1)
    print_pause("really, that's amazing", 2)
    if gender2 == 'man':
        the_health = man[1] + z
        the_power = man[0] + z
    if gender2 == 'woman':
        the_health = woman[1] + z
        the_power = woman[0] + z
    print_pause(f"your health is {the_health} ", 1)
    print_pause(f"and your power is {the_power}", 1)
    print_pause("i think the great mother will appear now!", 1)
    print_pause("OMG,great mother is here,", 1)
    mother_health = 4000
    mother_power = 2500
    print_pause("start your attack", 1)
    attacking_style = input("aggressive(1)/defensive(2)")
    while attacking_style != "1" and attacking_style != "2":
        print('please,enter 1 or 2')
        attacking_style = input("")
        if attacking_style == '1' or attacking_style == '2':
            break
    if attacking_style == '1':
        j = 1
    else:
        j = 1 / 10

    while True:

        the_health = the_health - (mother_power * j)
        mother_health = mother_health - (the_power * j)
        if the_health < 0:
            the_health = 0
        if mother_health < 0:
            mother_health = 0
        print_pause(f"{random.choice(congratulations)} you "
                    f"decreased the Great mother health to "
                    f"{mother_health}pt", 1)
        print_pause(f"but you are attacked,your health is"
                    f" {the_health}pt", 1)
        print_pause("                                      ", 0)
        if mother_health <= 0 or the_health <= 0:
            break
    if mother_health <= 0:
        print_pause("congratulation, you killed all of them", 1)
        print_pause("     (: you won :)     ", 1)
        print_pause("do you wanna play again??", 1)
        play_again = input("yes(1)/no(2)")
        while play_again != '1' and play_again != '2':
            print_pause('please,enter 1 or 2', 1)
            play_again = input("")
            if play_again == '1' or play_again == '2':
                break
        if play_again == '1':
            playing_again()
        if play_again == '2':
            sys.exit("okay, see you in another invasion")
    if the_health <= 0:
        print_pause("Game Over", 2)
        print_pause(" you are killed", 1)
        print_pause("do you wanna play again??", 1)
        play_again = input("yes(1)/no(2)")
        while play_again != '1' and play_again != '2':
            print_pause('please,enter 1 or 2', 1)
            play_again = input("")
            if play_again == '1' or play_again == '2':
                break
        if play_again == '1':
            playing_again()
        if play_again == '2':
            sys.exit("okay, see you in another invasion")


playing_again()
