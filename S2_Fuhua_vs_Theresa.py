import random
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.disable()

if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # TheresaWin 德丽莎赢得次数 FuhuaWin 浮华赢的次数
    Theresalife = 100
    Theresaatk = 19
    Theresadef = 12
    Theresaskill = 1

    Fuhualife = 100
    Fuhuaatk = 17
    Fuhuadef = 15
    Fuhuaskill = 1
    FuhuaInk = 0

    TheresaWin = 0
    FuhuaWin = 0

    for index in range(0, 100000):
        while(Theresalife > 0 and Fuhualife > 0):
            # 德丽莎先手攻击
            # 形之笔墨
            # 在西安踢人
            if Theresaskill % 3 == 0:
                Theresaskill = 1
                # 每次攻击判定一次命中率
                for _ in range(5):
                    if random.randint(1, 100) <= min(25 * FuhuaInk, 100):
                        pass
                    else:
                        Fuhualife = Fuhualife - (16 - Fuhuadef)
            else:
                # 攻击不会低于0
                if random.randint(1, 100) <= min(25 * FuhuaInk, 100):
                    pass
                else:
                    Fuhualife = Fuhualife - \
                                max((Theresaatk - Fuhuadef), 0)

            # 血犹大第一可爱！
            if random.randint(1, 10) <= 3:
                Fuhuadef -= 5
                # 设防御不低于0
                if Fuhuadef <= 0:
                    Fuhuadef = 0
            Theresaskill += 1

            # 浮华后手攻击
            # 形之笔墨
            if Fuhuaskill % 3 == 0:
                Theresalife = Theresalife - 18
                FuhuaInk += 1
                Fuhuaskill = 1
            else:
                Theresalife = Theresalife - Fuhuaatk
            Fuhuaskill += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Fuhualife <= 0:
            TheresaWin = TheresaWin + 1
        else:
            FuhuaWin = FuhuaWin + 1

        # 数值重置
        Theresalife = 100
        Theresaatk = 19
        Theresadef = 12
        Theresaskill = 1

        Fuhualife = 100
        Fuhuaatk = 17
        Fuhuadef = 15
        Fuhuaskill = 1
        FuhuaInk = 0

    # 结果展示
    print("德丽莎赢的概率为%f" % (TheresaWin / (TheresaWin + FuhuaWin)))
    print("一共赢了%d场" % (TheresaWin))

    print("浮华赢的概率为%f" % (FuhuaWin / (TheresaWin + FuhuaWin)))
    print("一共赢了%d场" % (FuhuaWin))

    print("投票德丽莎赔率期望")
    print((TheresaWin / (TheresaWin + FuhuaWin))*3)

    print("投票浮华赔率期望")
    print((FuhuaWin / (TheresaWin + FuhuaWin))*2)
