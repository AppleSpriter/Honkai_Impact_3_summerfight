import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # KianaWin 琪亚娜赢得次数 DurandalWin 幽兰黛尔&屎蛋赢的次数
    Kianalife = 100
    Kianaatk = 24
    Kianadef = 11
    Kianaskill = 1

    Durandallife = 100
    Durandalatk = 19
    Durandaldef = 10
    Durandalskill = 1

    KianaWin = 0
    DurandalWin = 0

    for index in range(0, 1000000):
        while(Kianalife > 0 and Durandallife > 0):
            # 琪亚娜先手攻击
            # 吃我一矛
            if Kianaskill == 2:
                # 反弹！反弹无效！
                if random.randint(1, 100) <= 16:
                    Kianalife = Kianalife - (30 - Kianadef)
                else:
                    Durandallife = Durandallife - \
                                    (Durandaldef + Kianaatk)
                Kianaskill = 1
                # print("吃我一矛")
                # 音浪太强
                if random.randint(1, 100) <= 35:
                    Kianaskill = 0
                    # print("音浪太强")
            # 音浪太强副作用，跳过攻击
            elif Kianaskill == 0:
                Kianaskill = 2
            elif Kianaskill == 1:
                Durandallife = Durandallife - \
                                (Kianaatk - Durandaldef)
                Kianaskill += 1

            # print("幽兰黛尔&屎蛋生命：%d" %(Durandallife))

            # 幽兰黛尔&屎蛋后手攻击
            # 摸鱼的快乐
            Durandalatk += 3
            Kianalife = Kianalife - (Durandalatk - Kianadef)

            # print("琪亚娜生命：%d" %(Kianalife))

        # 判定输赢，速度慢的后手方放前面先判断
        if Durandallife <= 0:
            KianaWin = KianaWin + 1
        else:
            DurandalWin = DurandalWin + 1

        # 数值重置
        Kianalife = 100
        Kianaatk = 24
        Kianadef = 11
        Kianaskill = 1
        Durandallife = 100
        Durandalatk = 19
        Durandaldef = 10
        Durandalskill = 1

    # 结果展示
    print("琪亚娜赢的概率为%f，一共赢了%d场"
          % (KianaWin / (KianaWin + DurandalWin), KianaWin))

    print("幽兰黛尔&屎蛋赢的概率为%f 一共赢了%d场"
          % (DurandalWin / (KianaWin + DurandalWin), DurandalWin))

    print("投票琪亚娜赔率期望")
    print((KianaWin / (KianaWin + DurandalWin))*1.9)

    print("投票幽兰黛尔&屎蛋赔率期望")
    print((DurandalWin / (KianaWin + DurandalWin))*3.2)
