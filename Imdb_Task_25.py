from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException

class Imdb:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # maximize the window
        self.driver.maximize_window()
        
        # implicitly to wait
        self.driver.implicitly_wait(20)
        
        # action function to use the live action in webpage
        self.action = ActionChains(self.driver)
        
        # use the url to send and get the infomation
        self.driver.get("https://www.imdb.com/search/name/")
        
        # webdriverWait is used to explicit wait
        self.wait = WebDriverWait(self.driver, 10)
        
    def Advance_name_search(self):
        try:
            """ i give the variable name to find the element"""
            
            # first we need to find and open the name dropdown function 
            name_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'nameTextAccordion'))).click()
            
            # loctate the input element and send the input key
            name_input_box = self.wait.until(ec.presence_of_element_located((By.NAME, 'name-text-input'))).send_keys("vijay")
            
            # first we need to find and open the birthday_date dropdown function
            birthday_date_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'birthDateAccordion'))).click()
            
            # loctate the input element and send the input key to date from
            date_from = self.wait.until(ec.presence_of_element_located((By.NAME, 'birth-date-start-input'))).send_keys('07-07-2023')
            
            # loctate the input element and send the input key to date to
            date_to = self.wait.until(ec.presence_of_element_located((By.NAME, 'birth-date-end-input'))).send_keys('24-04-2024')
            
            # first we need to find and open the birthday field open dropdown function
            Birthday_field_open = self.wait.until(ec.element_to_be_clickable((By.ID, 'birthdayAccordion'))).click()
            
            # loctate the input element and send the input key to inputField_birthday
            inputField_birthday = self.wait.until(ec.presence_of_element_located((By.NAME, 'birthday-input'))).send_keys('22-06')
            
            # first we need to find and open the Awards dropdown function
            Awards_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'awardsAccordion'))).click()
            
            # locate the best_actor_win button using xpath and click it
            best_actor_win = self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Best Actor-Winning"]')))
            
            # click the best_actor_win button using actionChains to click located element
            best_actor_win_button = self.action.move_to_element(best_actor_win).click().perform()

            
            # try to locate Page_topic_dropdown_field by using id locator
            page_topics = self.wait.until(ec.element_to_be_clickable((By.ID, 'pageTopicsAccordion'))).click()
            
            #FIND THE element place of birth xpath
            place_OF_birth = self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Place of birth"]')))
            
            # click place_birth button using actionChains to click element for select
            place_birth = self.action.move_to_element(place_OF_birth).click().perform()
            
            #FIND THE element place of search_within_topics
            search_within_topics = self.wait.until(ec.presence_of_element_located((By.ID, 'within-topic-dropdown-id')))
            
            # using Select class with select_by_value is used to identify that element
            select = Select(search_within_topics)
            
            #send the key to select the element BIRTH_PLACE
            brith_place = select.select_by_value('BIRTH_PLACE')
            
            #send the key to the element places_text
            places_text = self.wait.until(ec.presence_of_element_located((By.NAME, 'within-topic-input'))).send_keys("chennai")
            
            # find the drop down function for death_date_dropdown
            death_date_dropdown = self.wait.until(ec.element_to_be_clickable((By.ID, 'deathDateAccordion'))).click()
            
            #send the key death from and death to text
            death_from = self.wait.until(ec.presence_of_element_located((By.NAME, 'death-date-start-input'))).send_keys('22-06-1974')
            death_to = self.wait.until(ec.presence_of_element_located((By.NAME, 'death-date-end-input'))).send_keys('26-04-2024')
            
            # locate the element genders 
            gender = self.wait.until(ec.element_to_be_clickable((By.ID, 'genderIdentityAccordion'))).click()
            
            # cilck the male to select the gender
            male =self.wait.until(ec.presence_of_element_located((By.XPATH, '//span[text()="Male"]')))
            
            # after dropdown_opens the male
            gender_male = self.action.move_to_element(male).click().perform()
            
            # try to locate credits using id locator and click it
            credits = self.wait.until(ec.element_to_be_clickable((By.ID, 'filmographyAccordion'))).click()
            
            #send the text credits to fill the box
            text_credit = self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input'))).send_keys("nill")
            
            # adult names dropdown function
            adult_name = self.wait.until(ec.element_to_be_clickable((By.ID, 'adultNamesAccordion'))).click()
            
            # here we have radiobutton and if it is already clicked we want use coditional Staments to finish the process
            include_button = self.wait.until(ec.element_to_be_clickable((By.ID, 'include-adult-names')))
            
            #try to select the include button
            if include_button.is_selected():
                pass
            # if selected move to click 
            else:
                include_button.click()
                
            # to locate see_results button by using xpath element
            see_result = self.wait.until(ec.presence_of_element_located((By.XPATH, '//button/span[@class="ipc-btn__text"]')))
            
            # click the see results button
            self.action.move_to_element(see_result).click().perform()

        # to find the error from click_intercepted 
        except ElementClickInterceptedException as click_error:
            print(click_error)
            
        # to find the error from not_intercepted 
        except ElementNotInteractableException as not_interact:
            print(not_interact)

# to call the function
imdb_page_source = Imdb()
imdb_page_source.Advance_name_search()