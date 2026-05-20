import requests

def dados_api(moeda_origem,moeda_destino):
    url_base = "https://economia.awesomeapi.com.br/json/last/"
    url = url_base+moeda_origem+"-"+moeda_destino
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave_par_moeda = moeda_origem+moeda_destino
        dados_par_moeda = dados[chave_par_moeda]
        return dados_par_moeda
    else:
        return None

def cotacao_atual(moeda_origem,moeda_destino):
    url_base = "https://economia.awesomeapi.com.br/json/last/"
    url = url_base+moeda_origem+"-"+moeda_destino

    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave_par_moeda = moeda_origem+moeda_destino
        dados_par_moeda = dados[chave_par_moeda]
        valor_bid = float(dados_par_moeda["bid"])
        return valor_bid
    else:
        return 0

def converter_moeda(valor,moeda_origem,moeda_destino):
    taxa_cambio = cotacao_atual(moeda_origem,moeda_destino)
    if taxa_cambio > 0:
        valor_convertido = valor * taxa_cambio
        return valor_convertido
    else:
        return None

def historico_simples(dias,par_moeda):
    url = f"https://economia.awesomeapi.com.br/json/daily/{par_moeda}/{dias}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_historico = resposta.json()
        return dados_historico
    else:
        return []
    


    
