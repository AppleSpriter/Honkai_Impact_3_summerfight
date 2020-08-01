import random
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.disable()

if __name__ == "__main__":
    # life生命 atk攻击 def防御 GlobalRound全局回合
    # MeiWin 芽衣赢得次数 RavensWin 渡鸦赢的次数
    Meilife = 100
    Meiatk = 22
    Meidef = 12
    Meispeed = 30
    MeiParalysis = 0

    Ravenslife = 100
    Ravensatk = 23
    Ravensdef = 14
    Ravensspeed = 14
    RavensRate = 1

    GlobalRound = 1

    MeiWin = 0
    RavensWin = 0

    for index in range(0, 100000):
        while(Meilife > 0 and Ravenslife > 0):
            # 不是针对你
            if random.randint(1, 100) <= 25 and Ravensspeed == 14:
                RavensRate = 1.25
                # 加一个约束每场战斗只判定一次
                Ravensspeed = 1127

            # 芽衣先手攻击
            # 雷电家的龙女仆
            if GlobalRound % 2 == 0:
                Ravenslife = Ravenslife - 5 * 3
            else:
                Ravenslife = Ravenslife - (Meiatk - Ravensdef)
            # 崩坏世界的歌姬
            if random.randint(1, 10) <= 3:
                MeiParalysis = 1

            # 渡鸦后手攻击
            # 判定芽衣麻痹
            if MeiParalysis == 1:
                MeiParalysis = 0
            else:
                # 别墅小岛
                if GlobalRound % 3 == 0:
                    Meilife = Meilife - 7 * (int(16 * RavensRate) - Meidef)
                else:
                    Meilife = Meilife - (int(Ravensatk * RavensRate) - Meidef)

            GlobalRound += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Ravenslife <= 0:
            MeiWin = MeiWin + 1
        else:
            RavensWin = RavensWin + 1

        # 数值重置
        Meilife = 100
        Meiatk = 22
        Meidef = 12
        Meispeed = 30
        MeiParalysis = 0

        Ravenslife = 100
        Ravensatk = 23
        Ravensdef = 14
        Ravensspeed = 14
        RavensRate = 1

        GlobalRound = 1

    # 结果展示
    print("芽衣赢的概率为%f" % (MeiWin / (MeiWin + RavensWin)))
    print("一共赢了%d场" % (MeiWin))

    print("渡鸦赢的概率为%f" % (RavensWin / (MeiWin + RavensWin)))
    print("一共赢了%d场" % (RavensWin))

    # print("投票芽衣赔率期望")
    # print((MeiWin / (MeiWin + RavensWin))*2.1)

    # print("投票渡鸦赔率期望")
    # print((RavensWin / (MeiWin + RavensWin))*2.8)
