import random
if __name__ == "__main__":
    #(l Lita r Rosalia) life生命 atk攻击 def防御 skill技能计数 sum计算次数 LitaWin丽塔赢的次数 RosalialeWin萝莎莉娅赢的次数
    llife = 100
    rlife = 100
    latk = 26
    ratk = 30
    ldef = 8
    rdef = 4
    lskill = 1
    rskill1 = 1 # 萝莎莉娅1技能倍率
    rskill2 = 1
    sum = 1000000

    LitaWin = 0
    RosalialeWin = 0

    for index in range(0,sum):
        while(llife>0 and rlife>0):
            # 萝莎莉娅先手攻击
                
            # 计算丽塔2技能后，萝莎莉娅攻击
            if(lskill > 0):

                # 萝莎莉娅2技能触发验证
                if(rskill2<3):
                    llife = llife - (ratk - ldef) * rskill1
                    rskill2 = rskill2 + 1
                else:
                    llife = llife - (15 - ldef) * 10 * rskill1
                    rskill2 = 1
                    lskill = -1     # 直接设置丽塔被动实现跳过一回合

                # 萝莎莉娅1技能触发，伤害1-3增加 8-10减少
                tmp = random.randint(1,10)
                if tmp < 4:
                    rskill1 = 1.5
                elif tmp > 7:
                    rskill1 = 0.5
                else:
                    rskill1 = 1

            # 重置丽塔2技能
            lskill = lskill + 1

            # 丽塔后手攻击
            rlife = rlife - (latk - rdef)
            
            # 丽塔被动1
            if(random.randint(1,10)<4):
                tmp = llife + (latk - rdef)
                if(tmp > 100):
                    llife = 100
                else:
                    llife = tmp
            
            # 丽塔被动2
            if(random.randint(1,10)<3):
                lskill = 0
        
        #判定输赢
        if llife<=0:
            RosalialeWin = RosalialeWin + 1
        else:
            LitaWin = LitaWin + 1
        
        #数值重置
        llife = 100
        rlife = 100
        latk = 26
        ratk = 30
        ldef = 8
        rdef = 4
        lskill = 1
        rskill1 = 1
        rskill2 = 1


    print("萝莎莉娅赢的概率为")
    print(RosalialeWin/(RosalialeWin + LitaWin))

    print("丽塔赢的概率为")
    print(LitaWin/(RosalialeWin + LitaWin))

    print("投票萝莎莉娅赔率期望")
    print((RosalialeWin/(RosalialeWin + LitaWin))*1.9)

    print("投票丽塔赔率期望")
    print((LitaWin/(RosalialeWin + LitaWin))*4.1)

    
