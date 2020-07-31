import random
import logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.disable()

if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # LitaWin 丽塔赢得次数 FuhuaWin 浮华赢的次数
    Litalife = 100
    Litaatk = 26
    Litadef = 11
    Litaskill = 1
    LitaLoving = 0

    Fuhualife = 100
    Fuhuaatk = 17
    Fuhuadef = 15
    Fuhuaskill = 1
    FuhuaInk = 0
    FuhuaatkRate = 1

    LitaWin = 0
    FuhuaWin = 0

    for index in range(0, 100000):
        while(Litalife > 0 and Fuhualife > 0):
            # 丽塔先手攻击
            # 形之笔墨
            if random.randint(1, 100) <= min(25 * FuhuaInk, 100):
                logging.debug("浮华形之笔墨生效，丽塔攻击未命中")
            else:
                # 女仆的温柔清理
                if random.randint(1, 100) <= 35:
                    Fuhualife = Fuhualife - (Litaatk - Fuhuadef - 3)
                    logging.debug("浮华生命为%d" % (Fuhualife))
                    Fuhuaatk -= 4
                    # 攻击力不低于0
                    if Fuhuaatk <= 0:
                        Fuhuaatk = 0
                    logging.debug("女仆的温柔清理，浮华攻击为%d" % (Fuhuaatk))
                else:
                    Fuhualife = Fuhualife - (Litaatk - Fuhuadef)
                    logging.debug("浮华生命为%d" % (Fuhualife))

                # 完美心意
                if Litaskill % 4 == 0:
                    Fuhualife = Fuhualife + 4
                    # 血量上限
                    if Fuhualife > 100:
                        Fuhualife = 100
                    # 重置技能
                    Litaskill = 1
                    # 添加魅惑状态
                    LitaLoving = 2
                    logging.debug("发动完美心意")

            Litaskill += 1

            # 浮华后手攻击
            # 完美心意判定
            if LitaLoving != 0:
                LitaLoving -= 1
                # 永久修改本场攻击倍率
                FuhuaatkRate = 0.4
                Litalife = Litalife - int(Fuhuaatk * FuhuaatkRate)
                logging.debug("完美心意效果，浮华无法使用技能")
                logging.debug("丽塔生命为%d" % (Litalife))
            else:
                # 形之笔墨
                if Fuhuaskill % 3 == 0:
                    Litalife = Litalife - 18
                    FuhuaInk += 1
                    Fuhuaskill = 1
                    logging.debug("形之笔墨生效，丽塔生命为%d" % (Litalife))
                else:
                    Litalife = Litalife - Fuhuaatk * FuhuaatkRate
                    logging.debug("丽塔生命为%d" % (Litalife))

            Fuhuaskill += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Fuhualife <= 0:
            LitaWin = LitaWin + 1
        else:
            FuhuaWin = FuhuaWin + 1

        # 数值重置
        Litalife = 100
        Litaatk = 26
        Litadef = 11
        Litaskill = 1
        LitaLoving = 0

        Fuhualife = 100
        Fuhuaatk = 17
        Fuhuadef = 15
        Fuhuaskill = 1
        FuhuaInk = 0
        FuhuaatkRate = 1

    # 结果展示
    print("丽塔赢的概率为%f" % (LitaWin / (LitaWin + FuhuaWin)))
    print("一共赢了%d场" % (LitaWin))

    print("浮华赢的概率为%f" % (FuhuaWin / (LitaWin + FuhuaWin)))
    print("一共赢了%d场" % (FuhuaWin))

    # print("投票丽塔赔率期望")
    # print((LitaWin / (LitaWin + FuhuaWin))*2.1)

    # print("投票浮华赔率期望")
    # print((FuhuaWin / (LitaWin + FuhuaWin))*2.8)
