import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

def show_modeling():
    st.markdown("## 🤖 Modeling: Regresi Logistik")

    # =============================
    # CEK DATA
    # =============================
    df = st.session_state.get("clean_df")

    if df is None:
        st.warning("⚠️ Data belum tersedia. Silakan lakukan preprocessing dan analysis terlebih dahulu.")
        return

    # =============================
    # DEFINISI TARGET & FITUR
    # =============================
    target_col = "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik"

    feature_cols = [
        "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari",
        "berapa_lama_anda_tidur_dalam_sehari",
        "apakah_penggunaan_media_sosial_dapat_mempengaruhi_prestasi_akademik_anda",

        # Platform media sosial
        "platform_tiktok",
        "platform_instagram",
        "platform_whatsapp",
        "platform_youtube",
        "platform_line",
        "platform_telegram",
        "platform_x"
    ]

    # Pastikan kolom ada
    missing_cols = [col for col in feature_cols + [target_col] if col not in df.columns]

    if missing_cols:
        st.error(f"❌ Kolom berikut tidak ditemukan: {missing_cols}")
        return

    X = df[feature_cols]
    y = df[target_col]

    # =============================
    # SPLIT DATA
    # =============================
    st.subheader("📂 Pembagian Data (Train & Test)")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    st.write(f"Jumlah data training: {X_train.shape[0]}")
    st.write(f"Jumlah data testing: {X_test.shape[0]}")

    # =============================
    # TRAINING MODEL
    # =============================
    st.subheader("⚙️ Training Model Regresi Logistik")

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    st.success("✅ Model Regresi Logistik berhasil dilatih.")

    # =============================
    # EVALUASI MODEL
    # =============================
    st.subheader("📊 Evaluasi Model")

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    st.metric("Akurasi Model", f"{acc:.2%}")

    # Confusion Matrix
    st.markdown("**Confusion Matrix**")
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(
        cm,
        index=["Aktual Tidak", "Aktual Ya"],
        columns=["Prediksi Tidak", "Prediksi Ya"]
    )
    st.dataframe(cm_df, use_container_width=True)

    # Classification Report
    st.markdown("**Classification Report**")
    st.code(classification_report(y_test, y_pred))

    # =============================
    # INTERPRETASI KOEFISIEN
    # =============================
    st.subheader("📈 Interpretasi Koefisien Regresi")

    coef_df = pd.DataFrame({
        "Variabel": feature_cols,
        "Koefisien": model.coef_[0]
    }).sort_values(by="Koefisien", ascending=False)

    st.dataframe(coef_df, use_container_width=True)

    st.markdown("""
    **Interpretasi Koefisien:**
    - Koefisien **positif** → meningkatkan peluang IPK baik
    - Koefisien **negatif** → menurunkan peluang IPK baik
    - Nilai absolut yang lebih besar → pengaruh lebih kuat
    """)

    # =============================
    # KESIMPULAN MODEL
    # =============================
    st.subheader("📝 Kesimpulan Pemodelan")

    st.markdown(f"""
    Model Regresi Logistik yang dibangun menghasilkan tingkat akurasi
    sebesar **{acc:.2%}**, yang menunjukkan bahwa model cukup mampu
    membedakan mahasiswa dengan prestasi akademik yang baik dan tidak.

    Variabel dengan pengaruh paling dominan dapat diidentifikasi
    melalui nilai koefisien regresi, sehingga model ini tidak hanya
    bersifat prediktif tetapi juga interpretatif.
    """)

    st.success("🎯 Pemodelan Regresi Logistik selesai.")

    if st.button("Next: Visualisasi ›", type="primary"):
        st.session_state["page"] = "Visualisasi"
        st.rerun()
