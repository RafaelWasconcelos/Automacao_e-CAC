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
                st.session_state.driver.quit() # Close any existing driver if it's still open
            except Exception:
                pass
            st.session_state.driver = None

        try:
            options = uc.ChromeOptions()
            options.add_argument("--start-maximized") # Open browser maximized

            # Store the undetected driver in session state
            st.session_state.driver = uc.Chrome(options=options)
            
            # Navigate to the e-CAC login page
            st.session_state.driver.get("https://cav.receita.fazenda.gov.br/autenticacao/login")
            
            # elemento_govbr = st.session_state.driver.find_element("xpath", "//input[@alt='Acesso Gov BR']")
            # elemento_govbr.click()
            
            return True
        except Exception as e:
            st.error(f"Erro ao abrir o navegador para o e-CAC: {e}")
            st.session_state.driver = None
            return False
        