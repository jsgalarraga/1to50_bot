import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Game1to50Bot:
    def __init__(self):
        with open('chrome_driver_path.json', 'r') as f:
            path = json.load(f)
        options = Options()
        options.add_argument('start-maximized')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=path)
        self.driver.get('http://zzzscore.com/1to50/en/')
        sleep(1)
        

    def play(self):
        grid = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]")
        button_dict = {}
        button_dict2 = {}
        for tile_id in range(1, 26):
            button = grid.find_element_by_xpath("div[{}]".format(tile_id))
            button_dict[button.text] = button
        
        for number in range(1, 26):
            button_dict[str(number)].click()
        
        sleep(0.15) # Necesario para que al siguiente bucle le de tiempo a refrescar el texto

        for _, button in button_dict.items():
            button_dict2[button.text] = button

        for number in range(26, 51):
            button_dict2[str(number)].click()

        sleep(30)


bot = Game1to50Bot()
bot.play()
