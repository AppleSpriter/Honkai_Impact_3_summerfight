import random
if __name__ == "__main__":
    #(k Kallen l Lita) life生命 atk攻击 def防御 skill技能计数 KallenWin卡莲赢的次数 LitaWin丽塔赢的次数
    klife = 100
    llife = 100
    katk = 26
    latk = 26
    kdef = 6
    ldef = 8
    kskill = 0
    lskill = 0
    sum = 1000000

    KallenWin = 0
    LitaWin = 0

    for index in range(0,sum):
        while(klife>0 and llife>0):
            # 卡莲先手攻击，验证丽塔必杀技是否发动
            if(lskill == 0):
                # 卡莲被动发动，丽塔血量清零
                if(random.randint(1,100)<6):
                    llife = 0
                    break
                else:
                    llife = llife - (katk - ldef)
                    # 卡莲必杀技判定
                    if(random.randint(1,10)<4):
                        kskill = 2
            else:
                lskill = 0

            # 丽塔后手攻击，判断卡莲必杀技是否发动
            if(kskill < 1):
                klife = klife - (latk - kdef)
                # 丽塔被动技能
                if(random.randint(1,10)<4):
                    tmp = llife + (latk - kdef)
                    if(tmp > 100):
                        llife = 100
                    else:
                        llife = tmp
            else:
                # 卡莲发动必杀技丽塔攻击减少15
                klife = klife - (latk - 15 - kdef)
                # 丽塔被动技能
                if(random.randint(1,10)<4):
                    tmp = llife + (latk - 15 - kdef)
                    if(tmp > 100):
                        llife = 100
                    else:
                        llife = tmp
                # 卡莲必杀技减少一回合冷却
                kskill = kskill - 1

            # 丽塔必杀技
            if(random.randint(1,10)<3):
                lskill = 1

                
        #判定输赢
        if llife<=0:
            KallenWin = KallenWin + 1
        else:
            LitaWin = LitaWin + 1
        
        #数值重置
        klife = 100
        llife = 100
        katk = 26
        latk = 26
        kdef = 6
        ldef = 8
        kskill = 0
        lskill = 0


    print("卡莲赢的场次为")
    print("%d场"%(KallenWin/(KallenWin + LitaWin)*sum))

    print("丽塔赢的场次为")
    print("%d场"%(LitaWin/(KallenWin + LitaWin)*sum))

    print("投票卡莲赔率期望")
    print((KallenWin/(KallenWin + LitaWin))*2)

    print("投票丽塔赔率期望")
    print((LitaWin/(KallenWin + LitaWin))*4.7)

    
