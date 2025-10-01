def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))


cheakerBorad = []

alt1 = [1,0,1,0,1,0,1,0]
alt2 = [0,1,0,1,0,1,0,1]

cheakerBorad.append(alt2)
cheakerBorad.append(alt1)
cheakerBorad.append(alt2)
cheakerBorad.append([0]*8)
cheakerBorad.append([0]*8)
cheakerBorad.append(alt1)
cheakerBorad.append(alt2)
cheakerBorad.append(alt1)

print_board(cheakerBorad)