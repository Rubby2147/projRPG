def calc_damage (dado,ataques,bonus,dano,crit,ac):
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque=(ataques*(hc*(dano))+(dado/20)*crit)

atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))
ac=int(input('qual ac quer acertar:'))

dado = int(input('quantos dados vai rolar:')) 
ataques= int(input('quantos ataques iguais vai fazer:'))
bonus= int(input('qual seu bonus para acertar:'))
dano=int(input('dano por cada ataque:'))
crit =int(input('dano em um critico:'))

resultados = []
for i in range(atk):
    fatores = [dado,ataques,bonus,dano,crit]
    resultado = [calc_damage(*fatores, ac)]

    print(f'dano por round:{resultado}')