import streamlit as st
import Classes as cl 
import time # For simulating a small delay
from Classes import Autenticacao

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Automação e-CAC",
    layout="centered", # Or "wide" if you prefer more space
    initial_sidebar_state="collapsed"
)

# --- Header Section ---
st.title("🤖 Automação e-CAC")
st.markdown("Bem-vindo(a) à ferramenta de automação para consulta de dívidas na Receita Federal (e-CAC).")
st.markdown("Esta aplicação visa agilizar o processo de levantamento de inscrições para advogados tributaristas.")

st.markdown("---")

# --- Login Section ---
st.subheader("Login e Autenticação")
st.write("Para iniciar o processo de coleta de dados, você precisa primeiro autenticar-se no portal e-CAC.")
st.info("⚠️ Ao clicar em 'Login no e-CAC', uma **nova janela do navegador será aberta**. Por favor, realize seu login através do **Gov.br** ou **Certificado Digital** nessa nova janela.")

# Button to trigger the login process
if st.button("🔑 Login no e-CAC", help="Clique para abrir a página de login do e-CAC."):
    with st.spinner("Preparando para abrir a página de login do e-CAC..."):
        time.sleep(2) # Simulate a small delay for preparation
        if Autenticacao.autenticacao.abrir_navegador():
            st.success("Nova janela do navegador aberta! Por favor, prossiga com o login no Gov.br/Certificado Digital na janela que apareceu.")
            st.warning("⚠️ **Volte para esta tela (Streamlit) após concluir o login** para prosseguir com a inserção do CPF/CNPJ.")

            # --- Placeholder for next steps (to be implemented later) ---
            # After successful manual login, the user would come back here.
            # We can simulate the next step or indicate where to go next.
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
                    # Here you'd call the main scraping logic with the CPF/CNPJ
                    # and display results/download buttons.
                    
# --- Footer Section ---
st.markdown("---")
st.caption("Desenvolvido para advogados tributaristas por NPath Labs.")