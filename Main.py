#Developed by Richardson Jacques
#A point-based multiple choice quiz that gives your grade at the end of the quiz as well as a phrase that corresponds to said grade.

#Code descriptions

#Citations

#Introduction
name = input("What is your name? ")
print("Hello",name+"!", "I am your testing instructor.\nDon't worry about your skill in academics, \nthis is just a pop quiz about one of the world's favorite pasttimes, videogames!\nJust type in 'start' when you want to begin." )
print("P.S. You may need to type in the answers in capital form.")
#operator & descriptions
# + adds numerical values and connects strings
# - subtracts numerical values
# * multiplication
# ** exponents
# / traditional divison
# // interger division; gives the quotient without the remainder(or decimal)
# % divides by the divisor but outputs the remainder

#Quiz start


#Score Coding
score = 0

#Questions

#Question 1
answer1 = "C"
print("Question 1:\nLink, the main protagonist of the Legend of Zelda games, is in possession of which triforce piece?")
print("A: The Triforce of Power \nB: The Triforce of Wisdom \nC: The Triforce of Courage")
if(input() == answer1):
    score = score + 10 
else:
    score = score

#Question 2
answer2 = "B"
print("Question 2:\nWhat games are PuffBallsUnited 'best' known for?")
print("A: SPORTS (LDJam) \nB: The Henry Stickmin Games \nC: Lucky Tower")
if(input() == answer2):
    score = score + 10 
else:
    score = score

#Question 3
answer3 = "A"
print("Question 3:\nWhat game series is Ninja Kiwi 'best' known for?")
print("A: Bloons Tower Defence \nB: SAS Zombie Assault \nC: Red Reign")
if(input() == answer3):
    score = score + 10 
else:
    score = score

#Question 4
answer4 = "A"
print("Question 4:\nWhere does Assassin's Creed Valhalla take place?")
print("A: England \nB: Finland \nC: Greenland")
if(input() == answer4):
    score = score + 10 
else:
    score = score

#Question 5
answer5 = "C"
print("Question 5:\nWhat is the name of the scientist who commonly aids Mario or Luigi in their adventures?")
print("A: Kamek \nB: Toadsworth \nC: Professor Elvin Gadd ")
if(input() == answer5):
    score = score + 10 
else:
    score = score

#Question 6
answer6 = "A"
print("Question 6:\nWhich video game made the most sales since its release?")
print("A: Minecraft \nB: Tetris \nC: Grand Theft Auto V")
if(input() == answer6):
    score = score + 10 
else:
    score = score

#Question 7
answer7 = "B"
print("Question 7:\nWho was Toby Fox's main partner during Undertale's development?")
print("A: Eric Barone \nB: Temmie Chang \nC: Kouichi Ooyama")
if(input() == answer7):
    score = score + 10 
else:
    score = score

#Question 8
answer8 = "B"
print("Question 8:\nWhat is the name of the secret boss in Deltarune?")
print("A: Rouxls Kaard \nB: Jevil \nC: Seam")
if(input() == answer8):
    score = score + 10 
else:
    score = score

#Question 9
answer9 = "C"
print("Question 9:\nWhat is the known release date of the Playstation 5(in the USA)?")
print("A: Oct 27, 2020 \nB: Nov. 7,2020 \nC: Nov. 12, 2020")
if(input() == answer9):
    score = score + 10 
else:
    score = score

#Question 10
answer10 = "B"
print("Question 10:\nWhat month does E3 typically take place in?")
print("A: May \nB: June \nC: July")
if(input() == answer10):
    score = score + 10 
else:
    score = score

#Scores & comments
if score == 100:
    print(name,"you got:", score,"Perfect!")
elif score >= 90:
    print(name,"you got:", score,"Execelent")
elif score >= 80:
    print(name,"you got:", score,"Really Good")
elif score >= 70:
    print(name,"you got:", score,"Fair")
elif score >= 60:
    print(name,"you got:", score,"Poor")
else:
    print(name,"you got:", score,"Better luck next time")

#possible edits
#add a couple of price questions and company price questions
#add code that shows an error message if the player clicks enter before inputting an answer
