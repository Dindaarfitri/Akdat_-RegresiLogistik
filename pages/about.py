import streamlit as st
import base64

def get_img_as_base64(file_path):
    """Konversi gambar lokal ke string Base64 dan kembalikan Data URL."""
    try:
        # Buka file dalam mode biner (rb)
        with open(file_path, "rb") as f:
            # Encode Base64 dan decode ke string
            img_bytes = f.read()
            base64_encoded = base64.b64encode(img_bytes).decode()
            
            # Mendapatkan jenis file (misalnya 'jpeg')
            file_extension = file_path.split('.')[-1]
            
            # Kembalikan Data URL
            return f"data:image/{file_extension};base64,{base64_encoded}"
            
    except FileNotFoundError:
        # Jika file tidak ditemukan, kembalikan string kosong atau URL placeholder
        st.warning(f"File gambar tidak ditemukan: {file_path}")
        return "" # Mengembalikan string kosong akan mencegah gambar ditampilkan
    except Exception as e:
        st.error(f"Error saat memproses gambar {file_path}: {e}")
        return ""


def show_about():
    # ===== HEADER =====
    st.markdown("""
        <div class="about-header">
            <div class="about-icon">📊</div>
            <h1 class="about-title">Tentang Aplikasi</h1>
            <p class="about-subtitle">
                Analisis Pengaruh Media Sosial dan Durasi Tidur terhadap Prestasi Akademik Mahasiswa
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ===== INTRO SECTION =====
    st.markdown("""
        <div class="about-desc-card">
            <p class="adc-text">
                Aplikasi ini dikembangkan untuk menganalisis bagaimana 
                <strong>penggunaan media sosial</strong> dan 
                <strong>durasi tidur</strong> berpengaruh terhadap 
                <strong>prestasi akademik mahasiswa</strong>.
                <br><br>
                Sistem ini menggunakan pendekatan statistik 
                <strong>Regresi Logistik</strong>, yang sesuai untuk memodelkan
                variabel target bersifat kategorikal, seperti prestasi akademik
                (baik atau tidak baik), serta untuk melihat peluang dan arah
                pengaruh dari setiap faktor yang dianalisis.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ===== PURPOSE =====
    st.markdown("""
        <div class="team-header">
            <span class="team-h-icon">🎯</span>
            <span class="team-h-title">Tujuan Pengembangan</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="about-desc-card">
            <ul class="adc-text">
                <li>Menganalisis pengaruh penggunaan media sosial terhadap prestasi akademik mahasiswa.</li>
                <li>Menganalisis hubungan durasi tidur dengan capaian akademik mahasiswa.</li>
                <li>Menyediakan model prediksi prestasi akademik berbasis regresi logistik.</li>
                <li>Menyajikan visualisasi dan hasil analisis yang mudah dipahami.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # ===== TEAM SECTION =====
    st.markdown("""
        <div class="team-header">
            <span class="team-h-icon">👨‍🏫</span>
            <span class="team-h-title">Pengembang</span>
        </div>
    """, unsafe_allow_html=True)

    team_members = [
        {"name": "Annisa Revalina Harahap", "nim": "2311521001", "image": "images/annisa.jpeg"},
        {"name": "Dinda Arfitri", "nim": "2311521002", "image": "images/dinda.jpeg"},
        {"name": "Velisa Dwi Sonia", "nim": "2311522039", "image": "images/velisa.jpeg"},
    ]

    cols = st.columns(len(team_members))
    
    for idx, m in enumerate(team_members):
        # MENGGUNAKAN FUNGSI BARU UNTUK MENDAPATKAN DATA URL BASE64
        data_url = get_img_as_base64(m['image'])
        
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <div class="team-avatar-container">
                        <img src="{data_url}" alt="{m['name']}" class="team-avatar-img">
                    </div> 
                    <div class="team-name">{m['name']}</div>
                    <div class="team-nim">{m['nim']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # KODE TRY-EXCEPT UNTUK CEK FILE DIHAPUS KARENA SUDAH DIHANDLE OLEH FUNGSI DI ATAS
            # if data_url == "":
            #     st.warning(f"Bingkai {m['name']} muncul, tapi foto hilang karena FileNotFoundError!")
            

    # ===== TECH =====
    st.markdown("""
        <div class="tech-header">
            <span class="tech-h-icon">⚙️</span>
            <span class="tech-h-title">Teknologi Utama</span>
        </div>
    """, unsafe_allow_html=True)

    tech_cols = st.columns(4)
    techs = [
        ("Python", "🐍"),
        ("Streamlit", "💻"),
        ("Scikit-Learn", "🤖"),
        ("Pandas", "🐼")
    ]

    for i, (name, icon) in enumerate(techs):
        with tech_cols[i]:
            st.markdown(f"""
                <div class="tech-card">
                    <div class="tech-icon">{icon}</div>
                    <div class="tech-name">{name}</div>
                </div>
            """, unsafe_allow_html=True)

    # ===== FOOTER =====
    st.markdown("""
        <div class="about-footer">
            <p>© 2025 | Analisis Pengaruh Media Sosial dan Durasi Tidur terhadap Prestasi Akademik Mahasiswa</p>
        </div>
    """, unsafe_allow_html=True)