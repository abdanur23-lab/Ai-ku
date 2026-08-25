import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Coding Assistant", page_icon="💻")

st.title("💻 Asisten AI Koding Pribadi")
st.write("Tanya apa saja seputar koding atau minta buatkan kode di sini!")

api_key = st.text_input("Masukkan Google Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    user_prompt = st.text_area("Tuliskan pertanyaan atau kode yang ingin dibuat:")

    if st.button("Kirim ke AI"):
        if user_prompt:
            with st.spinner("Sedang meracik kode..."):
                prompt_system = "Bertindaklah sebagai Senior Programmer. Berikan jawaban koding yang bersih, rapi, beserta penjelasan singkat."
                response = model.generate_content(prompt_system + "\n" + user_prompt)
                
                st.subheader("Hasil Koding / Jawaban:")
                st.markdown(response.text)
        else:
            st.warning("Isi dulu pertanyaannya!")
else:
    st.info("Masukkan API Key Anda di atas untuk mulai.")
