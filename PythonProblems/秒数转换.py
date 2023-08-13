'''
要求
1) 输入一行，一个整数，表示总秒数
2) 输出一行，表示小时、分钟、秒，每两个数之间用一个空格隔开
'''

print("----------|程序开始运行|----------")

while True:
    ent = input("请输入一个整数(按回车退出程序): ")

    if ent == "":
        break
    elif int(ent) != float(ent):
        print("##########|您未输入一个整数|##########")
    elif int(ent) == float(ent):
        ent = int(ent)
        seco = ent % 60
        hour = int( ( ent - seco ) / 3600 )
        minu = ( ent - hour * 3600 - seco ) / 60
        print( "%d时%d分%d秒" % ( hour, minu, seco ) )

print("----------|程序运行结束|----------")