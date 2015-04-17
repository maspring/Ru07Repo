import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random_word(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def display_board(HANGMANPICS, missed_letters, correct_letters, secretWord):
    print HANGMANPICS[len(missed_letters)]
    print

    print 'Missed letters:', missed_letters
    print

    blanks = '_' * len(secretWord) # Fancy way to print multiple underscores

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correct_letters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # In python, you have to have an empty to string to join on
    print ' '.join(blanks)

def get_guess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secretWord = get_random_word(words)
game_is_done = False

while True:
  """This is the game loop"""
  display_board(HANGMANPICS, missed_letters, correct_letters, secretWord)

  # Let the player type in a letter.
  guess = get_guess(missed_letters + correct_letters)

  if guess in secretWord:
      correct_letters = correct_letters + guess

      # Check if the player has won
      found_all_letters = True
      for i in range(len(secretWord)):
          if secretWord[i] not in correct_letters:
              found_all_letters = False
              break
      if found_all_letters:
          print('Yes! The secret word is "' + secretWord + '"! You have won!')
          game_is_done = True
  else:
      missed_letters = missed_letters + guess

      # Check if player has guessed too many times and lost
      if len(missed_letters) == len(HANGMANPICS) - 1:
          display_board(HANGMANPICS, missed_letters, correct_letters, secretWord)
          print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secretWord + '"')
          game_is_done = True

  # Ask the player if they want to play again (but only if the game is done).
  if game_is_done:
      if play_again():
          missed_letters = ''
          correct_letters = ''
          game_is_done = False
          secretWord = get_random_word(words)
      else:
          break
