🇺🇸 **English version:** [Click here](https://github.com/Carlos-Eduardo-Sayao/Dashboard_Cotacoes/blob/main/README_EN.md)

# Dashboard de Cotações Cambiais

Aplicação web interativa desenvolvida em **Python + Streamlit** para consulta de **cotações cambiais em tempo real**, conversão entre moedas e visualização de histórico simplificado.

Os dados são consumidos através da API pública **AwesomeAPI**, permitindo acompanhar rapidamente o mercado de câmbio de forma simples e intuitiva.

---

## Funcionalidades

### Monitor de Cotação
Consulta a cotação atual entre duas moedas selecionadas.

Exemplo:

- USD → BRL
- EUR → USD
- GBP → JPY

Exibe:

- valor atual da cotação
- variação percentual (`pctChange`)
- data/hora da última atualização da API

---

### Conversor de Moedas
Permite converter valores entre diferentes moedas automaticamente.

Exemplo:

```text
100 USD → BRL
Resultado: R$ 562.30
```

---

### Histórico Simplificado
Consulta o histórico de cotação dos últimos dias para um par de moedas.

Exibe:

- Data da cotação
- Valor (`bid`)
- Variação percentual

---

## Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Requests**
- **AwesomeAPI (Economia)**

---

## Estrutura do projeto

```bash
Dashboard_Cotacoes/
│
├── app.py               # Interface principal Streamlit
├── api_financeira.py    # Funções de integração com API
├── requirements.txt     # Dependências
└── README.md            # Documentação
```

---

## API utilizada

Dados obtidos pela API pública:

**AwesomeAPI**

Documentação: https://docs.awesomeapi.com.br/api-de-moedas


Endpoints utilizados:

```bash
https://economia.awesomeapi.com.br/json/last/
https://economia.awesomeapi.com.br/json/daily/
```

---

## Como instalar

### 1. Clone o repositório

```bash
git clone https://github.com/Carlos-Eduardo-Sayao/Dashboard_Cotacoes.git
```

---

### 2. Entre na pasta do projeto

```bash
cd Dashboard_Cotacoes
```

---

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

---

### 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Como executar

Inicie a aplicação com:

```bash
streamlit run app.py
```

Depois abra no navegador:

```bash
http://localhost:8501
```

---

## Moedas disponíveis

Atualmente o sistema suporta:

- USD — Dólar Americano
- EUR — Euro
- GBP — Libra Esterlina
- JPY — Iene Japonês
- BRL — Real Brasileiro
- CAD — Dólar Canadense

---

## Interface

O dashboard possui três abas principais:

### Aba 1 — Câmbio
Monitoramento da cotação atual.

### Aba 2 — Conversor
Conversão instantânea de valores.

### Aba 3 — Histórico
Tabela com histórico simplificado das cotações.

---

## Dependências principais

```txt
streamlit
pandas
requests
```

Instalação manual:

```bash
pip install streamlit pandas requests
```

---

## Autor

**Carlos Eduardo Sayão Santana Junior**

GitHub: https://github.com/Carlos-Eduardo-Sayao



---

