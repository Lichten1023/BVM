class compiler:
    def __init__(self):
        self.AsmProgram = None
        self.BinProgram = None
        self.Version = "lilac alpha"

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