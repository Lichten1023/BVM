from cpu import cpu
import sys

class writer:
    def __init__(self, CPUInstance):
        self.CPU = CPUInstance
        self.BinProgram = None

    def Write(self, Address:int, Binary:int):
        Adr1 = (Address >> 8) & 0xFF
        Adr2 = Address & 0xFF
        self.CPU.Memory[Adr1][Adr2] = Binary
        print(f"{Adr1:02X}{Adr2:02X} : {self.CPU.Memory[Adr1][Adr2]:08b}")

    def RunBinFile(self, File):
        with open(File, "r") as p:
            self.BinProgram = p.read().replace("\n", "").replace("\r", "").replace(" ", "")
            self.BinProgram = [self.BinProgram[i:i+8] for i in range(0, len(self.BinProgram), 8)]
            print(self.BinProgram)
            for i in range(len(self.BinProgram)):
                self.Write(i+0x2000, int(self.BinProgram[i], 2))

    def Run(self, Start):
        Return = C.Run(Start)
        if Return == "HALT":
            sys.exit()

if __name__ == "__main__":
    C = cpu()
    W = writer(C)
    W.RunBinFile("lilac\\lilac.bin")
    print(C.GetMemory(0x2000, 0x201F))