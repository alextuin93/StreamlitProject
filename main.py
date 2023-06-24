import streamlit as st
import datetime


st.sidebar.title("Registre os seus plantões")

input_data = st.sidebar.date_input("Selecione o dia:", datetime.date.today())
input_setor = st.sidebar.selectbox("Select an option", ["UTI 1", "UTI 2", "UTI 3"])
input_turno = st.sidebar.selectbox(label="Selecione o turno:", options=["DIURNO", "MANHÃ", "TARDE", "NOITE", "DIURNO+NOITE", "TARDE+NOITE"])

if input_turno == "DIURNO":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 240
        else:
            input_valores = 220
elif input_turno == "MANHÃ":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 120
        else:
            input_valores = 110
elif input_turno == "TARDE":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 120
        else:
            input_valores = 110
elif input_turno == "NOITE":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 150
        else:
            input_valores = 120
elif input_turno == "DIURNO+NOITE":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 390
        else:
            input_valores = 340
elif input_turno == "TARDE+NOITE":
        dias_da_semana = input_data.weekday()
        if dias_da_semana  in [5, 6]:
            input_valores = 270
        else:
            input_valores = 230
        
input_button_submit = st.sidebar.button("Inserir", use_container_width=True)

if input_button_submit:
               

        dias_inteiros = input_data.strftime("%d/%m")

        dia_semana_atual = input_data.strftime("%A")

        st.sidebar.write(f'Dia: {dias_inteiros}')
        st.sidebar.write(f'Dia da semana: {dia_semana_atual}')
        st.sidebar.write(f'Setor: {input_setor}')
        st.sidebar.write(f'Turno: {input_turno}')
        st.sidebar.write(f'Valor: {input_valores}')



