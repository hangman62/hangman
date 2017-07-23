import random
import sys

print '''
                    ********
                ****      ************
                **    **  **************
              ****        **
              ******    **************
              ********
            ************
            ************
          **********  ****
          **********  ******
        ************  ******
        **********  ********
      **********  **********  ****
      ******    **********    **
    ****************************
  ********  ******  **        **
********            **
  ******            **
    ****          ********
      **                **



'''

print u'Welcome to Hangman by Boobie (the Bird) Productions\u2122\n\n\n'

words = ['soldier', 'sailor', 'tinker', 'tailor', 'spy', 'stalker', 'orthodontist', 'ninja', 'doctor', 'teacher', 'samurai', 'chef', 'nurse', 'radiographer', 'carpenter', 'swimminginstructor', 'hatter']
the_word = random.choice(words)

print 'Word to guess:', '_ ' * len(the_word), '\n\n'

correct_guesses = []
while True:
    guess = raw_input("Guess a letter (or if you're a smarty pants, the whole damn word): ")

    if guess == the_word:
        print "You're a frickin' genius.  Go drink some prosecco and get off your tits."
        sys.exit(0)

    output = []
    for letter in the_word:
        if letter == guess:
            output.append(guess)
        elif letter in correct_guesses:
            output.append(letter)
        else:
            output.append("_")

    if ''.join(output) == the_word:
        print 'Congratulations.  You are not a loser.  You are super super smart and you should wear a medal.'
        sys.exit(0)

    if guess in the_word:
        print 'Good Job!'
        print ' '.join(output)
        correct_guesses.append(guess)

    else:
        print 'Better luck next time: lose a life, sucker!'
