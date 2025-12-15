import streamlit as st
import pandas as pd

def show_upload_dataset():
    # =============================
    # HEADER SECTION
    # =============================
    st.markdown("""
        <div class="upload-header">
            <h1 class="upload-title">📂 Upload Dataset Mahasiswa</h1>
            <p class="upload-subtitle">
                Unggah file CSV berisi data penggunaan media sosial dan prestasi akademik mahasiswa
            </p>
        </div>
    """, unsafe_allow_html=True)

    # =============================
    # JIKA DATASET SUDAH ADA
    # =============================
    if st.session_state.get("raw_df") is not None:
        df = st.session_state["raw_df"]

        st.markdown("""
            <div class="success-banner">
                <span class="success-icon">✓</span>
                <span class="success-text">Dataset berhasil dimuat dan siap digunakan!</span>
            </div>
        """, unsafe_allow_html=True)

        # =============================
        # KOLOM PENTING (SESUAI CSV ASLI)
        # =============================
        required_cols = [
            "jenis_kelamin_",
            "tingkat_semester_",
            "berapa_lama_anda_menggunakan_media_sosial_dalam_sehari",
            "berapa_lama_anda_tidur_dalam_sehari",
            "apakah_anda_merasa_prestasi_akademik_ipk_anda_baik",
            "apakah_penggunaan_media_sosial_dapat_mempengaruhi_prestasi_akademik_anda"
        ]

        available = [c for c in required_cols if c in df.columns]
        is_complete = len(available) == len(required_cols)

        status = "Lengkap ✓" if is_complete else "Tidak Lengkap ⚠"
        status_class = "complete" if is_complete else "incomplete"

        # =============================
        # STATISTIK RINGKAS
        # =============================
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-icon">👨‍🎓</div>
                    <div class="stat-content">
                        <div class="stat-label">Total Responden</div>
                        <div class="stat-value">{df.shape[0]:,}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-icon">📑</div>
                    <div class="stat-content">
                        <div class="stat-label">Jumlah Kolom</div>
                        <div class="stat-value">{df.shape[1]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-card {status_class}">
                    <div class="stat-icon">{'✓' if is_complete else '⚠'}</div>
                    <div class="stat-content">
                        <div class="stat-label">Status Kolom</div>
                        <div class="stat-value">{status}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # =============================
        # PREVIEW DATA
        # =============================
        st.markdown("""
            <div class="section-header">
                <span class="section-icon">🔍</span>
                <span class="section-title">Preview Data Mahasiswa</span>
            </div>
        """, unsafe_allow_html=True)

        st.dataframe(df.head(), use_container_width=True)

        if not is_complete:
            missing = [c for c in required_cols if c not in df.columns]
            st.markdown(f"""
                <div class="warning-banner">
                    <span class="warning-icon">⚠</span>
                    <span class="warning-text">
                        Kolom berikut tidak ditemukan: <b>{", ".join(missing)}</b>
                    </span>
                </div>
            """, unsafe_allow_html=True)

        # =============================
        # ACTION BUTTONS
        # =============================
        col_btn1, col_btn2, col_spacer, col_next = st.columns([2, 2, 4, 2])

        with col_btn1:
            if st.button("🔄 Ganti Dataset", use_container_width=True):
                st.session_state["show_uploader"] = True
                st.rerun()

        with col_btn2:
            if st.button("🗑️ Hapus Dataset", use_container_width=True):
                for k in ["raw_df", "clean_df", "scaled_df", "scaler"]:
                    st.session_state[k] = None
                st.rerun()

        with col_next:
            if st.button("Next: Preprocessing ›", type="primary", use_container_width=True):
                st.session_state["page"] = "Preprocessing"
                st.rerun()

    # =============================
    # FILE UPLOADER
    # =============================
    if st.session_state.get("raw_df") is None or st.session_state.get("show_uploader", False):

        uploaded_file = st.file_uploader(
            "Upload file CSV Anda di sini",
            type=["csv"],
            key="dataset_uploader"
        )

        if uploaded_file is not None:
            try:
                # =============================
                # BACA CSV (AUTO DELIMITER)
                # =============================
                df = pd.read_csv(
                    uploaded_file,
                    encoding="latin1",
                    sep=None,
                    engine="python"
                )

                # =============================
                # NORMALISASI HEADER
                # =============================
                df.columns = (
                    df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace("?", "", regex=False)
                    .str.replace(":", "", regex=False)
                    .str.replace("/", "_", regex=False)
                    .str.replace("(", "", regex=False)
                    .str.replace(")", "", regex=False)
                    .str.replace("-", "_", regex=False)
                    .str.replace(" ", "_", regex=False)
                )

                st.session_state["raw_df"] = df
                st.session_state["show_uploader"] = False

                st.success("✅ Dataset berhasil diupload dan dibaca dengan benar!")
                st.rerun()

            except Exception as e:
                st.error(f"❌ Error saat memuat file: {e}")
