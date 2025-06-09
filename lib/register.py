class Register:
    """Simple register holding an integer value."""

    def __init__(self, width: int = 8):
        self.width = width
        self.mask = (1 << width) - 1
        self.value = 0

    def read(self) -> int:
        return self.value

    def write(self, value: int) -> None:
        self.value = value & self.mask

    def __repr__(self) -> str:
        return f"Register({self.value:#0{self.width // 4 + 2}x})"
