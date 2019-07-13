import random
if __name__ == "__main__":
    #(t Teresa b Bronya) life生命 atk攻击 def防御 skill技能计数 TeresaWin德丽莎赢得次数 BronyaWin布洛尼亚赢的次数
    tlife = 100
    blife = 100
    tatk = 24
    batk = 26
    tdef = 8
    bdef = 8
    tskill = 1
    bskill = 1
    sum = 1000000

    TeresaWin = 0
    BronyaWin = 0

    for index in range(0,sum):
        while(tlife>0 and blife>0):
            # 德丽莎先手攻击，德丽莎2技能触发
            if(tskill<2):
                # 板鸭1技能闪避判定
                if(random.randint(1,100)>15):
                    blife = blife - (tatk - bdef)
                tskill = tskill + 1
            else:
                # 板鸭1技能闪避判定
                if(random.randint(1,100)>15):
                    blife = blife - random.randint(1,16) * 4
                tskill = 1

            # 板鸭后手攻击
            if(bskill<3):
               tlife = tlife - (batk - tdef)
               bskill = bskill + 1
            else:
                tmp = random.randint(1,100)
                if(tmp>tdef):
                    tlife = tlife - (tmp - tdef)
                bskill = 1
                
        #判定输赢
        if blife<=0:
            TeresaWin = TeresaWin + 1
        else:
            BronyaWin = BronyaWin + 1
        
        #数值重置
        tlife = 100
        blife = 100
        tatk = 24
        batk = 26
        tdef = 8
        bdef = 8
        tskill = 1
        bskill = 1


    print("德丽莎赢的概率为")
    print("%3f"%(TeresaWin/(TeresaWin + BronyaWin)))

    print("布洛尼亚赢的概率为")
    print("%3f"%(BronyaWin/(TeresaWin + BronyaWin)))

    print("投票德丽莎赔率期望")
    print((TeresaWin/(TeresaWin + BronyaWin))*2.2)

    print("投票布洛尼亚赔率期望")
    print((BronyaWin/(TeresaWin + BronyaWin))*3.5)

    
