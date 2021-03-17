grid = {'T1': ' ', 'T2': ' ', 'T3': ' ',
        'M1': ' ', 'M2': ' ', 'M3': ' ',
        'L1': ' ', 'L2': ' ', 'L3': ' ',
        "STOP": " "}


def checker(board):
    win = False
    if board["T1"] == board["T2"] == board["T3"] != " ":
        win = True
    if board["M1"] == board["M2"] == board["M3"] != " ":
        win = True
    if board["L1"] == board["L2"] == board["L3"] != " ":
        win = True
    if board["T1"] == board["M2"] == board["L3"] != " ":
        win = True
    if board["L1"] == board["M2"] == board["T3"] != " ":
        win = True
    if board["L1"] == board["M1"] == board["T1"] != " ":
        win = True
    if board["L2"] == board["M2"] == board["T2"] != " ":
        win = True
    if board["L3"] == board["M3"] == board["T3"] != " ":
        win = True

    return win


def show_(y):
    print(y["T1"] + " " + "|" + ' ' + y['T2'] + ' ' + '|' + ' ' + y["T3"])
    print('__+___+__')
    print(y["M1"] + " " + "|" + ' ' + y['M2'] + ' ' + '|' + ' ' + y["M3"])
    print('__+___+__')
    print(y["L1"] + " " + "|" + ' ' + y['L2'] + ' ' + '|' + ' ' + y["L3"])
    print(" ")
    print("************************************************")


player = 0
moves = 0
list1 = []
command = ""
print("TIC TAC TOE")
print(" ")
print("positions for reference")
print("T1" + " " + "|" + ' ' + 'T2' + ' ' + '|' + ' ' + "T3")
print('___+____+___')
print("M1" + " " + "|" + ' ' + 'M2' + ' ' + '|' + ' ' + "M3")
print('___+____+___')
print("L1" + " " + "|" + ' ' + 'L2' + ' ' + '|' + ' ' + "L3")
print(" ")
print("************************************************")

while command != "STOP":
    show_(grid)
    if not checker(grid) and moves <= 9:
        if player % 2 == 0:
            command = input("player 1 ").upper()
            if command not in list1:
                grid[command] = "X"
                list1.append(command)
            else:
                print(" position occupied")
                continue
        else:
            command = input("player 2 ").upper()
            if command not in list1:
                grid[command] = "0"
                list1.append(command)
            else:
                print(" position occupied")
                continue
        player += 1
        moves += 1
    if checker(grid) or moves == 9:
        if checker(grid) and player % 2 == 0:
            show_(grid)
            print('')
            print("player 1 has won")
        elif checker(grid) and player % 2 != 0:
            show_(grid)
            print('')
            print("player 2 has won")
        elif moves == 9:
            show_(grid)
            print('')
            print("match tied")
        break
