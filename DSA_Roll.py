import numpy as np
import streamlit as st


def dsa_talent_roll(attr, talent):
    attr = np.asarray(attr)
    die = np.random.randint(1,20+1,3)
    st.write(f'Eigenschaften: {attr}')
    st.write(f'Talentwert: {talent}')
    st.write(f'Würfelwurf: {die}')
    count_20 = np.count_nonzero(die == 20)
    count_1= np.count_nonzero(die == 1)
    diff = attr - die
    count = np.count_nonzero(diff >= 0)
    
    
    if count_1 == 3:
        st.write('Tripple 1!!!!!!!')
    elif count_1 == 2:
        st.write('Doppel 1!!!')
    elif count_20 == 3:
        st.write('Tripple 20!!!!!!')
    elif count_20 ==2:
        st.write('Doppel 20!!!')
    elif count == 3:
        st.write(f'Gelungene Probe mit {die}\nAlle {talent} Punkte übrig!')
    else:
        for i in range(3):
            if diff[i] < 0:
                talent = talent + diff[i]
        if talent < 0:
            st.write(f'Probe um {talent} Punkt(e) nicht geschafft :(.')
        else:
            st.write(f'Probe mit {talent} Punkt(en) geschafft :).')
            


def dsa_single_roll(talent):
    counter_1 = 0
    counter_20 = 0
    counter_damage = 0
    die = np.random.randint(1,20+1,1)
    st.write(f'Talentwert: {talent}')
    st.write(f'Würfelwurf: {die}')
    if die == 1:
        die_1 = np.random.randint(1,20+1,1)
        if die_1 <= talent:
            st.write(f'Erfolgreicher Krit mit {die} und {die_1}!')
        else:
            st.write(f'Leider nur normaler Hit mit {die} und {die_1}.')
    elif die == 20:
        die_20 = np.random.randint(1,20+1,1)
        if die_20 <= talent:
            st.write(f'Puh, glück gehabt. Nur versagt mit {die} und {die_20} :D')
        else:
            st.write(f'Kritische versagt mit {die} und {die_20}!')

    else:
        if die <= talent:
            st.write(f'Angriff erfolgreich mit {die}, um {talent - die} unterwürfelt')
        else:
            st.write(f'Angriff nicht erfolgreich mit {die}, um {die - talent} überwürfelt')
