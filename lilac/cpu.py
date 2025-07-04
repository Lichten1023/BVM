class cpu:
    def __init__(self):
        self.Memory = [[0x00 for _ in range(256)] for _ in range(256)]
        self.PC = 0x0000

    def Fetch(self, Address:int):
        Adr1 = (Address >> 8) & 0xFF
        Adr2 = Address & 0xFF
        print(f"Address : {Adr1}, {Adr2}")
        print(f"Memory : {self.Memory[Adr1][Adr2]}")

    def TestMemory(self):
        self.Memory[0x01][0x03] = 0xFF
        print(self.Memory[0x01][0x03], self.Memory[0x01][0x02])

    def Run(self, PC):
        Address = PC + 0x2000
        Adr1 = (Address >> 8) & 0xFF
        Adr2 = Address & 0xFF
        if self.Memory[Adr1][Adr2] == 0x00:
            self.HALT(0)
            self.PC += 1

    def HALT(self, ExitCode):
        print(f"HALT called | Exit code : {ExitCode}")
        return "HALT"

if __name__ == "__main__":
    Instance = cpu()
    # Instance.TestMemory()
    # Instance.Fetch(0x0103)
    Instance.Run(0x0103)