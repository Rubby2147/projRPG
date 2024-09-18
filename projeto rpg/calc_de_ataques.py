def calc_damage (dado,ataques,bonus,dano,crit,ac,cc):
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque=(ataques*(hc*(dano))+((dado+cc)/20)*crit)
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
    print('='*50)
    
    fatores  = [dado,ataques,bonus,dano,cc,crit]

    resultado = [calc_damage(*fatores,ac)]
    resultados.append(resultado)
total_de_dano =  resultados

hc = (1-pow(((ac-bonus)/20),dado))
dano_uma_vez= dano_em_um_atk*(pow(hc,(ataques*atk))) 

print('='*50)
print ('por favor faça a soma final')
print ('seu dano por turno é:',total_de_dano)
print('+')
print (dano_uma_vez)
print('='*50)