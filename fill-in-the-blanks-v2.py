# Udacity, Introduction to Programming, project 3: Code Your Own Quiz
# by: Michael Schneider

# First thing: we have our quizzes. These will be pulled by the Program
# deppending on what the user would like to try.  Then the Program
# will itterate through the texts and decide when there is a question that
# needs user input.
quiz = [
        '''When you take 44 and subtract 42 you will be left with ___a___.
Of course the square root of 9 equals ___b___. To compound 1 + 2 + 3 will give
___c___. Now if we divide 100 by 25 we get ___d___. Finally we know that
2 * 2 * 2 equals ___e___.''',

        '''If we use two or more slices of bread to contain or wrap some
other food we would call that a ___a___.  A traditional Mexican dish
using corn or wheat tortillas to fold or roll the food is a ___b___, not to be
confused with its big brother the burrito. But, dont forget the Japanese. They
prepare their ___c___ by using vinegared rice either as wrapping or bedding.
The Italian's also have something special by Raffaele Esposito he created the
first ___d___, fit for a Queen. It had tomatoes, mozzarella and bazil all the
colors of the Italian flag. And of course, dont forget George Crum. He took
thinly sliced potatoes and fried them; the ___e___ was born and we've all been
happier since!''',

        '''The brightest star in the night sky is ___a___, found in the Canis
Major constalation.  Only two planets have no moons, Mercury and ___b___.  At
night you can calculate your ___c___ by measuring the angle between the horizon
and the North Star (Polaris).  The Horsehead Nebula is a dust cloud in the
constalation of ___d___, where proto-stars are collapsing to form new stars.
Olympus Mons is the largest volcano in the solar system, located on the planet
___e___.'''
        ]

# This is how we let the program know there is a question that needs answering.
blank_spaces = ["___a___", "___b___", "___c___", "___d___", "___e___"]

#This is the list of correct answers
answers = [
        ["2", "3", "6", "4", "8"],
        ["sandwich", "taco", "sushi", "pizza", "potato chip"],
        ["Sirius", "Venus", "latitude", "Orion", "Mars"],
        ]

# Will use this string to store user answers.
user_answers = ['','','','','']

#this counts number of words per line so that I can put in line breaks later on
words_this_line = 0

#checks our words to see if there is a blank space
def word_is_blank (word, blank_spaces):
    for spaces in blank_spaces:
        if spaces in word:
            return spaces
    return None

#If the main program has found a blank space, or testquestion: this takes that
#input and then outputs a corrisponding number that is used to coordinate
#the correct string position for questions and answers
def answer_number (testquestion):
    if "a" in testquestion:
        return 0
    if "b" in testquestion:
        return 1
    if "c" in testquestion:
        return 2
    if "d" in testquestion:
        return 3
    if "e" in testquestion:
        return 4
    return None

#Pulls the correct quiz based on what the user has inputed they want to play
def get_quiz (quiz_choice):
    print " "
    if "easy" in quiz_choice:
        print "You chose the softest possible! ...easy peasy:"
        return 0
    if "medium" in quiz_choice:
        print "The cheddar cheese option? ...medium it is:"
        return 1
    if "hard" in quiz_choice:
        print "Yeah, Hard! Remember to capitalize proper nouns on this one:"
        return 2
    print "Check your spelling...  easy chosen by default."
    return 0

#Checks what answer number we're on and then compares the user_input to the
#correct answer for that space.
def check_answer (user_input, testquestion, answers):

    AnsNum = answer_number(testquestion)
    MaxTries = 4

    if user_input == answers[AnsNum]:
        print "True!"
        if AnsNum < MaxTries:
            print "Next Question:"
        print " "
        return 1
    else:
        print "False!"
        return 0

#Does the question asking and reasking if need be
#Inputs:  word, testquestion, answers, ANumber, user_answers
#Outputs:  word: either the correct answer or -WRONG ANSWER-
def ask_questions (word, testquestion, answers, ANumber, user_answers):

    tries = 4
    #Actually gives 5 tries, as it doesn't count the first attempt
    while (tries >= 0):

        user_input = raw_input("Please type in an answer for " + testquestion + " ")
    #---------> tests input by sending it to a function that checks against the answer key
        if (check_answer(user_input, testquestion, answers) == 1):
            user_answers[ANumber] = user_input
            return word.replace(testquestion, user_input)
        else:
    #---------> gives the user more tries at getting the correct answer
            if tries == 1:
                print str(tries) + " Try remaining!"
            elif tries == 0:
                user_answers[ANumber] = "-WRONG ANSWER-"
                print str(tries) + " tries remaining...  Next Question:"
                return word.replace(testquestion, "-WRONG ANSWER-")
            else:
                print str(tries) + " tries remaining!"
            print " "
            tries = tries - 1

#>>>>>>>-----------------------------------<<<<<<<<<<
#>>>>>>>-------------MAIN PROGRAM----------<<<<<<<<<<
#>>>>>>>-----------------------------------<<<<<<<<<<
def start_quiz (quiz, blank_spaces, answers, user_answers, words_this_line):

    #need a finished string to drop stuff into
    #and need to split the quiz so I can work on each individual word
    finished_quiz = []
    quiz = quiz.split()

    #then we itterate through our quiz
    for word in quiz:
        #if words per line gets above 8 I want to start a new line
        words_this_line = words_this_line + 1
        if words_this_line == 8:
            finished_quiz.append("\n")
            #and then reset it for a new line
            words_this_line = 0

        #and run a test to see if our word is a blank space
        testquestion = word_is_blank(word, blank_spaces)

#If our word came back as a blank_space, we'll ask the user for answers
        if (testquestion != None):
            #figure out what question we're on
            ANumber = answer_number(testquestion)
            #if the quiz asks the same question multiple times this will
            #limit asking the question again and simply take the user's
            #first attempt
            if (user_answers[ANumber] != ''):
                finished_quiz.append(word.replace(testquestion, user_answers[ANumber]))
            #If the question isn't answered, this does the actual question asking
            #by sending over all the relavant data and getting a word back, either
            #the correct answer or -WRONG ANSWER-
            else:
                finished_quiz.append(ask_questions(word, testquestion, answers, ANumber, user_answers))
#--- Push non-break words through like normal ----
        else:
            finished_quiz.append(word)

    #Now we need to put join all our words backtogether into one finished string
    #and return it to the main program, whew!
    finished_quiz = " ".join(finished_quiz)
    return finished_quiz



##This is the actual game
print "Welcome one and all! This is The AmazingTextBasedQuizGame Extravaganza!"
print " "
print "Please choose a quiz difficulty level."
player_choice = raw_input("Your choices are: easy, medium, or hard:  ")
difficulty = get_quiz(player_choice)
print " "
print quiz[difficulty]
print " "
print start_quiz(quiz[difficulty], blank_spaces, answers[difficulty], user_answers, words_this_line) + "\n"

#the only point of this code is to prevent the window from closing at the very
#end and give the user a chance to think over what just happened.
review = raw_input("\n" + "On a scale from 1-10 how much fun was this Quiz?")
print " "
print (review + " ") * 700
