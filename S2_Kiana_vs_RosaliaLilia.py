import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # KianaWin 琪亚娜赢得次数 RosaliaLiliaWin 罗莎莉亚&莉莉娅赢的次数
    Kianalife = 100
    Kianaatk = 24
    Kianadef = 11
    Kianaskill = 1

    RosaliaLilialife = 100
    RosaliaLiliaatk = 18
    RosaliaLiliadef = 10
    RosaliaLiliaskill = 1

    KianaWin = 0
    RosaliaLiliaWin = 0

    for index in range(0, 1000000):
        while(Kianalife > 0 and RosaliaLilialife > 0):
            # 琪亚娜先手攻击
            # 吃我一矛
            if Kianaskill == 2:
                RosaliaLilialife = RosaliaLilialife - \
                                (RosaliaLiliadef + Kianaatk)
                Kianaskill = 1
            #     print("吃我一矛")
                # 音浪太强
                if random.randint(1, 100) <= 35:
                    Kianaskill = 0
            #         print("音浪太强")
            # 音浪太强副作用，跳过攻击
            elif Kianaskill == 0:
                Kianaskill = 2
            elif Kianaskill == 1:
                RosaliaLilialife = RosaliaLilialife - \
                                (Kianaatk - RosaliaLiliadef)
                Kianaskill += 1

            # print("萝莉姐妹生命：%d" %(RosaliaLilialife))

            # 罗莎莉亚&莉莉娅后手攻击
            # 96度生命之水
            if RosaliaLilialife <= 0 and RosaliaLiliaskill == 1:
                RosaliaLilialife = 20
                RosaliaLiliaskill = 0
                # 变成星星吧！
                if random.randint(1, 2) == 1:
                    Kianalife = Kianalife - (233 - Kianadef)
            #         print("变成星星吧！！！！！")
                else:
                    Kianalife = Kianalife - (50 - Kianadef)
            #         print("变成星星吧！")

            else:
                Kianalife = Kianalife - (RosaliaLiliaatk - Kianadef)

            # print("琪亚娜生命：%d" %(Kianalife))

        # 判定输赢，速度慢的后手方放前面先判断
        if RosaliaLilialife <= 0:
            KianaWin = KianaWin + 1
        else:
            RosaliaLiliaWin = RosaliaLiliaWin + 1

        # 数值重置
        Kianalife = 100
        Kianaatk = 24
        Kianadef = 11
        Kianaskill = 1
        RosaliaLilialife = 100
        RosaliaLiliaatk = 18
        RosaliaLiliadef = 10
        RosaliaLiliaskill = 1

    # 结果展示
    print("琪亚娜赢的概率为%f，一共赢了%d场"
          % (KianaWin / (KianaWin + RosaliaLiliaWin), KianaWin))

    print("罗莎莉亚&莉莉娅赢的概率为%f 一共赢了%d场"
          % (RosaliaLiliaWin / (KianaWin + RosaliaLiliaWin), RosaliaLiliaWin))

    print("投票琪亚娜赔率期望")
    print((KianaWin / (KianaWin + RosaliaLiliaWin))*2.4)

    print("投票罗莎莉亚&莉莉娅赔率期望")
    print((RosaliaLiliaWin / (KianaWin + RosaliaLiliaWin))*2.4)
