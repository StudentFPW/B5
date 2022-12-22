# Игру разработал студент (Leonids Jofe) из школы SkillFactory, курс Full-stack python developer, класс FPW-104

starting_space = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

cell_step = 0


def over():
    row = -1
    column = -1
    result = False
    # Здесь я должен был написать алгоритм на проверку по диагонали, но не додумался как лучше это сделать.
    # Были варианты, но все приводило к ошибке с выводом победы.
    for i in range(len(starting_space)):
        column_win_x = 0
        column_win_o = 0
        column += 1
        for j in range(len(starting_space)):
            # Это проверка, выиграл ли игрок по вертикали.
            if starting_space[j][i] == "x":
                column_win_x += 1
            if starting_space[j][i] == "o":
                column_win_o += 1
            if column == 0 and column_win_x == 3 or column_win_o == 3:
                if column_win_x == 3:
                    result = "Игрок x выиграл вертикально"
                else:
                    result = "Игрок o выиграл вертикально"
                break
            if column == 1 and column_win_x == 3 or column_win_o == 3:
                if column_win_x == 3:
                    result = "Игрок x выиграл вертикально"
                else:
                    result = "Игрок o выиграл вертикально"
                break
            if column == 2 and column_win_x == 3 or column_win_o == 3:
                if column_win_x == 3:
                    result = "Игрок x выиграл вертикально"
                else:
                    result = "Игрок o выиграл вертикально"
                break

    for i in range(len(starting_space)):
        row_win_x = 0
        row_win_o = 0
        row += 1
        for j in range(len(starting_space)):
            # Это проверка, выиграл ли игрок по горизонтали.
            if starting_space[i][j] == "x":
                row_win_x += 1
            if starting_space[i][j] == "o":
                row_win_o += 1
            if row == 0 and row_win_x == 3 or row_win_o == 3:
                if row_win_x == 3:
                    result = "Игрок x выиграл горизонтально"
                else:
                    result = "Игрок o выиграл горизонтально"
                break
            if row == 1 and row_win_x == 3 or row_win_o == 3:
                if row_win_x == 3:
                    result = "Игрок x выиграл горизонтально"
                else:
                    result = "Игрок o выиграл горизонтально"
                break
            if row == 2 and row_win_x == 3 or row_win_o == 3:
                if row_win_x == 3:
                    result = "Игрок x выиграл горизонтально"
                else:
                    result = "Игрок o выиграл горизонтально"
                break

    return result


def cell_result():
    print(" ", *list(range(len(starting_space))))
    for i in range(len(starting_space)):
        print(i, *starting_space[i])


def cells(step, symbol):
    global cell_step
    if symbol == "x":
        if starting_space[int(step[0])][int(step[1])] == "o":
            print(f"Ячейка {int(step[0]), int(step[1])} занята игроком o")
            tictactoe_player_1()
        if starting_space[int(step[0])][int(step[1])] == "x":
            print(f"Ячейка {int(step[0]), int(step[1])} занята вами")
            tictactoe_player_1()
        if starting_space[int(step[0])][int(step[1])] == "-":
            starting_space[int(step[0])][int(step[1])] = symbol
            if over():  # Это проверка на конец игры.
                print("========== Конец игры ==========")
                cell_result()
                print(over())
            else:
                tictactoe_player_2()

    if symbol == "o":
        if starting_space[int(step[0])][int(step[1])] == "x":
            print(f"Ячейка {int(step[0]), int(step[1])} занята игроком x")
            cell_step -= 1
            tictactoe_player_2()
        if starting_space[int(step[0])][int(step[1])] == "o":
            print(f"Ячейка {int(step[0]), int(step[1])} занята вами")
            cell_step -= 1
            tictactoe_player_2()
        if starting_space[int(step[0])][int(step[1])] == "-":
            starting_space[int(step[0])][int(step[1])] = symbol
            if over():
                print("========== Конец игры ==========")
                cell_result()
                print(over())
            else:
                tictactoe_player_1()


def tictactoe_player_1():
    cell_result()
    cell_player_1 = input("↑ ход игрока x = ")
    cells(cell_player_1, "x")


def tictactoe_player_2():
    cell_result()
    global cell_step
    if cell_step < 4:  # Это проверка на количество ходов игрока о.
        cell_step += 1
        cell_player_2 = input("↑ ход игрока o = ")
        cells(cell_player_2, "o")
    else:
        print("========== Конец игры ==========")


def start(player):
    if player == "y":
        print("Ход игры подается без пробелов между цифр, например (11)правильно, (1 1)неправильно")
        print("Игрок x начинает первый :)")
        tictactoe_player_1()
    else:
        print("До встречи :)")


start(input("Начать игру ? y/n = ").lower())
