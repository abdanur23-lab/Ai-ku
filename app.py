import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Coding Assistant", page_icon="💻")

st.title("💻 Asisten AI Koding Pribadi")
st.write("Tanya apa saja seputar koding atau minta buatkan kode di sini!")

api_key = st.text_input("Masukkan Google Gemini API Key:", type="password")

if api_key:
    try:
        # Menghapus spasi yang tidak sengaja ter-copy
        clean_key = api_key.strip()
        genai.configure(api_key=clean_key)
        
        # Otomatis deteksi model yang aktif dan tersedia untuk akun Anda
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        # Memilih model terbaik secara otomatis
        selected_model = None
        for preferred in ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro']:
            if preferred in available_models:
                selected_model = preferred
                break
        
        if not selected_model and available_models:
            selected_model = available_models[0]

        user_prompt = st.text_area("Tuliskan pertanyaan atau kode yang ingin dibuat:")

        if st.button("Kirim ke AI"):
            if user_prompt:
                if selected_model:
                    with st.spinner("Sedang meracik kode..."):
                        model = genai.GenerativeModel(selected_model)
                        prompt_system = "Bertindaklah sebagai Senior Programmer. Berikan jawaban koding yang bersih, rapi, beserta penjelasan singkat.\n\n"
                        response = model.generate_content(prompt_system + user_prompt)
                        
                        st.subheader("Hasil Koding / Jawaban:")
                        st.markdown(response.text)
                else:
                    st.error("Tidak ada model AI yang cocok ditemukan.")
            else:
                st.warning("Isi dulu pertanyaannya!")
    except Exception as e:
        st.error(f"Terjadi kesalahan pada API Key atau koneksi: {e}")
else:
    st.info("Masukkan API Key Anda di atas untuk mulai.")
