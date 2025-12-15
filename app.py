import streamlit as st

# Pastikan file state.py dan style.py tersedia
from state import init_session_state
from style import add_custom_css

# =========================================================
# IMPORT SEMUA HALAMAN
# =========================================================
from pages.home import show_home
from pages.upload_dataset import show_upload_dataset
from pages.preprocessing import show_preprocessing
from pages.analysis import show_analysis      # Analisis / Clustering
from pages.modeling  import show_modeling
from pages.visualization import show_visualization
from pages.prediction import show_prediction_page
from pages.about import show_about

# =========================================================
# KONFIGURASI HALAMAN APLIKASI
# =========================================================
st.set_page_config(
    page_title="Analisis Pengaruh Penggunaan Media Sosial dan Durasi Tidur terhadap Prestasi Akademik Mahasiswa Menggunakan Regresi Logistik",
    layout="wide"
)

# =========================================================
# INISIALISASI SESSION STATE & CSS
# =========================================================
init_session_state()
add_custom_css()

# =========================================================
# SIDEBAR NAVIGASI
# =========================================================
with st.sidebar:
    st.image("static/logo.png", width=110)
    st.markdown("---")

    menu = [
        "Home",
        "Upload Dataset",
        "Preprocessing",
        "Analisis Data",
        "Model Regresi Logistik",
        "Visualisasi",
        "About"
    ]

    current_page = st.session_state.get("page", "Home")

    for item in menu:
        btn_type = "primary" if item == current_page else "secondary"
        if st.button(item, type=btn_type, use_container_width=True, key=f"nav_{item}"):
            st.session_state["page"] = item
            st.rerun()

# =========================================================
# ROUTER HALAMAN
# =========================================================
page = st.session_state["page"]

if page == "Home":
    show_home()

elif page == "Upload Dataset":
    show_upload_dataset()

elif page == "Preprocessing":
    show_preprocessing()

elif page == "Analisis Data":
    show_analysis()

elif page == "Model Regresi Logistik":
    show_modeling()

elif page == "Visualisasi":
    show_visualization()


elif page == "About":
    show_about()

# =========================================================
# FALLBACK
# =========================================================
else:
    st.error(f"Halaman tidak ditemukan: {page}")
    show_home()
