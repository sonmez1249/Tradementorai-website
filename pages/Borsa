import streamlit as st
import datetime
import yfinance as yf
import requests

# Sayfa yapılandırması (ikon eklendi)
st.set_page_config(
    page_title="Hisse Senedi Haberleri",
    page_icon="images//Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ile tasarım
custom_css = """
<style>
    /* Sayfa arka planı */
    body {
        background-color: #2c2f33; /* Koyu gri arka plan */
        color: #ffffff; /* Beyaz yazılar */
    }

    /* Sidebar tasarımı */
    [data-testid="stSidebar"] {
        background-color: #23272a; /* Sidebar arka planı */
        padding: 20px;
        color: white; /* Yazılar beyaz */
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

    /* Başlıklar */
    h1, h2, h3 {
        text-align: center;
        color: #7289da; /* Pastel mavi tonlu başlıklar */
    }

    /* Veri tabloları */
    .stDataFrame {
        background-color: #40444b; /* Tablo arka planı */
        color: #ffffff; /* Tablo yazıları beyaz */
        border-radius: 10px; /* Kenar yumuşatma */
        border: 1px solid #7289da; /* Kenarlık */
    }

    /* Haber başlıkları */
    .news-title {
        color: #faa61a; /* Sarı başlıklar */
        font-weight: bold;
        font-size: 20px;
        text-align: center; /* Başlıklar ortalanır */
        margin-bottom: 10px;
    }

    /* Haber açıklaması */
    .news-description {
        color: #ffffff; /* Beyaz açıklama */
        font-size: 16px;
        text-align: justify; /* Metin düzenli hizalama */
        margin: 10px auto;
        line-height: 1.6;
        width: 80%;
    }

    /* Yayın tarihi */
    .news-date {
        color: #ffffff; /* Beyaz tarih */
        font-size: 14px;
        text-align: center; /* Tarihi ortala */
        margin-bottom: 10px;
    }

    /* Haber ayırıcı çizgi */
    .news-divider {
        border-top: 2px dashed #7289da; /* Kesikli mavi çizgi */
        margin: 20px auto;
        width: 80%;
    }

    /* Linkler */
    a {
        color: #faa61a; /* Sarı renk link */
        text-decoration: none; /* Alt çizgi kaldır */
    }

    a:hover {
        color: #f1c40f; /* Hover renginde açık sarı */
    }

    /* İletişim baloncuğu */
    .contact-bubble {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #faa61a; /* Sarı arka plan */
        color: white; /* Yazı rengi */
        border-radius: 50%; /* Yuvarlak şekil */
        width: 50px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        cursor: pointer;
        font-size: 20px;
        text-decoration: none;
        transition: transform 0.2s ease-in-out;
    }
    .contact-bubble:hover {
        transform: scale(1.1); /* Hover durumunda büyütme */
        background-color: #f1c40f; /* Hover'da açık sarı */
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# NewsAPI anahtarınız
api_key = "dc482f4ae1fc4005bd3b6887d20e8c90"

# Kullanıcıdan sembol ve tarih bilgilerini al
symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value='GOOGL')
st.markdown(f'<h1>{symbol} Hisse Senedi Grafiği</h1>', unsafe_allow_html=True)

start_date = st.sidebar.date_input('Başlangıç tarihi', value=datetime.datetime(2020, 1, 1))
end_date = st.sidebar.date_input('Bitiş tarihi', value=datetime.datetime.now())

# Haberleri sadece bir kez çekme
news_data = None
if symbol:
    news_url = f'https://newsapi.org/v2/everything?q={symbol}&language=tr&apiKey={api_key}'
    response = requests.get(news_url)
    if response.status_code == 200:
        news_data = response.json()

# Verileri indir
df = yf.download(symbol, start=start_date, end=end_date)

# Grafik ve tablo
st.markdown('<h2>Hisse Senedi Grafiği</h2>', unsafe_allow_html=True)
st.line_chart(df['Close'], use_container_width=True)

st.markdown('<h2>Hisse Senedi Fiyatlar Tablosu</h2>', unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

# Haberler
st.markdown(f'<h2>{symbol} Hakkındaki Türkçe Haberler</h2>', unsafe_allow_html=True)
if news_data and 'articles' in news_data:
    for article in news_data['articles'][:5]:
        st.markdown(f'<p class="news-title">{article["title"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="news-description">{article["description"]}</p>', unsafe_allow_html=True)

# İletişim Baloncuğu
def contact_bubble():
    st.markdown(
        """
        <a class="contact-bubble" href="https://servispy-2etfjh5ephbuz2qeltdvsk.streamlit.app/" target="_blank">
            📞
        </a>
        """,
        unsafe_allow_html=True
    )
contact_bubble()









