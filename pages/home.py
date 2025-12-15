import streamlit as st
import base64
from pathlib import Path

def show_home():
    """
    Halaman Beranda (Home)
    Analisis Pengaruh Media Sosial terhadap Prestasi Akademik Mahasiswa
    menggunakan Regresi Logistik
    """

    # =====================================================
    # 1. LOAD LOGO
    # =====================================================
    logo_path = Path("static/logo.png")
    logo_css_style = (
        "width: 50px; height: 50px; margin-right: 15px; "
        "vertical-align: middle; border-radius: 8px;"
    )

    logo_html = '<span style="font-size: 3rem; margin-right: 15px;">📱</span>'
    if logo_path.exists():
        try:
            with open(logo_path, "rb") as img_file:
                logo_base64 = base64.b64encode(img_file.read()).decode()
            logo_html = (
                f'<img src="data:image/png;base64,{logo_base64}" '
                f'style="{logo_css_style}" alt="Logo">'
            )
        except Exception:
            pass

    # =====================================================
    # 2. HERO SECTION
    # =====================================================
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown(f"""
        <h1 class="hero-title" style="text-align: center !important;">
            {logo_html}
            Analisis Pengaruh Penggunaan Media Sosial dan Durasi Tidur terhadap Prestasi Akademik Mahasiswa Menggunakan Regresi Logistik
        </h1>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # 3. TENTANG APLIKASI
    # =====================================================
    st.markdown("""
        <div class="intro-section">
            <h3 style="color: #2980b9; margin-top: 0;">Tentang Aplikasi</h3>
            <p class="intro-text">
                Aplikasi ini bertujuan untuk menganalisis bagaimana 
                <strong>penggunaan media sosial</strong> dan 
                <strong>durasi tidur</strong> berpengaruh terhadap 
                <strong>prestasi akademik mahasiswa</strong>.
                <br><br>
                Analisis dilakukan menggunakan pendekatan statistik 
                <strong>Regresi Logistik</strong>, yang sesuai untuk
                memodelkan variabel target bersifat kategori 
                (prestasi akademik baik atau tidak).
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # 4. TUJUAN PENGEMBANGAN
    # =====================================================
    st.markdown(
        '<h2 class="section-title" style="text-align: center; color: #2c3e50;">🎯 Tujuan Pengembangan</h2>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Analisis Hubungan</h3>
                <p class="feature-desc">
                    Menganalisis hubungan antara durasi media sosial,
                    durasi tidur, dan karakteristik mahasiswa
                    terhadap prestasi akademik.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <h3 class="feature-title">Pendekatan Statistik</h3>
                <p class="feature-desc">
                    Menggunakan regresi logistik untuk menguji
                    signifikansi dan arah pengaruh setiap variabel.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3 class="feature-title">Prediksi Akademik</h3>
                <p class="feature-desc">
                    Memprediksi peluang prestasi akademik mahasiswa
                    berdasarkan kebiasaan dan karakteristiknya.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # 5. ALUR PENGGUNAAN
    # =====================================================
    st.markdown(
        '<h2 class="section-title" style="text-align: center; color: #2c3e50;">🧭 Alur Penggunaan Aplikasi</h2>',
        unsafe_allow_html=True
    )

    st.markdown("""
    1. **Upload Dataset**  
       Mengunggah data survei mahasiswa dalam format CSV.

    2. **Preprocessing Data**  
       Membersihkan data dari duplikasi dan nilai kosong.

    3. **Analisis Data**  
       Menganalisis hubungan antar variabel menggunakan tabel proporsi dan korelasi.

    4. **Visualisasi & Modeling**  
       Melatih model regresi logistik dan mengevaluasi performanya.

    5. **Prediksi Prestasi Akademik**  
       Menghasilkan probabilitas prestasi akademik mahasiswa.
    """)

    st.markdown("<br>")
    st.markdown("---")

    # =====================================================
    # 6. FOOTER
    # =====================================================
    st.markdown("""
        <div style="text-align: center; color: #7f8c8d; font-size: 0.9em; padding: 10px 0;">
            © 2025 | Analisis Pengaruh Media Sosial terhadap Prestasi Akademik Mahasiswa
        </div>
    """, unsafe_allow_html=True)

    if st.button("Next: Upload Dataset ›", type="primary"):
        st.session_state["page"] = "Upload Dataset"
        st.rerun()
