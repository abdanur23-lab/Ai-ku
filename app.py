import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Coding Assistant", page_icon="💻")

st.title("💻 Asisten AI")
st.write("Tanya apa saja!")

# Ambil API key dari Secrets Streamlit
api_key = st.secrets.get("GEMINI_API_KEY", "").strip()

# Cadangan jika Secrets kosong
if not api_key:
    api_key = st.text_input("Masukkan Google Gemini API Key:", type="password").strip()

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-3.6-flash')

        user_prompt = st.text_area("Tuliskan pertanyaan:")

        if st.button("Kirim ke AI"):
            if user_prompt:
                with st.spinner("Sedang mencari..."):
                    prompt_system = "Bertindaklah sebagai Senior Programmer. Berikan jawaban koding yang bersih, rapi, beserta penjelasan singkat.\n\n"
                    response = model.generate_content(prompt_system + user_prompt)
                    
                    st.subheader("Hasil:")
                    st.markdown(response.text)
            else:
                st.warning("Isi dulu pertanyaannya!")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada API Key: {e}")
else:
    st.info("Masukkan API Key Anda di atas untuk mulai.")
