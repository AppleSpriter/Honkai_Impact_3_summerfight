import random
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.disable()

if __name__ == "__main__":
    # life生命 atk攻击 def防御 GlobalRound全局回合
    # MeiWin 芽衣赢得次数 HimekoWin 姬子赢的次数
    Meilife = 100
    Meiatk = 22
    Meidef = 12
    Meispeed = 30
    MeiParalysis = 0

    Himekolife = 100
    Himekoatk = 23
    Himekodef = 9
    Himekospeed = 12
    HimekoHit = 0

    GlobalRound = 1

    MeiWin = 0
    HimekoWin = 0

    for index in range(0, 100000):
        while(Meilife > 0 and Himekolife > 0):
            # 芽衣先手攻击
            # 雷电家的龙女仆
            if GlobalRound % 2 == 0:
                Himekolife = Himekolife - 5 * 3
            else:
                Himekolife = Himekolife - (Meiatk - Himekodef)
            # 崩坏世界的歌姬
            if random.randint(1, 10) <= 3:
                MeiParalysis = 1

            # 姬子后手攻击
            # 判定芽衣麻痹
            if MeiParalysis == 1:
                MeiParalysis = 0
            else:
                # 干杯，朋友
                if GlobalRound % 2 == 0:
                    Himekoatk = Himekoatk * 2
                    HimekoHit += 1
                # 命中率下降
                if random.randint(1, 100) <= min(35 * HimekoHit, 100):
                    pass
                else:
                    Meilife = Meilife - (Himekoatk - Meidef)

            GlobalRound += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Himekolife <= 0:
            MeiWin = MeiWin + 1
        else:
            HimekoWin = HimekoWin + 1

        # 数值重置
        Meilife = 100
        Meiatk = 22
        Meidef = 12
        Meispeed = 30
        MeiParalysis = 0

        Himekolife = 100
        Himekoatk = 23
        Himekodef = 9
        Himekospeed = 12
        HimekoHit = 0

        GlobalRound = 1

    # 结果展示
    print("芽衣赢的概率为%f" % (MeiWin / (MeiWin + HimekoWin)))
    print("一共赢了%d场" % (MeiWin))

    print("姬子赢的概率为%f" % (HimekoWin / (MeiWin + HimekoWin)))
    print("一共赢了%d场" % (HimekoWin))

    # print("投票芽衣赔率期望")
    # print((MeiWin / (MeiWin + HimekoWin))*2.1)

    # print("投票姬子赔率期望")
    # print((HimekoWin / (MeiWin + HimekoWin))*2.8)
