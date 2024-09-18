def calc_damage (dado,ataques,bonus,dano,crit,ac,cc,wmd):
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque=(ataques*(hc*(dano))+((dado*(cc/20))*crit))+wmd
    return ataque

print('='*50)
ac=int(input('qual ac quer acertar:'))
atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))

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

    hc = (1-pow(((ac-bonus)/20),dado))
    
    if wm == 'vex' and dado>2:
         wmd = ((ataques-1)*(hc*(dano))+(dado*(cc/20)*crit))*0.1
    elif wm == 'topple'and dado>2:
         wmd = ((ataques-1)*(hc*(dano))+(dado*(cc/20)*crit))*0.1*0.4
    elif wm =='graze':
        dg=int(input('dano do graze:'))
        wmd = ((1-hc)*dg)*ataques
    else:
         wmd = 0

    fatores  = [dado,ataques,bonus,dano,cc,crit,wmd]

    resultado = [calc_damage(*fatores,ac)]
    resultados.append(resultado)
total_de_dano =  resultados
 
dano_em_um_atk= float(input('dano em um ataque só:'))
dano_uma_vez= dano_em_um_atk*(pow(hc,(ataques*atk))) 

print('='*50)
print ('por favor faça a soma final')
print ('seu dano por turno é:',total_de_dano)

if gwm =="s":
    print('+',((ataques*(hc*(dano))+((dado*(cc/20)*crit)+(1-hc)*wmd)*((dado*cc))/20)))
else:
     print

if sm == "s":
      print('+',((ataques-1)*(hc*(dano))+((dado*(cc/20)*crit)*0.1*0.4)))
else:
      print

if kye == 's':
    print('+',((ataques-1)*(hc*(dano))+((dado*(cc/20)*crit)*(1-hc)*0.1)))
else:
     print

print ('+',dano_uma_vez)
print('='*50)