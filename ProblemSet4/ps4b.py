from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maximum_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList) == True:

        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            word_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if word_score > maximum_score:
                maximum_score = word_score
                # Update your best score, and best word accordingly
                best_word = word

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0
    while compChooseWord(hand, wordList, n) != None:
        print "Current Hand: ",
        displayHand(hand)
        comp_choose_word = compChooseWord(hand, wordList, n)
        total_score += getWordScore(comp_choose_word, n)
        print "\"" + comp_choose_word + "\"" + " earned" + str(getWordScore(comp_choose_word, n)) \
            + " points." + " Total: " + str(total_score) + " points."
        print
        for x in comp_choose_word:
                        hand[x] = hand.get(x) - 1     
    if calculateHandlen(hand) > 0: 
        print "Current Hand: ",
        displayHand(hand)
        print " Total: " + str(total_score) + " points."
    else:
        print " Total: " + str(total_score) + " points."
    

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    times_of_input_n = 0
    user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
    while user_input_how != "e":
        if user_input_how == "n":
            hand = dealHand(HAND_SIZE)
            times_of_input_n += 1
            user_input_who = raw_input("Enter u to have yourself play, c to have the computer play:")
            while user_input_who != "u" and user_input_who != "c":
                print "Invalid command."
                user_input_who = raw_input("Enter u to have yourself play, c to have the computer play:")

            if user_input_who == "u":
                playHand(hand, wordList, HAND_SIZE)
                user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
            elif user_input_who == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
                user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
            
        elif user_input_how == "r" and times_of_input_n > 0:
            user_input_who = raw_input("Enter u to have yourself play, c to have the computer play:")
            while user_input_who != "u" and user_input_who != "c":
                print "Invalid command."
                user_input_who = raw_input("Enter u to have yourself play, c to have the computer play:")
            if user_input_who == "u":
                playHand(hand, wordList, HAND_SIZE)
                user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
            elif user_input_who == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
                user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
            
        elif user_input_how == "r" and times_of_input_n == 0:
            print "You have not played a hand yet. Please play a new hand first!"
            print
            user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")

        else:
            print "Invalid command."
            user_input_how = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


