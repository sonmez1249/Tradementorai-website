import streamlit as st
import yfinance as yf
from datetime import datetime
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import os

# Başlık ve ayarlar
TITLE = "VERİ GÖRSELLEŞTİRME"
st.set_page_config(
    page_title="TraderMentorAI",
    page_icon="images\\Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",  # İkon dosya yolu
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ile genel tasarım ve sidebar tasarımı
custom_css = """
<style>
    body {
        background-color: #2c2f33; /* Koyu gri arka plan */
        color: #ffffff; /* Beyaz yazılar */
    }

    [data-testid="stSidebar"] {
        background-color: #23272a; /* Sidebar arka planı */
        padding: 20px;
        color: white; /* Sidebar yazıları beyaz */
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #faa61a; /* Başlıklar sarı */
        text-align: center;
    }
    [data-testid="stSidebar"] a {
        color: white; /* Linkler beyaz */
        text-decoration: none;
        font-weight: bold;
        margin: 10px 0;
    }
    [data-testid="stSidebar"] a:hover {
        color: #7289da; /* Hover durumunda pastel mavi */
    }
    [data-testid="stSidebar"] .sidebar-item {
        background-color: #7289da; /* Seçenek arka plan rengi */
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 10px;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    [data-testid="stSidebar"] .sidebar-item:hover {
        background-color: #f1c40f; /* Hover durumunda sarı */
        transform: scale(1.05); /* Hafif büyüme efekti */
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: #7289da;'>{TITLE}</h1>", unsafe_allow_html=True)

# Kripto para sembolleri ve logo URL'leri
crypto_info = {
    "Bitcoin": {"symbol": "BTC-USD", "logo": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"},
    "Ethereum": {"symbol": "ETH-USD", "logo": "https://assets.coingecko.com/coins/images/279/large/ethereum.png"},
    "Binance Coin": {"symbol": "BNB-USD", "logo": "https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png"},
    "Ripple": {"symbol": "XRP-USD", "logo": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png"},
    "Cardano": {"symbol": "ADA-USD", "logo": "https://assets.coingecko.com/coins/images/975/large/cardano.png"},
    "Dogecoin": {"symbol": "DOGE-USD", "logo": "https://assets.coingecko.com/coins/images/5/large/dogecoin.png"},
    "Polygon": {"symbol": "MATIC-USD", "logo": "https://assets.coingecko.com/coins/images/4713/large/matic-token-icon.png"},
    "Solana": {"symbol": "SOL-USD", "logo": "https://assets.coingecko.com/coins/images/4128/large/solana.png"},
    "Toncoin": {"symbol": "TON-USD", "logo": "https://assets.coingecko.com/coins/images/17980/large/ton_symbol.png"},
    "Shiba Inu": {"symbol": "SHIB-USD", "logo": "https://assets.coingecko.com/coins/images/11939/large/shiba.png"},
    "Stellar": {"symbol": "XLM-USD", "logo": "https://assets.coingecko.com/coins/images/100/large/Stellar_symbol_black_RGB.png"},
    "Litecoin": {"symbol": "LTC-USD", "logo": "https://assets.coingecko.com/coins/images/2/large/litecoin.png"},
    "Binance USD": {"symbol": "BUSD-USD", "logo": "https://assets.coingecko.com/coins/images/9576/large/BUSD.png"},
    "Polkadot": {"symbol": "DOT-USD", "logo": "https://assets.coingecko.com/coins/images/12171/large/polkadot.png"},
    "Tron": {"symbol": "TRX-USD", "logo": "https://assets.coingecko.com/coins/images/1094/large/tron-logo.png"},
    "Avalanche": {"symbol": "AVAX-USD", "logo": "https://assets.coingecko.com/coins/images/12559/large/coin-round-red.png"},
    "Chainlink": {"symbol": "LINK-USD", "logo": "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png"}
}

# Fonksiyon: Kripto para grafiği çizme
def plot_crypto_chart(symbol, start_date, end_date, chart_type):
    data = yf.download(symbol, start=start_date, end=end_date)
    if data.empty:
        st.error("Seçilen tarih aralığında veri bulunamadı.")
        return data

    plt.figure(figsize=(10, 6))
    if chart_type == "Line":
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.title(f"{symbol} Line Grafik")
    elif chart_type == "Bar":
        plt.bar(data.index, data['Close'], label='Close Price', color='orange', width=0.8)
        plt.title(f"{symbol} Bar Grafik")
    elif chart_type == "Scatter":
        plt.scatter(data.index, data['Close'], label='Close Price', alpha=0.7, color='green')
        plt.title(f"{symbol} Scatter Grafik")

    plt.xlabel("Tarih")
    plt.ylabel("Fiyat (USD)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    return data

# Yan menüde filtreleme seçenekleri
st.sidebar.header("Filtreleme Seçenekleri")

# Kripto para seçimi
coin_name = st.sidebar.selectbox("Bir Kripto Para Seçin", list(crypto_info.keys()))
symbol = crypto_info[coin_name]["symbol"]
logo_url = crypto_info[coin_name]["logo"]

# Tarih aralığı seçimi
start_date = st.sidebar.date_input("Başlangıç Tarihi", datetime(2021, 1, 1))
end_date = st.sidebar.date_input("Bitiş Tarihi", datetime.now())

# Grafik türü seçimi
chart_type = st.sidebar.selectbox("Grafik Türü Seçin", ["Line", "Bar", "Scatter"])

# Logo gösterimi
try:
    response = requests.get(logo_url)
    logo = Image.open(BytesIO(response.content))
    st.sidebar.image(logo, width=80)
except Exception as e:
    st.sidebar.warning(f"{coin_name} için logo yüklenemedi. Hata: {e}")

# Grafik çizme ve veri çekme
st.markdown(f"<h2 style='text-align: center; color: #7289da;'>{coin_name} Grafikleri</h2>", unsafe_allow_html=True)
data = plot_crypto_chart(symbol, start_date, end_date, chart_type)

# Veri setini gösterme
if not data.empty:
    st.markdown(f"<h2 style='color: #7289da;'>{coin_name} Veri Setleri</h2>", unsafe_allow_html=True)
    st.dataframe(data[['Close']], use_container_width=True)  # Sadece ilgili sütunları göster
else:
    st.error(f"{coin_name} için veri bulunamadı.")

# İletişim baloncuğu
def contact_bubble():
    st.markdown(
        """
        <style>
        .contact-bubble {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #faa61a;
            color: white;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            font-size: 20px;
            text-decoration: none;
        }

        .contact-bubble:hover {
            transform: scale(1.1);
            background-color: #f1c40f;
        }
        </style>
        <a class="contact-bubble" href="https://servispy-2etfjh5ephbuz2qeltdvsk.streamlit.app/" target="_blank">
            📞
        </a>
        """,
        unsafe_allow_html=True
    )

contact_bubble()








