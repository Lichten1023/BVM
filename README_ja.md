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

## テストの実行

プロジェクトルートを ``sys.path`` に追加するため、 ``python -m pytest`` を
使用してください。

```bash
python -m pytest -q
```
