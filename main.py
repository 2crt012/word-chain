import array

globals()['is_first_word_added'] = False
globals()['cur_player'] = 1
globals()['p1name'] = "Player One"
globals()['p2name'] = "Player Two"
used_words = []

print("Welcome to word-chain, a game where players take turns saying words that begin with the last letter of the previous word.")
globals()['p1name'] = input("Player One, please enter your name: ")
globals()['p2name'] = input("Player Two, please enter your name: ")
input("Press Enter to start the game...")
def startgame():
    if not globals()['is_first_word_added']:
        global used_words
        used_words = []
        word = input(f"{globals()['p1name']}, enter a word: ").lower()
        used_words.append(word)
        globals()['word_e'] = word[-1]
        globals()['is_first_word_added'] = True
        globals()['cur_player'] = 2
    else:
        if globals()['cur_player'] == 1:
            globals()['cur_player_name'] = globals()['p1name']
        elif globals()['cur_player'] == 2:
            globals()['cur_player_name'] = globals()['p2name']
        else:
            print("Something is seriously wrong with the code of this game. The number of the current player is not 1 or 2.")
        word = input(f"{globals()['cur_player_name']}, enter a word that starts with '{globals()['word_e']}': ").lower()
        if word in used_words:
            print(f"Oops! {globals()['cur_player_name']} lost because they entered a word that was already said.")
            input("Press Enter to try again.")
            globals()['is_first_word_added'] = False
        used_words.append(word)
        word_s = word[0]
        if globals()['word_e'] == word_s:
            globals()['word_e'] = word[-1]
            if globals()['cur_player'] == 1:
                globals()['cur_player'] = 2
            elif globals()['cur_player'] == 2:
                globals()['cur_player'] = 1
        else:
            print(f"Oops! {globals()['cur_player_name']} lost because the word didn't start with the correct letter.")
            input("Press Enter to try again")
            globals()['is_first_word_added'] = False
        
while True:
    startgame()