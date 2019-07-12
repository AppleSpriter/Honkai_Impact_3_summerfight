import random
if __name__ == "__main__":
    #(l Lita s Seele) life生命 atk攻击 def防御 skill技能计数 sum计算次数 LitaWin丽塔赢得次数 SeeleWin希儿赢的次数
    llife = 100
    slife = 100
    latk = 26
    satk = 23
    ldef = 8
    sdef = 10
    lskill = 1
    sskill = 1
    sum = 1000000

    LitaWin = 0
    SeeleWin = 0

    for index in range(0,sum):
        while(llife>0 and slife>0):
            # 希儿先手攻击

            # 希儿被动1触发，最高100滴血
            tmp = slife + 7
            if(tmp > 100):
                slife = 100
            else:
                slife = tmp
                
            # 计算丽塔2技能后，希儿攻击
            if(lskill > 0):
                if(sskill<4):
                    llife = llife - (satk - ldef)
                    sskill = sskill + 1
                else:
                    # 希儿2技能，25%的命中率
                    if(random.randint(1,100)<26):
                        llife = llife - (100 - ldef)
                    sskill = 1

            # 重置丽塔2技能
            lskill = lskill + 1

            # 丽塔后手攻击
            slife = slife - (latk - sdef)
            
            # 丽塔被动1
            if(random.randint(1,10)<4):
                tmp = llife + (latk - sdef)
                if(tmp > 100):
                    llife = 100
                else:
                    llife = tmp
            
            # 丽塔被动2
            if(random.randint(1,10)<3):
                lskill = 0
        
        #判定输赢
        if llife<=0:
            SeeleWin = SeeleWin + 1
        else:
            LitaWin = LitaWin + 1
        
        #数值重置
        llife = 100
        slife = 100
        latk = 26
        satk = 23
        ldef = 8
        sdef = 10
        lskill = 1
        sskill = 1


    print("希儿赢的概率为")
    print(SeeleWin/(SeeleWin + LitaWin))

    print("丽塔赢的概率为")
    print(LitaWin/(SeeleWin + LitaWin))

    print("投票希儿赔率期望")
    print((SeeleWin/(SeeleWin + LitaWin))*2.7)

    print("投票丽塔赔率期望")
    print((LitaWin/(SeeleWin + LitaWin))*2.2)

    
