def hangman(word):
    stages = [
        "",
        "________        ",
        "|               ",
        "|        |      ",
        "|        O      ",
        "|       /|\\     ",
        "|       / \\     ",
        "|               "
    ]

    board = ["_"] * len(word)
    wrong = 0

    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:

        print("\nPalavra:", " ".join(board))
        guess = input("Guess a letter: ").lower()

        found = False

        for i in range(len(word)):
            if word[i].lower() == guess:
                board[i] = word[i]
                found = True

        if not found:
            wrong += 1

        print("\n".join(stages[:wrong + 1]))

        if "_" not in board:
            print("\nYou won!")
            print("Palavra:", "".join(board))
            return

    print("\nYou lose!")
    print("The word was:", word)


hangman("letter")