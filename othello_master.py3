##盤面の初期化
#0は何も石を置いていない,1は黒,2は白
othello_board = [[0 for i in range(8)] for j in range(8)]

othello_board[3][3] = 1
othello_board[4][4] = 1
othello_board[3][4] = 2
othello_board[4][3] = 2

##各ターンの処理
#skip_swが偶数なら"黒白どちらも置けない"のでループ終了
while not skip_sw % 2 == 0:

    skip_sw = 0

    #黒が置けない場合はターンをスキップ
    if 黒が置けない:
        skip_sw += 1

    #黒が置ける場合は盤面配列を更新
    else:
        a = int(input("黒のプレイヤーは行を入力してください";))
        b = int(input("黒のプレイヤーは列を入力してください";))
        othello_board[a][b] = 1
        #石を裏返す関数

    #白が置けない場合はターンをスキップ
    if 白が置けない:
        skip_sw += 1

    #黒が置ける場合は盤面配列を更新
    else:
        a = int(input("白のプレイヤーは行を入力してください";))
        b = int(input("白のプレイヤーは列を入力してください";))
        othello_board[a][b] = 2
        #石を裏返す関数

##勝敗判定
cnt_bk = othello_board.count(1)
cnt_wt = othello_board.count(2)

if cnt_bk < cnt_wt:
    print("白の勝ち")
elif cnt_bk > cnt_wt:
    print("黒の勝ち")
else:
    print("引き分け")
