# BVM Lily v0.1 readme

## サンプルプログラム
各命令の詳細な動作が知りたい場合は先頭に付されている`VERBOSE`のコメントアウトを外して実行してください(出力例には`VERBOSE`が無効化されている時のものを掲載しています)

### ADDとSUB

簡単な足し算と引き算を実行するプログラムです。

```Assembly
// VERBOSE

10  LDI R1 2       // R1 ← 2（初期値をセット）
20  LDI R2 3       // R2 ← 3（加算・減算に使う値）

30  ADD R1 R2      // R1 ← R1 + R2（2 + 3 = 5）
40  SUB R1 R2      // R1 ← R1 - R2（5 - 3 = 2）→ 結果的にR1は元の値に戻る

50  HALT           // プログラム終了
```

```出力
Verbose disable.
Initialized. | Verbose : False

Called HALT.
Exitcode : 0
Status : 正常終了
```

### n^m

```Assembly
// VERBOSE

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
```

```出力
Verbose disable.
Initialized. | Verbose : False

R1 : 32

Called HALT.
Exitcode : 0
Status : 正常終了
```