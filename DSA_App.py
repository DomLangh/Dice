import numpy as np
import streamlit as st
import DSA_Roll
choice = st.radio('Einzel oder dreier Wurf?', ('Einzel', 'Drei'))

if choice == 'Drei':
    talent = st.number_input('Talentwert', step = 1)    
    attrib_1 = st.number_input('Eigenschaftswert 1', min_value = 0, step = 1, key = 'attrib1')
    attrib_2 = st.number_input('Eigenschaftswert 2', min_value = 0, step = 1, key = 'attrib2')
    attrib_3 = st.number_input('Eigenschaftswert 3', min_value = 0, step = 1, key = 'attrib3')
    attrib = [attrib_1, attrib_2, attrib_3]
    roll = st.button('Würfeln!')
    if roll:
        DSA_Roll.dsa_talent_roll(attrib, talent)
elif choice == 'Einzel':
    talent = st.number_input('Talentwert', step = 1)
    roll = st.button('Würfeln!')
    if roll:
        DSA_Roll.dsa_single_roll(talent)