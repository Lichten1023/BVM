class vm:   # １行プログラムの実行器として動作。PC等のステート管理は行わない。
    def __init__(self, verbose=False):
        self.memory = [0] * 0x10000  # メインメモリ（64KB）
        self.registers = [0] * 8     # 汎用レジスタ R0〜R7（8本）
        self.Flags = 0
        self.verbose = verbose       # 実行中の状態を表示する詳細モードの有効/無効（True/False）
        print(f"Initialized. | Verbose : {self.verbose}\n")

    def RunAssembly(self, index, opcode, arg1=None, arg2=None, arg3=None):
        binary = ""
        if self.verbose:
            print(f"Line index : {index}\nOpcode : {opcode}")

        if opcode == "HALT":
            binary = "0000" + "0" * 12  # 引数なし、残りは0で埋める

        elif opcode == "ADD":
            binary = "0001"
            binary += format(arg1, "04b")
            binary += format(arg2, "04b")
            binary += "0" * 4  # 残り4bitパディング

        elif opcode == "LDI":
            binary = "0010"
            binary += format(arg1, "04b")
            binary += format(arg2, "08b")

        elif opcode == "SUB":
            binary = "0011"
            binary += format(arg1, "04b")
            binary += format(arg2, "04b")
            binary += "0" * 4

        elif opcode == "MUL":
            binary = "0100"
            binary += format(arg1, "04b")
            binary += format(arg2, "04b")
            binary += "0" * 4

        elif opcode == "CMP":
            binary = "0101"
            binary += format(arg1, "04b")
            binary += format(arg2, "04b")
            binary += "0" * 4

        elif opcode == "JE":
            binary = "0110" + "0000"  # unused bits
            binary += format(arg1, "08b")

        elif opcode == "JNE":
            binary = "0111" + "0000"
            binary += format(arg1, "08b")

        elif opcode == "JG":
            binary = "1000" + "0000"
            binary += format(arg1, "08b")

        elif opcode == "JL":
            binary = "1001" + "0000"
            binary += format(arg1, "08b")

        elif opcode == "JMP":
            binary = "1010" + "0000"
            binary += format(arg1, "08b")

        elif opcode == "MOV":
            binary = "1011"
            binary += format(arg1, "04b")
            binary += format(arg2, "04b")
            binary += "0" * 4

        elif opcode == "NOP":
            binary = "1100" + "0" * 12

        elif opcode == "PRINT":
            binary = "1101"
            binary += format(arg1, "04b")
            binary += "0" * 8  # 残りは0で埋める
        
        if len(binary) != 16:   # 命令長を調節
            binary = binary.ljust(16, "0")

        r = None
        r = self.RunBinary(binary)
        return r

    def RunBinary(self, binary):  #16bitバイナリを入力
        if self.verbose:
            print(binary)
        if len(binary) != 16:   # 不正な命令長を検知
            print("Invalid instruction length.")
            self.halt(101)   # "不正な命令長"

        instruction = binary[0:4]   # 命令を抽出

        if instruction == "0000":   # HALT
            self.halt(0)  # "正常終了"
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

        if instruction == "0101":   # CMP
            ra = int(binary[4:8], 2)
            rb = int(binary[8:12], 2)
            self.cmp(ra, rb)
            return

        if instruction == "0110":   # JE
            imm = int(binary[8:16], 2)
            return self.je(imm)

        if instruction == "0111":   # JNE
            imm = int(binary[8:16], 2)
            self.jne(imm)
            return

        if instruction == "1000":   # JG
            imm = int(binary[8:16], 2)
            self.jg(imm)
            return

        if instruction == "1001":   # JL
            imm = int(binary[8:16], 2)
            self.jl(imm)
            return

        if instruction == "1010":   # JMP
            imm = int(binary[8:16], 2)
            self.jmp(imm)
            return

        if instruction == "1011":   # MOV
            ra = int(binary[4:8], 2)
            rb = int(binary[8:12], 2)
            self.mov(ra, rb)
            return

        if instruction == "1100":   # NOP
            self.nop()
            return

        if instruction == "1101":   # PRINT
            r = int(binary[4:8], 2)
            self.print_reg(r)
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

        return f"Exitcode : {ExitCode} \nStatus : {ErrorDict[ExitCode]}"

    def halt(self, ExitCode=-1): # HALT : 停止命令
        print(f"\nCalled HALT. \n{self.GetExitStatus(ExitCode)}\n")
        quit()

    def add(self, r1, r2):
        if self.verbose:
            print(f"Called ADD.\nR{r1} : {self.registers[r1]}, R{r2} : {self.registers[r2]}")
        self.registers[r1] += self.registers[r2]

        if self.verbose:
            print(f"R{r1} : {self.registers[r1]}\n")
        pass

    def ldi(self, r, imm):
        self.registers[r] = int(imm)
        if self.verbose:
            print(f"Called LDI. R{r} set to {imm}.\nR{r} : {self.registers[r]}\n")

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

    def cmp(self, r1, r2):
        if self.registers[r1] == self.registers[r2]:
            self.Flags = 0
        elif self.registers[r1] < self.registers[r2]:
            self.Flags = 1
        elif self.registers[r1] > self.registers[r2]:
            self.Flags = 2
        if self.verbose:
            d = {0:"=", 1:"<", 2:">"}
            print(f"R{r1} {d[self.Flags]} R{r2}, so FLAGS became {self.Flags}\n")

    def je(self, addr): # FLAGSがEqual(0)のとき、指定番地にジャンプ
        if self.Flags == 0:
            return True
        else:
            return False
        
    def jne(self, addr):
        pass  # FLAGSがNot Equalのとき、指定番地にジャンプ

    def jg(self, addr):
        pass  # FLAGSがGreaterのとき、指定番地にジャンプ

    def jl(self, addr):
        pass  # FLAGSがLessのとき、指定番地にジャンプ

    def jmp(self, addr):
        pass  # 無条件で指定番地にジャンプ program.pyで処理

    def mov(self, r_dest, r_src):
        pass  # r_dest ← r_src の値をコピー

    def nop(self):
        if self.verbose:
            print(f"Called NOP.\n")
    

    def print_reg(self, r):
        print(f"R{r} : {self.registers[r]}")

    
if __name__ == "__main__":
    program = [("LDI", 1, 8), ("LDI", 2, 8), ("ADD", 1, 2), ("SUB", 1, 2), ("MUL", 1, 2), ("HALT",)]
    VM = vm(verbose=True)  # VMのインスタンスを生成。verbose=Trueで詳細モードを有効化。
    for i in range(len(program)):
        VM.RunAssembly(*program[i])

###
# - オペコード ; バイナリ ; 引数情報 ; 備考 ;
# - HALT ; 0000 ; 引数なし ; ステータスコードを表示する。対応表は別記。;
# - ADD ; 0001 ; レジスタ番号4bit, レジスタ番号4bit ; 前者のレジスタに後者の値を足し合わせ、前者の値を変化させる。;
# - LDI ; 0010 ; 代入先レジスタ4bit, 即値8bit ; レジスタを即値に設定する。レジスタの持つ値は上書きされる。;
# - SUB ; 0011 ; レジスタ番号4bit, レジスタ番号4bit ; 前者のレジスタから後者の値を引き算し、前者の値を変化させる。;
# - MUL ; 0100 ; レジスタ番号4bit, レジスタ番号4bit ; 前者のレジスタに後者の値を掛け算し、前者の値を変化させる。;
# - CMP ; 0101 ; レジスタ番号4bit, レジスタ番号4bit ; 2つのレジスタの値を比較し、FLAGSを設定する（=のとき0, <のとき1, >のとき2）。;
# - JE  ; 0110 ; 即値8bit ; CMPで等しい場合に指定番地へジャンプする。;
# - JNE ; 0111 ; 即値8bit ; CMPで等しくない場合に指定番地へジャンプする。;
# - JG  ; 1000 ; 即値8bit ; CMPで左が右より大きい場合に指定番地へジャンプする。;
# - JL  ; 1001 ; 即値8bit ; CMPで左が右より小さい場合に指定番地へジャンプする。;
# - JMP ; 1010 ; 即値8bit ; 無条件に指定番地へジャンプする。;
# - MOV ; 1011 ; レジスタ番号4bit, レジスタ番号4bit ; レジスタ間で値をコピーする（前者 ← 後者）。;
# - NOP ; 1100 ; 引数なし ; 何もしない命令（パディングやタイミング調整用）。;
# - PRINT ; 1101 ; レジスタ番号4bit ; 指定レジスタの値を標準出力に表示する（デバッグ用）。;
###
