def RunAssembly(Program:str) -> list:
    Program = PreprocessAssembly(Program)
    print(Program)
    AnalyzeAssemblyMetadata(Program)
    
def PreprocessAssembly(Program):
    Program = Program.split("\n")   # プログラムをリスト化
    i = 0   # カウンタをセット
    while i != len(Program):    # プログラムを整形
        if Program[i] == "":    # 空行を削除
            Program.pop(i)
        else:
            i += 1
    i = 0   # カウンタをリセット
    while i != len(Program):    # プログラムをタプル化
        Program[i] = tuple(Program[i].split())
        if "//" in Program[i]:  # コメントを削除
            Program[i] = Program[i][:Program[i].index("//")]
        i += 1
    i = 0   # カウンタをリセット
    while i != len(Program):    # プログラムを整形
        if Program[i] == ():    # 空行を削除 : コメントのみの行は空のタプルになっている
            Program.pop(i)
        else:
            i += 1
        
    return Program

def AnalyzeAssemblyMetadata(Program:list):  # メタデータの解析
    if ("VERBOSE",) in Program:    # Verboseの有効化をチェック
        Verbose = True
        print("Verbose enable")

def ProcessAssembly(Program:list):
        
    pass

program = """
VERBOSE
// This is a comment

LDI R1 2    // Load immediate value 2 into register R1 // This is a comment
LDI R2 3    // Load immediate value 3 into register R2
ADD R1 R2   // Add values in R1 and R2
HALT       // Stop execution
"""

RunAssembly(program)