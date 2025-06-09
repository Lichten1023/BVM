class Memory:
    """Byte-addressable memory."""

    def __init__(self, size: int):
        self.data = bytearray(size)

    def read(self, addr: int) -> int:
        return self.data[addr]

    def write(self, addr: int, value: int) -> None:
        self.data[addr] = value & 0xFF

    def load(self, data: bytes, start: int = 0) -> None:
        self.data[start:start+len(data)] = data
