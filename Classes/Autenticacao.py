import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

class autenticacao:
    
    @staticmethod
    def abrir_navegador():
        """
        Opens a new browser window and navigates to the e-CAC login page.
        Stores the driver in Streamlit's session state.
        """
        if 'driver' not in st.session_state:
            st.session_state.driver = None

        if st.session_state.driver:
            try:
                st.session_state.driver.quit() # feche qualquer driver que estiver aberto
            except Exception:
                pass
            st.session_state.driver = None

        try:
            options = uc.ChromeOptions()
            options.add_argument("--start-maximized") # abre o navegador maximizado 

            # Armazena o driver "undetected" no session_state
            st.session_state.driver = uc.Chrome(options=options)
            
            # Navega até a página de login do e-CAC
            st.session_state.driver.get("https://cav.receita.fazenda.gov.br/autenticacao/login")
            
            
            return True
        except Exception as e:
            st.error(f"Erro ao abrir o navegador para o e-CAC: {e}")
            st.session_state.driver = None
            return False
        