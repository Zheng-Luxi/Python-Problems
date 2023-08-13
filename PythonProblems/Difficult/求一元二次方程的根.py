"""
题目背景
利用公式x1 = (-b + sqrt(bb-4ac))/(2a), x2 = (-b - sqrt(bb-4ac))/(2a)求一元二次方程ax2+ bx + c =0的根，其中a不等于0。

输入输出格式
输入格式

输入一行，包含三个浮点数a, b, c（它们之间以一个空格分开），分别表示方程ax2 + bx + c =0的系数。

输出格式

输出一行，表示方程的解。
若b2 = 4 * a * c,则两个实根相等，则输出形式为：x1=x2=...。
若b2 > 4 * a * c,则两个实根不等，则输出形式为：x1=...;x2 = ...，其中x1>x2。
若b2 < 4 * a * c，则有两个虚根，则输出：x1=实部+虚部i; x2=实部-虚部i，即x1的虚部系数大于等于x2的虚部系数，实部为0时不可省略。实部 = -b / (2a), 虚部 = sqrt(4ac-bb) / (2*a)

所有实数部分要求精确到小数点后5位，数字、符号之间没有空格。
"""

class EquationSolver:
    def __init__( self, info ):
        self.a = float( info[0] )
        self.b = float( info[1] )
        self.c = float( info[2] )
        self.Delta = self.b * self.b - 4 * self.a * self.c
        x1, x2 = self.solve( self.judgeSolution() )
        self.printSolution( x1, x2 )
    
    def judgeSolution( self ):
        if self.Delta > 0:
            return 2
        elif self.Delta == 0:
            return 1
        else:
            return 0

    def solve( self, judgeBool ):
        if judgeBool - 1:
            x1 = format( ( -self.b + self.Delta ** 0.5 ) / ( 2 * self.a ), ".5f" )
            x2 = format( ( -self.b - self.Delta ** 0.5 ) / ( 2 * self.a ), ".5f" )
        elif judgeBool:
            x1 = x2 = format( -self.b / ( 2 * self.a ), ".5f" )
        else:
            x1 = format( -self.b / ( 2 * self.a ), ".2f" ) + "+" + format( ( -self.Delta ) ** 0.5 / ( 2 * self.a ), ".5f" ) + "i"
            x2 = format( -self.b / ( 2 * self.a ), ".2f" ) + "-" + format( ( -self.Delta ) ** 0.5 / ( 2 * self.a ), ".5f" ) + "i"
        return x1, x2

    def printSolution( self, x1, x2 ):
        print( "该一元二次方程的解为: x1=%s, x2=%s" % ( x1, x2 ) )


solver = EquationSolver( input("请输入信息: ").split(" ") )