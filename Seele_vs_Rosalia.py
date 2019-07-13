import random
if __name__ == "__main__":
    #(r Rosalia s Seele) life生命 atk攻击 def防御 skill技能计数 sum计算次数 RosaliaWin萝莎莉娅赢的次数 SeeleWin希儿赢的次数
    rlife = 100
    slife = 100
    ratk = 30
    satk = 23
    rdef = 4
    sdef = 10
    rskill1 = 1 # 萝莎莉娅1技能倍率
    rskill2 = 1
    sskill = 1
    tired = 0   # 萝莎莉娅2技能疲劳
    sum = 1000000

    RosaliaWin = 0
    SeeleWin = 0

    for index in range(0,sum):
        while(rlife>0 and slife>0):
            # 希儿先手攻击

            # 希儿被动1触发，最高100滴血
            tmp = slife + 7
            if(tmp > 100):
                slife = 100
            else:
                slife = tmp
                
            # 希儿攻击
            if(sskill<4):
                rlife = rlife - (satk - rdef)
                sskill = sskill + 1
            else:
                # 希儿2技能，25%的命中率
                if(random.randint(1,100)<26):
                    rlife = rlife - (100 - rdef)
                sskill = 1

            # 萝莎莉娅后手攻击
            if(tired < 1):
                if(rskill2<3):
                    slife = slife - (ratk - sdef) * rskill1
                    rskill2 = rskill2 + 1
                else:
                    slife = slife - (15 - sdef) * 10 * rskill1
                    rskill2 = 1
                    tired = 2     # 下回合跳过回合
            
            # 萝莎莉娅疲劳重置
            tired = tired - 1

            # 萝莎莉娅1技能触发，伤害1-3增加 8-10减少
            tmp = random.randint(1,10)
            if tmp < 4:
                rskill1 = 1.5
            elif tmp > 7:
                rskill1 = 0.5
            else:
                rskill1 = 1

        
        #判定输赢
        if rlife<=0:
            SeeleWin = SeeleWin + 1
        else:
            RosaliaWin = RosaliaWin + 1
        
        #数值重置
        rlife = 100
        slife = 100
        ratk = 30
        satk = 23
        rdef = 4
        sdef = 10
        rskill1 = 1 # 萝莎莉娅1技能倍率
        rskill2 = 1
        sskill = 1
        tired = 0   # 萝莎莉娅2技能疲劳


    print("希儿赢的概率为")
    print(SeeleWin/(SeeleWin + RosaliaWin))

    print("萝莎莉娅赢的概率为")
    print(RosaliaWin/(SeeleWin + RosaliaWin))

    print("投票希儿赔率期望")
    print((SeeleWin/(SeeleWin + RosaliaWin))*5)

    print("投票萝莎莉娅赔率期望")
    print((RosaliaWin/(SeeleWin + RosaliaWin))*1.6)

    
