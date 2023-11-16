from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

def move(board,dir): # 동서남북으로 모으는 함수
    if dir == 0: # 북쪽
        for j in range(N):
            point = 0
            for i in range(1,N):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[point][j] == 0: # 해당 자리가 빈 경우
                        board[point][j] = tmp
                    elif board[point][j] == tmp: # 해당 자리가 수가 같은경우
                        board[point][j] = 2 * tmp
                        point += 1
                    else: # 해당 자리가 수가 다른경우
                        point += 1
                        board[point][j] = tmp

    elif dir == 1: # 동쪽
        for i in range(N):
            point = N-1
            for j in range(N-2,-1,-1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][point] == 0: # 해당 자리가 빈 경우
                        board[i][point] = tmp
                    elif board[i][point] == tmp: # 해당 자리가 수가 같은경우
                        board[i][point] = 2 * tmp
                        point -= 1
                    else: # 해당 자리가 수가 다른경우
                        point -= 1
                        board[i][point] = tmp


    elif dir == 2: # 남쪽
        for j in range(N):
            point = N-1
            for i in range(N-2,-1,-1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[point][j] == 0: # 해당 자리가 빈 경우
                        board[point][j] = tmp
                    elif board[point][j] == tmp: # 해당 자리가 수가 같은경우
                        board[point][j] = 2 * tmp
                        point -= 1
                    else: # 해당 자리가 수가 다른경우
                        point -= 1
                        board[point][j] = tmp

    elif dir == 3: # 서쪽
        for i in range(N):
            point = 0
            for j in range(1,N):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][point] == 0: # 해당 자리가 빈 경우
                        board[i][point] = tmp
                    elif board[i][point] == tmp: # 해당 자리가 수가 같은경우
                        board[i][point] = 2 * tmp
                        point += 1
                    else: # 해당 자리가 수가 다른경우
                        point += 1
                        board[i][point] = tmp

    return board


def dfs(level, board):
    global res
    if level == 5: # 5번 이동 시행 후 확인
        for i in range(N):
            for j in range(N):
                res = max(res,board[i][j])
        return

    else:

        for i in range(4):
            copy_board = move(deepcopy(board),i)
            dfs(level+1, copy_board)


dfs(0,arr)
print(res)