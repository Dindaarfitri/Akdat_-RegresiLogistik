import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# =========================================================
# HELPER: DECODE LABEL (SAMA DENGAN ANALYSIS)
# =========================================================
def decode_column(df, col_name):
    label_encoders = st.session_state.get("label_encoders", {})
    if col_name in label_encoders:
        le = label_encoders[col_name]
        return pd.Series(le.inverse_transform(df[col_name]), name=col_name)
    return df[col_name]

def show_visualization():
    

    # =============================
    # CEK DATA
    # =============================
    df = st.session_state.get("clean_df")

    if df is None:
        st.warning("⚠️ Data belum tersedia. Silakan lakukan preprocessing terlebih dahulu.")
        return
    
     # =============================
    # DEFINISI KOLOM
    # =============================
    target_col = "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik"
    col_usage = "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari"
    col_sleep = "berapa_lama_anda_tidur_dalam_sehari"
    col_gender = "jenis_kelamin_"

    # =============================
    # DECODE LABEL (KUNCI UTAMA)
    # =============================
    usage = decode_column(df, col_usage)
    sleep = decode_column(df, col_sleep)
    target = decode_column(df, target_col)
    gender = decode_column(df, col_gender)

    # =============================
    # DEFINISI TARGET & FITUR
    # =============================
    target_col = "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik"

    feature_cols = [
        "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari",
        "berapa_lama_anda_tidur_dalam_sehari",
        "apakah_penggunaan_media_sosial_dapat_mempengaruhi_prestasi_akademik_anda",

        "platform_tiktok",
        "platform_instagram",
        "platform_whatsapp",
        "platform_youtube",
        "platform_line",
        "platform_telegram",
        "platform_x"
    ]

    # =============================
    # VALIDASI KOLOM
    # =============================
    missing_cols = [c for c in feature_cols + [target_col] if c not in df.columns]
    if missing_cols:
        st.error(f"❌ Kolom berikut tidak ditemukan: {missing_cols}")
        return

    st.markdown("## 📊 Visualisasi Hubungan Antar Variabel")
    st.subheader("📱 Durasi Media Sosial vs Prestasi Akademik")

    usage_ipk = pd.crosstab(usage, target, normalize="index")

    fig1, ax1 = plt.subplots(figsize=(7, 4))
    usage_ipk.plot(kind="bar", stacked=True, ax=ax1)

    ax1.set_xlabel("Durasi Penggunaan Media Sosial")
    ax1.set_ylabel("Proporsi")
    ax1.set_title("Durasi Media Sosial vs Prestasi Akademik")
    ax1.legend(title="Prestasi Akademik")

    st.pyplot(fig1)

    st.subheader("😴 Durasi Tidur vs Prestasi Akademik")

    sleep_ipk = pd.crosstab(sleep, target, normalize="index")

    fig2, ax2 = plt.subplots(figsize=(7, 4))
    sleep_ipk.plot(kind="bar", stacked=True, ax=ax2)

    ax2.set_xlabel("Durasi Tidur")
    ax2.set_ylabel("Proporsi")
    ax2.set_title("Durasi Tidur vs Prestasi Akademik")
    ax2.legend(title="Prestasi Akademik")

    st.pyplot(fig2)

    st.subheader("📲 Durasi Media Sosial vs Durasi Tidur")

    usage_sleep = pd.crosstab(usage, sleep, normalize="index")

    fig3, ax3 = plt.subplots(figsize=(7, 4))
    usage_sleep.plot(kind="bar", stacked=True, ax=ax3)

    ax3.set_xlabel("Durasi Media Sosial")
    ax3.set_ylabel("Proporsi")
    ax3.set_title("Media Sosial vs Durasi Tidur")
    ax3.legend(title="Durasi Tidur")

    st.pyplot(fig3)

    st.subheader("👥 Jenis Kelamin vs Prestasi Akademik")

    gender_ipk = pd.crosstab(gender, target)

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    gender_ipk.plot(kind="bar", ax=ax4)

    ax4.set_xlabel("Jenis Kelamin")
    ax4.set_ylabel("Jumlah Mahasiswa")
    ax4.set_title("Jenis Kelamin vs Prestasi Akademik")
    ax4.legend(title="Prestasi Akademik")

    st.pyplot(fig4)


    st.markdown("## 📊 Visualisasi Model Regresi Logistik")

    X = df[feature_cols]
    y = df[target_col]

    # =============================
    # SPLIT DATA
    # =============================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    # =============================
    # TRAIN MODEL
    # =============================
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # =============================
    # PREDIKSI
    # =============================
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # =============================
    # AKURASI MODEL
    # =============================
    st.subheader("🎯 Akurasi Model")

    st.metric(
        label="Akurasi Regresi Logistik",
        value=f"{accuracy * 100:.2f}%"
    )

    st.markdown("""
    **Penjelasan:**  
    Akurasi menunjukkan kemampuan model dalam mengklasifikasikan
    mahasiswa dengan prestasi akademik **baik** dan **tidak baik**
    berdasarkan faktor penggunaan media sosial dan durasi tidur.
    """)

    st.divider()

    # =============================
    # CONFUSION MATRIX
    # =============================
    st.subheader("📊 Confusion Matrix")

    cm = confusion_matrix(y_test, y_pred)

    fig_cm, ax_cm = plt.subplots(figsize=(6, 4))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax_cm
    )

    ax_cm.set_xlabel("Prediksi")
    ax_cm.set_ylabel("Aktual")
    ax_cm.set_title("Confusion Matrix - Regresi Logistik")

    st.pyplot(fig_cm)

    st.markdown("""
    **Penjelasan Confusion Matrix:**  
    - **True Positive (TP):** IPK baik diprediksi baik  
    - **True Negative (TN):** IPK tidak baik diprediksi tidak baik  
    - **False Positive (FP):** Prediksi baik tapi aktual tidak  
    - **False Negative (FN):** Prediksi tidak tapi aktual baik  

    Model yang baik memiliki nilai besar pada diagonal utama.
    """)

    st.divider()

    # =============================
    # VISUALISASI KOEFISIEN REGRESI
    # =============================
    st.subheader("📈 Pengaruh Variabel (Koefisien Regresi)")

    coef_df = pd.DataFrame({
        "Variabel": feature_cols,
        "Koefisien": model.coef_[0]
    }).sort_values(by="Koefisien", ascending=True)

    st.dataframe(coef_df, use_container_width=True)

    fig_coef, ax_coef = plt.subplots(figsize=(8, 5))
    ax_coef.barh(coef_df["Variabel"], coef_df["Koefisien"])
    ax_coef.set_xlabel("Nilai Koefisien")
    ax_coef.set_title("Koefisien Regresi Logistik")

    st.pyplot(fig_coef)

    st.markdown("""
    **Interpretasi Koefisien:**
    - Koefisien **positif** → meningkatkan peluang IPK baik  
    - Koefisien **negatif** → menurunkan peluang IPK baik  
    - Semakin besar nilai absolut → semakin kuat pengaruhnya  

    Visualisasi ini membantu memahami faktor mana yang paling
    memengaruhi prestasi akademik mahasiswa.
    """)

    st.success("✅ Visualisasi Regresi Logistik selesai.")

    
