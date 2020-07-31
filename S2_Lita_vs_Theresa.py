import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # TheresaWin 德丽莎赢得次数 LitaWin 丽塔赢的次数
    Theresalife = 100
    Theresaatk = 19
    Theresadef = 12
    Theresaskill = 1
    TheresaatkRate = 1

    Litalife = 100
    Litaatk = 26
    Litadef = 11
    Litaskill = 1
    LitaLoving = 0

    TheresaWin = 0
    LitaWin = 0

    for index in range(0, 100000):
        while(Theresalife > 0 and Litalife > 0):
            # 德丽莎先手攻击
            # 完美心意判定
            if LitaLoving != 0:
                LitaLoving -= 1
                # 永久修改本场攻击倍率
                TheresaatkRate = 0.4
                Litalife = Litalife - max((Theresaatk *
                                          TheresaatkRate - Litadef), 0)
            else:
                # 在西安踢人
                if Theresaskill % 3 == 0:
                    Theresaskill = 1
                    Litalife = Litalife - 5 * (16 - Litadef)
                else:
                    # 攻击不会低于0
                    Litalife = Litalife - max((Theresaatk *
                                              TheresaatkRate - Litadef), 0)
                    # print("丽塔生命：%d" %(Litalife))
            Theresaskill += 1

            # 血犹大第一可爱！
            if random.randint(1, 10) <= 3:
                Litadef -= 5
                # 设防御不低于0
                if Litadef <= 0:
                    Litadef = 0

            # 丽塔后手攻击
            # 女仆的温柔清理
            if random.randint(1, 100) <= 35:
                Theresalife = Theresalife - (Litaatk - Theresadef - 3)
                Theresaatk -= 4
                # 攻击力不低于0
                if Theresaatk <= 0:
                    Theresaatk = 0
            else:
                Theresalife = Theresalife - (Litaatk - Theresadef)

            # 完美心意
            if Litaskill == 4:
                Theresalife = Theresalife + 4
                # 血量上限
                if Theresalife > 100:
                    Theresalife = 100
                # 重置技能
                Litaskill = 1
                # 添加魅惑状态
                LitaLoving = 2
            Litaskill += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if Litalife <= 0:
            TheresaWin = TheresaWin + 1
        else:
            LitaWin = LitaWin + 1

        # 数值重置
        Theresalife = 100
        Theresaatk = 19
        Theresadef = 12
        Theresaskill = 1
        TheresaatkRate = 1

        Litalife = 100
        Litaatk = 26
        Litadef = 11
        Litaskill = 1
        LitaLoving = 0

    # 结果展示
    print("德丽莎赢的概率为%f" % (TheresaWin / (TheresaWin + LitaWin)))
    print("一共赢了%d场" % (TheresaWin))

    print("丽塔赢的概率为%f" % (LitaWin / (TheresaWin + LitaWin)))
    print("一共赢了%d场" % (LitaWin))

    print("投票德丽莎赔率期望")
    print((TheresaWin / (TheresaWin + LitaWin))*1.9)

    print("投票丽塔赔率期望")
    print((LitaWin / (TheresaWin + LitaWin))*3.2)
