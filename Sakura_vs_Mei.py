import random
if __name__ == "__main__":
    #(s Sakura m Mei) life生命 atk攻击 def防御 skill技能计数 SakuraWin八重樱赢的次数 MeiWin芽衣赢的次数
    slife = 100
    mlife = 100
    satk = 28
    matk = 26
    sdef = 7
    mdef = 6
    sskill = 0
    mskill = 0
    sum = 1000000

    SakuraWin = 0
    MeiWin = 0

    for index in range(0,sum):
        while(slife>0 and mlife>0):
            # 八重樱点燃效果
            if(sskill > 0):
                mlife = mlife - 5
            
            # 点燃效果减少一回合
            sskill = sskill - 1

            # 八重樱先手攻击，验证芽衣必杀技是否发动
            if(mskill < 1):
                # 八重樱必杀技
                if(random.randint(1,100)<26):
                    mlife = mlife - (satk - mdef) * 2
                else:
                    mlife = mlife - (satk - mdef)

                # 八重樱被动挂点燃
                if(random.randint(1,5)==1):
                    sskill = 3
            # 触发芽衣必杀，八重樱无法发动技能，必杀重置
            else:
                mlife = mlife - (satk - mdef)
                mskill = 0

            # 芽衣后手攻击
            slife = slife - (matk - sdef) - 5
            # 芽衣必杀技计算
            if(random.randint(1,10)<4):
                slife = slife - 15
                mskill = 1

                
        #判定输赢
        if mlife<=0:
            SakuraWin = SakuraWin + 1
        else:
            MeiWin = MeiWin + 1
        
        #数值重置
        slife = 100
        mlife = 100
        satk = 28
        matk = 26
        sdef = 7
        mdef = 6
        sskill = 0
        mskill = 0


    print("八重樱赢的概率为")
    print(SakuraWin/(SakuraWin + MeiWin))

    print("芽衣赢的概率为")
    print(MeiWin/(SakuraWin + MeiWin))

    print("投票八重樱赔率期望")
    print((SakuraWin/(SakuraWin + MeiWin))*2.2)

    print("投票芽衣赔率期望")
    print((MeiWin/(SakuraWin + MeiWin))*3.8)

    
