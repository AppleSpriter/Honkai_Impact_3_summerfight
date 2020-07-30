import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数 SakuraKallenWin 八重樱&卡莲赢得次数 SeeleWin 希儿赢的次数
    SakuraKallenlife = 100
    SakuraKallenatk = 20
    SakuraKallendef = 9
    SakuraKallenskill = 1

    Seelelife = 100
    Seeleatk = 23
    Seeledef = 13
    Seeleskill = 1

    SakuraKallenWin = 0
    SeeleWin = 0

    for index in range(0, 1000000):
        while(SakuraKallenlife > 0 and Seelelife > 0):
            # 希儿先手攻击，先变黑希0再变白希1
            if Seeleskill == 1:
                Seeleatk += 10
                Seeledef -= 5
                Seeleskill = 0
            else:
                Seeleatk -= 10
                Seeledef += 5
                Seelelife += random.randint(1, 15)
                Seeleskill = 1

            # 攻击判定
            SakuraKallenlife = SakuraKallenlife - (Seeleatk - SakuraKallendef)

            # 八重樱&卡莲后手攻击
            if random.randint(1, 100) <= 30:
                SakuraKallenlife += 25

            if SakuraKallenskill == 2:
                Seelelife = Seelelife - 25
                SakuraKallenskill = 1
            else:
                Seelelife = Seelelife - (SakuraKallenatk - Seeledef)
                SakuraKallenskill += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if SakuraKallenlife <= 0:
            SeeleWin = SeeleWin + 1
        else:
            SakuraKallenWin = SakuraKallenWin + 1

        # 数值重置
        SakuraKallenlife = 100
        SakuraKallenatk = 20
        SakuraKallendef = 9
        SakuraKallenskill = 1
        Seelelife = 100
        Seeleatk = 23
        Seeledef = 13
        Seeleskill = 1

    # 结果展示
    print("八重樱&卡莲赢的概率为%f，一共赢了%d场"
          % (SakuraKallenWin / (SakuraKallenWin + SeeleWin), SakuraKallenWin))

    print("希儿赢的概率为%f 一共赢了%d场"
          % (SeeleWin / (SakuraKallenWin + SeeleWin), SeeleWin))

    print("投票八重樱&卡莲赔率期望")
    print((SakuraKallenWin / (SakuraKallenWin + SeeleWin))*2.5)

    print("投票希儿赔率期望")
    print((SeeleWin / (SakuraKallenWin + SeeleWin))*2.3)
