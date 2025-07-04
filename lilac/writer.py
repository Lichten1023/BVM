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
        print(self.CPU.Memory[Adr1][Adr2])

    def RunBinFile(self, File):
        with open(File, "r") as p:
            self.BinProgram = 

    def Run(self, Start):
        Return = C.Run(Start)
        if Return == "HALT":
            sys.exit()

if __name__ == "__main__":
    C = cpu()
    W = writer(C)
    W.Write(0x0102, 32)
    W.Run(0)