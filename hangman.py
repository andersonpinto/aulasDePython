def hangman(word):
    wrong = 0
    stages =    ["",
                "________        ",
                "|               ",
                "|        |      ",
                "|        0      ",
                "|       /|\\    ",
                "|       / \\    ",
                "|               "
    ]
    rletters = list(word)
    board = [" __ "] * len(word)
    win = False
    print("Bem-vindo ao jogo da forca")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Adivinhe a palavra secreta: "
        char = input(msg)
        if char in rletters:
            cind= rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if " __ " not in board:
            print("Você ganhou!!!")
            print(" ".join(board))
            win = True
            break
            if not win:
                print("\n".join(stages[0:wrong]))
                print("Você perdeu! A palavra secreta é {}.".format(word))

hangman("baal")