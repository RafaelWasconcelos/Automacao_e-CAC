import streamlit as st
import Classes as cl 
import time # Para simular um pequeno atraso
from Classes import Autenticacao

# --- Configuração da Página Streamlit ---
st.set_page_config(
    page_title="Automação e-CAC",
    layout="centered", # Ou "wide" se preferir mais espaço
    initial_sidebar_state="collapsed"
)

# --- Seção de Cabeçalho ---
st.title("🤖 Automação e-CAC")
st.markdown("Bem-vindo(a) à ferramenta de automação para consulta de dívidas na Receita Federal (e-CAC).")
st.markdown("Esta aplicação visa agilizar o processo de levantamento de inscrições para advogados tributaristas.")

st.markdown("---")

# --- Seção de Login ---
st.subheader("Login e Autenticação")
st.write("Para iniciar o processo de coleta de dados, você precisa primeiro autenticar-se no portal e-CAC.")
st.info("⚠️ Ao clicar em 'Login no e-CAC', uma **nova janela do navegador será aberta**. Por favor, realize seu login através do **Gov.br** ou **Certificado Digital** nessa nova janela.")

# Botão para iniciar o processo de login
if st.button("🔑 Login no e-CAC", help="Clique para abrir a página de login do e-CAC."):
    with st.spinner("Preparando para abrir a página de login do e-CAC..."):
        time.sleep(2) # Simulate a small delay for preparation
        if Autenticacao.autenticacao.abrir_navegador():
            st.success("Nova janela do navegador aberta! Por favor, prossiga com o login no Gov.br/Certificado Digital na janela que apareceu.")
            st.warning("⚠️ **Volte para esta tela (Streamlit) após concluir o login** para prosseguir com a inserção do CPF/CNPJ.")

            # --- Espaço reservado para os próximos passos (a serem implementados depois) ---
            # Após o login manual bem-sucedido, o usuário deve retornar aqui.
            # Podemos simular o próximo passo ou indicar para onde ir em seguida.
            st.markdown("---")
            st.subheader("Passo 2: Inserção do CPF/CNPJ (Após Login)")
            st.write("Após realizar o login na janela do e-CAC, retorne aqui para inserir o CPF/CNPJ do cliente e iniciar a coleta.")
            
            cpf_cnpj_input = st.text_input(
                "Insira o CPF/CNPJ do cliente (somente números):",
                placeholder="Ex: 12345678900 ou 12345678000190",
                max_chars=14,
                key="cpf_cnpj_after_login" # Use a unique key if multiple text_inputs
            )
            
            if st.button("🚀 Iniciar Coleta de Dívidas", help="Inicia a coleta de dados após o login no e-CAC."):
                if not cpf_cnpj_input:
                    st.error("Por favor, insira um CPF/CNPJ para iniciar a coleta.")
                else:
                    st.success(f"Coleta iniciada para {cpf_cnpj_input}! (Lógica de scraping virá aqui)")
                    # Aqui você chamaria a lógica principal de scraping com o CPF/CNPJ
                    # e exibiria os resultados/botões de download.
                    
# --- Footer Section ---
st.markdown("---")
st.caption("Desenvolvido para advogados tributaristas por NPath Labs.")