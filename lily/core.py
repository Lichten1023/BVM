class vm:   # １行プログラムの実行器として動作。PC等のステート管理は行わない。
    def __init__(self, verbose=False):
        self.memory = [0] * 0x10000  # メインメモリ（64KB）
        self.registers = [0] * 8     # 汎用レジスタ R0〜R7（8本）
        self.verbose = verbose       # 実行中の状態を表示する詳細モードの有効/無効（True/False）
        print(f"Initialized. | Verbose : {self.verbose}")

    def RunAssembly(self, opcode, arg1=None, arg2=None, arg3=None):
        binary = ""
        if self.verbose:
            print(f"Opcode : {opcode}")

        if opcode == "HALT":    # HALT
            binary = "0000"
        if opcode == "ADD":   # ADD
            binary = "0001"
            binary += str(format(arg1, f"0{4}b"))   # レジスタ(代入先)を追加
            binary += str(format(arg2, f"0{4}b"))   # レジスタ(代入元)を追加
        if opcode == "LDI":   # LDI
            binary = "0010"
            binary += str(format(arg1, f"0{4}b"))   # レジスタ(代入先)を追加
            binary += str(format(arg2, f"0{8}b"))   # 即値を追加
        if opcode == "SUB":   # SUB
            binary = "0011"
            binary += str(format(arg1, f"0{4}b"))   # レジスタ(代入先)を追加
            binary += str(format(arg2, f"0{4}b"))   # レジスタ(代入元)を追加
        if opcode == "MUL":   # MUL
            binary = "0100"
            binary += str(format(arg1, f"0{4}b"))   # レジスタ(代入先)を追加
            binary += str(format(arg2, f"0{4}b"))   # レジスタ(代入元)を追加
        
        if len(binary) != 16:   # 命令長を調節
            binary = binary.ljust(16, "0")

        self.RunBinary(binary)

    def RunBinary(self, binary):  #16bitバイナリを入力
        if self.verbose:
            print(binary)
        if len(binary) != 16:   # 不正な命令長を検知
            print("Invalid instruction length.")
            self.halt(101)   # "不正な命令長"

        instruction = binary[0:4]   # 命令を抽出

        if instruction == "0000":   # HALT
            self.halt(0) # "正常終了"
            return
        if instruction == "0001":   # ADD
            ra = int(binary[4:8], 2)
            rb = int(binary[8:12], 2)
            self.add(ra, rb)
            return
        if instruction == "0010":   # LDI
            r = int(binary[4:8], 2)
            imm = int(binary[8:16], 2)
            self.ldi(r, imm)
            return
        if instruction == "0011":   # SUB
            ra = int(binary[4:8], 2)
            rb = int(binary[8:12], 2)
            self.sub(ra, rb)
            return
        if instruction == "0100":   # MUL
            ra = int(binary[4:8], 2)
            rb = int(binary[8:12], 2)
            self.mul(ra, rb)
            return

        else:   # 不正な命令で停止
            self.halt(1) # "不正な命令"
            return

    def GetExitStatus(self, ExitCode):    # エラーコードと対応するメッセージをまとめてreturn
        ErrorDict = {
            -1 : "未定義または不明ステータス, 非正常終了",
            0 : "正常終了",
            1 : "不正な命令",
            101 : "不正な命令長"
        }
        if not(ExitCode in ErrorDict):
            ExitCode = -1

        return f"""Exitcode : {ExitCode} \nStatus : {ErrorDict[ExitCode]}"""

    def halt(self, ExitCode=-1): # HALT : 停止命令
        print(f"Called HALT. \n{self.GetExitStatus(ExitCode)}")
        quit()

    def add(self, r1, r2):
        if self.verbose:
            print(f"Called ADD.\nR{r1} : {self.registers[r1]}, R{r2} : {self.registers[r2]}")
        self.registers[r1] += self.registers[r2]

        if self.verbose:
            print(f"R{r1} : {self.registers[r1]}\n")
        pass

    def sub(self, r1, r2):
        if self.verbose:
            print(f"Called SUB.\nR{r1} : {self.registers[r1]}, R{r2} : {self.registers[r2]}")
        self.registers[r1] -= self.registers[r2]

        if self.verbose:
            print(f"R{r1} : {self.registers[r1]}\n")
        pass

    def mul(self, r1, r2):
        if self.verbose:
            print(f"Called MUL.\nR{r1} : {self.registers[r1]}, R{r2} : {self.registers[r2]}")
        self.registers[r1] *= self.registers[r2]

        if self.verbose:
            print(f"R{r1} : {self.registers[r1]}\n")
        pass

    def ldi(self, r, imm):
        self.registers[r] = int(imm)
        if self.verbose:
            print(f"Called LDI. R{r} set to {imm}.\nR{r} : {self.registers[r]}\n")

if __name__ == "__main__":
    program = [("LDI", 1, 8), ("LDI", 2, 8), ("ADD", 1, 2), ("SUB", 1, 2), ("MUL", 1, 2), ("HALT",)]
    VM = vm(verbose=True)  # VMのインスタンスを生成。verbose=Trueで詳細モードを有効化。
    for i in range(len(program)):
        VM.RunAssembly(*program[i])

###
# - オペコード ; バイナリ ; 引数情報 ; 備考 ;
# - HALT ; 0000 ; 引数なし ; ステータスコードを表示する。対応表は別記。;
# - ADD ; 0001 ; レジスタ番号4bit, レジスタ番号4bit ; 前者のレジスタに後者の値を足し合わせ、前者の値を変化させる.;
# - LDI ; 0010 ; 代入先レジスタ4bit, 即値8bit ; レジスタを即値に設定する。レジスタの持つ値は上書きされる.;
# - SUB ; 0011 ; レジスタ番号4bit, レジスタ番号4bit ; 前者のレジスタから後者の値を引き算し、前者の値を変化させる.;
# ###
