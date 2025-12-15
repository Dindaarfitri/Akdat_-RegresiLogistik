import streamlit as st

def init_session_state():
    # =============================
    # HALAMAN DEFAULT
    # =============================
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    # =============================
    # DATASET
    # =============================
    if "raw_df" not in st.session_state:
        st.session_state["raw_df"] = None

    if "clean_df" not in st.session_state:
        st.session_state["clean_df"] = None

    # =============================
    # MODEL MACHINE LEARNING
    # =============================
    if "rf_model" not in st.session_state:
        st.session_state["rf_model"] = None

    # =============================
    # SCALER (OPSIONAL)
    # =============================
    if "scaler" not in st.session_state:
        st.session_state["scaler"] = None

    # =============================
    # HASIL PREDIKSI
    # =============================
    if "prediction_result" not in st.session_state:
        st.session_state["prediction_result"] = None

    # =============================
    # FITUR (X) – SESUAI HEADER CSV
    # =============================
    if "features" not in st.session_state:
        st.session_state["features"] = [
            "jenis_kelamin_",
            "tingkat_semester_",
            "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari",
            "berapa_lama_anda_tidur_dalam_sehari",
            "platform_media_sosial_apa_yang_paling_sering_anda_gunakan",
            "apakah_penggunaan_media_sosial_berpengaruh_terhadap_jam_tidur_anda",
            "apakah_penggunaan_media_sosial_dapat_mempengaruhi_prestasi_akademik_anda"
        ]

    # =============================
    # TARGET (Y)
    # =============================
    if "target" not in st.session_state:
        st.session_state["target"] = (
            "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik"
        )
