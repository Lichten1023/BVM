import re
from typing import List

class VM:
    def __init__(self, memory_size: int = 256):
        self.registers = [0] * 8
        self.memory = [0] * memory_size
        self.pc = 0
        self.program = []
        self.output = []
        self.halted = False

    def load_program(self, lines: List[str]):
        self.program = []
        for line in lines:
            line = line.split(';')[0].strip()
            if not line:
                continue
            parts = re.split(r'\s+', line)
            op = parts[0].upper()
            args = [arg.strip(',') for arg in parts[1:]]
            self.program.append((op, args))

    def _reg_index(self, token: str) -> int:
        token = token.upper()
        if not token.startswith('R'):
            raise ValueError(f"Invalid register {token}")
        return int(token[1:])

    def step(self):
        if self.pc >= len(self.program):
            self.halted = True
            return
        op, args = self.program[self.pc]
        self.pc += 1
        if op == 'LDI':
            reg = self._reg_index(args[0])
            value = int(args[1])
            self.registers[reg] = value
        elif op == 'STR':
            reg = self._reg_index(args[0])
            addr = int(args[1])
            self.memory[addr] = self.registers[reg]
        elif op == 'PRN':
            reg = self._reg_index(args[0])
            self.output.append(chr(self.registers[reg]))
        elif op == 'HLT':
            self.halted = True
        else:
            raise ValueError(f'Unknown opcode {op}')

    def run(self):
        while not self.halted:
            self.step()

def run_file(path: str) -> VM:
    with open(path) as f:
        lines = f.readlines()
    vm = VM()
    vm.load_program(lines)
    vm.run()
    return vm
