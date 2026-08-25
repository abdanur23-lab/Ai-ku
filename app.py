import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Asisten Pribadi", page_icon="🤖")

# Sembunyikan Menu dan Header bawaan Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🤖 AI Asisten Pribadi")
st.write("Tanya apa saja di sini!")

# Ambil API key dari Secrets Streamlit
api_key = st.secrets.get("GEMINI_API_KEY", "").strip()

if not api_key:
    api_key = st.text_input("Masukkan Google Gemini API Key:", type="password").strip()

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-3.6-flash')

        user_prompt = st.text_area("Tuliskan pertanyaan Anda:")

        if st.button("Kirim ke AI"):
            if user_prompt:
                with st.spinner("Sedang memproses..."):
                    # Instruksi agar AI menjawab secara umum tanpa blok kode/istilah koding
                    prompt_system = (
                        "Bertindaklah sebagai asisten umum yang ramah dan pintar. "
                        "Jawab pertanyaan pengguna secara langsung, jelas, dan alami. "
                        "Jangan berikan contoh kode kodingan atau istilah teknis pemrograman "
                        "kecuali jika pengguna secara khusus meminta kode.\n\n"
                    )
                    response = model.generate_content(prompt_system + user_prompt)
                    
                    st.subheader("Jawaban:")
                    st.markdown(response.text)
            else:
                st.warning("Isi dulu pertanyaannya!")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
else:
    st.info("Masukkan API Key Anda di atas untuk mulai.")
