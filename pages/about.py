import streamlit as st

def show_about():
    # ===== HEADER =====
    st.markdown("""
        <div class="about-header">
            <div class="about-icon">📊</div>
            <h1 class="about-title">Tentang Aplikasi</h1>
            <p class="about-subtitle">Analisis Faktor Ekonomi dan Pengaruhnya terhadap IPK Mahasiswa</p>
        </div>
    """, unsafe_allow_html=True)

    # ===== INTRO SECTION =====
    st.markdown("""
        <div class="about-desc-card">
            <p class="adc-text">
                Aplikasi ini dibuat untuk membantu memahami bagaimana kondisi ekonomi mahasiswa 
                dapat berpengaruh terhadap capaian IPK. Sistem memanfaatkan algoritma 
                <strong>Random Forest Regression</strong> untuk menganalisis pola dan 
                menemukan variabel ekonomi yang paling berperan dalam memengaruhi performa akademik.
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
                <li>Menyediakan alat analisis sederhana berbasis machine learning.</li>
                <li>Memberikan gambaran hubungan antara ekonomi dan IPK.</li>
                <li>Menyajikan visualisasi yang mudah dibaca dan informatif.</li>
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
        {"name": "Nama Anggota 1", "nim": "NIM001", "icon": "🧑‍💻"},
        {"name": "Nama Anggota 2", "nim": "NIM002", "icon": "🧑‍💻"},
        {"name": "Nama Anggota 3", "nim": "NIM003", "icon": "🧑‍💻"},
    ]

    cols = st.columns(len(team_members))
    for idx, m in enumerate(team_members):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <div class="team-avatar">{m['icon']}</div>
                    <div class="team-name">{m['name']}</div>
                    <div class="team-nim">{m['nim']}</div>
                </div>
            """, unsafe_allow_html=True)

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
            <p>© 2025 Proyek Analisis Faktor Ekonomi dan IPK</p>
        </div>
    """, unsafe_allow_html=True)
