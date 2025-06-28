def RunAssembly(Program:str) -> list:
    Program = PreprocessAssembly(Program)
    AnalyzeAssemblyMetadata(Program)
    

def PreprocessAssembly(Program):
    Program = Program.split("\n")   # プログラムをリスト化
    print(Program)
    i = 0
    while i != len(Program):    # プログラムを整形
        if Program[i] == "":
            Program.pop(i)
            print(Program)
        else:
            i += 1

def AnalyzeAssemblyMetadata(Program:list):
    if ("VERBOSE" in Program):
        Verbose = True
        print("Verbose enable")

program = """
VERBOSE

LDI R1 2
LDI R2 3
ADD R1 R2
HALT
"""

RunAssembly(program)