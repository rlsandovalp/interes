# import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Convierte tasas de interes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

tiempos = ['Anual', 'Semestral', 'Trimestral', 'Mensual', 'Diario']


r'''
# Calcular la tasa de interes 📈

Aquí te mostramos como convertir la tasa de interes para diferentes periodos de tiempo.

'''

tasa = st.number_input('¿Cual es la tasa de interes (%)?', 0.00, 100.00, 0.00, 0.10)
variable = st.selectbox('¿En que unidad de tiempo tienes tu tasa de interes?:', variables, 0)

if variable == 'Diario':
    Tasa_anual = (1+tasa/100)**365-1
elif variable == 'Mensual':
    Tasa_anual = (1+tasa/100)**12-1
elif variable == 'Trimestral':
    Tasa_anual = (1+tasa/100)**4-1
elif variable == 'Semestral':
    Tasa_anual = (1+tasa/100)**2-1

tasa_diaria = (1+Tasa_anual)**(1/365)-1
tasa_mensual = (1+Tasa_anual)**(1/12)-1
tasa_trimestral = (1+Tasa_anual)**(1/4)-1
tasa_semestral = (1+Tasa_anual)**(1/2)-1


## Visualizacion de los resultados

st.write('La tasa de interes diaria es: ', round(tasa_diaria*100,2), '%')
st.write('La tasa de interes mensual es: ', round(tasa_mensual*100,2), '%')
st.write('La tasa de interes trimestral es: ', round(tasa_trimestral*100,2), '%')
st.write('La tasa de interes semestral es: ', round(tasa_semestral*100,2), '%')
st.write('La tasa de interes anual es: ', round(Tasa_anual*100,2), '%')


# col1, col2 = st.columns([2,2])

# with col1:
#     st.pyplot(plot_two_histograms(variable, variables))
# with col2:
#     st.pyplot(plot_two_series(variable, variables))