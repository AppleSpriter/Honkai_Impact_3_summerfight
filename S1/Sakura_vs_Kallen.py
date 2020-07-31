import random
if __name__ == "__main__":
    #(k Kallen s Sakura) life生命 atk攻击 def防御 skill技能计数 KallenWin卡莲赢的次数 SakuraWin小八赢的次数
    klife = 100
    slife = 100
    katk = 26
    satk = 28
    kdef = 6
    sdef = 7
    kskill = 0
    sskill = 0
    sum = 1000000

    KallenWin = 0
    SakuraWin = 0

    for index in range(0,sum):
        while(klife>0 and slife>0):
            # 卡莲先手攻击
            # 卡莲被动发动，八重樱血量清零
            if(random.randint(1,100)<6):
                slife = 0
                break
            else:
                slife = slife - (katk - sdef)
                # 卡莲必杀技判定
                if(random.randint(1,10)<4):
                    kskill = 2


            # 八重樱后手攻击，判断卡莲必杀技没有发动
            if(kskill < 1):
                # 八重樱必杀技伤害翻倍
                if(random.randint(1,100)<26):
                    klife = klife - (satk - kdef) * 2
                else:
                    klife = klife - (satk - kdef)
                
            else:
                # 卡莲发动必杀技八重樱攻击减少15
                # 八重樱必杀技伤害翻倍
                if(random.randint(1,100)<26):
                    klife = klife - (satk - 15 - kdef) * 2
                else:
                    klife = klife - (satk - 15 - kdef)

                # 卡莲必杀技减少一回合冷却
                kskill = kskill - 1

            # 八重樱被动挂点燃
            if(random.randint(1,5)==1):
                sskill = 3

             # 八重樱点燃效果
            if(sskill > 0):
                klife = klife - 5
            
            # 点燃效果减少一回合
            sskill = sskill - 1

                
        #判定输赢
        if slife<=0:
            KallenWin = KallenWin + 1
        else:
            SakuraWin = SakuraWin + 1
        
        #数值重置
        klife = 100
        slife = 100
        katk = 26
        satk = 28
        kdef = 6
        sdef = 7
        kskill = 0
        sskill = 0


    print("卡莲赢的场次为")
    print("%d场"%(KallenWin/(KallenWin + SakuraWin)*sum))

    print("八重樱赢的场次为")
    print("%d场"%(SakuraWin/(KallenWin + SakuraWin)*sum))

    print("投票卡莲赔率期望")
    print((KallenWin/(KallenWin + SakuraWin))*3)

    print("投票八重樱赔率期望")
    print((SakuraWin/(KallenWin + SakuraWin))*3.4)

    
