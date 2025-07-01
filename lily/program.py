from core import vm

def Run(Program:str) -> list:
    Program = PreprocessAssembly(Program)
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
    LineIndexList = []  # 行番号を格納するリスト
    for i in range(len(Program)):
        ProcessedProgram = []   # 処理済みプログラムを格納するリスト
    
        LineIndexList.append(int(Program[i][0]))  # 行番号を追加

        if Program[i][1] == "LDI":  # LDI命令を処理
            ProcessedProgram.append(Program[i][1])
            ProcessedProgram.append(int(Program[i][2][1]))
            ProcessedProgram.append(int(Program[i][3]))
        elif Program[i][1] == "ADD" or Program[i][1] == "SUB" or Program[i][1] == "MUL":    # ADD命令を処理
            ProcessedProgram.append(Program[i][1])
            ProcessedProgram.append(int(Program[i][2][1]))
            ProcessedProgram.append(int(Program[i][3][1]))
        elif Program[i][1] == "HALT":   # HALT命令を処理
            ProcessedProgram.append(Program[i][1])
        elif Program[i][1] == "JMP":  # JMP命令を処理
            ProcessedProgram.append(Program[i][1])
            ProcessedProgram.append(int(Program[i][2]))
        elif Program[i][1] == "JE":  # JE命令を処理
            ProcessedProgram.append(Program[i][1])
            ProcessedProgram.append(int(Program[i][2]))
        elif Program[i][1] == "NOP":   # NOP命令を処理
            ProcessedProgram.append(Program[i][1])
        elif Program[i][1] == "CMP":    # CMP命令を処理
            ProcessedProgram.append(Program[i][1])
            ProcessedProgram.append(int(Program[i][2][1]))
            ProcessedProgram.append(int(Program[i][3][1]))
        else:
            print("Invalid program detected")

        Program[i] = tuple(ProcessedProgram)
    
    print(Program)  # 処理済みプログラムを表示
    print(LineIndexList)  # 行番号リストを表示

    PC = 0  # プログラムカウンタを初期化
    VM = vm(verbose=Verbose)  # VMのインスタンスを生成して実行

    while PC < len(Program):  # プログラムカウンタがプログラムの長さより小さい間ループ
        if Program[PC][0] == "JMP":
            PC = LineIndexList.index(int(Program[PC][1]))  # JMP命令の処理
            if Verbose:
                print(f"Jumping to instruction at address {LineIndexList[PC]}.\n")
        if Program[PC][0] == "JE":  # FLAGSがEqual(0)のとき、指定番地にジャンプ
            if VM.RunAssembly(LineIndexList[PC], *Program[PC]):
                PC = LineIndexList.index(int(Program[PC][1]))
                if Verbose:
                    print(f"Jumping to instruction at address {LineIndexList[PC]}.\n")
            else:
                if Verbose:
                    print("FLAGS was not Equal (0), so the jump was not taken.")
                PC += 1

        else:
            VM.RunAssembly(LineIndexList[PC], *Program[PC])
            PC += 1 # プログラムカウンタをインクリメント
    pass

program = """
VERBOSE
// This is a comment

10 LDI R1 3      // R1 にループ回数3をセット（カウンタ）
20 LDI R2 1      // R2 に定数1（減算用）をセット
30 LDI R3 0

// ループ開始
40 CMP R1 R3     // R1 == 0 かを比較
41 JE 90         // もしゼロなら終了

// ここに繰り返したい処理を書く（例：NOP 的な処理）
60 SUB R1 R2     // カウンタを1減らす
70 JMP 40        // 再び条件判定へ

// ループ終了
90 HALT
"""

Run(program)