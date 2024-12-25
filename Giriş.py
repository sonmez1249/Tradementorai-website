import streamlit as st
from PIL import Image

TITLE = "Trade Mentor AI'a Hoşgeldiniz"

# Page configuration with updated icon
st.set_page_config(
    page_title="TradeMentorAI",
    page_icon="images\\Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",  # İkon için görsel yolu
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# CSS ile genel tasarım
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #2c2f33, #5865f2); /* Gradient arka plan */
        color: white; /* Yazı rengi */
    }
    h1 {
        color: #7289da; /* Sarı başlık */
        text-align: center; /* Ortalanmış başlık */
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .contact-section {
        background-color: #23272a; /* Koyu gri kutu arka planı */
        padding: 30px;
        border-radius: 15px;
        margin: 30px auto;
        text-align: center;
        width: 60%; /* Daha dar genişlik */
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.4); /* Hafif gölge efekti */
    }
    .contact-section h2 {
        color: #faa61a; /* Sarı alt başlık */
        font-size: 28px;
        margin-bottom: 20px;
    }
    .contact-details {
        font-size: 18px;
        line-height: 1.8; /* Daha rahat okuma için satır aralığı */
        color: #ffffff; /* Yazı rengi beyaz */
    }
    .contact-details strong {
        color: #f1c40f; /* Sarı vurgulama */
    }
    .footer {
        text-align: center; /* Ortalanmış metin */
        margin-top: 40px;
        font-size: 14px;
        color: #aaaaaa; /* Hafif gri metin */
    }
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
    </style>
    """,
    unsafe_allow_html=True
)

# Başlık
st.markdown(f"<h1>{TITLE}</h1>", unsafe_allow_html=True)

# Görüntü yükleme ve gösterme
image_path = "images\\Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg"
image = Image.open(image_path)
image = image.resize((300, 300))  # Görsel boyutunu küçültme

# Görüntüyü ortalamak için sütunlar
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(image, caption="Kripto Dünyasına Hoş Geldiniz", use_column_width=False)

# İletişim bilgileri bölümü
st.markdown(
    """
    <div class="contact-section">
        <h2>İletişim Bilgileri</h2>
        <p class="contact-details">
            <strong>Telefon Numarası:</strong> +90 555 123 4567<br>
            <strong>E-posta:</strong> info@tradementorai.com<br>
            <strong>Adres:</strong> Büyükdere Caddesi No:123, Maslak, İstanbul<br>
            <strong>Merkez Adresi:</strong> Trade Mentor AI Merkezi, İstanbul, Türkiye
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# İletişim baloncuğu
def contact_bubble():
    st.markdown(
        """
        <style>
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
            transform: scale(1.1); /* Hover büyütme efekti */
            background-color: #f1c40f; /* Hover'da açık sarı */
        }
        </style>
        <a class="contact-bubble" href="https://servispy-2etfjh5ephbuz2qeltdvsk.streamlit.app/" target="_blank">
            📞
        </a>
        """,
        unsafe_allow_html=True
    )

# İletişim baloncuğunu göster
contact_bubble()

# Footer
st.markdown(
    """
    <div class="footer">
        <p>&copy; 2024 Trade Mentor AI. Tüm Hakları Saklıdır.</p>
    </div>
    """,
    unsafe_allow_html=True
)



