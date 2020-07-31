import random
if __name__ == "__main__":
    #(b Bronya f Fuhua) life生命 atk攻击 def防御 skill技能计数 BronyaWin布洛尼亚赢的次数 FuhuaWin浮华赢的次数
    blife = 100
    flife = 100
    batk = 26
    fatk = 27
    bdef = 8
    fdef = 8
    bskill = 1
    fskill1 = 1
    fskill2 = 1
    sum = 1000000

    BronyaWin = 0
    FuhuaWin = 0

    for index in range(0,sum):
        while(blife>0 and flife>0):
            # 浮华先手攻击
            if(fskill2 < 3):
                # 判定板鸭闪避
                if(random.randint(1,100)>15):
                    blife = blife - (fatk - bdef)
                fskill2 = fskill2 + 1
            else:
                if(random.randint(1,100)>15):
                    blife = blife - random.randint(10,30)
                fskill2 = 1

            # 板鸭后手攻击
            if(bskill < 3):
                flife = flife - (batk - fdef)
                bskill = bskill + 1
                # 浮华装死技能判定
                if(flife<1 and fskill1 == 1):
                        flife = 1
                        fskill1 = 0
            else:
                tmp = random.randint(1,100)
                if(tmp > fdef):
                    flife = flife - (tmp - fdef)
                bskill = 1
                # 浮华装死技能判定
                if(flife<1 and fskill1 == 1):
                        flife = 1
                        fskill1 = 0

                
        # 判定输赢
        if blife<=0:
            FuhuaWin = FuhuaWin + 1
        else:
            BronyaWin = BronyaWin + 1
        
        #数值重置
        blife = 100
        flife = 100
        batk = 26
        fatk = 27
        bdef = 8
        fdef = 8
        bskill = 1
        fskill1 = 1
        fskill2 = 1


    print("板鸭赢的场次为")
    print("%d场"%(BronyaWin/(BronyaWin + FuhuaWin)*sum))

    print("浮华赢的场次为")
    print("%d场"%(FuhuaWin/(BronyaWin + FuhuaWin)*sum))

    print("投票板鸭赔率期望")
    print((BronyaWin/(BronyaWin + FuhuaWin))*3.5)

    print("投票浮华赔率期望")
    print((FuhuaWin/(BronyaWin + FuhuaWin))*2.8)

    
