import pandas as pd
import streamlit as st

st.title("Calculadora de IMC")

with st.sidebar:
    st.title("Classificação de Peso e Altura")
    st.write("Tipos de Classificação")

peso = st.number_input(label="Digita o seu peso em kilos", min_value=0.0)
altura = st.number_input(label="Digita sua altura", min_value=0.0)

if st.button("Calcular"):
   imc = peso / (altura ** 2)
   imc_deal = 21.7
   imc_delta = imc - imc_deal

   if imc <18.5:
     resultado = {'Classe': 'Estar Baixo do Peso',
     'delta': imc_delta}

   elif imc <=18.5:
     resultado = {'Classe': 'Estar no Peso ideal',
     'delta': imc_delta}
      
   elif 25 <= imc < 30:
     resultado = {'Classe': 'Estar no Peso ideal',
     'delta': imc_delta}  

   elif imc > 30:
     resultado = {'Classe': 'Estar emcima do Peso',
     'delta': imc_delta}  

   else:
     resultado = {'Classe': 'voce estar morto',
     'delta': imc_delta

     }
st.code(f"O resultado e {resultado}")

col1, col2 = st.columns(2)
col1.metric("IMC Classificado",resultado["Classe"], resultado["delta"], delta_color="inverse")
col2.metric("IMC Calculado", round(imc, 2) , resultado["delta"], delta_color="off")

st.divider()
st.text("Fonte")




