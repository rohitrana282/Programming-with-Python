def bat_score(d):
    if d['role']=='bat':
        pt=0
        pt+=d['runs']/2
        if d['runs']>50 :
            pt+=5
        if d['runs']>100 :
            pt+=10
        sr=d['runs']/d['balls']*100
        if (sr>=80 and sr<=100):
            pt+=2
        if sr>100 :
            pt+=4
        pt+=d['4']
        pt+=d['6']*2
        pt+=d['field']*10
        b={'name': d['name'], 'batscore':int(pt)}
        print(b)
    else :
        pt=0
        pt+=d['wkts']*10
        if d['wkts']>=3 :
            pt+=5
        if d['wkts']>=5 :
            pt+=10
        er=d['runs']/d['overs']
        if (er>=3.5 and er<=4.5):
            pt+=4
        if (er>=2 and er<3.5):
            pt+=7
        if (er<2):
            pt+=10
        pt+=d['field']*10
        d={'name':d['name'], 'bowlscore': int(pt)}
        print(d)


    
