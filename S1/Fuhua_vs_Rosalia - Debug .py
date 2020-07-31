import random
if __name__ == "__main__":
    #(r Rosalia f Fuhua) life生命 atk攻击 def防御 skill技能计数 sum计算次数 RosaliaWin萝莎莉娅赢的次数 FuhuaWin浮华赢的次数
    rlife = 100
    flife = 100
    ratk = 30
    fatk = 27
    rdef = 4
    fdef = 8
    rskill1 = 1 # 萝莎莉娅1技能倍率
    rskill2 = 1 # 萝莎莉娅2技能
    fskill1 = 1 # 浮华1技能
    fskill2 = 1 # 浮华2技能
    tired = 0   # 萝莎莉娅2技能疲劳
    round = 1
    sum = 1

    RosaliaWin = 0
    FuhuaWin = 0

    for index in range(0,sum):
        while(rlife>0 and flife>0):
            # 浮华先手攻击
            print("第%d回合"%round)
            # 浮华攻击
            if(fskill2<3):
                rlife = rlife - (fatk - rdef)
                print("浮华对萝莉造成%d伤害"%(fatk - rdef))
                fskill2 = fskill2 + 1
            else:
                # 浮华2技能
                tmp = random.randint(10,30)
                rlife = rlife - tmp
                print("浮华发动2技能对萝莉造成%d伤害"%tmp)
                fskill2 = 1

            # 萝莎莉娅后手攻击
            if(tired < 1):
                if(rskill2<3):
                    flife = flife - (ratk - fdef) * rskill1
                    print("萝莉对浮华造成%d伤害"%((ratk - fdef) * rskill1))
                    if(flife<1 and fskill1 == 1):
                        print("浮华发动装死技能，生命值置为1")
                        flife = 1
                        fskill1 = 0
                    rskill2 = rskill2 + 1
                else:
                    flife = flife - (15 - fdef) * 10 * rskill1
                    print("萝莉对浮华造成%d伤害"%((15 - fdef) * 10 * rskill1))
                    if(flife<1 and fskill1 == 1):
                        print("浮华发动装死技能，生命值置为1")
                        flife = 1
                        fskill1 = 0
                    rskill2 = 1
                    tired = 2     # 下回合跳过回合
            
            # 萝莎莉娅疲劳重置
            tired = tired - 1

            # 萝莎莉娅1技能触发，伤害1-3增加 8-10减少
            tmp = random.randint(1,10)
            if tmp < 4:
                rskill1 = 1.5
                print("萝莉下回合伤害增加为1.5倍")
            elif tmp > 7:
                rskill1 = 0.5
                print("萝莉下回合伤害降低为0.5倍")
            else:
                rskill1 = 1

            round = round + 1

        
        #判定输赢
        if rlife<=0:
            FuhuaWin = FuhuaWin + 1
            print("浮华胜利")
        else:
            RosaliaWin = RosaliaWin + 1
            print("萝莉胜利")
        
        #数值重置
        rlife = 100
        flife = 100
        ratk = 30
        fatk = 27
        rdef = 4
        fdef = 8
        rskill1 = 1 # 萝莎莉娅1技能倍率
        rskill2 = 1 # 萝莎莉娅2技能
        fskill1 = 1 # 浮华1技能
        fskill2 = 1 # 浮华2技能
        tired = 0   # 萝莎莉娅2技能疲劳 
        round = 1


    print("浮华赢的概率为")
    print("%3f"%(FuhuaWin/(FuhuaWin + RosaliaWin)))

    print("萝莎莉娅赢的概率为")
    print("%3f"%(RosaliaWin/(FuhuaWin + RosaliaWin)))

    print("投票浮华赔率期望")
    print((FuhuaWin/(FuhuaWin + RosaliaWin))*1.6)

    print("投票萝莎莉娅赔率期望")
    print((RosaliaWin/(FuhuaWin + RosaliaWin))*15)

    
