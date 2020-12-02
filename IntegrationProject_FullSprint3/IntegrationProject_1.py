"""Intro to Computer Science Integration Program"""
__author__ = "Richardson Jacques"
# A point-based multiple choice quiz that gives your grade at the end of the
# quiz as well as a phrase that corresponds to said grade.

# Code descriptions

# Citations

# Introduction
name = input("What is your name? ")
print("Hello", name + "!",
      "I am your testing instructor.\nDon't worry about your skill in "
      "academics, \nthis is just a pop quiz about one of the world's "
      "favorite pasttimes, videogames!")
print("P.S. You may need to type in the answers in capital form.")


def topics():
    """This function lists all of the topics in the quiz in order"""
    print("To be more specific, we are going to cover the following "
          "topics:")
    game_topics = open('GameTopics.txt')
    for index in range(1, 14):
        gt = game_topics.readline()
        print(str(index) + ". ", gt)


# operator & descriptions
# + adds numerical values and connects strings
# - subtracts numerical values
# * multiplication
# ** exponents
# / traditional divison
# // interger division; gives the quotient without the remainder(or decimal)
# % divides by the divisor but outputs the remainder

# Quiz start Programming (This was based off of repl.it 8.2)
def quiz_start():
    """This function officially starts the quiz for the user when they are
    ready, if a different input is typed the programmed error message
    repeats the function until the correct input is used"""
    start = input("Just type in 'S' when you want to start.")
    while start == "S":
        test()
    else:
        print("Error. Please follow the instructions.")
        quiz_start()


def test():
    """This is the entirity of the test. The first part is the score system
    the rest are the multiple choice questions w/fun facts to go with each
    of them. The last parts of the function is meant to tell the user their
    scores and question whether or not they want to try the test again."""
    # Score Coding()
    score = 0
    point_gain = 100/20
    format(point_gain, '.1f')

    # Questions

    # Question 1
    answer1 = "C"
    print("Question 1:\nLink, the main protagonist of the Legend of Zelda "
          "games, is in possession of which triforce piece?")
    print("A: The Triforce of Power \nB: The Triforce of Wisdom \nC: The "
          "Triforce of Courage")
    if input() == answer1:
        score += point_gain
    else:
        score = score

    # Question 2
    answer2 = "B"
    print("Question 2:\nWhat games are PuffBallsUnited 'best' known for?")
    print("A: SPORTS (LDJam) \nB: The Henry Stickmin Games \nC: Lucky Tower")
    if input() == answer2:
        score += point_gain
    else:
        score = score

    # Question 3
    answer3 = "A"
    print("Question 3:\nWhat game series is Ninja Kiwi 'best' known for?")
    print("A: Bloons Tower Defence \nB: SAS Zombie Assault \nC: Red Reign")
    if input() == answer3:
        score += point_gain
    else:
        score = score

    # Question 4
    answer4 = "A"
    print("Question 4:\nWhere does Assassin's Creed Valhalla take place?")
    print("A: England \nB: Finland \nC: Greenland")
    if input() == answer4:
        score += point_gain
    else:
        score = score

    # Question 5
    answer5 = "C"
    print("Question 5:\nWhat is the name of the scientist who commonly aids "
          "Mario or Luigi in their adventures?")
    print("A: Kamek \nB: Toadsworth \nC: Professor Elvin Gadd ")
    if input() == answer5:
        score += point_gain
    else:
        score = score

    # Question 6
    answer6 = "A"
    print("Question 6:\nWhich video game made the most sales since its "
          "release?")
    print("A: Minecraft \nB: Tetris \nC: Grand Theft Auto V")
    if input() == answer6:
        score += point_gain
    else:
        score = score

    # Question 7
    answer7 = "B"
    print("Question 7:\nWho was Toby Fox's main partner during Undertale's "
          "development?")
    print("A: Eric Barone \nB: Temmie Chang \nC: Kouichi Ooyama")
    if input() == answer7:
        score += point_gain
    else:
        score = score

    # Question 8
    answer8 = "B"
    print("Question 8:\nWhat is the name of the secret boss in Deltarune?")
    print("A: Rouxls Kaard \nB: Jevil \nC: Seam")
    if input() == answer8:
        score += point_gain
    else:
        score = score

    # Question 9
    answer9 = "C"
    print("Question 9:\nWhat is the known release date of the Playstation 5"
          "(in the USA)?")
    print("A: Oct 27, 2020 \nB: Nov. 7,2020 \nC: Nov. 12, 2020")
    if input() == answer9:
        score += point_gain
    else:
        score = score

    # Question 10
    answer10 = "B"
    print("Question 10:\nWhat month does E3 typically take place in?")
    print("A: May \nB: June \nC: July")
    if input() == answer10:
        score += point_gain
    else:
        score = score

    # Question 11
    answer11 = "B"
    print("\nQuestion 11: Which of the Klonoa games introduces the 360 "
          "degree in their boss fights ")
    print("A: Klonoa: Door to Phantomile \nB: Klonoa 2 Lunatea's Veil")
    if input() == answer11:
        score += point_gain
    else:
        score = score
    # FunFact (connecting strings with + operator)
    print("Aside from these two options above, there are 5 more Klonoa games "
          "developed and released from outside the US" + "\n(discluding the "
                                                         "remakes of course)."
          + "\nThis means that there are 7 Klonoa games in total!")

    # Question 12
    answer12 = "C"
    print("Question 12: \n In 'A Hat in Time' which hat allows you to "
          "materialize holographic objects")
    print("A: Ice Hat \nB: Brewing Hat \nC: Dweller's Mask")
    if input() == answer12:
        score += point_gain
    else:
        score = score
    # FunFact(using multiplication with the * operator)
    print("There are 6 main hats you can use in this game as well as 16 "
          "different badges, not to mention you can equip 2 each each with "
          "their own ability. In other words there are", (6 * (16 * 16)),
          "different combinations of ways to play this game")

    # Question 13(Using % to find the remainder to tell whether or not the
    # number is even or odd)
    answer13 = "B"
    print("Question 13: On the game website 'Poptropica' how many islands are "
          "there (discluding Poptropica Worlds)")
    print("A: 44 \nB: 47 \nC: 49")
    if input() == answer13:
        score += point_gain
    else:
        score = score
    # FunFact
    if 47 % 2 != 0:
        print("Poptropica has an odd total of 47 islands (discluding "
              "Poptropica Worlds) ")

    # Question 14
    answer14 = "A"
    print(
        "Question 14: In Infamous Second Son, which power is Delsin's main "
        "goal in obtaining")
    print("A: Concrete \nB: Video \nC: Neon")
    if input() == answer14:
        score += point_gain
    else:
        score = score
    # FunFact
    print(
        "There are a total of 350 blast shards in Infamous Second Son ("
        "discluding mission gained shards) with 147 in the Neon district, "
        "135 in the Warren district and 68 in the Historic district")

    # Question 15
    answer15 = "B"
    print(
        "Question 15: What is the name of the Island in which several of "
        "Nintendo's Wii fitness games takes place?")
    print("A: Wii Fit Island \nB: Wuhu Island \nC: Mii Island")
    if input() == answer15:
        score += point_gain
    else:
        score = score
    # FunFact
    print("Wuhu Island used to be referred to as Wii Fit Island until "
          "Shigeru Miyamoto later changed it to Wuhu Island with the release "
          "of Wii Sports Resort")

    # Question 16
    answer16 = "A"
    print("Question 16: In Super Smash Bros Ultimate: World of Light which "
          "character survives Galeem's attack?")
    print("A: Kirby \nB: Shulk \nC: Mario")
    if input() == answer16:
        score += point_gain
    else:
        score = score
    # FunFact
    print("Kirby debuted on the GameBoy in 1992, and has been one of the "
          "major mascots of Nintendo ever since")

    # Question 17
    answer17 = "A"
    print("Question 17: What is the name of the secretary that aids you in "
          "Animal Crossing?")
    print("A: Isabelle \nB: Tom Nook \nC: Ankha")
    if input() == answer17:
        score += point_gain
    else:
        score = score
    # FunFact
    print("Isabelle's appearance resembles that of a Shih Tzu (this is "
          "similar to her Japanese name - Shizue).")

    # Question 18
    answer18 = "C"
    print("Question 18: What is the name of Minecraft's most recent update?")
    print("A: Nether Update \nB: Buzzy Bees \nC: Caves and Cliffs")
    if input() == answer18:
        score += point_gain
    else:
        score = score
    # FunFact
    print("In this update there are new cave Biomes such as the Lush Caves, "
          "Caves, Deep Dark, and Mesh Caves, as well as new cave and "
          "mountain generation. Included with this are new items and mobs "
          "that relate to these Biomes such as goats and Wardens.")

    # Question 19
    answer19 = "A"
    print("Question 19: What is the main theme of the most recent Fortnite "
          "season?")
    print("A: Marvel \nB: DC \nC: Milestone Media")
    if input() == answer19:
        score += point_gain
    else:
        score = score
    # FunFact
    print("Fortnite Battle Royale (as well as PUBG) is inspired by the "
          "Japanese film ‘Battle Royale’, where a class of middle schooler "
          "are trapped on an isolated island and have to kill each other "
          "until there’s only one student left.")

    # Question 20
    answer20 = "B"
    print("Question 20: How many Pokemon game generations are there?")
    print("A: 7 \nB: 8 \nC: 9")
    if input() == answer20:
        score += point_gain
    else:
        score = score
    # FunFact
    print("During planning stages for the anime, Clefairy of all Pokemon was "
          "considered for Ash’s sidekick. Although eventually Pikachu was "
          "chosen")

    # Correct or Wrong (list each question number and states whether or not you
    # got it right or not)(Range Function could be used to list the correct
    # and wrong answers and then build up the score here instead of each
    # question)

    # Scores & comments
    if score == 100:
        print(name, "you got:", score, "Perfect!")
    elif score >= 90:
        print(name, "you got:", score, "Excellent")
    elif score >= 80:
        print(name, "you got:", score, "Really Good")
    elif score >= 70:
        print(name, "you got:", score, "Fair")
    elif score >= 60:
        print(name, "you got:", score, "Poor")
    else:
        print(name, "you got:", score, "Better luck next time")

    # Closing (I found the termination code exit on hashbangcode (I couldn't
    # stop the entire program from looping))
    if score != 100:
        print(
            "There's always another chance to leave with a higher score. Do "
            "you want to try again? Type 'Y' (in CAPS) to try again and N to "
            "quit.")
        start = input()
        if start == "Y":
            quiz_start()
        else:
            print("Thank you for taking my test! Done")
            exit()

    if score == 100:
        print(
            "Congratulations for passing the test perfectly.  I hope you "
            "also enjoyed the FunFacts included with some of the questions."
            "\nThank you for taking my test! Done")
        exit()


# Possible edits
# add a couple of price questions and company price questions
# add code that shows an error message if the player clicks enter before
# inputting an answer

topics()
quiz_start()
