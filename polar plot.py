def polar(s):
    import math
    
    seq=s.upper()
    a=0
    x=0
    y=0
    cox=[0]
    coy=[0]
    qrx=0
    qry=0
    qr=0
    z=0
    n=0

    amino=['E','A','C','V','F','L','I','W','M','T','Y','G','Q','R','N','P','H','K','D','S']
    angle={}

    k=0
    for i in range(0,360,18):
        angle[amino[k]]=i
        k+=1


    for i in range(len(seq)):
        if seq[i] in amino:
            a=angle[seq[i]]

            x+=math.cos(((math.pi)/180)*a)
            y+=math.sin(((math.pi)/180)*a)
            qrx+=x
            qry+=y
            n+=1

            cox.append(x)
            coy.append(y)
        elif seq[i]==' ':
            pass
        elif seq[i]=='\n':
            pass
        else:
            z+=1

    qr=(((qrx/n)**2)+((qry/n)**2))**0.5

    return [cox,coy,qrx,qry,n,z,qr]

    # cox and coy are list of coordinates. If (x1,y1) is coordinate at some point
    # x1 is stored in cox and y1 s stored in coy. So traverse both the lists
    # simultaneously to get the coordinates.


    
