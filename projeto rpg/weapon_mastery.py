def calc_damage (dado,ataques,bonus,dano,crit,ac,cc,graze):
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque=(ataques*(hc*(dano))+((dado+cc)/20)*crit)+(1-hc)*graze
    return ataque

print('='*50)
ac=int(input('qual ac quer acertar:'))
atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))
dano_em_um_atk= float(input('dano em um ataque só:'))

resultados= []
for x in (range(atk)):
    ataques= int(input('quantos ataques iguais vai fazer:'))
    dado = int(input('quantos dados vai rolar:')) 
    bonus= int(input('qual seu bonus para acertar:'))
    dano=float(input('dano por cada ataque:'))
    cc=int(input('quantas faces do dado que dá critco:'))
    crit =float(input('dano em um critico:'))
    graze=float(input('dano quando errar:'))
    wm= input('qual sua weapon mastery:')
    sm= input('você tem shield master:(s/n)')
    gwm= input('você tem great weapon master:(s/n)')
    kye= input('vocÊ ganha vantagem se errar:(s/n)')
    print('='*50)
    
    fatores  = [dado,ataques,bonus,dano,cc,crit,graze]

    resultado = [calc_damage(*fatores,ac)]
    resultados.append(resultado)
total_de_dano =  resultados
 
hc = (1-pow(((ac-bonus)/20),dado))
dano_uma_vez= dano_em_um_atk*(pow(hc,(ataques*atk))) 


print('='*50)
print ('por favor faça a soma final')
print ('seu dano por turno é:',total_de_dano)

if gwm =="s":
    print('+',((ataques*(hc*(dano))+((dado+cc)/20)*crit)+(1-hc)*graze)*((dado+cc))/20)

if sm == "s":
      print('+',calc_damage(*fatores,ac))*0.1*0.4
else:
      print

if wm == 'vex':
        print('+',calc_damage(*fatores,ac))*hc*0.1
elif wm == 'topple':
        print('+',calc_damage(*fatores,ac))*hc*0.1*0.4
else:
    print

if kye == 's':
      print(print('+',calc_damage(*fatores,ac))*(1-hc)*0.1)
print ('+',dano_uma_vez)
print('='*50)