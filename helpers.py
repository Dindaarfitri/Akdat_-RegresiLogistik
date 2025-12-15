import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# =====================================
# VALIDASI STATE
# =====================================
def require_raw_data():
    if st.session_state.get("raw_df") is None:
        st.warning("⚠️ Silakan upload dataset terlebih dahulu di menu **Upload Dataset**.")
        st.stop()

def require_clean_data():
    if st.session_state.get("clean_df") is None:
        st.warning("⚠️ Silakan lakukan preprocessing data terlebih dahulu.")
        st.stop()

def require_model():
    if st.session_state.get("rf_model") is None:
        st.warning("⚠️ Model belum dilatih. Silakan latih model terlebih dahulu.")
        st.stop()

# =====================================
# KONVERSI NUMERIK (AMAN)
# =====================================
def convert_numeric_columns(df: pd.DataFrame, columns: list):
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

# =====================================
# PREPROCESS DATA (SURVEI MAHASISWA)
# =====================================
def preprocess_data(df: pd.DataFrame):
    df = df.copy()

    features = st.session_state["features"]
    target = st.session_state["target"]

    # Validasi kolom
    missing = [c for c in features + [target] if c not in df.columns]
    if missing:
        st.error(f"❌ Kolom berikut tidak ditemukan: {missing}")
        st.stop()

    # Encode target (Ya/Tidak, Baik/Tidak, dll)
    target_encoder = LabelEncoder()
    df[target] = target_encoder.fit_transform(df[target].astype(str))

    # Encode fitur kategorikal
    feature_encoders = {}
    for col in features:
        if df[col].dtype == "object":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            feature_encoders[col] = le

    # Drop missing
    df = df.dropna()

    # Scaling fitur numerik
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])
    df_scaled = pd.DataFrame(X_scaled, columns=features, index=df.index)

    return df, df_scaled, scaler, target_encoder, feature_encoders

# =====================================
# FEATURE IMPORTANCE (VISUAL)
# =====================================
def plot_feature_importance(model, feature_names):
    importance = model.feature_importances_
    sorted_idx = np.argsort(importance)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(np.array(feature_names)[sorted_idx], importance[sorted_idx])
    ax.set_title("Feature Importance\nPengaruh Media Sosial terhadap Prestasi Akademik")
    ax.set_xlabel("Tingkat Kepentingan")
    st.pyplot(fig)

# =====================================
# VISUALISASI HUBUNGAN
# =====================================
def plot_relationship(df, x, y):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[x], df[y])
    ax.set_title(f"Hubungan {x} terhadap {y}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)

# =====================================
# GENERATE PDF REPORT
# =====================================
def generate_pdf_report(df_clean, model):
    from matplotlib.backends.backend_pdf import PdfPages
    import io
    from datetime import datetime

    features = st.session_state["features"]

    buffer = io.BytesIO()

    with PdfPages(buffer) as pdf:

        # =====================
        # COVER PAGE
        # =====================
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.5, 0.7, "LAPORAN ANALISIS", ha="center", fontsize=26, fontweight="bold")
        fig.text(
            0.5, 0.62,
            "Pengaruh Penggunaan Media Sosial terhadap Prestasi Akademik Mahasiswa",
            ha="center",
            fontsize=16
        )
        fig.text(
            0.5, 0.54,
            f"Tanggal: {datetime.now().strftime('%d %B %Y')}",
            ha="center",
            fontsize=12
        )
        fig.text(
            0.5, 0.48,
            f"Jumlah Responden: {len(df_clean)} mahasiswa",
            ha="center",
            fontsize=12
        )
        plt.axis("off")
        pdf.savefig(fig)
        plt.close()

        # =====================
        # FEATURE IMPORTANCE
        # =====================
        importance = model.feature_importances_
        sorted_idx = np.argsort(importance)

        fig, ax = plt.subplots(figsize=(11, 8.5))
        ax.barh(np.array(features)[sorted_idx], importance[sorted_idx])
        ax.set_title("Feature Importance Model Random Forest")
        ax.set_xlabel("Tingkat Kepentingan")
        pdf.savefig(fig)
        plt.close()

    buffer.seek(0)
    return buffer.getvalue()
