import random
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.disable()

if __name__ == "__main__":
    # life生命 atk攻击 def防御 GlobalRound全局回合
    # RavensWin 渡鸦赢得次数 HimekoWin 姬子赢的次数
    Ravenslife = 100
    Ravensatk = 23
    Ravensdef = 14
    Ravensspeed = 14
    RavensRate = 1

    Himekolife = 100
    Himekoatk = 23
    Himekodef = 9
    Himekospeed = 12
    HimekoHit = 0

    GlobalRound = 1

    RavensWin = 0
    HimekoWin = 0

    for index in range(0, 100000):
        while(Ravenslife > 0 and Himekolife > 0):
            # 渡鸦先手攻击
            # 不是针对你
            if random.randint(1, 100) <= 25 and Ravensspeed == 14:
                RavensRate = 1.25
                # 加一个约束每场战斗只判定一次
                Ravensspeed = 1127

            # 别墅小岛
            if GlobalRound % 3 == 0:
                Himekolife = Himekolife - \
                            7 * (int(16 * RavensRate) - Himekodef)
            else:
                Himekolife = Himekolife - \
                            (int(Ravensatk * RavensRate) - Himekodef)

            # 姬子后手攻击
            # 干杯，朋友
            if GlobalRound % 2 == 0:
                Himekoatk = Himekoatk * 2
                HimekoHit += 1
            # 命中率下降
            if random.randint(1, 100) <= min(35 * HimekoHit, 100):
                pass
            else:
                Ravenslife = Ravenslife - (Himekoatk - Ravensdef)

            GlobalRound += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Himekolife <= 0:
            RavensWin = RavensWin + 1
        else:
            HimekoWin = HimekoWin + 1

        # 数值重置
        Ravenslife = 100
        Ravensatk = 23
        Ravensdef = 14
        Ravensspeed = 14
        RavensRate = 1

        Himekolife = 100
        Himekoatk = 23
        Himekodef = 9
        Himekospeed = 12
        HimekoHit = 0

        GlobalRound = 1

    # 结果展示
    print("渡鸦赢的概率为%f" % (RavensWin / (RavensWin + HimekoWin)))
    print("一共赢了%d场" % (RavensWin))

    print("姬子赢的概率为%f" % (HimekoWin / (RavensWin + HimekoWin)))
    print("一共赢了%d场" % (HimekoWin))

    # print("投票渡鸦赔率期望")
    # print((RavensWin / (RavensWin + HimekoWin))*2.1)

    # print("投票姬子赔率期望")
    # print((HimekoWin / (RavensWin + HimekoWin))*2.8)
