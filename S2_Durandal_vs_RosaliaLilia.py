import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # DurandalWin 幽兰黛尔&屎蛋赢得次数 RosaliaLiliaWin 罗莎莉亚&莉莉娅赢的次数
    Durandallife = 100
    Durandalatk = 19
    Durandaldef = 10
    Durandalskill = 1

    RosaliaLilialife = 100
    RosaliaLiliaatk = 18
    RosaliaLiliadef = 10
    RosaliaLiliaskill = 1

    DurandalWin = 0
    RosaliaLiliaWin = 0

    for index in range(0, 1000000):
        while(Durandallife > 0 and RosaliaLilialife > 0):
            # 幽兰黛尔&屎蛋先手攻击
            # 摸鱼的快乐
            Durandalatk += 3
            RosaliaLilialife = RosaliaLilialife - \
                (Durandalatk - RosaliaLiliadef)

            # print("萝莉姐妹生命：%d" %(RosaliaLilialife))

            # 罗莎莉亚&莉莉娅后手攻击
            # 96度生命之水
            if RosaliaLilialife <= 0 and RosaliaLiliaskill == 1:
                RosaliaLilialife = 20
                RosaliaLiliaskill = 0
                # 反弹！反弹无效！
                if random.randint(1, 100) <= 16:
                    RosaliaLilialife = RosaliaLilialife - \
                        (30 - RosaliaLiliadef)
                else:
                    # 变成星星吧！
                    if random.randint(1, 2) == 1:
                        Durandallife = Durandallife - (233 - Durandaldef)
                        # print("变成星星吧！！！！！")
                    else:
                        Durandallife = Durandallife - (50 - Durandaldef)
                        # print("变成星星吧！")

            else:
                Durandallife = Durandallife - (RosaliaLiliaatk - Durandaldef)

            # print("幽兰黛尔&屎蛋生命：%d" %(Durandallife))

        # 判定输赢，速度慢的后手方放前面先判断
        if RosaliaLilialife <= 0:
            DurandalWin = DurandalWin + 1
        else:
            RosaliaLiliaWin = RosaliaLiliaWin + 1

        # 数值重置
        Durandallife = 100
        Durandalatk = 19
        Durandaldef = 10
        Durandalskill = 1
        RosaliaLilialife = 100
        RosaliaLiliaatk = 18
        RosaliaLiliadef = 10
        RosaliaLiliaskill = 1

    # 结果展示
    print("幽兰黛尔&屎蛋赢的概率为%f，一共赢了%d场"
          % (DurandalWin / (DurandalWin + RosaliaLiliaWin), DurandalWin))

    print("罗莎莉亚&莉莉娅赢的概率为%f 一共赢了%d场"
          % (RosaliaLiliaWin / (DurandalWin + RosaliaLiliaWin),
             RosaliaLiliaWin))

    print("投票幽兰黛尔&屎蛋赔率期望")
    print((DurandalWin / (DurandalWin + RosaliaLiliaWin))*2.1)

    print("投票罗莎莉亚&莉莉娅赔率期望")
    print((RosaliaLiliaWin / (DurandalWin + RosaliaLiliaWin))*2.8)
