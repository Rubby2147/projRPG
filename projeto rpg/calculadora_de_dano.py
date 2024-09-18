quer=input('quer calcular:(s/n)')
while quer=='s':
    print('='*50)
    ac=int(input('qual ac quer acertar:'))
    atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))
    print('='*50)
    resultados= []
    for x in (range(atk)):
        ataques= int(input('quantos ataques iguais vai fazer:'))
        dado = int(input('quantos dados vai rolar:')) 
        bonus= float(input('qual seu bonus para acertar:'))
        dano=float(input('dano por cada ataque:'))
        cc=int(input('quantas faces do dado que dá critco:'))
        crit =float(input('dano em um critico:'))
        wm= input('qual sua weapon mastery:')
        sm= input('você tem mestre de escudo:(s/n)')
        gwm= input('você tem mastre de armas grandes:(s/n)')
        kye= input('você ganha vantagem se errar:(s/n)')
        print('='*50)

        hc=(1-pow(((ac-bonus)/20),dado))
        ataque=float((ataques*(hc*(dano))+((dado*(cc/20))*crit)))

        if wm == 'vex' and dado<2:
             wmd = (((ataques-1)*(hc+(hc*pow(hc,2)))*(dano))+hc*((dado+1)*(cc/20)*crit))
        elif wm == 'topple'and dado<2:
         wmd = (((ataques-1)*(hc+(hc*pow(hc,2)))*(dano))+hc*((dado+1)*(cc/20)*crit))*0.4
        elif wm =='graze':
            dg=int(input('dano do graze:'))
            wmd = ((1-hc)*dg)*ataques
        else:
             wmd = 0

        resultado = [ataque+wmd]
        resultados.append(resultado)
    total_de_dano =  resultados
 
    dano_em_um_atk= float(input('dano em um ataque só:'))
    dano_uma_vez= dano_em_um_atk*(pow(hc,(ataques*atk))) 

    print('='*50)
    print ('por favor faça a soma final')
    print ('seu dano por turno é:',total_de_dano)

    if gwm =="s":
        print('+',((ataques*(hc*(dano))+((dado*(cc/20)*crit)+(1-hc)*wmd))*((dado*cc))/20))
    else:
         print

    if sm == "s" and dado <1:
      print('+',(((ataques-1)*(hc+(hc*pow(hc,2)))*(dano))+hc*((dado+1)*(cc/20)*crit))*0.4)
    else:
      print

    if kye == 's':
        print('+',(((ataques-1)*(hc+((1-hc)*pow(hc,2)))*(dano))+(1-hc)*((dado+1)*(cc/20)*crit)))
    else:
         print

    print ('+',dano_uma_vez)

    print('='*50)
    quer=input('quer calcular:(s/n)')