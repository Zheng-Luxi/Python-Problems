print("----------|程序运行开始|----------")

rows = int(input("请输入行数: ")) # 用户输入行数
cols = 2 * rows - 1 # 计算列数

if int( rows ) != rows: # 判断行数是否为整数
    print("##########|要保证列数是奇数哦|##########")
else:
    for i in range( 1, rows + 1, 1 ): # 开始循环
        print( int( ( cols + 1 ) / 2 - i ) * " ", ( 2 * i - 1 ) * "*", end='\n') # 输出 *

print("----------|程序运行结束|----------")