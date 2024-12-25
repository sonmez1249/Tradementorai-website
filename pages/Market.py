import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time

# Streamlit sayfa ayarları
st.set_page_config(
    page_title="TraderMentorAI",
    page_icon="images\\Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an extremely cool app!"
    }
)

# CSS tasarımı
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #2c2f33, #5865f2); /* Gradient arka plan */
        color: white;
    }
    h1, h2, h3 {
        color: #faa61a; /* Başlık rengi */
        text-align: center;
    }
    .coin-box {
        background-color: #23272a; /* Kutu arka plan rengi */
        border-radius: 10px; /* Yuvarlak köşeler */
        padding: 15px;
        margin: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Hafif gölge efekti */
        text-align: center;
        color: white;
    }
    .coin-box img {
        margin-bottom: 10px;
    }
    .coin-box h4 {
        font-size: 18px;
        margin-bottom: 5px;
    }
    .coin-box p {
        margin: 5px 0;
    }
    /* Sidebar tasarımı */
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
    """,
    unsafe_allow_html=True
)

# Coin bilgilerini alma fonksiyonu
@st.cache_data(ttl=600)  # 10 dakika önbellekleme
def get_coin_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    coin_ids = [
        "bitcoin", "ethereum", "cardano", "binancecoin", "solana", "polygon",
        "dogecoin", "shiba-inu", "ripple", "toncoin", "matic-network", "binance-usd",
        "tron", "polkadot", "avalanche-2", "litecoin", "stellar", "chainlink"
    ]
    params = {
        "vs_currency": "usd",
        "ids": ",".join(coin_ids)
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [
            {
                "name": coin["name"],
                "price": coin["current_price"],
                "change_24h": coin["price_change_percentage_24h"],
                "volume_24h": coin["total_volume"],
                "logo": coin["image"]
            }
            for coin in data
        ]
    except requests.exceptions.RequestException as e:
        st.error(f"Veri alınırken hata oluştu: {e}")
        return None

# Güncel coin bilgilerini çekme ve gösterme
coin_data = get_coin_data()

if coin_data:
    st.markdown("<h1>Güncel Coin Fiyatları</h1>", unsafe_allow_html=True)

    # Coin bilgilerini grid formatında gösterme
    cols = st.columns(3)  # 3 sütun halinde gösterim
    for idx, coin in enumerate(coin_data):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="coin-box">
                    <img src="{coin['logo']}" alt="{coin['name']} logo" width="75">
                    <h4>{coin['name']}</h4>
                    <p>Fiyat: ${coin['price']:.2f}</p>
                    <p>24 Saatlik Değişim: <span style="color:{'red' if coin['change_24h'] < 0 else 'green'};">
                    {coin['change_24h']:.2f}%</span></p>
                    <p>24 Saatlik Hacim: ${coin['volume_24h']:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    time.sleep(0.5)  # Yükleme süresini kontrol etmek için ufak bir bekleme süresi






