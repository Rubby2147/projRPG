ac = int(input('qual a armadura:'))
bonus= int(input('qual seu bonus pra acertar'))
dado=int(input('quantos dados vai rolar'))
ataques= int(input('quantos ataques iguais vai fazer:'))
atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))
hc = (1-pow(((ac-bonus)/20),dado))

dano_em_um_atk= float(input('dano em um ataque só:'))

dano_uma_vez= dano_em_um_atk*(pow(hc,(ataques*atk))) 
print (dano_uma_vez)