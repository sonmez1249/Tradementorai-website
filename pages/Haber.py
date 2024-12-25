import streamlit as st
import requests

# NewsAPI anahtarınızı buraya ekleyin
api_key = "dc482f4ae1fc4005bd3b6887d20e8c90"

# Sayfa yapılandırması (ikon eklendi)
st.set_page_config(
    page_title="Türkçe Haber Başlıkları",
    page_icon="pages//images//Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ile genel tasarım ve sidebar tasarımı
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

    /* Başlık tasarımı */
    h1, h2 {
        color: #7289da; /* Başlık mavi tonu */
        text-align: center; /* Ortalanmış başlık */
    }

    /* Kesikli çizgi */
    .dashed-line {
        border-top: 1px dashed #7289da; /* Kesikli çizgi rengi pastel mavi */
        margin: 15px 0; /* Üst ve alt boşluk */
    }

    /* Linkler */
    a {
        color: #faa61a; /* Sarı linkler */
        text-decoration: none; /* Alt çizgi kaldır */
    }

    a:hover {
        color: #f1c40f; /* Hover renginde açık sarı */
    }

    /* Haber başlıkları */
    .news-title {
        font-size: 20px;
        font-weight: bold;
        color: #f0b90b; /* Sarı başlıklar */
        text-align: center;
    }

    /* Haber açıklamaları */
    .news-description {
        font-size: 16px;
        color: #ffffff; /* Beyaz açıklama yazısı */
        text-align: center;
    }

    /* Yayın tarihi */
    .news-date {
        font-size: 14px;
        color: #aaaaaa; /* Gri yayın tarihi */
        text-align: center;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit ile başlık ve arama terimi almak
st.markdown('<h1>Türkçe Haber Başlıkları</h1>', unsafe_allow_html=True)
query = st.text_input('Arama Terimi Girin:', 'Teknoloji')

# API'yi çağırma ve haberleri çekme fonksiyonu
def get_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&language=tr&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

# Haberleri çekme ve gösterme
if query:
    news_data = get_news(query)

    if news_data['status'] == 'ok':
        articles = news_data['articles']

        # Başlıkları listele
        for article in articles[:10]:  # İlk 10 haberi göster
            st.markdown(f'<div class="news-title">{article["title"]}</div>', unsafe_allow_html=True)  # Haber başlığı
            st.markdown(f'<div class="news-date">Yayın Tarihi: {article["publishedAt"]}</div>', unsafe_allow_html=True)  # Yayın tarihi
            st.markdown(f'<div class="news-description">{article["description"]}</div>', unsafe_allow_html=True)  # Haber açıklaması
            st.markdown(f'<div style="text-align:center;"><a href="{article["url"]}">Detaylar için tıklayın</a></div>', unsafe_allow_html=True)  # Link
            st.markdown('<div class="dashed-line"></div>', unsafe_allow_html=True)  # Kesikli çizgi
    else:
        st.error("Haberler alınırken bir hata oluştu.")



