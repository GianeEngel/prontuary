# -*- coding: utf-8 -*-
"""
Codigo para fazer a predicao a partir do modelo treinado.
versao giane.sav
Tipo: floresta randomica

@author: mirkos@gmail.com
"""

import joblib
import streamlit as st
import pandas as pd

gravidade = ['Low','Medium','High']

nome = 'giane.sav'
modelo = joblib.load(nome)
st.title('AI-Blood - COVID-19 Prognosis')
siri = 0
aisi = 0
nlr = 0
plr = 0
sii = 0
rdw = st.number_input('RDW (%)')
leu = st.number_input('Leukocytes (10^9/L)')
lin = st.number_input('Lymphocytes (10^9/L)')
mon = st.number_input('Monocytes (10^9/L)')
neu = st.number_input('Neutrophils (10^9/L)')
pcr = st.number_input('CRP (mg/dL)')
pla = st.number_input('Platelets (10^9/L)')
satO = st.selectbox('Saturation Oximetry',('<95','>=95'))
if satO == '<95':
    sat=0
else:
    sat=1
dbm2 = st.selectbox('Type 2 diabetes mellitus',('No','Yes'))
if dbm2=='No':
    dm2 = 0
else:
    dm2 = 1
none = st.selectbox('Hypertension (HAS):',('No','Yes'))


#st.write('RDW:',rdw)
#st.write('Leukocytes:',leu)
#st.write('Lymphocytes:',lin)
#st.write('Monocytes:',mon)
#st.write('Neutrophils:',neu)
#st.write('CRP:',pcr)
#st.write('Platelets:',pla)


if lin == 0:
     nlr = 0
     plr = 0
     aisi = 0
elif mon == 0:
     siri = 0
elif neu == 0:
    sii = 0
else:
     siri = nlr/float(mon)
     aisi = (float(neu)*int(pla)*float(mon))/float(lin)
     nlr = float(neu)/float(lin)
     plr = float(pla)/float(lin)
     sii = plr/float(neu)

#nlr = st.number_input('NLR.1')
##nlr = int(neu)/int(lin)
#plr = st.number_input('PLR.1')
##plr = int(pla)/int(lin)
#sii = st.number_input('SII.1')
##sii = plr/int(neu)
#siri = st.number_input('SIRI.1')
##siri = nlr/int(mon)
#aisi = st.number_input('AISI.1')
##aisi = (int(neu)*int(pla)*int(mon))/int(lin)

limit_float_nlr = round(nlr, 2)
st.write('NLR:',limit_float_nlr)
limit_float_plr = round(plr, 2)
st.write('PLR:',limit_float_plr)
limit_float_sii = round(sii, 2)
st.write('SII:',limit_float_sii)
limit_float_siri = round(siri, 2)
st.write('SIRI:',limit_float_siri)   
limit_float_aisi = round(aisi, 2)
st.write('AISI:',limit_float_aisi)  


#dt = {'NLR':[nlr],'PLR':[nlr],'SII':[sii],'SIRI':[siri],'AISI':[aisi]}
#formulas = pd.DataFrame(data=dt)
#st.dataframe(formulas)

pac = [rdw,leu,neu,pcr,sat,dm2,nlr,plr,sii,siri,aisi]
pred = modelo.predict([pac])




if st.button('Analyse'):
    indice = int(pred)
    #st.write('Severity pred:',gravidade[int(pred)])
    if indice == 0:
        st.write('NON-SEVERE')
        st.image('low-risk.png',width=150)
    else:
        if indice==1:
           st. write('SEVERE')
            st.image('moderate-risk.png',width=150)
        else:
            st.write('CRITICAL')
            st.image('high-risk.png',width=150)
    
