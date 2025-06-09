from dataclasses import dataclass

@dataclass
class Instruction:
    opcode: int
    operands: list[int]

    @classmethod
    def from_bytes(cls, data: list[int]) -> "Instruction":
        if not data:
            raise ValueError("No data to decode")
        opcode = data[0]
        operands = data[1:]
        return cls(opcode, operands)
