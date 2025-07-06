class compiler:
    def __init__(self):
        self.AsmProgram = None
        self.BinProgram = None
        self.Version = "lilac alpha"

        self.compiledict = {
            "NOP"   : (0x00, 0),
            "BRK"   : (0x01, 0),
            "JMP"   : (0x02, 4),
            "JSR"   : (0x03, 4),
            "RTS"   : (0x04, 0),
            "JZ"    : (0x05, 4),
            "JNZ"   : (0x06, 4),
            "JC"    : (0x07, 4),
            "JN"    : (0x08, 4),
            "MOV"   : (0x10, 1),
            "LOADimm"   : (0x12, 2),
            "LOADmem"   : (0x12, 3),
            "STORE" : (0x13, 3),
            "LDIX"  : (0x14, 1),
            "STIX"  : (0x15, 1),
            "JC"    : (0x00, 1),
            "JC"    : (0x00, 4),
        }

    def CompileASMFile(self, FilePath):
        try:
            with open(FilePath, "r", encoding="utf-8") as f:
                self.AsmProgram = f.read().replace("\n", "").replace(" ", "")
                print("Assembly file loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{FilePath}' was not found.")

    def CompileBINFile(self, FilePath):
        try:
            with open(FilePath, "r", encoding="utf-8") as f:
                self.BinProgram = f.read()
                print("Binary file loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{FilePath}' was not found.")

    def StartSession(self):
        print(f"Version: {self.Version}")
        print("Compiler session started.")
        print("Select the file type you want to compile.")
        choice = input("1: Assembly File (ASM)\n2: Binary File (BIN)\nEnter your choice (1 or 2): ")
        if choice == "1":
            print("Please enter the file path of the assembly file to compile:")
            asm_file_path = input("ASM File Path: ")
            self.CompileASMFile(asm_file_path)
        elif choice == "2":
            print("Please enter the file path of the binary file to compile:")
            bin_file_path = input("BIN File Path: ")
            self.CompileBINFile(bin_file_path)
        else:
            print("Invalid choice.")

compiler_instance = compiler()
if __name__ == "__main__":
    compiler_instance.StartSession()