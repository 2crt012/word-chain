globals()['is_first_word_added'] = False

print("Welcome to word-chain, a game where players take turns saying words that begin with the last letter of the previous word.")
input("Press Enter to start the game...")
def startgame():
    if not globals()['is_first_word_added']:
        word = input("Enter a word: ").lower()
        globals()['word_e'] = word[-1]
        globals()['is_first_word_added'] = True
    else:
        word = input(f"Enter a word that starts with '{globals()['word_e']}': ").lower()
        word_s = word[0]
        if globals()['word_e'] == word_s:
            globals()['word_e'] = word[-1]
        else:
            print("Oops! You lost.")
            input("Press Enter to try again")
            globals()['is_first_word_added'] = False
        
while True:
    startgame()