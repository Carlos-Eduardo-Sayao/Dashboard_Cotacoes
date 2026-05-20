# Exchange Rate Dashboard

Interactive web application developed with **Python + Streamlit** for **real-time exchange rate consultation**, currency conversion, and simplified historical data visualization.

The data is consumed through the public **AwesomeAPI**, allowing users to quickly follow the foreign exchange market in a simple and intuitive way.

---

## Features

### Exchange Rate Monitor
Check the current exchange rate between two selected currencies.

Example:

- USD → BRL
- EUR → USD
- GBP → JPY

Displays:

- current exchange rate
- percentage variation (`pctChange`)
- date/time of the latest API update

---

### Currency Converter
Allows converting values between different currencies automatically.

Example:

```text
100 USD → BRL
Result: R$ 562.30
```

---

### Simplified History
Check the exchange rate history of the last few days for a currency pair.

Displays:

- Exchange date
- Value (`bid`)
- Percentage variation

---

## Technologies used

- **Python**
- **Streamlit**
- **Pandas**
- **Requests**
- **AwesomeAPI (Finance)**

---

## 📂 Project structure

```bash
Dashboard_Cotacoes/
│
├── app.py               # Main Streamlit interface
├── api_financeira.py    # API integration functions
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## API used

Data obtained from the public API:

**AwesomeAPI**

Documentation: https://docs.awesomeapi.com.br/api-de-moedas


Endpoints used:

```bash
https://economia.awesomeapi.com.br/json/last/
https://economia.awesomeapi.com.br/json/daily/
```

---

## How to install

### 1. Clone the repository

```bash
git clone https://github.com/Carlos-Eduardo-Sayao/Dashboard_Cotacoes.git
```

---

### 2. Enter the project folder

```bash
cd Dashboard_Cotacoes
```

---

### 3. Create a virtual environment

```bash
python -m venv venv
```

---

### 4. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## How to run

Start the application with:

```bash
streamlit run app.py
```

Then open it in the browser:

```bash
http://localhost:8501
```

---

## Available currencies

Currently the system supports:

- USD — US Dollar
- EUR — Euro
- GBP — British Pound
- JPY — Japanese Yen
- BRL — Brazilian Real
- CAD — Canadian Dollar

---

## Interface

The dashboard has three main tabs:

### Tab 1 — Exchange Rate
Current exchange rate monitoring.

### Tab 2 — Converter
Instant value conversion.

### Tab 3 — History
Table with simplified exchange rate history.

---

## Main dependencies

```txt
streamlit
pandas
requests
```

Manual installation:

```bash
pip install streamlit pandas requests
```

---

## Author

**Carlos Eduardo Sayão Santana Junior**

GitHub: https://github.com/Carlos-Eduardo-Sayao
