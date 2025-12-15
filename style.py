import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.
    Tema: Deep Maroon & Gold (Royal Elegance)
    Peningkatan: Enhanced contrast, softer shadows, subtle hover animations.
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts - Poppins tetap yang terbaik */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        
        /* ===== COLOR PALETTE (Nuansa Merah Tua (Maroon) & Emas - Royal Elegance) ===== */
        :root {
            --bg-light-cream: #FFF5F7; /* Lightest Off-White/Pinkish Cream */
            --sidebar-cream: #A34057; /* Medium Deep Rose/Maroon Muda */
            --accent-gold: #800020; /* Deep Rich Maroon/Merah Tua Utama */
            --accent-orange: #C11B17; /* Bright Crimson/Merah yang lebih cerah/kontras */
            --text-dark: #200008; /* Very Dark Maroon/Hampir Hitam */
            --text-light: #ffffff;
            --shadow-soft: 0 10px 40px rgba(0, 0, 0, 0.15); /* Shadow lebih dalam tapi lembut */
        }
        
        /* Global Styles */
        * {
            font-family: 'Poppins', sans-serif;
            color: var(--text-dark); 
        }
        
        /* ===== BACKGROUND: MESH GRADIENT + DEPTH EFFECT (Warm Royal Tone) ===== */
        
        .main {
            background: 
                /* Mesh blob 1 - top left (Soft Pinkish Cream) */
                radial-gradient(ellipse at 10% 20%, rgba(163, 64, 87, 0.5) 0%, transparent 60%),
                /* Mesh blob 2 - center (Medium Crimson) */
                radial-gradient(ellipse at 50% 50%, rgba(193, 27, 23, 0.15) 0%, transparent 60%),
                /* Mesh blob 3 - top right (Light Cream) */
                radial-gradient(ellipse at 85% 15%, rgba(163, 64, 87, 0.8) 0%, transparent 55%),
                /* Mesh blob 4 - bottom left (Deep Maroon) */
                radial-gradient(ellipse at 15% 85%, rgba(128, 0, 32, 0.1) 0%, transparent 60%),
                /* Base gradient - Light Cream */
                linear-gradient(135deg, var(--bg-light-cream) 0%, #FFFAFB 100%);
            background-attachment: fixed;
            min-height: 100vh;
            position: relative;
        }
        
        /* Noise texture (dijadikan lebih halus) */
        .main::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
            opacity: 0.05; /* Lebih halus */
            pointer-events: none;
            z-index: 0;
        }
        
        .stApp {
            background: transparent;
        }
        
        /* Glass Panel Effect for Content Container (Glassmorphism lebih elegan) */
        .block-container {
            position: relative;
            z-index: 1;
            background: rgba(255, 255, 255, 0.98); /* Lebih solid */
            backdrop-filter: blur(10px); /* Blur lebih ringan */
            -webkit-backdrop-filter: blur(10px);
            border-radius: 25px; /* Lebih membulat */
            border: 1px solid rgba(128, 0, 32, 0.2); /* Border Maroon Halus */
            box-shadow: 
                var(--shadow-soft),
                inset 0 1px 0 rgba(255, 255, 255, 0.95); /* Inner highlight lebih terang */
            margin: 1.5rem auto !important;
            padding: 2.5rem !important;
            max-width: 1100px; /* Lebar lebih besar */
        }
        
        
        /* ===== SIDEBAR STYLING ===== */
        
        /* Sembunyikan navigasi bawaan Streamlit (Tetap) */
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="stSidebarNavItems"] { display: none !important; }
        section[data-testid="stSidebar"] > div > div:first-child > div:first-child { display: none !important; }

        /* Main Sidebar Container (Lebih berkelas) */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, var(--sidebar-cream) 0%, #903A50 100%); /* Gradient ke warna lebih gelap */
            padding-top: 1.5rem;
            box-shadow: 
                5px 0 40px rgba(0, 0, 0, 0.3), /* Shadow lebih jelas */
                inset -2px 0 0 rgba(128, 0, 32, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        /* Animated Gradient Border (Dipertegas) */
        [data-testid="stSidebar"]::after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 4px; /* Lebih tebal */
            height: 100%;
            background: linear-gradient(180deg, 
                var(--accent-gold) 0%, 
                var(--accent-orange) 50%, 
                var(--accent-gold) 100%
            );
            background-size: 100% 300%; /* Lebih panjang untuk animasi yang lebih dramatis */
            animation: borderGlow 6s ease-in-out infinite; /* Animasi lebih lambat */
            box-shadow: 
                0 0 20px rgba(128, 0, 32, 0.7),
                0 0 40px rgba(193, 27, 23, 0.5); /* Glow lebih kuat */
            z-index: 10;
        }
        
        @keyframes borderGlow {
            0%, 100% { background-position: 0% 0%; }
            50% { background-position: 0% 100%; }
        }
        
        /* Logo Styling */
        [data-testid="stSidebar"] img {
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.8); 
            backdrop-filter: blur(8px);
            border: 2px solid var(--accent-gold);
            box-shadow: 
                0 10px 30px rgba(0, 0, 0, 0.2),
                0 0 25px rgba(128, 0, 32, 0.5);
        }
        
        [data-testid="stSidebar"] img:hover {
            border-color: var(--accent-orange);
            transform: scale(1.02);
        }
        
        /* Sidebar Headings (Dipertegas) */
        [data-testid="stSidebar"] .stMarkdown h2,
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: var(--text-dark) !important; 
            text-shadow: 0 0 8px rgba(128, 0, 32, 0.5);
            font-weight: 900;
        }
        
        /* Sidebar Divider - Glowing (Dipertegas) */
        [data-testid="stSidebar"] hr {
            background: linear-gradient(90deg, 
                transparent 0%, 
                var(--accent-gold) 20%, 
                var(--accent-orange) 50%, 
                var(--accent-gold) 80%, 
                transparent 100%
            );
            box-shadow: 0 0 15px rgba(128, 0, 32, 0.8);
            height: 2px;
        }
        
        /* ===== MENU BUTTONS - Glass Style (Diperhalus) ===== */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 255, 255, 0.7) !important; 
            backdrop-filter: blur(10px);
            color: var(--text-dark) !important; 
            border: 1px solid rgba(128, 0, 32, 0.3) !important;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); /* Transisi lebih profesional */
        }
        
        /* Hover Glow Effect */
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(128, 0, 32, 0.2) !important; /* Maroon Transparan lembut */
            border-color: var(--accent-gold) !important;
            color: var(--text-dark) !important;
            transform: translateX(8px); /* Geser lebih jauh */
            box-shadow: 
                0 0 15px rgba(128, 0, 32, 0.6),
                inset 0 0 5px rgba(255, 255, 255, 0.5) !important;
        }
        
        /* ===== ACTIVE/PRIMARY BUTTON (Current Page) ===== */
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, 
                rgba(128, 0, 32, 0.5) 0%, 
                rgba(193, 27, 23, 0.6) 100%
            ) !important;
            border: 2px solid var(--accent-orange) !important;
            border-left: 8px solid var(--accent-gold) !important; /* Border tebal */
            color: var(--text-light) !important; /* Warna teks diubah ke putih agar kontras */
            font-weight: 800 !important;
            box-shadow: 
                0 0 30px rgba(128, 0, 32, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
            transform: translateX(8px);
        }
        
        
        /* ================================================= */
        /* ===== HOME PAGE STYLES - Diperhalus ===== */
        /* ================================================= */

        /* --- 1. Hero Section (Header Utama) --- */
        .hero-section {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%); 
            padding: 3rem 2rem; /* Padding lebih besar */
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(193, 27, 23, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.7); /* Border Putih lembut */
        }
        
        .hero-title {
            font-size: 2.5rem; /* Lebih besar */
            font-weight: 900;
            color: var(--text-light); /* Diganti ke putih agar kontras dengan latar maroon */
            text-shadow: 0 3px 5px rgba(0, 0, 0, 0.4); /* Shadow lebih kuat */
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            color: var(--text-light); /* Diganti ke putih agar kontras dengan latar maroon */
            font-weight: 600;
        }
        
        /* --- 2. Intro Section --- */
        .intro-section {
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(163, 64, 87, 0.3) 100%); /* Warna Cream dengan Maroon Transparan */
            border-left: 6px solid var(--accent-gold); /* Border lebih tebal, warna Deep Maroon */
            padding: 1.5rem 2rem;
            border-radius: 18px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
        
        /* --- 3. Feature Cards --- */
        .feature-card {
            background: linear-gradient(135deg, var(--bg-light-cream) 0%, rgba(255, 255, 255, 0.95) 100%);
            border: 1px solid rgba(128, 0, 32, 0.1);
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
            transition: all 0.4s ease; 
        }
        
        .feature-card:hover {
            transform: translateY(-8px) scale(1.03); /* Hover lebih menonjol */
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
            border-color: var(--accent-orange);
        }
        
        .feature-icon {
            font-size: 3rem; /* Ikon lebih besar */
            color: var(--accent-gold);
            filter: drop-shadow(0 4px 5px rgba(193, 27, 23, 0.5));
        }
        
        .feature-title {
            font-size: 1.3rem !important;
            font-weight: 900 !important;
            /* Latar belakang judul dihilangkan agar lebih bersih */
            background: none; 
            padding: 0;
            margin-bottom: 0.8rem !important;
        }
        
        /* --- 4. Section Title (Umum) --- */
        .section-title {
            font-size: 2rem;
            font-weight: 900;
            color: var(--text-dark);
            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            border-bottom: 3px solid var(--accent-gold);
            padding-bottom: 0.5rem;
        }
        
        /* --- 5. Step Cards (How It Works) --- */
        .step-card {
            background: var(--bg-light-cream);
            border: 1px solid rgba(128, 0, 32, 0.2);
            border-radius: 18px;
            padding: 1.2rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease; 
        }
        
        .step-card:hover {
            transform: translateX(5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            border-left: 5px solid var(--accent-orange);
        }
        
        /* Nomor langkah */
        .step-card > p:first-child {
            font-size: 1.8rem; 
            font-weight: 900; 
            color: var(--accent-orange); 
            border: 3px solid var(--accent-gold);
            background: var(--sidebar-cream); /* Warna lebih jelas */
            box-shadow: 0 0 5px rgba(128, 0, 32, 0.5);
        }
        
        /* Pastikan judul langkah berwarna Text Dark */
        .step-title {
            font-size: 1.2rem !important;
            font-weight: 900 !important;
            color: var(--text-dark) !important;
            margin: 0 0 0.5rem 0 !important;
            /* Latar belakang dihilangkan agar lebih bersih */
            background: none; 
            padding: 0;
        }
        
        /* --- 6. CTA Section (Call to Action) --- */
        .cta-section {
            background: linear-gradient(135deg, var(--sidebar-cream) 0%, var(--bg-light-cream) 100%);
            border: 4px double var(--accent-gold); /* Border Double untuk efek mewah */
            border-radius: 25px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(193, 27, 23, 0.2);
        }
        
        .cta-title {
            font-size: 2rem !important;
            font-weight: 900 !important;
            color: var(--accent-gold) !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* ================================================= */
        /* ===== UPLOAD DATASET PAGE STYLES - Diperhalus ===== */
        /* ================================================= */
        
        /* Upload Header */
        .upload-header {
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(163, 64, 87, 0.5) 100%);
            border-radius: 20px;
            padding: 1.5rem; 
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(128, 0, 32, 0.1);
        }
        
        /* Judul menggunakan Dark Maroon/Crimson gradient */
        .upload-title {
            font-size: 2.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--text-dark) 0%, var(--accent-orange) 100%); 
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* CUSTOM FILE UPLOADER STYLING (Override Streamlit Component) */
        
        /* File uploader drag-drop area (Lebih elegan) */
        .main [data-testid="stFileUploader"] section > div {
            background: var(--text-dark) !important; 
            border: 4px dashed var(--accent-gold) !important;
            border-radius: 25px !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5) !important;
            padding: 3rem !important;
            transition: all 0.4s ease;
        }
        
        .main [data-testid="stFileUploader"] section > div:hover {
            background: #400010 !important; /* Warna Darker Maroon */
            border-color: var(--accent-orange) !important;
        }
        
        /* Browse files button */
        .main [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%) !important;
            color: var(--text-light) !important; /* Diubah ke putih agar kontras */
            box-shadow: 0 5px 15px rgba(193, 27, 23, 0.5) !important;
            font-weight: 700 !important;
        }
        
        /* Uploaded file display */
        .main [data-testid="stFileUploader"] section + div {
            background: var(--bg-light-cream) !important;
            border: 3px solid var(--accent-gold) !important;
            border-radius: 12px !important;
        }

        /* Stats Cards (untuk display data) */
        .stat-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, var(--sidebar-cream) 100%);
            border: 1px solid rgba(128, 0, 32, 0.3);
            border-radius: 18px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            padding: 1.2rem;
            transition: all 0.3s ease;
        }
        
        .stat-card:hover {
            border-color: var(--accent-orange);
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }
        
        .stat-icon {
            color: var(--accent-gold);
            font-size: 2rem;
        }
        
        .stat-value {
            color: var(--text-dark);
            font-weight: 800;
            font-size: 1.5rem;
        }


        /* ================================================= */
        /* ===== ABOUT PAGE STYLES - Diperhalus ===== */
        /* ================================================= */

        /* --- 1. Header Section (about-header) --- */
        .about-header {
            background: linear-gradient(135deg, var(--sidebar-cream) 0%, #903A50 100%); 
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 2.5rem;
            border: 2px solid var(--accent-gold);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }

        .about-icon {
            font-size: 3.5rem;
            color: var(--accent-orange);
            text-shadow: 0 0 10px rgba(193, 27, 23, 0.5);
        }

        .about-title {
            font-size: 2.5rem !important;
            font-weight: 900 !important;
            color: var(--text-dark) !important;
            text-shadow: 0 3px 5px rgba(128, 0, 32, 0.6);
        }

        .about-subtitle {
            font-size: 1.1rem !important;
            color: #503038; /* Darker text for readability */
            font-weight: 600;
        }

        /* --- 2. Description Card (about-desc-card) --- */
        .about-desc-card {
            background: var(--bg-light-cream);
            border-left: 6px solid var(--accent-gold);
            padding: 1.8rem;
            border-radius: 16px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .adc-text strong {
            color: var(--accent-gold);
            font-weight: 800;
        }

        /* --- 3. Team & Tech Headers (Lebih jelas) --- */
        .team-header, .tech-header {
            border-bottom: 3px solid var(--accent-orange);
            padding-bottom: 0.6rem;
            margin-top: 2rem;
        }

        .team-h-title, .tech-h-title {
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--text-dark);
        }

        /* --- 4. Team Card (Lebih mewah) --- */
        .team-card {
            padding: 1.2rem 0.8rem;
            background: linear-gradient(135deg, var(--bg-light-cream) 0%, rgba(255, 255, 255, 0.95) 100%);
            border: 1px solid rgba(128, 0, 32, 0.2);
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease; 
        }

        .team-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            border-color: var(--accent-gold);
        }
        
        .team-avatar-img {
            border-radius: 50% !important; 
            height: 110px; 
            width: 110px;
            border: 4px solid var(--accent-gold); /* Border lebih tebal */
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        .team-name {
            font-weight: 800;
            color: var(--text-dark);
            font-size: 1.1rem;
        }

        .team-nim {
            font-size: 0.9rem;
            color: #63404B; /* Darker text for readability */
        }

        /* --- 5. Tech Card --- */
        .tech-card {
            padding: 1rem 0.8rem;
            background: var(--sidebar-cream);
            border-radius: 10px;
            border: 2px solid var(--accent-gold);
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
        }

        .tech-card:hover {
            background: var(--accent-gold);
            transform: scale(1.08);
            box-shadow: 0 5px 15px rgba(128, 0, 32, 0.5);
        }

        .tech-icon {
            font-size: 1.8rem;
        }

        .tech-name {
            font-weight: 700;
            font-size: 1rem;
        }

        /* --- 6. Footer --- */
        .about-footer {
            border-top: 2px solid rgba(32, 0, 8, 0.1);
            padding-top: 1.5rem;
        }

        /* --- STYLES BAWAAN STREAMLIT (Penambahan untuk tombol) --- */
        
        /* Tombol Streamlit Bawaan (Bukan Sidebar) - Diperjelas */
        .stButton button {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%) !important;
            color: var(--text-light) !important; /* Diubah ke putih agar kontras */
            font-weight: 800 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.5rem 1.5rem;
            box-shadow: 0 5px 15px rgba(193, 27, 23, 0.5);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        
        .stButton button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(193, 27, 23, 0.8);
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)

# Contoh penggunaan (opsional, untuk memastikan kode berjalan)
if __name__ == '__main__':
    st.set_page_config(layout="wide")
    add_custom_css()
    
    st.markdown('<div class="hero-section"><h1 class="hero-title">Aplikasi Analisis Data Royal Maroon</h1><p class="hero-subtitle">Visualisasi Data dengan Gaya Deep Maroon & Gold</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="intro-section">Ini adalah contoh seksi Intro dengan border kiri Deep Maroon.</div>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">Fitur Utama</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-card"><span class="feature-icon">📊</span><h3 class="feature-title">Visualisasi Canggih</h3><p>Gunakan chart dan grafik yang elegan.</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-card"><span class="feature-icon">💾</span><h3 class="feature-title">Upload Data Fleksibel</h3><p>Mendukung format CSV dan Excel.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-card"><span class="feature-icon">🚀</span><h3 class="feature-title">Performa Tinggi</h3><p>Dibuat dengan Python dan Streamlit.</p></div>', unsafe_allow_html=True)
    
    st.sidebar.title("NAVIGASI")
    st.sidebar.markdown('<hr>', unsafe_allow_html=True)
    
    # Contoh tombol sidebar biasa
    st.sidebar.markdown('<p style="margin-top: 2rem; color: var(--text-dark); font-weight: 600;">Halaman</p>', unsafe_allow_html=True)
    st.sidebar.button("Home", key="home_btn")
    
    # Contoh tombol sidebar primer (sebagai halaman aktif)
    st.sidebar.button("Upload Data", key="upload_btn", type="primary")
    st.sidebar.button("Tentang Kami", key="about_btn")
    
    # Contoh bagian 'About' (untuk menunjukkan CSS About Page)
    st.markdown('---')
    st.markdown('<div class="about-header"><span class="about-icon">👑</span><h2 class="about-title">Tentang Proyek Royal Maroon</h2><p class="about-subtitle">Menggabungkan kemewahan dengan kehangatan warna royal.</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="about-desc-card"><p class="adc-text">Aplikasi ini dibuat untuk menampilkan kemampuan kustomisasi <strong>Streamlit</strong> menggunakan tema <strong>Deep Maroon & Gold</strong> yang elegan dan berkelas.</p></div>', unsafe_allow_html=True)