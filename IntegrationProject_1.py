#Developed by Richardson Jacques
#A point-based multiple choice quiz that gives your grade at the end of the quiz as well as a phrase that corresponds to said grade.

#Code descriptions

#Citations

#Introduction
name = input("What is your name? ")
print("Hello",name+"!", "I am your testing instructor.\nDon't worry about your skill in academics, \nthis is just a pop quiz about one "
    "of the world's favorite pasttimes, videogames!")
print("P.S. You may need to type in the answers in capital form.")
#operator & descriptions
# + adds numerical values and connects strings
# - subtracts numerical values
# * multiplication
# ** exponents
# / traditional divison
# // interger division; gives the quotient without the remainder(or decimal)
# % divides by the divisor but outputs the remainder

#Quiz start Programming (This was based off of repl.it 8.2)
def quizStart():
    start = input("Just type in 'S' when you want to start.")
    while start == "S":
        test()
    else:
        print("Error. Please follow the instructions.")
        quizStart()

def test():
    import math
    # Score Coding()
    score = 0
    pointGain= (7.14285714286)
    format(pointGain,'.11f')

    # Questions

    # Question 1
    answer1 = "C"
    print("Question 1:\nLink, the main protagonist of the Legend of Zelda games, is in possession of which triforce piece?")
    print("A: The Triforce of Power \nB: The Triforce of Wisdom \nC: The Triforce of Courage")
    if input() == answer1:
        score = score + pointGain
    else:
        score = score

    # Question 2
    answer2 = "B"
    print("Question 2:\nWhat games are PuffBallsUnited 'best' known for?")
    print("A: SPORTS (LDJam) \nB: The Henry Stickmin Games \nC: Lucky Tower")
    if (input() == answer2):
        score = score + pointGain
    else:
        score = score

    # Question 3
    answer3 = "A"
    print("Question 3:\nWhat game series is Ninja Kiwi 'best' known for?")
    print("A: Bloons Tower Defence \nB: SAS Zombie Assault \nC: Red Reign")
    if (input() == answer3):
        score = score + pointGain
    else:
        score = score

    # Question 4
    answer4 = "A"
    print("Question 4:\nWhere does Assassin's Creed Valhalla take place?")
    print("A: England \nB: Finland \nC: Greenland")
    if (input() == answer4):
        score = score + pointGain
    else:
        score = score

    # Question 5
    answer5 = "C"
    print("Question 5:\nWhat is the name of the scientist who commonly aids Mario or Luigi in their adventures?")
    print("A: Kamek \nB: Toadsworth \nC: Professor Elvin Gadd ")
    if (input() == answer5):
        score = score + pointGain
    else:
        score = score

    # Question 6
    answer6 = "A"
    print("Question 6:\nWhich video game made the most sales since its release?")
    print("A: Minecraft \nB: Tetris \nC: Grand Theft Auto V")
    if (input() == answer6):
        score = score + pointGain
    else:
        score = score

    # Question 7
    answer7 = "B"
    print("Question 7:\nWho was Toby Fox's main partner during Undertale's development?")
    print("A: Eric Barone \nB: Temmie Chang \nC: Kouichi Ooyama")
    if (input() == answer7):
        score = score + pointGain
    else:
        score = score

    # Question 8
    answer8 = "B"
    print("Question 8:\nWhat is the name of the secret boss in Deltarune?")
    print("A: Rouxls Kaard \nB: Jevil \nC: Seam")
    if (input() == answer8):
        score = score + pointGain
    else:
        score = score

    # Question 9
    answer9 = "C"
    print("Question 9:\nWhat is the known release date of the Playstation 5(in the USA)?")
    print("A: Oct 27, 2020 \nB: Nov. 7,2020 \nC: Nov. 12, 2020")
    if (input() == answer9):
        score = score + pointGain
    else:
        score = score

    # Question 10
    answer10 = "B"
    print("Question 10:\nWhat month does E3 typically take place in?")
    print("A: May \nB: June \nC: July")
    if (input() == answer10):
        score = score + pointGain
    else:
        score = score

    # Question 11
    answer11 = "B"
    print("\nQuestion 11: Which of the Klonoa games introduces the 360 degree in "
          "their boss fights ")
    print("A: Klonoa: Door to Phantomile \nB: Klonoa 2 Lunatea's Veil")
    if (input() == answer11):
        score = score + pointGain
    else:
        score = score
    # FunFact (connecting strings with + operator)
    print("Aside from these two options above, there are 5 more Klonoa games "
          "developed and released from outside the US" + "\n(discluding the remakes of course)."
          + "\nThis means that there are 7 Klonoa games in total!")

    # Question 12
    answer12 = ""
    print("Question 12: \n In 'A Hat in Time' which hat allows you to "
          "materialize holographic objects")
    print("A: Ice Hat \nB: Brewing Hat \nC: Dweller's Mask")
    if (input() == answer12):
        score = score + pointGain
    else:
        score = score
    # FunFact(using multiplication with the * operator)
    print("There are 6 main hats you can use in this game as well as 16 "
          "different badges, not to mention you can equip 2 each each with "
          "their own ability. In other words there are", (6 * (16 * 16)), "different combinations of ways to play this game")

    # Question 13(Using % to find the remainder to tell whether or not the number
    # is even or odd)
    answer13 = "B"
    print("Question 13: On the game website 'Poptropica' how many islands are "
          "there (discluding Poptropica Worlds)")
    print("A: 44 \nB: 47 \nC: 49")
    if (input() == answer13):
        score = score + pointGain
    else:
        score = score
    # FunFact
    if 47 % 2 != 0:
        print("Poptropica has an odd total of 47 islands (discluding Poptropica "
              "Worlds) ")

    # Question 14
    answer14 = "A"
    print("Question 14: In Infamous Second Son, which power is Delsin's main goal in obtaining")
    print("A: Concrete \nB: Video \nC: Neon")
    if (input() == answer14):
        score = score + pointGain
    else:
        score = score
    # FunFact
    print("There are a total of 350 blast shards in Infamous Second Son (discluding mission gained shards) with 147 in the Neon district, "
          "135 in the Warren district and 68 in the Historic district")

    # Correct or Wrong (list each question number and states whether or not you
    # got it right or not)(Range Function could be used to list the correct and wrong answers and then build up the score here instead of
    # each question)

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

    # Closing (I found the termination code exit on hashbangcode (I couldn't stop the entire program from looping))
    if score != 100:
        print("There's always another chance to leave with a higher score. Do you want to try again? Type 'Y' (in CAPS) to try again and N to quit.")
        start = input()
        if start == "Y":
            quizStart()
        else:
            print("Thank you for taking my test! Done")
            exit()

    if score == 100:
        print("Congratulations for passing the test perfectly.  I hope you also enjoyed the FunFacts included with some of the questions "
              "\nThank you for taking my test! Done")




#Possible edits
#add a couple of price questions and company price questions
#add code that shows an error message if the player clicks enter before inputting an answer

quizStart()
