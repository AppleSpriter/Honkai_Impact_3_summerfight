import random
if __name__ == "__main__":
    # life生命 atk攻击 def防御 skill技能计数
    # SakuraKallenWin 八重樱&卡莲赢得次数 BronyaWin 布洛妮娅赢的次数
    SakuraKallenlife = 100
    SakuraKallenatk = 20
    SakuraKallendef = 9
    SakuraKallenskill = 1

    Bronyalife = 100
    Bronyaatk = 21
    Bronyadef = 10
    Bronyaskill = 1

    SakuraKallenWin = 0
    BronyaWin = 0

    for index in range(0, 1000000):
        while(SakuraKallenlife > 0 and Bronyalife > 0):
            # 布洛妮娅先手攻击
            # 摩托bikeだ！
            if Bronyaskill == 3:
                SakuraKallenlife = SakuraKallenlife - random.randint(1, 100)
                Bronyaskill = 1
            else:
                Bronyaskill += 1
                # 天使重构
                if random.randint(1, 100) <= 25:
                    SakuraKallenlife = SakuraKallenlife - \
                                        4 * (12 - SakuraKallendef)
                else:
                    SakuraKallenlife = SakuraKallenlife - \
                                        (Bronyaatk - SakuraKallendef)

            # 八重樱&卡莲后手攻击
            if random.randint(1, 100) <= 30:
                SakuraKallenlife += 25

            if SakuraKallenskill == 2:
                Bronyalife = Bronyalife - 25
                SakuraKallenskill = 1
            else:
                Bronyalife = Bronyalife - (SakuraKallenatk - Bronyadef)
                SakuraKallenskill += 1

        # 判定输赢，速度慢的后手方放前面先判断
        if SakuraKallenlife <= 0:
            BronyaWin = BronyaWin + 1
        else:
            SakuraKallenWin = SakuraKallenWin + 1

        # 数值重置
        SakuraKallenlife = 100
        SakuraKallenatk = 20
        SakuraKallendef = 9
        SakuraKallenskill = 1
        Bronyalife = 100
        Bronyaatk = 21
        Bronyadef = 10
        Bronyaskill = 1

    # 结果展示
    print("八重樱&卡莲赢的概率为%f，一共赢了%d场"
          % (SakuraKallenWin / (SakuraKallenWin + BronyaWin), SakuraKallenWin))

    print("布洛妮娅赢的概率为%f 一共赢了%d场"
          % (BronyaWin / (SakuraKallenWin + BronyaWin), BronyaWin))

    print("投票八重樱&卡莲赔率期望")
    print((SakuraKallenWin / (SakuraKallenWin + BronyaWin))*4.2)

    print("投票布洛妮娅赔率期望")
    print((BronyaWin / (SakuraKallenWin + BronyaWin))*1.8)
