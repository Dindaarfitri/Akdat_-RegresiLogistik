import streamlit as st
import pandas as pd

# =========================================================
# HELPER: DECODE LABEL
# =========================================================
def decode_column(df, col_name):
    label_encoders = st.session_state.get("label_encoders", {})
    if col_name in label_encoders:
        le = label_encoders[col_name]
        return pd.Series(le.inverse_transform(df[col_name]), name=col_name)
    return df[col_name]

# =========================================================
# MAIN PAGE
# =========================================================
def show_analysis():
    st.markdown("## 📊 Analisis Data Mahasiswa dan Media Sosial")

    df = st.session_state.get("clean_df")
    if df is None:
        st.warning("⚠️ Dataset belum dipreprocessing.")
        return

    col_target = "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik"

    # =========================================================
    # A. ANALISIS DESKRIPTIF
    # =========================================================
    st.markdown("## 🅰️ Analisis Deskriptif")

    st.markdown("""
    Analisis deskriptif bertujuan untuk memberikan gambaran umum
    mengenai karakteristik responden, pola penggunaan media sosial,
    serta persepsi prestasi akademik mahasiswa.
    """)

    # -----------------------------
    # A1. Karakteristik Responden
    # -----------------------------
    st.subheader("A1️⃣ Karakteristik Responden")

    cols_demo = {
        "jenis_kelamin_": "Jenis Kelamin",
        "tingkat_semester_": "Tingkat Semester",
        "program_studi_jurusan_": "Program Studi"
    }

    for col, title in cols_demo.items():
        if col in df.columns:
            decoded = decode_column(df, col)
            dist = decoded.value_counts().rename("Jumlah").to_frame()

            st.markdown(f"**Distribusi {title}**")
            st.dataframe(dist, use_container_width=True)

    # -----------------------------
    # A2. Pola Penggunaan Media Sosial
    # -----------------------------
    st.subheader("A2️⃣ Pola Penggunaan Media Sosial")

    col_usage = "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari"

    if col_usage in df.columns:
        decoded = decode_column(df, col_usage)
        usage_dist = decoded.value_counts(normalize=True).rename("Proporsi").to_frame()
        st.dataframe(usage_dist, use_container_width=True)

    # -----------------------------
    # A3. Persepsi Prestasi Akademik
    # -----------------------------
    st.subheader("A3️⃣ Persepsi Prestasi Akademik")

    if col_target in df.columns:
        decoded = decode_column(df, col_target)
        target_dist = decoded.value_counts(normalize=True).rename("Proporsi").to_frame()
        st.dataframe(target_dist, use_container_width=True)

    st.divider()

    # =========================================================
    # B. ANALISIS HUBUNGAN
    # =========================================================
    st.markdown("## 🅱️ Analisis Hubungan Antar Variabel")

    # -----------------------------
    # B1. Media Sosial vs IPK
    # -----------------------------
    st.subheader("B1️⃣ Media Sosial ↔ Prestasi Akademik")

    if col_usage in df.columns and col_target in df.columns:
        usage = decode_column(df, col_usage)
        target = decode_column(df, col_target)

        usage_ipk = pd.crosstab(usage, target, normalize="index")
        st.dataframe(usage_ipk, use_container_width=True)

        st.markdown("""
        **Interpretasi:**  
        Terdapat variasi proporsi prestasi akademik berdasarkan
        durasi penggunaan media sosial, yang mengindikasikan
        adanya hubungan antara intensitas penggunaan media sosial
        dan persepsi IPK mahasiswa.
        """)

    # -----------------------------
    # B2. Durasi Tidur vs IPK
    # -----------------------------
    st.subheader("B2️⃣ Durasi Tidur ↔ Prestasi Akademik")

    col_sleep = "berapa_lama_anda_tidur_dalam_sehari"

    if col_sleep in df.columns:
        sleep = decode_column(df, col_sleep)
        target = decode_column(df, col_target)

        sleep_ipk = pd.crosstab(sleep, target, normalize="index")
        st.dataframe(sleep_ipk, use_container_width=True)

        st.markdown("""
        **Interpretasi:**  
        Mahasiswa dengan durasi tidur yang lebih cukup
        cenderung memiliki proporsi prestasi akademik yang lebih baik,
        menunjukkan pentingnya kualitas istirahat terhadap performa akademik.
        """)

    # -----------------------------
    # B3. Media Sosial vs Durasi Tidur
    # -----------------------------
    st.subheader("B3️⃣ Media Sosial ↔ Durasi Tidur")

    if col_usage in df.columns and col_sleep in df.columns:
        usage = decode_column(df, col_usage)
        sleep = decode_column(df, col_sleep)

        usage_sleep = pd.crosstab(usage, sleep, normalize="index")
        st.dataframe(usage_sleep, use_container_width=True)

        st.markdown("""
        **Interpretasi:**  
        Intensitas penggunaan media sosial menunjukkan kecenderungan
        berhubungan dengan durasi tidur mahasiswa,
        yang secara tidak langsung dapat memengaruhi prestasi akademik.
        """)

    # -----------------------------
    # B4. Jenis Kelamin vs IPK
    # -----------------------------
    st.subheader("B4️⃣ Jenis Kelamin ↔ Prestasi Akademik")

    col_gender = "jenis_kelamin_"

    if col_gender in df.columns:
        gender = decode_column(df, col_gender)
        target = decode_column(df, col_target)

        gender_ipk = pd.crosstab(gender, target, normalize="index")
        st.dataframe(gender_ipk, use_container_width=True)


    # =========================================================
    # C. ANALISIS PREDIKTIF (PENGANTAR MODEL)
    # =========================================================
    st.markdown("## 🅲 Analisis Prediktif")

    st.markdown("""
    Berdasarkan karakteristik data yang bersifat kategorikal
    dan variabel target biner (prestasi akademik: baik/tidak),
    metode **Regresi Logistik** dipilih sebagai model analisis prediktif.
    """)

    st.markdown("""
    **Alasan Pemilihan Regresi Logistik:**
    - Variabel target bersifat dikotomi (Ya/Tidak)
    - Dapat mengukur pengaruh masing-masing variabel independen
    - Menghasilkan probabilitas prestasi akademik yang baik
    - Mudah diinterpretasikan secara akademik
    """)

    st.markdown("""
    **Variabel Input Model:**
    - Durasi penggunaan media sosial  
    - Durasi tidur  
    - Platform media sosial  
    - Persepsi pengaruh media sosial  

    **Output Model:**
    - Probabilitas mahasiswa memiliki prestasi akademik yang baik
    """)

    st.success("✅ Tahap analisis selesai. Selanjutnya dilakukan pemodelan Regresi Logistik.")

    if st.button("Next: Model Regresi Logistik ›", type="primary"):
        st.session_state["page"] = "Model Regresi Logistik"
        st.rerun()

