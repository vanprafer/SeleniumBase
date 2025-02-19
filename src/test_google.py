from pytest_dependency import depends
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
import pytest
import undetected_chromedriver
from selenium.webdriver.chrome.options import Options

username = ""
password = ""

class GoogleTest(BaseCase):

    def tearDown(self):
        pass

    @pytest.mark.dependency(name="google_logger")
    def test_1_google_logger(self):
        # Modificamos Chrome para que no sea detectado como un bot
        self.driver = undetected_chromedriver.Chrome()
        # Maximizamos la pestaña
        self.driver.maximize_window()
        # Vamos a la url de login
        self.get("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://www.google.com/&ec=GAZAmgQ")
        # Introducimos el usuario
        self.type("//input[@type='email']", username)
        # Aceptar
        self.click("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
        # Introducimos la contraseña
        self.type("input.whsOnd.zHQkBf", password)
        # Aceptar
        self.click("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
        # Esperamos a que aparezca la barra de búsqueda
        self.wait_for_element("#APjFqb")
        # Buscamos "Gatitos"
        self.type("#APjFqb", "Gatitos")
        # Enviamos el input
        self.click("input.gNO89b")


    @pytest.mark.dependency(name="logout")
    def test_logout(self):
        pass