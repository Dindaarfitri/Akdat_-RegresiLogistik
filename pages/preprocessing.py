import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# =============================
# FUNGSI STANDARISASI PLATFORM
# =============================
def normalize_platform(text):
    text = str(text).lower()

    replacements = {
        # WhatsApp
        "whatsapp": "wa",
        "wa": "wa",

        # Instagram
        "instagram": "ig",
        "ig": "ig",

        # TikTok
        "tiktok": "tiktok",
        "tik tok": "tiktok",

        # YouTube
        "youtube": "youtube",
        "you tube": "youtube",

        # LINE
        "line": "line",

        # Telegram
        "telegram": "telegram",
        "tele": "telegram",

        # Twitter / X
        "twitter": "x",
        "x": "x"
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    # hapus kata penghubung
    for sep in [" dan ", ",", "&"]:
        text = text.replace(sep, " ")

    return text


def show_preprocessing():
    st.markdown("""
        <h1>🧪 Preprocessing Data Mahasiswa</h1>
        <p>Tahap pembersihan dan transformasi data sebelum pemodelan</p>
        <hr>
    """, unsafe_allow_html=True)

    # =============================
    # CEK DATASET
    # =============================
    if st.session_state.get("raw_df") is None:
        st.warning("⚠ Dataset belum diupload. Silakan upload dataset terlebih dahulu.")
        return

    df = st.session_state["raw_df"].copy()

    # =============================
    # 1️⃣ STATISTIK SEBELUM PREPROCESSING
    # =============================
    st.subheader("📊 Statistik Sebelum Preprocessing")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Jumlah Baris", df.shape[0])
    with col2:
        st.metric("Jumlah Kolom", df.shape[1])
    with col3:
        st.metric("Total Missing Value", int(df.isnull().sum().sum()))

    st.markdown("**Preview Data:**")
    st.dataframe(df.head(25), use_container_width=True)

    # =============================
    # 2️⃣ CEK & HAPUS DATA DUPLIKAT
    # =============================
    st.subheader("🗑️ Penghapusan Data Duplikat")

    dup_mask = df.duplicated()
    dup_count = dup_mask.sum()

    st.write(f"Jumlah data duplikat ditemukan: **{dup_count}**")

    if dup_count > 0:
        st.markdown("**Preview Data Duplikat:**")
        st.dataframe(df[dup_mask], use_container_width=True)

        df = df.drop_duplicates()
        st.success(f"✅ {dup_count} data duplikat berhasil dihapus.")
    else:
        st.info("ℹ️ Tidak ditemukan data duplikat.")

    # =============================
    # 3️⃣ CEK NILAI KOSONG
    # =============================
    st.subheader("❓ Pemeriksaan Nilai Kosong")

    missing_table = df.isnull().sum()
    missing_table = missing_table[missing_table > 0]

    if missing_table.empty:
        st.success("✅ Tidak ada nilai kosong.")
    else:
        st.warning("⚠ Ditemukan nilai kosong:")
        st.dataframe(missing_table.rename("Jumlah Missing"), use_container_width=True)

    # =============================
    # 4️⃣ PENANGANAN NILAI KOSONG
    # =============================
    st.subheader("🧹 Penanganan Nilai Kosong")

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == "object":
                df[col].fillna(df[col].mode()[0], inplace=True)
            else:
                df[col].fillna(df[col].median(), inplace=True)

    st.success("✅ Nilai kosong berhasil ditangani.")

    # =============================
    # 5️⃣ PENGHAPUSAN KOLOM IDENTITAS 🔥 WAJIB DI SINI
    # =============================
    st.subheader("🪪 Penghapusan Kolom Identitas")

    identity_cols = ["ï»¿nama_"]

    cols_to_drop = [col for col in identity_cols if col in df.columns]

    if cols_to_drop:
        df.drop(columns=cols_to_drop, inplace=True)
        st.success(f"Kolom identitas dihapus: {', '.join(cols_to_drop)}")
    else:
        st.info("Tidak ada kolom identitas yang ditemukan.")

    # =============================
    # 5️⃣ STANDARISASI TEKS (PLATFORM MEDIA SOSIAL)
    # =============================
    st.subheader("🧾 Standarisasi Teks Platform Media Sosial")

    platform_col = "platform_media_sosial_apa_yang_paling_sering_anda_gunakan"

    if platform_col in df.columns:
        df[platform_col] = df[platform_col].apply(normalize_platform)

        st.success("✅ Teks platform berhasil distandarisasi.")
        st.markdown("**Preview hasil standarisasi (25 data):**")
        st.dataframe(
            df[[platform_col]].head(25),
            use_container_width=True
        )
    else:
        st.info("ℹ️ Kolom platform media sosial tidak ditemukan.")

    # =============================
    # 6️⃣ MULTI-LABEL ENCODING PLATFORM MEDIA SOSIAL
    # =============================
    st.subheader("📱 Multi-label Encoding Platform Media Sosial")

    if platform_col in df.columns:
        df["platform_tiktok"] = df[platform_col].apply(lambda x: 1 if "tiktok" in x else 0)
        df["platform_instagram"] = df[platform_col].apply(lambda x: 1 if "ig" in x else 0)
        df["platform_whatsapp"] = df[platform_col].apply(lambda x: 1 if "wa" in x else 0)
        df["platform_youtube"] = df[platform_col].apply(lambda x: 1 if "youtube" in x else 0)
        df["platform_line"] = df[platform_col].apply(lambda x: 1 if "line" in x else 0)
        df["platform_telegram"] = df[platform_col].apply(lambda x: 1 if "telegram" in x else 0)
        df["platform_x"] = df[platform_col].apply(lambda x: 1 if "x" in x else 0)

        # Hapus kolom teks asli
        df.drop(columns=[platform_col], inplace=True)

        st.success("✅ Multi-label encoding platform selesai.")
        st.markdown("**Preview hasil multi-label encoding (25 data):**")
        st.dataframe(
            df[
                [
                    "platform_tiktok",
                    "platform_instagram",
                    "platform_whatsapp",
                    "platform_youtube",
                    "platform_line",
                    "platform_telegram",
                    "platform_x"
                ]
            ].head(25),
            use_container_width=True
        )

    # =============================
    # 8️⃣ ENCODING DATA KATEGORIKAL
    # =============================
    st.subheader("🔤 Encoding Data Kategorikal")

    label_encoders = {}

    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    if categorical_cols:
        st.write("Kolom yang diencoding:")
        st.code(", ".join(categorical_cols))
    else:
        st.info("Tidak ada kolom kategorikal yang perlu diencoding.")

    # =============================
    # 8️⃣ RINGKASAN SETELAH PREPROCESSING
    # =============================
    st.subheader("📈 Statistik Setelah Preprocessing")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Jumlah Baris", df.shape[0])
    with col2:
        st.metric("Jumlah Kolom", df.shape[1])
    with col3:
        st.metric("Total Missing Value", int(df.isnull().sum().sum()))

    st.markdown("**Preview Data Setelah Preprocessing:**")
    st.dataframe(df.head(25), use_container_width=True)

    # =============================
    # 9️⃣ SIMPAN KE SESSION STATE
    # =============================
    st.session_state["clean_df"] = df
    st.session_state["label_encoders"] = label_encoders

    st.success("🎉 Preprocessing selesai! Data siap digunakan untuk Analisis Data.")

    # =============================
    # NEXT BUTTON
    # =============================
    if st.button("Next: Analisis Data ›", type="primary"):
        st.session_state["page"] = "Analisis Data"
        st.rerun()
