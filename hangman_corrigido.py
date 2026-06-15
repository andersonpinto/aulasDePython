def hangman(word):
    stages = [
        "",
        "__________",
        "|        |",
        "|        |",
        "|        O",
        "|       /|\\",
        "|       / \\",
        "|"
    ]

    board = ["_"] * len(word)
    wrong = 0
    used_letters = set()   # <-- fora do while

    print("Bem-vindo ao jogo da forca!")

    while wrong < len(stages) - 1:

        print("\nPalavra:", " ".join(board))
        print("Letras usadas:", ", ".join(sorted(used_letters)))

        guess = input("Digite uma letra: ").lower()

        if guess in used_letters:
            print("Você já tentou essa letra!")
            continue

        used_letters.add(guess)

        found = False

        for i in range(len(word)):
            if word[i].lower() == guess:
                board[i] = word[i]
                found = True

        if not found:
            wrong += 1

        print("\n".join(stages[:wrong + 1]))

        if "_" not in board:
            print("\nVocê ganhou!")
            print("Palavra:", "".join(board))
            return

    print("\nVocê perdeu!")
    print("A palavra era:", word)


hangman("letter")