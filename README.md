# BVM General README (Japanese)

BVMはシンプルな仮想マシン (VM) の最小実装と、デモプログラム、ユニットテ
ストを収めたリポジトリです。

## デモの実行

``hello.asm`` デモプログラムは VM を使って ``Hello World`` を表示します。
``8001.vm`` モジュールの ``run_file`` を利用して実行できます。

```bash
python - <<'EOF'
import importlib, os
vm = importlib.import_module('8001.vm')
program = os.path.join('8001', 'programs', 'hello.asm')
print('Output:', ''.join(vm.run_file(program).output))
EOF
```

## サンプルプログラム

```
VERBOSE

LDI R1 2
LDI R2 3
ADD R1 R2
SUB R1 R2
HALT
```
簡単な足し算と引き算を実行するプログラムです。
