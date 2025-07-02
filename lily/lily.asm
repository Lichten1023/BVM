// Verbose

200 ldi r1 1
201 ldi r2 2
202 cmp r1 r2      // r1 != r2 → FLAGS ≠ 0
203 jne 210        // ジャンプする

204 ldi r0 42      // ← 実行されない
205 print r0

210 ldi r3 123
211 print r3       // 出力: 123
212 halt
