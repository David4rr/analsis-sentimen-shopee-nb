from __future__ import annotations

import streamlit as st
import textwrap

from data.model import ModelBundle
from data.preprocess import preprocess_text
from data.sarcasm import detect_sarcasm
from ui.components import render_page_header, render_probability_bars


LABEL_DISPLAY = {
    "positif": "Positif",
    "negatif": "Negatif",
    "netral": "Netral",
}


def _predict(text: str, model_components: dict) -> tuple[str, dict[str, float], str]:
    cleaned = preprocess_text(text)
    pipe = model_components["pipeline"]
    pred = pipe.predict([cleaned])[0]
    proba = pipe.predict_proba([cleaned])[0]
    labels = pipe.classes_
    proba_dict = {labels[i]: float(proba[i]) for i in range(len(labels))}
    return pred, proba_dict, cleaned


def render_prediction(model_bundle: ModelBundle) -> None:
    render_page_header(
        "Prediksi Langsung",
        "Masukkan ulasan dan lihat hasil prediksi sentimen dalam satu panel ringkas.",
    )

    if not model_bundle.ready:
        st.error(model_bundle.error or "Model belum tersedia.")
        return

    with st.form("prediction_form"):
        user_text = st.text_area(
            "Tulis ulasan Shopee",
            placeholder="Contoh: Barang bagus, pengiriman cepat, seller ramah.",
            height=160,
        )
        submitted = st.form_submit_button("Prediksi Sentimen")

    if submitted:
        if not user_text.strip():
            st.warning("Masukkan teks ulasan terlebih dahulu.")
        else:
            pred, proba_dict, cleaned = _predict(user_text.strip(), model_bundle.model)
            confidence = proba_dict.get(pred, 0.0) * 100
            badge_class = f"badge-{pred}"
            label = LABEL_DISPLAY.get(pred, pred)

            # Deteksi Sarkasme
            sarcasm_info = detect_sarcasm(user_text.strip())
            sarcasm_reason = ""
            if sarcasm_info["is_sarcasm"]:
                badge_class = "badge-sarkasme"
                label = "Sarkasme"
                sarcasm_reason = f"<div style='margin-top: 16px; padding-top: 12px; border-top: 1px solid #1f2937; color: #c084fc; font-size: 0.85rem;'>💡 <b>Sarkasme Terdeteksi:</b> {sarcasm_info['reason']}</div>"

            html_content = f'<div class="card" style="margin-bottom: 16px; margin-top: 16px;"><div class="section-title">Hasil Prediksi</div><div style="display:flex; align-items:center; gap:12px; margin-bottom: 16px;"><div class="badge {badge_class}">{label}</div><div class="muted">Confidence (NB) {confidence:.1f}%</div></div>{render_probability_bars(proba_dict)}{sarcasm_reason}</div>'

            st.markdown(html_content, unsafe_allow_html=True)

            with st.expander("Detail preprocessing", expanded=False):
                st.markdown(
                    textwrap.dedent(f"""
                    <div style="background:#1e293b; padding:12px; border-radius:8px; margin-bottom:12px; border: 1px solid #334155;">
                        <div class="muted" style="margin-bottom:4px; font-size:0.85rem;">Input asli:</div>
                        <div style="color:#e2e8f0; font-size:0.95rem;">{user_text.strip()}</div>
                    </div>
                    <div style="background:#1e293b; padding:12px; margin-bottom: 12px;border-radius:8px; border: 1px solid #334155;">
                        <div class="muted" style="margin-bottom:4px; font-size:0.85rem;">Setelah preprocessing:</div>
                        <div style="color:#e2e8f0; font-size:0.95rem;">{cleaned if cleaned else '(kosong)'}</div>
                    </div>
                    """),
                    unsafe_allow_html=True
                )

    st.markdown("<div class='section-title' style='margin-top:32px;'>Contoh Ulasan</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            textwrap.dedent("""
            <div class="card" style="height: 100%;">
                <div class="badge badge-positif" style="margin-bottom: 8px; display: inline-block;">Positif</div>
                <div style="color: #e2e8f0; font-size: 0.9rem;">"Cuman sayang ongkirnya mahal, tapi barangnya bagus"</div>
            </div>
            """),
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            textwrap.dedent("""
            <div class="card" style="height: 100%;">
                <div class="badge badge-negatif" style="margin-bottom: 8px; display: inline-block;">Negatif</div>
                <div style="color: #e2e8f0; font-size: 0.9rem;">"2x pesan barang lewat aplikasi ini, pesanan sy tdk 1 pun yg sampai Payah"</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(
            textwrap.dedent("""
            <div class="card" style="height: 100%;">
                <div class="badge badge-netral" style="margin-bottom: 8px; display: inline-block;">Netral</div>
                <div style="color: #e2e8f0; font-size: 0.9rem;">"Biaya penanganan yg awal nya 1000 terus 2000 sekarang jadi 5500?????"</div>
            </div>
            """),
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            textwrap.dedent("""
            <div class="card" style="height: 100%;">
                <div class="badge badge-sarkasme" style="margin-bottom: 8px; display: inline-block;">Sarkasme</div>
                <div style="color: #e2e8f0; font-size: 0.9rem;">"Wah bagus ya barangnya, sampai rusak semua pas dateng. Parah."</div>
            </div>
            """),
            unsafe_allow_html=True,
        )



