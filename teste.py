import streamlit as st

def main():
    
    # Título romântico
    st.markdown("<h1 style='text-align: center; color: #ED231C;'>Um pouco sobre a gente 💘</h1>", unsafe_allow_html=True)

    # Divider
    st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

    # URL do vídeo romântico
    video_url = "https://youtu.be/uHiNJBH5agQ?si=Er477abSVUVBdYi7"

    # Exibindo o vídeo localmente
    st.video(video_url)
    
    st.text("Grande amor da minha vida")
    st.text("Nunca se sinta sozinha")
    st.text("Meu amor, eu te prometo")
    st.text("A cada momento te fazer feliz")
    st.text("Meu amor eu agradeço")
    st.text("Para sempre o dia que eu te conheci ❤️")

    # Botão para curtir o vídeo
    if st.button("Curtir ❤️"):
        st.text("Maravilhoso!!!! você curtiu o vídeo. Eu te amo meu bem ❤️ ")

if __name__ == "__main__":
    main()
