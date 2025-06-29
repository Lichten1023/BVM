from core import vm

def Run(Program:str) -> list:
    Program = PreprocessAssembly(Program)
    print(Program)
    Program = AnalyzeAssemblyMetadata(Program)
    ProcessAssembly(Program, Verbose=Verbose)

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
    global Verbose
    if ("VERBOSE",) in Program:    # Verboseの有効化をチェック
        Verbose = True
        print("Verbose enable.")
        Program.pop(Program.index(("VERBOSE",)))  # VERBOSEを確認して削除
    else:
        Verbose = False
        print("Verbose disable.")

    return Program

def ProcessAssembly(Program:list, Verbose:bool=False) -> None:
    for i in range(len(Program)):
        ProcessedProgram = []   # 処理済みプログラムを格納するリスト
        if Program[i][0] == "LDI":  # LDI命令を処理
            ProcessedProgram.append(Program[i][0])
            ProcessedProgram.append(int(Program[i][1][1]))
            ProcessedProgram.append(int(Program[i][2]))
        elif Program[i][0] == "ADD" or Program[i][0] == "SUB" or Program[i][0] == "MUL":    # ADD命令を処理
            ProcessedProgram.append(Program[i][0])
            ProcessedProgram.append(int(Program[i][1][1]))
            ProcessedProgram.append(int(Program[i][2][1]))
        elif Program[i][0] == "HALT":   # HALT命令を処理
            ProcessedProgram.append(Program[i][0],)
        Program[i] = tuple(ProcessedProgram)

    print(Program)  # 処理済みプログラムを表示

    VM = vm(verbose=Verbose)  # VMのインスタンスを生成して実行
    for i in range(len(Program)):
        VM.RunAssembly(*Program[i])
    pass

program = """
VERBOSE
// This is a comment

LDI R1 2    // Load immediate value 2 into register R1
LDI R2 3    // Load immediate value 3 into register R2
ADD R1 R2   // Add values in R1 and R2
SUB R1 R2   // Subtract values in R1 and R2
HALT       // Stop execution
"""

Run(program)