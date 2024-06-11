import streamlit as st
from PIL import Image

# Configurações da barra de navegação
st.set_page_config(page_title="Recordações de um amor", layout="wide")

# Página principal
st.sidebar.title("Navegue com moderação, para não se apaixonar ❤️")

# Digite o nome na barra lateral
name = st.sidebar.text_input("Digite o nome do amor da minha vida:")

# Definindo a função para exibir a galeria
def show_gallery(name):
    st.header('Retratos de um Amor: Memórias Eternas.❤️')
    st.text(f"Bem-vinda, meu amor {name}. Espero que goste desta pequena lembrança e que possamos viver o nosso amor da melhor maneira possível, todos os dias.")
    st.text('Cada Parte de Você, Sempre Comigo.')
    # Lista de imagens e legendas correspondentes
    images = [
        r"C:\Users\matheus.tonini\diaromantc\pb1.png",
        r"C:\Users\matheus.tonini\diaromantc\pb2.png",
        r"C:\Users\matheus.tonini\diaromantc\pb3.png",
        r"C:\Users\matheus.tonini\diaromantc\pb4.png", # Nova imagem
        r"C:\Users\matheus.tonini\diaromantc\pb6.png", # Nova imagem
        r"C:\Users\matheus.tonini\diaromantc\pb5.png", # Nova imagem
        r"C:\Users\matheus.tonini\diaromantc\pb8.png", # Nova imagem
        r"C:\Users\matheus.tonini\diaromantc\pb7.png"  # Nova imagem
    ]  
    captions = [
        "Eu escolho você hoje, escolho você todos os dias e sempre vou escolher você.Eu amo você do jeitinho é. ❤️", 
        "Você é alguém que vale a pena, vale a pena ficar ao seu lado. Encontrei a pessoa certa, e essa pessoa é você. ❤️", 
        "A melhor escolha que fiz na minha vida foi me apaixonar por você. ❤️",
        "Que nossas mãos sempre se encontrem, como foi no primeiro encontro, eu te amo demais meu benzinho❤️", 
        "O dia que te pedi em namoro, sempre vai ser por você, sempre foi por você, obrigado por me fazer tão bem. ❤️", 
        "O nossos sorriso, a nossa felicidade, o nosso amor, seja sempre leve e gostoso de se viver, a vida é linda ao seu lado. ❤️ ", 
        "Todas as barreiras que aparecerem em nossos caminhos, vamos conseguir vencê-las juntos. ❤️",
        "E-U-T-E-A-M-O, Meu Amô.❤️"  
    ]

    # Exibição das fotos em colunas
    col1, col2, col3, col4 = st.columns(4)

    for i, image_path in enumerate(images):
        with col1 if i % 4 == 0 else col2 if i % 4 == 1 else col3 if i % 4 == 2 else col4:
            image = Image.open(image_path)
            st.image(image, caption=captions[i], use_column_width=True)

# Função para exibir o quiz
def show_quiz():
    st.header("Quiz sobre Nós ❤️")
    st.text("Espero que você acerte todas as resposta :)")

    # Questões do quiz
    questions = [
        {
            "question": "Qual dia a gente se conheceu pessoalmente?",
            "options": ["18 de Dezembro", "23 de Dezembro", "22 de Dezembro", " de Dezembro"],
            "answer": "23 de Dezembro"
        },
        {
            "question": "Qual é a nossa música:",
            "options": ["Eu amo você - Tim Maia", "Só Nós Dois - Tim Bernardes", "My Baby - Russ", "Those Eyes - New West"],
            "answer": "Só Nós Dois - Tim Bernardes"
        },
        {
            "question": "Onde foi nosso primeiro encontro?",
            "options": ["Pastel", "Pizzaria", "Restaurante", "hamburgueria"],
            "answer": "hamburgueria"
        }
    ]

    # Apresenta as questões do quiz
    for i, question in enumerate(questions, 1):
        st.subheader(f"Pergunta {i}: {question['question']}")
        selected_option = st.radio("Escolha uma opção:", question["options"], key=i)
        if selected_option == question["answer"]:
            st.success("Resposta correta!")
        else:
            st.error("Resposta incorreta. Tente novamente.")

    st.text("Obrigado por ter participado, volte sempre")
    
    
def show_video():
    
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


# Função para exibir a carta de amor
def show_love_letter(name):
    st.header(f"Carta de Amor para {name} ❤️")
    st.write(f"Meu amor {name},")
    st.write("Hoje é dia dos namorados, 12 de Junho de 2024 e quero celebrar nosso amor da melhor maneira possivel, Que este lembrete gentil seja apenas o começo de um dia repleto de amor e carinho. 💑🏻")
    st.write("Estar ao seu lado é incrível. Cada momento juntos me faz sentir a pessoa mais sortuda do mundo. Seus beijos, abraços e carinhos significam tudo para mim. Espero que nosso amor seja abençoado a cada dia. Quero passar o resto da minha vida com você. 👰🏻‍")
    st.write( "Você é a pessoa mais linda que já conheci eu sou completamente apaixonado por você e nunca vou me cansar de mostrar o quanto te amo todos os dias. Você é tudo para mim, minha melhor amiga, minha melhor companheira. Obrigado por estar ao meu lado, por me ouvir, por sonhar e querer construir um futuro ao meu lado. Sua luz e energia são de outro mundo, e seu sorriso é a coisa mais linda que já vi. 🥰")
    st.write("Que Deus continue te abençoando, te protegendo e te guiando em todos os momentos. Acredito em você e em cada um dos seus sonhos. Que você alcance todas as suas metas e conquiste tudo o que deseja nesta vida. Que a mão do Senhor esteja sempre sobre nós, abençoando nossos planos, nossas viagens e cada aventura nossa. Cada momento ao seu lado é precioso para mim, todos momentos nossos vou guardar eternamente em minhas memórias. Você tem um lugar muito especial no meu coração. ❤️👼🏼")
    st.write("Obrigado por ser você, por me amar e por fazer parte da minha vida. Eu te amo e nunca vou conseguir expressar em palavras o que eu sinto por você.")
    st.text("Com todo o meu amor, Matheus Tonini ❤️🦔")

# Aba lateral com a seleção de opções
tabs = ["Galeria", "Vídeo", "Carta", "Quiz"]
selected_tab = st.sidebar.radio("Escolha uma opção:", tabs)


# Verifica qual aba foi selecionada
if selected_tab == "Galeria":
    if name == "Ana Carolina":
        st.sidebar.success("Parabéns, você é amor da minha vida ❤️")
        show_gallery(name)
    else:
        st.text("Para continuar, preciso saber se você é a Ana Carolina :) ")
        st.sidebar.warning("Desculpe, esta seção é apenas para Ana Carolina. 😡")
elif selected_tab == "Vídeo":
    if name == "Ana Carolina":
        show_video()
    else:
        st.text("Para continuar, preciso saber se você é a Ana Carolina :)")
        st.sidebar.warning("Desculpe, esta seção é apenas para Ana Carolina. 😡")
elif selected_tab == "Carta":
    if name == "Ana Carolina":
        show_love_letter(name)
    else:
        st.text("Para continuar, preciso saber se você é a Ana Carolina :)")
        st.sidebar.warning("Desculpe, esta seção é apenas para Ana Carolina. 😡")
elif selected_tab == "Quiz":
    if name == "Ana Carolina":
        show_quiz()
    else:
        st.text("Para continuar, preciso saber se você é a Ana Carolina :)")
        st.sidebar.warning("Desculpe, esta seção é apenas para Ana Carolina. 😡")
else:
    st.write(f"Conteúdo da {selected_tab}")
