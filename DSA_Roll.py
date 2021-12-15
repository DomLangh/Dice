import numpy as np

attr = np.array([15,9,10])
talent = 10
def dsa_talent_roll(attr, talent):
    die = np.random.randint(1,20+1,3)
    print(f'Talentwerte: {attr}')
    print(f'Würfelwurf: {die}')
    count_20 = np.count_nonzero(die == 20)
    count_1= np.count_nonzero(die == 1)
    diff = attr - die
    count = np.count_nonzero(diff >= 0)
    
    
    if count_1 == 3:
        print('Tripple 1!!!!!!!')
    elif count_1 == 2:
        print('Doppel 1!!!')
    elif count_20 == 3:
        print('Tripple 20!!!!!!')
    elif count_20 ==2:
        print('Doppel 20!!!')
    elif count == 3:
        print(f'Gelungene Probe mit {die}\nAlle {talent} Punkte übrig!')
    else:
        for i in range(3):
            if diff[i] < 0:
                talent = talent + diff[i]
        if talent < 0:
            print(f'Probe um {talent} Punkt(e) nicht geschafft :(.')
        else:
            print(f'Probe mit {talent} Punkt(en) geschafft :).')
            
dsa_talent_roll(attr, talent)

def dsa_battle_roll(talent):
    counter_1 = 0
    counter_20 = 0
    counter_damage = 0
#    die = np.random.randint(1,20+1,1)
    die = np.random.randint(1,20+1,1)
    print(die)
    if die == 1:
        die_1 = np.random.randint(1,20+1,1)
        if die_1 <= talent:
            print(f'Erfolgreicher Krit mit {die} und {die_1}!')
        else:
            print(f'Leider nur normaler Hit mit {die} und {die_1}.')
    elif die == 20:
        die_20 = np.random.randint(1,20+1,1)
        if die_20 <= talent:
            print(f'Puh, glück gehabt. Nur versagt mit {die} und {die_20} :D')
        else:
            print(f'Kritische versagt mit {die} und {die_20}!')

    else:
        if die <= talent:
            print(f'Angriff erfolgreich mit {die}, um {talent - die} unterwürfelt')
        else:
            print(f'Angriff nicht erfolgreich mit {die}, um {die - talent} überwürfelt')
dsa_battle_roll(talent)