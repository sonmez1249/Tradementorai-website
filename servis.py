import streamlit as st

# Sayfa yapılandırması (ikon eklendi)
st.set_page_config(
    page_title="İletişim Bilgileri",
    page_icon="Leonardo_Phoenix_Create_a_modern_sleek_logo_for_the_stock_trad_2.jpg",  # İkon dosya yolu
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ile genel ve sidebar tasarımı
custom_css = """
<style>
    body {
        background-color: #FFD700; /* Koyu gri arka plan */
        color: #ffffff; /* Beyaz yazılar */
    }
    
    /* Sidebar tasarımı */
    [data-testid="stSidebar"] {
        background-color: #23272a; /* Sidebar arka plan rengi */
        padding: 20px;
        color: white;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #faa61a; /* Sidebar başlık sarı */
        text-align: center;
    }
    [data-testid="stSidebar"] a {
        color: white; /* Sidebar link beyaz */
        text-decoration: none;
        font-weight: bold;
        margin: 10px 0;
    }
    [data-testid="stSidebar"] a:hover {
        color: #7289da; /* Hover pastel mavi */
    }
    [data-testid="stSidebar"] .sidebar-item {
        background-color: #7289da; /* Sidebar buton pastel mavi */
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
    
    h1 {
        color: #7289da; /* Pastel mavi başlık */
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    h2 {
        color: #f1c40f; /* Sarı alt başlık */
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .contact-info {
        background-color: #D4AF37; /* Pastel mavi kutu rengi */
        padding: 25px;
        border-radius: 15px; /* Daha yuvarlatılmış kenarlar */
        margin: 20px auto;
        text-align: center; /* İçeriği ortala */
        border: 2px solid #FFD700; /* Pastel mavi kenarlık */
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); /* Hafif gölge efekti */
        width: 80%; /* Daha dar genişlik */
        color: white;
    }
    .separator {
        border-top: 2px dashed #f1c40f; /* Sarı kesikli çizgi */
        margin: 20px auto;
        width: 80%;
    }
    input, textarea {
        background-color: #2c2f33; /* Kutucuk arka plan rengi */
        color: white; /* Yazılar beyaz */
        border: 1px solid #7289da; /* Kenarlık pastel mavi */
        border-radius: 10px; /* Daha yuvarlatılmış kenarlar */
        padding: 10px;
        width: 100%;
        box-sizing: border-box;
        margin-bottom: 15px;
    }
    input:focus, textarea:focus {
        outline: none;
        border: 2px solid #f1c40f; /* Sarı odak rengi */
    }
    button {
        background-color: #7289da;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    button:hover {
        background-color: #f1c40f;
        transform: translateY(-2px);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sayfa başlığı
st.markdown("<h1>İletişim Bilgilerimiz</h1>", unsafe_allow_html=True)

# İletişim bilgileri kutusu
st.markdown(
    """
   <div class="contact-info">
        <h2>Bize Ulaşın</h2>
        <p><strong>Telefon:</strong> +90 123 456 7890</p>
        <p><strong>E-posta:</strong> tradementorai@gmail.com</p>
        <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/Tradementorai</a></p>
        <p><strong>Twitter:</strong> <a href="https://twitter.com/yourhandle" target="_blank">@Tradementorai</a></p>
    </div>
    """, unsafe_allow_html=True
)

# Minimalist ayrım çizgisi
st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# İletişim formu için başlık
st.markdown("<h2>Alternatif olarak aşağıdaki formu doldurabilirsiniz:</h2>", unsafe_allow_html=True)

# İletişim formu
name = st.text_input("Adınız")
email = st.text_input("E-posta adresiniz")
message = st.text_area("Mesajınız")

# Gönderme butonu
if st.button("Gönder"):
    if name and email and message:
        st.success("Mesajınız başarıyla gönderildi! Teşekkür ederim.")
    else:
        st.error("Lütfen tüm alanları doldurun.")

