import random
if __name__ == "__main__":
    #(f Fuhua s Sakura) life生命 atk攻击 def防御 skill技能计数 FuhuaWin浮华赢的次数 SakuraWin小八赢的次数
    flife = 100
    slife = 100
    fatk = 27
    satk = 28
    fdef = 8
    sdef = 7
    fskill1 = 1 # 浮华被动技能
    fskill2 = 1 # 浮华必杀技判定
    sskill = 0  # 小八被动技能
    sum = 10000000

    FuhuaWin = 0
    SakuraWin = 0

    for index in range(0,sum):
        while(flife>0 and slife>0):
            # 浮华先手攻击，必杀技判断未发动
            if(fskill2 < 3):
                slife = slife - (fatk - sdef)
                fskill2 = fskill2 + 1
            # 浮华发动必杀技
            else:
                slife = slife - random.randint(10,30)
                fskill2 = 1

            # 八重樱后手攻击，八重樱必杀技伤害翻倍
            if(random.randint(1,100)<26):
                flife = flife - (satk - fdef) * 2
            else:
                flife = flife - (satk - fdef)
            
            # 判断浮华装死技能
            if(fskill1 == 1 and flife <= 0):
                flife = 1
                fskill1 = 0

            # 浮华装死技能发动后免疫元素伤害
            if(fskill1 == 1):
                # 八重樱被动挂点燃
                if(random.randint(1,5)==1):
                    sskill = 3

                # 八重樱点燃效果
                if(sskill > 0):
                    flife = flife - 5
                
                # 点燃效果减少一回合
                sskill = sskill - 1

                
        #判定输赢
        if slife<=0:
            FuhuaWin = FuhuaWin + 1
        else:
            SakuraWin = SakuraWin + 1
        
        #数值重置
        flife = 100
        slife = 100
        fatk = 27
        satk = 28
        fdef = 8
        sdef = 7
        fskill1 = 1
        fskill2 = 1
        sskill = 0


    print("浮华赢的场次为")
    print("%d场"%(FuhuaWin/(FuhuaWin + SakuraWin)*sum))

    print("八重樱赢的场次为")
    print("%d场"%(SakuraWin/(FuhuaWin + SakuraWin)*sum))

    print("投票浮华赔率期望")
    print((FuhuaWin/(FuhuaWin + SakuraWin))*3.6)

    print("投票八重樱赔率期望")
    print((SakuraWin/(FuhuaWin + SakuraWin))*4.4)

    
