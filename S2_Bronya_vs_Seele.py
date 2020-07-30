import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # BronyaWin 布洛妮娅赢得次数 SeeleWin 希儿赢的次数
    Bronyalife = 100
    Bronyaatk = 21
    Bronyadef = 10
    Bronyaskill = 1

    Seelelife = 100
    Seeleatk = 23
    Seeledef = 13
    Seeleskill = 1

    BronyaWin = 0
    SeeleWin = 0

    for index in range(0, 1000000):
        while(Bronyalife > 0 and Seelelife > 0):
            # 希儿先手攻击，先变黑希0再变白希1
            # 拜托了另一个我
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
            Bronyalife = Bronyalife - (Seeleatk - Bronyadef)

            # 布洛妮娅后手攻击
            # 摩托bikeだ！
            if Bronyaskill == 3:
                Seelelife = Seelelife - random.randint(1, 100)
                Bronyaskill = 1
            else:
                Bronyaskill += 1
                # 天使重构
                if random.randint(1, 100) <= 25:
                    Seelelife = Seelelife - \
                                        4 * (12 - Seeledef)
                else:
                    Seelelife = Seelelife - \
                                        (Bronyaatk - Seeledef)

        # 判定输赢，速度慢的后手方放前面先判断
        if Bronyalife <= 0:
            SeeleWin = SeeleWin + 1
        else:
            BronyaWin = BronyaWin + 1

        # 数值重置
        Bronyalife = 100
        Bronyaatk = 21
        Bronyadef = 10
        Bronyaskill = 1
        Seelelife = 100
        Seeleatk = 23
        Seeledef = 13
        Seeleskill = 1

    # 结果展示
    print("布洛妮娅赢的概率为%f，一共赢了%d场"
          % (BronyaWin / (BronyaWin + SeeleWin), BronyaWin))

    print("希儿赢的概率为%f 一共赢了%d场"
          % (SeeleWin / (BronyaWin + SeeleWin), SeeleWin))

    print("投票布洛妮娅赔率期望")
    print((BronyaWin / (BronyaWin + SeeleWin))*3.2)

    print("投票希儿赔率期望")
    print((SeeleWin / (BronyaWin + SeeleWin))*1.9)
