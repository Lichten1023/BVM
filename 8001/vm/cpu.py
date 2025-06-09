from __future__ import annotations

from lib.memory import Memory
from lib.register import Register
from lib.instruction import Instruction


class CPU:
    """Very small CPU implementing a fetch-decode-execute loop."""

    def __init__(self, memory_size: int = 256):
        self.memory = Memory(memory_size)
        self.registers = {
            "PC": Register(16),  # program counter
            "ACC": Register(8),  # accumulator
        }
        self.running = False

    # Instruction set opcodes
    NOP = 0x00
    LOAD_IMM = 0x01
    HALT = 0xFF

    def load_program(self, data: bytes, start: int = 0) -> None:
        self.memory.load(data, start)
        self.registers["PC"].write(start)

    def fetch(self) -> int:
        pc = self.registers["PC"].read()
        opcode = self.memory.read(pc)
        self.registers["PC"].write(pc + 1)
        return opcode

    def decode(self, opcode: int) -> Instruction:
        if opcode == self.LOAD_IMM:
            pc = self.registers["PC"].read()
            value = self.memory.read(pc)
            self.registers["PC"].write(pc + 1)
            return Instruction(opcode, [value])
        return Instruction(opcode, [])

    def execute(self, instr: Instruction) -> None:
        if instr.opcode == self.NOP:
            pass
        elif instr.opcode == self.LOAD_IMM:
            self.registers["ACC"].write(instr.operands[0])
        elif instr.opcode == self.HALT:
            self.running = False
        else:
            raise ValueError(f"Unknown opcode {instr.opcode:#x}")

    def run(self) -> None:
        self.running = True
        while self.running:
            opcode = self.fetch()
            instr = self.decode(opcode)
            self.execute(instr)
