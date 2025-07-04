VERBOSE

10  LDI R1 1       // R1 ← 1（結果の初期値）
20  LDI R2 2       // R2 ← 2（累乗の底: 固定値）
30  LDI R3 5       // R3 ← 5（カウンタ: 指数）
40  LDI R4 1       // R4 ← 1（ループで減算する値）
50  LDI R5 0       // R5 ← 0（ループ終了の判定用）

60  MUL R1 R2      // R1 ← R1 × R2（結果に底を掛ける）
70  SUB R3 R4      // R3 ← R3 - 1（指数を1減らす）
80  CMP R3 R5      // R3 == 0 ?（カウンタがゼロか比較）
90  JNE 60         // R3 ≠ 0なら60行目にジャンプ（ループ継続）

100 PRINT R1       // 計算結果（2^5 = 32）を出力
110 HALT           // プログラム終了