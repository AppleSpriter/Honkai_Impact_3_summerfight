import random
if __name__ == "__main__":
    #(t Teresa k Kiana) life生命 atk攻击 def防御 skill技能计数 TeresaWin德丽莎赢得次数 KianaWin琪亚娜赢的次数
    tlife = 100
    klife = 120
    tatk = 24
    katk = 23
    tdef = 8
    kdef = 11
    tskill = 1
    kskill = 1

    TeresaWin = 0
    KianaWin = 0

    for index in range(0,1000000):
        while(tlife>0 and klife>0):
            #德丽莎先手攻击
            if(tskill<2):
                klife = klife - (tatk - kdef)
                tskill = tskill + 1
            else:
                klife = klife - random.randint(1,16) * 4
                tskill = 1

            #琪亚娜后手攻击
            if(kskill<3):
               tlife = tlife - (katk - tdef)
               kskill = kskill + 1
            else:
                tlife = tlife - (12 - tdef) * 8
                kskill = 1
                
        #判定输赢
        if klife<=0:
            TeresaWin = TeresaWin + 1
        else:
            KianaWin = KianaWin + 1
        
        #数值重置
        tlife = 100
        klife = 120
        tatk = 24
        katk = 23
        tdef = 8
        kdef = 11
        tskill = 1
        kskill = 1


    print("德丽莎赢的概率为")
    print(TeresaWin/(TeresaWin + KianaWin))

    print("琪亚娜赢的概率为")
    print(KianaWin/(TeresaWin + KianaWin))

    print("投票德丽莎赔率期望")
    print((TeresaWin/(TeresaWin + KianaWin))*1.4)

    print("投票琪亚娜赔率期望")
    print((KianaWin/(TeresaWin + KianaWin))*21)

    
