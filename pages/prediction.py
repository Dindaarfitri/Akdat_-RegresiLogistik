import streamlit as st
import pandas as pd
import numpy as np

def show_prediction_page():
    st.markdown("## 🎯 Prediksi Prestasi Akademik Mahasiswa")

    # =============================
    # CEK MODEL
    # =============================
    model = st.session_state.get("rf_model")
    model_features = st.session_state.get("model_features")

    if model is None or model_features is None:
        st.warning(
            "⚠️ Model belum tersedia. Silakan lakukan **Preprocessing** dan "
            "**Visualisasi (Training Model)** terlebih dahulu."
        )
        return

    # =============================
    # INPUT USER
    # =============================
    st.subheader("📝 Masukkan Data Mahasiswa")

    jenis_kelamin = st.selectbox(
        "Jenis Kelamin",
        ["Laki-laki", "Perempuan"]
    )

    tingkat_semester = st.selectbox(
        "Tingkat Semester",
        [1, 2, 3, 4, 5, 6, 7, 8]
    )

    durasi_sosmed = st.selectbox(
        "Durasi Penggunaan Media Sosial per Hari",
        df := [
            "< 1 Jam",
            "1–2 Jam",
            "3–4 Jam",
            "> 4 Jam"
        ]
    )

    durasi_tidur = st.selectbox(
        "Durasi Tidur per Hari",
        ["< 5 Jam", "5–6 Jam", "7–8 Jam", "> 8 Jam"]
    )

    platform = st.selectbox(
        "Platform Media Sosial Utama",
        ["Instagram", "WhatsApp", "TikTok", "Twitter", "Facebook"]
    )

    pengaruh_tidur = st.selectbox(
        "Apakah Media Sosial Mempengaruhi Jam Tidur?",
        ["Ya", "Tidak"]
    )

    pengaruh_ipk = st.selectbox(
        "Apakah Media Sosial Mempengaruhi Prestasi Akademik?",
        ["Ya", "Tidak"]
    )

    # =============================
    # PREDIKSI
    # =============================
    if st.button("🔮 Prediksi Prestasi Akademik", type="primary"):

        try:
            # ---------------------------------
            # BUAT DATAFRAME KOSONG SESUAI MODEL
            # ---------------------------------
            input_df = pd.DataFrame(
                np.zeros((1, len(model_features))),
                columns=model_features
            )

            # ---------------------------------
            # ISI NILAI SESUAI INPUT USER
            # ---------------------------------
            # Jenis Kelamin
            col_gender = f"jenis_kelamin_{jenis_kelamin}"
            if col_gender in input_df.columns:
                input_df[col_gender] = 1

            # Tingkat Semester
            col_semester = f"tingkat_semester_{tingkat_semester}"
            if col_semester in input_df.columns:
                input_df[col_semester] = 1

            # Platform
            col_platform = f"platform_media_sosial_apa_yang_paling_sering_anda_gunakan_{platform}"
            if col_platform in input_df.columns:
                input_df[col_platform] = 1

            # Durasi Sosial Media
            if durasi_sosmed in input_df.columns:
                input_df[durasi_sosmed] = 1

            # Durasi Tidur
            if durasi_tidur in input_df.columns:
                input_df[durasi_tidur] = 1

            # Pengaruh ke tidur
            col_sleep = f"apakah_penggunaan_media_sosial_berpengaruh_terhadap_jam_tidur_anda_{pengaruh_tidur}"
            if col_sleep in input_df.columns:
                input_df[col_sleep] = 1

            # Pengaruh ke IPK
            col_ipk = f"apakah_penggunaan_media_sosial_dapat_mempengaruhi_prestasi_akademik_anda_{pengaruh_ipk}"
            if col_ipk in input_df.columns:
                input_df[col_ipk] = 1

            # ---------------------------------
            # PREDIKSI
            # ---------------------------------
            prediction = model.predict(input_df)[0]

            label = "Prestasi Akademik Baik ✅" if prediction == 1 else "Prestasi Akademik Kurang ⚠️"

            st.success(f"🎓 **Hasil Prediksi:** {label}")

        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat prediksi: {e}")
