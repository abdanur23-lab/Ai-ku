import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Coding Assistant", page_icon="💻")

st.title("💻 Asisten AI Koding Pribadi")
st.write("Tanya apa saja seputar koding atau minta buatkan kode di sini!")

api_key = st.text_input("Masukkan Google Gemini API Key:", type="password")

if api_key:
    try:
        clean_key = api_key.strip()
        genai.configure(api_key=clean_key)
        
        # Menggunakan versi model terbaru sesuai perintah error
        model = genai.GenerativeModel('gemini-3.6-flash')

        user_prompt = st.text_area("Tuliskan pertanyaan atau kode yang ingin dibuat:")

        if st.button("Kirim ke AI"):
            if user_prompt:
                with st.spinner("Sedang meracik kode..."):
                    prompt_system = "Bertindaklah sebagai Senior Programmer. Berikan jawaban koding yang bersih, rapi, beserta penjelasan singkat.\n\n"
                    response = model.generate_content(prompt_system + user_prompt)
                    
                    st.subheader("Hasil Koding / Jawaban:")
                    st.markdown(response.text)
            else:
                st.warning("Isi dulu pertanyaannya!")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada API Key atau koneksi: {e}")
else:
    st.info("Masukkan API Key Anda di atas untuk mulai.")
