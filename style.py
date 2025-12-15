import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.
    Tema: Cream & Gold Modern (IPK vs Ekonomi)
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        
        /* ===== COLOR PALETTE =====
            Primary Background: #FEF9E7 (Light Cream - Hampir Putih)
            Sidebar: #FAF0CA (Soft Cream/Khaki)
            Accent 1: #F4D35E (Golden Yellow/Gold)
            Accent 2: #EE964B (Orange/Copper)
            Text Dark: #2C3E50 (Dark Blue/Charcoal - untuk kontras)
            Text Light: #ffffff
        ========================== */
        
        /* Global Styles */
        * {
            font-family: 'Poppins', sans-serif;
            color: var(--text-dark); /* Default text color */
        }
        
        /* Root Variables */
        :root {
            --bg-light-cream: #FEF9E7; /* Latar Belakang Utama */
            --sidebar-cream: #FAF0CA; /* Sidebar */
            --accent-gold: #F4D35E;
            --accent-orange: #EE964B;
            --text-dark: #2C3E50; 
            --text-light: #ffffff;
            --card-white: #ffffff;
            --shadow-soft: 0 8px 32px rgba(44, 62, 80, 0.12);
        }
        
        
        /* ===== MESH GRADIENT + GLASS PANELS DESIGN (Latar Belakang Utama) ===== */
        
        /* Base Background - Light Cream to Gold mesh */
        .main {
            background: 
                /* Mesh blob 1 - top left (Soft Cream) */
                radial-gradient(ellipse at 10% 20%, rgba(250, 240, 202, 0.9) 0%, transparent 50%),
                /* Mesh blob 2 - center (Light Gold) */
                radial-gradient(ellipse at 50% 50%, rgba(244, 211, 94, 0.2) 0%, transparent 55%),
                /* Mesh blob 3 - top right (Light Cream) */
                radial-gradient(ellipse at 85% 15%, rgba(250, 240, 202, 0.8) 0%, transparent 45%),
                /* Mesh blob 4 - bottom left (Orange/Copper) */
                radial-gradient(ellipse at 15% 85%, rgba(238, 150, 75, 0.15) 0%, transparent 50%),
                /* Mesh blob 5 - bottom right (Light Cream) */
                radial-gradient(ellipse at 90% 80%, rgba(254, 249, 231, 0.7) 0%, transparent 50%),
                /* Base gradient - Light Cream */
                linear-gradient(135deg, var(--bg-light-cream) 0%, #FFFDF7 100%);
            background-attachment: fixed;
            min-height: 100vh;
            position: relative;
        }
        
        /* Noise texture overlay for premium feel */
        .main::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
            opacity: 0.08; /* Lebih jelas agar ada tekstur */
            pointer-events: none;
            z-index: 0;
        }
        
        /* Subtle gradient animation overlay */
        .main::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(ellipse at 30% 70%, rgba(244, 211, 94, 0.1) 0%, transparent 50%),
                radial-gradient(ellipse at 70% 30%, rgba(238, 150, 75, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        
        /* This targets the Streamlit main content area */
        .stApp {
            background: transparent;
        }
        
        /* Glass Panel Effect for Content Container */
        .block-container {
            position: relative;
            z-index: 1;
            background: rgba(255, 255, 255, 0.85); /* Light glass */
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 
                0 15px 50px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.7);
            margin: 1.5rem auto !important;
            padding: 2.5rem !important;
            max-width: 1000px;
        }
        
        
        /* ===== SIDEBAR STYLING ===== */
        
        /* Sembunyikan navigasi bawaan Streamlit */
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="stSidebarNavItems"] { display: none !important; }
        section[data-testid="stSidebar"] > div > div:first-child > div:first-child { display: none !important; }

        /* Main Sidebar Container (DIUBAH KE SOFT CREAM) */
        [data-testid="stSidebar"] {
            background: var(--sidebar-cream); /* #FAF0CA Soft Cream */
            padding-top: 1rem;
            box-shadow: 
                4px 0 30px rgba(0, 0, 0, 0.2),
                inset -1px 0 0 rgba(238, 150, 75, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        /* Animated Gradient Border on Right Edge */
        [data-testid="stSidebar"]::after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 3px;
            height: 100%;
            background: linear-gradient(180deg, 
                var(--accent-gold) 0%, 
                var(--accent-orange) 50%, 
                var(--accent-gold) 100%
            );
            background-size: 100% 200%;
            animation: borderGlow 4s ease-in-out infinite;
            box-shadow: 
                0 0 15px rgba(244, 211, 94, 0.5),
                0 0 30px rgba(238, 150, 75, 0.3);
            z-index: 10;
        }
        
        @keyframes borderGlow {
            0%, 100% { background-position: 0% 0%; }
            50% { background-position: 0% 100%; }
        }
        
        /* Mesh Gradient Overlay */
        [data-testid="stSidebar"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(ellipse at 0% 0%, rgba(238, 150, 75, 0.1) 0%, transparent 50%),
                radial-gradient(ellipse at 100% 50%, rgba(244, 211, 94, 0.1) 0%, transparent 40%),
                radial-gradient(ellipse at 30% 100%, rgba(238, 150, 75, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        
        /* Logo Styling */
        [data-testid="stSidebar"] img {
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.5); /* Background putih transparan */
            backdrop-filter: blur(10px);
            border: 1px solid rgba(238, 150, 75, 0.3);
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.15),
                0 0 20px rgba(244, 211, 94, 0.3);
        }
        
        [data-testid="stSidebar"] img:hover {
            border-color: rgba(244, 211, 94, 0.8);
        }
        
        /* All Sidebar Text (DIUBAH KE DARK CHARCOAL) */
        [data-testid="stSidebar"] * {
            color: var(--text-dark) !important; /* #2C3E50 */
            font-weight: 500;
        }
        
        /* Sidebar Headings (DIUBAH KE ACCENT GOLD) */
        [data-testid="stSidebar"] .stMarkdown h2,
        [data-testid="stSidebar"] .stMarkdown h3 {
            color: var(--accent-gold) !important; 
            text-shadow: 0 0 5px rgba(244, 211, 94, 0.8);
            font-weight: 800;
        }
        
        /* Sidebar Divider - Glowing */
        [data-testid="stSidebar"] hr {
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(244, 211, 94, 0.8) 20%, 
                rgba(238, 150, 75, 1) 50%, 
                rgba(244, 211, 94, 0.8) 80%, 
                transparent 100%
            );
            box-shadow: 0 0 10px rgba(244, 211, 94, 0.6);
        }
        
        /* ===== MENU BUTTONS - Glass Style ===== */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 255, 255, 0.5) !important; /* Latar Belakang Putih Transparan */
            backdrop-filter: blur(8px);
            color: var(--text-dark) !important; 
            border: 1px solid rgba(238, 150, 75, 0.3) !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease; 
        }
        
        /* Hover Glow Effect */
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(244, 211, 94, 0.3) !important; /* Background Gold Transparan */
            border-color: var(--accent-gold) !important;
            color: var(--text-dark) !important;
            transform: translateX(5px);
            box-shadow: 
                0 0 10px rgba(244, 211, 94, 0.4),
                inset 0 0 10px rgba(244, 211, 94, 0.1) !important;
        }
        
        /* ===== ACTIVE/PRIMARY BUTTON (Current Page) ===== */
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, 
                rgba(244, 211, 94, 0.4) 0%, 
                rgba(238, 150, 75, 0.5) 100%
            ) !important;
            border: 1px solid var(--accent-orange) !important;
            border-left: 5px solid var(--accent-gold) !important;
            color: var(--text-dark) !important; 
            font-weight: 700 !important;
            box-shadow: 
                0 0 25px rgba(244, 211, 94, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
            transform: translateX(5px);
        }
        
        
        /* ================================================= */
        /* ===== HOME PAGE STYLES (Dipastikan Konsisten) ===== */
        /* ================================================= */

        /* --- 1. Hero Section (Header Utama) --- */
        .hero-section {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%); 
            padding: 2rem 1.5rem;
            border-radius: 18px;
            text-align: center;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 25px rgba(238, 150, 75, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(254, 249, 231, 0.5) 0%, transparent 50%);
            pointer-events: none;
        }
        
        .hero-title {
            font-size: 2.2rem;
            font-weight: 900;
            color: var(--text-dark); 
            margin-bottom: 0.8rem;
            text-shadow: 0 2px 4px rgba(255, 255, 255, 0.5);
            display: flex; /* Memastikan logo dan teks sejajar */
            align-items: center;
            justify-content: center;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
            color: var(--text-dark); 
            font-weight: 600;
            max-width: 650px;
            margin: 0 auto;
            line-height: 1.5;
        }
        
        /* --- 2. Intro Section (About/Deskripsi Singkat) --- */
        .intro-section {
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(250, 240, 202, 0.9) 100%);
            border-left: 5px solid var(--accent-orange);
            padding: 1rem 1.5rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }
        
        .intro-text {
            font-size: 1rem;
            color: #4A4A4A; 
            font-weight: 500;
            line-height: 1.6;
            margin: 0;
        }

        /* --- 3. Feature Cards (3 Kolom) --- */
        .feature-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(254, 249, 231, 0.88) 100%);
            border: 1px solid rgba(238, 150, 75, 0.3);
            border-radius: 16px;
            padding: 1.2rem;
            box-shadow: 0 5px 18px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease; 
            text-align: center; /* Tambahkan rata tengah */
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
            border-color: var(--accent-gold);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 0.8rem;
            color: var(--accent-orange);
            filter: drop-shadow(0 2px 5px rgba(238, 150, 75, 0.3));
        }
        
        .feature-title {
            font-size: 1.2rem !important;
            font-weight: 900 !important;
            color: var(--text-dark) !important;
            margin-bottom: 0.6rem !important;
            background: linear-gradient(135deg, rgba(244, 211, 94, 0.2) 0%, rgba(238, 150, 75, 0.1) 100%);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            display: inline-block; /* Agar background hanya di teks */
        }
        
        .feature-desc {
            font-size: 0.85rem;
            color: #4A4A4A;
            font-weight: 400;
        }
        
        /* --- 4. Section Title (Umum) --- */
        .section-title {
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--text-dark);
            margin-bottom: 1.5rem;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        /* --- 5. Step Cards (How It Works) --- */
        .step-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(254, 249, 231, 0.88) 100%);
            border: 1px solid rgba(238, 150, 75, 0.2);
            border-radius: 14px;
            padding: 1rem;
            margin-bottom: 0.7rem;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
            display: flex; 
            align-items: center; 
            gap: 1rem; 
            transition: all 0.3s ease; 
        }
        
        .step-card:hover {
            transform: translateX(3px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            border-color: var(--accent-gold);
        }
        
        /* Nomor langkah */
        .step-card > p:first-child {
            font-size: 1.5rem; 
            font-weight: 800; 
            color: var(--accent-orange); 
            margin: 0; 
            flex-shrink: 0;
            line-height: 1;
            padding: 0.2rem 0.6rem;
            border-radius: 50%;
            border: 2px solid var(--accent-gold);
            background: var(--bg-light-cream);
        }

        /* Konten langkah */
        .step-content {
            flex-grow: 1;
        }
        
        /* Pastikan judul langkah berwarna Text Dark */
        .step-title {
            font-size: 1.1rem !important;
            font-weight: 900 !important;
            color: var(--text-dark) !important;
            margin: 0 0 0.4rem 0 !important;
            background: rgba(244, 211, 94, 0.15); /* Gold transparan */
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            display: inline-block; 
        }
        
        .step-desc {
            font-size: 0.85rem;
            color: #4A4A4A;
            font-weight: 400;
            margin: 0; 
        }
        
        /* --- 6. CTA Section (Call to Action) --- */
        .cta-section {
            background: linear-gradient(135deg, rgba(254, 249, 231, 1) 0%, rgba(250, 240, 202, 0.9) 100%);
            border: 3px solid var(--accent-gold);
            border-radius: 20px;
            padding: 1.8rem;
            box-shadow: 0 5px 20px rgba(238, 150, 75, 0.1);
            text-align: center; 
        }
        
        .cta-title {
            font-size: 1.8rem !important;
            font-weight: 900 !important;
            color: var(--text-dark) !important;
        }
        
        .cta-subtitle {
            font-size: 1rem !important;
            color: #4A4A4A !important;
            font-weight: 500 !important;
            margin: 0.5rem 0 1.5rem 0 !important; 
        }
        
        
        /* ================================================= */
        /* ===== UPLOAD DATASET PAGE STYLES (Diperbaiki) ===== */
        /* ================================================= */
        
        /* Upload Header */
        .upload-header {
            background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(250, 240, 202, 0.8) 100%);
            border-radius: 18px;
            padding: 1rem; 
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }
        
        /* Judul menggunakan Dark Charcoal/Orange gradient */
        .upload-title {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--text-dark) 0%, var(--accent-orange) 100%); 
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .upload-subtitle {
            font-size: 1.1rem;
            color: #5A6773;
        }
        
        /* Upload Zone (Ini adalah overlay untuk stFileUploader) - Hapus: tidak diperlukan jika sudah ada custom uploader di bawah */
        
        
        /* CUSTOM FILE UPLOADER STYLING (Override Streamlit Component) */
        
        /* File uploader drag-drop area */
        .main [data-testid="stFileUploader"] section > div {
            background: linear-gradient(135deg, var(--text-dark) 0%, #4A4A4A 100%) !important; 
            border: 3px dashed var(--accent-gold) !important;
            border-radius: 20px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
            padding: 2rem !important;
            transition: all 0.3s ease;
        }
        
        .main [data-testid="stFileUploader"] section > div:hover {
            background: linear-gradient(135deg, #4A4A4A 0%, var(--text-dark) 100%) !important;
            border-color: var(--accent-orange) !important;
        }
        
        /* Text inside uploader */
        .main [data-testid="stFileUploader"] section > div > div, 
        .main [data-testid="stFileUploader"] section small {
            color: var(--bg-light-cream) !important; /* Warna teks Light Cream */
        }
        
        /* Browse files button */
        .main [data-testid="stFileUploader"] button {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%) !important;
            color: var(--text-dark) !important;
            box-shadow: 0 3px 10px rgba(238, 150, 75, 0.4) !important;
        }
        
        /* Uploaded file display */
        .main [data-testid="stFileUploader"] section + div {
            background: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid var(--accent-gold) !important;
            border-radius: 10px !important;
            margin-top: 1rem;
        }

        /* Stats Cards (untuk display data) */
        .stat-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(254, 249, 231, 0.88) 100%);
            border: 1px solid rgba(238, 150, 75, 0.2);
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            padding: 1rem;
        }
        
        .stat-card:hover {
            border-color: var(--accent-gold);
        }
        
        .stat-icon {
            color: var(--accent-orange);
        }
        
        .stat-value {
            color: var(--text-dark);
        }
        
        /* --- STYLES BAWAAN STREAMLIT (Perlu Override agar tidak merusak tema) --- */
        
        /* Header Streamlit */
        header {
            background-color: transparent !important;
            box-shadow: none !important;
            border-bottom: none !important;
        }

        /* Judul Markdown (H1, H2, H3, H4) */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
            color: var(--text-dark) !important;
        }
        
        .stMarkdown h1 {
            font-weight: 900 !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Input widgets (Slider, Selectbox, NumberInput, TextInput) */
        /* Menggunakan selector yang lebih umum dan spesifik */
        [data-testid*="stForm"] > div > div, /* Target input di dalam form */
        div[data-testid*="stSlider"], 
        div[data-testid*="stSelectbox"],
        div[data-testid*="stNumberInput"],
        div[data-testid*="stTextInput"] {
            background: rgba(255, 255, 255, 0.8);
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid rgba(238, 150, 75, 0.2);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            margin-bottom: 1rem; /* Tambahkan sedikit jarak */
        }
        
        /* Warna Label (Selector yang lebih tahan lama) */
        /* Targets label elements */
        label {
            color: var(--text-dark) !important;
            font-weight: 600 !important;
        }
        
        /* Targets label in Streamlit components */
        div[data-testid*="stForm"] label,
        .st-emotion-cache-11r9nwr, 
        .st-emotion-cache-10oahgq, 
        .st-emotion-cache-vk3ypz {
             color: var(--text-dark) !important;
             font-weight: 700 !important; /* Ditingkatkan agar lebih kontras */
        }

        /* Tombol Streamlit Bawaan (Bukan Sidebar) */
        .stButton button {
            background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-orange) 100%) !important;
            color: var(--text-dark) !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 8px !important; /* Konsistenkan radius */
            box-shadow: 0 4px 10px rgba(238, 150, 75, 0.3);
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background: linear-gradient(135deg, var(--accent-orange) 0%, var(--accent-gold) 100%) !important;
            box-shadow: 0 6px 15px rgba(238, 150, 75, 0.4);
            transform: translateY(-2px);
        }
        
        /* Success/Warning/Error boxes */
        [data-testid="stAlert"] {
            border-left: 5px solid var(--accent-orange) !important;
            border-radius: 10px !important;
        }
        
        /* DataFrame/Tabel Styling */
        .stDataFrame, .stTable {
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )