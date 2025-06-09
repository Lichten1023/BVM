# BVM General README

This repository contains a minimal example of a very small virtual machine
(``VM``) implementation along with a demo program and unit tests.

## Running the demo

The ``hello.asm`` demo program prints ``Hello World`` using the VM. You can run
it with ``run_file`` from the ``8001.vm`` module:

```bash
python - <<'EOF'
import importlib, os
vm = importlib.import_module('8001.vm')
program = os.path.join('8001', 'programs', 'hello.asm')
print('Output:', ''.join(vm.run_file(program).output))
EOF
```

## Running the tests

Use ``python -m pytest`` so that the project root is added to ``sys.path``:

```bash
python -m pytest -q
```
