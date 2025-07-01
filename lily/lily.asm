// m^nを計算するプログラム
// R1とR2にm、r3にnを代入

// コメントアウトを削除してすべての命令の実行状況を表示
// verbose

20 ldi r1 2
30 ldi r2 2
40 ldi r3 8    // 乗数を決定
50 ldi r4 0
51 ldi r5 1    // 乗数デクリメント用

52 sub r3 r5
// ループ開始ポイント
60 cmp r3 r4
61 je 82
70 mul r1 r2
80 sub r3 r5
81 jmp 60

82 print r1
90 halt