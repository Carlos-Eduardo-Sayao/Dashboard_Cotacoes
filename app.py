import streamlit as st
import pandas as pd
from api_financeira import *

st.set_page_config(layout="centered")
st.title("Dashboard Interativo de Cotações Cambiais")

aba1 , aba2 , aba3= st.tabs(["Câmbio","Conversor","Histórico"])

with aba1:
    st.title("Monitor de Cotação")
    col1 , col2 = st.columns(2)
    moedas_disponiveis = ["USD","EUR","GBP","JPY","BRL","CAD"]
    simbolos = {"BRL": "R$","USD": "$","EUR": "€","GBP": "£","JPY": "¥","CAD": "C$"}
    with col1:
        moeda_origem = st.selectbox("Moeda Origem",moedas_disponiveis,index=0,key="origem_aba1")
    with col2:
        moeda_destino =st.selectbox("Moeda Destino",moedas_disponiveis,index=1,key="destino_aba1")
    
    if st.button("Obter Cotação Atual"):
        st.markdown("---")
        cotacao = cotacao_atual(moeda_origem,moeda_destino)
        dados_par_moeda = dados_api(moeda_origem,moeda_destino)
        simbolo_destino = simbolos[moeda_destino]
        st.subheader("Resultado da Cotação:")
        st.metric("",f"1 {moeda_origem} = {simbolo_destino}{cotacao:.4f}",delta=dados_par_moeda['pctChange'])
        st.info(f"Dados atualizados na API em:{dados_par_moeda['create_date']}")

     
with aba2:
    st.title("Conversor de Moedas Simples")
    moedas_disponiveis = ["USD","EUR","GBP","JPY","BRL","CAD"]
    simbolos = {"BRL": "R$","USD": "$","EUR": "€","GBP": "£","JPY": "¥","CAD": "C$"}
    col3 , col4 , col5 = st.columns(3)
    with col3:
        moeda_origem = st.selectbox("Moeda Origem",moedas_disponiveis,index=0,key="origem_aba2")
    with col4:
        moeda_destino = st.selectbox("Moeda Destino",moedas_disponiveis,index=1,key="destino_aba2")
    with col5:
        valor_converter = st.number_input(
            label="Valor a Converter",
            min_value=1.00,
            value=100.00
        )

    st.write("Configurações atuais:")
    simbolo_origem = simbolos[moeda_origem]
    simbolo_destino = simbolos[moeda_destino]
    st.text(f"De {moeda_origem.upper()} | Para {moeda_destino.upper()} | Valor:{simbolo_origem}{valor_converter}")
    if st.button("Realizar Conversão"):
        st.markdown("---")
        
        cotacao = cotacao_atual(moeda_origem,moeda_destino)
        resultado = converter_moeda(valor_converter,moeda_origem,moeda_destino)
        st.markdown(f"**{simbolo_origem}{valor_converter:.2f}** para **{moeda_destino}**")
        st.subheader(f"{simbolo_destino}{resultado:.2f}")

with aba3:
    st.title("Histórico Simplificado")
    pares_moedas_disponivies = [
        'USD-EUR', 'USD-GBP', 'USD-JPY', 'USD-BRL', 'USD-CAD',          
        'EUR-USD', 'EUR-GBP', 'EUR-JPY', 'EUR-BRL', 'EUR-CAD',
        'GBP-USD', 'GBP-EUR', 'GBP-JPY', 'GBP-BRL', 'GBP-CAD',
        'JPY-USD', 'JPY-EUR', 'JPY-GBP', 'JPY-BRL', 'JPY-CAD',
        'BRL-USD', 'BRL-EUR', 'BRL-GBP', 'BRL-JPY', 'BRL-CAD',
        'CAD-USD', 'CAD-EUR', 'CAD-GBP', 'CAD-JPY', 'CAD-BRL'
    ]
    par_moedas = st.selectbox("Par de Moedas(EX:USD-BRL):",pares_moedas_disponivies,index=0)
    dias = st.slider("Número de Dias:",min_value=1,max_value=10)
    historico = historico_simples(dias,par_moedas)

    if par_moedas:
        df = pd.DataFrame(historico)
        df["create_date"] = df["create_date"].fillna(df["create_date"].iloc[0])
        df_display = df[["create_date","bid","pctChange"]]
        df_display.colums = ["Data","Cotação(Bid)","Variação (%)"]

        st.dataframe(df_display,use_container_width=True)