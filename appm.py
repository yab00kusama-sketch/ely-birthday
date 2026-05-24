import streamlit as st
import time

# Sayfa ayarlarımızı yapalım - Mor kalp ve uzaylı temasına uygun ikonlar
st.set_page_config(page_title="Bir mektubun var! 💌", page_icon="💜", layout="centered")

# Sayfa başlığı ve tatlı bir arka plan efekti için CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F3E5F5; /* Çok Açık Pastel Mor / Eflatun Arka Plan */
    }
    .ana-baslik {
        text-align: center; 
        color: #4A148C; /* Koyu Mor Başlık */
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem;
        font-weight: bold;
        padding: 20px;
    }
    .mesaj-kutusu {
        border: 2px solid #CE93D8; /* Açık Mor Çerçeve */
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 20px;
        background-color: #FFFFFF; /* Mesaj kutusunun içi beyaz kalsın ki yazılar rahat okunsun */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlığımızı ekrana basalım
st.markdown("<div class='ana-baslik'>BU SENİN İÇİN! <br> (o・ω・o) ✨</div>", unsafe_allow_html=True)

st.write("\n" * 2)

# Kullanıcıyı etkileşime sokacak buton
st.write("### 💌 Hadi butona tıkla!")

if st.button("✉️ Mektubunu aç", use_container_width=True):
    # --- YEREL MP3 DOSYASINDAN MÜZİK ÇALMA ---
    # İndirdiğin dosyanın tam adını buraya yazdık:
    audio_file = open('andriig-happy-birthday-471211.mp3', 'rb')
    audio_bytes = audio_file.read()

    # Butona basıldığı an müzik otomatik olarak çalmaya başlayacak
    st.audio(audio_bytes, format='audio/mp3', autoplay=True)
    # ----------------------------------------


    # Ekrana balonlar fırlatalım
    st.balloons()

    time.sleep(0.5)

    # Ekrana tatlı bir kutu içinde doğum günü mesajımızı ve uzaylı emojilerini getirelim
    st.markdown(
        """
        <div class='mesaj-kutusu'>
            <h2 style='color: #8E24AA;'>🎉 İYİ Kİ DOĞDUN! 🎉</h2>
            <p style='color: #4a4a4a; font-size: 1.2rem;'>
                Doğum günün kutlu olsun Ely! <br>
                Hayallerini gerçekleştirebildiğin bir gelecek dilerim <br>
                Artık bir yıl daha yaşlısın, hehe~~💫 <br>
                ♪ヽ(´▽｀)/ 
            </p>
            <p style='font-size: 2rem;'>👽🛸🚀👾⭐☄️</p>
        </div>
        """,
        unsafe_allow_html=True
    )
