import time
from selenium import webdriver
from twilio.rest import Client
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


class JuiceBot:
    def __init__(self):
        PROXY = "138.68.240.218:8080"  # IP:PORT or HOST:PORT
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.browser = webdriver.Chrome()
        self.found = False
        self.targetSize="8"
        #MUST ENTER IN YOUR OWN TWILIO INFORMATION HERE
        account_sid = ''
        auth_token = ''
        #self.client = Client(account_sid, auth_token)

    def monitor(self,phone):
     self.browser.get('https://juicestore.com/collections/new-arrivals/')
     self.keyword = "nite jogger"

     #select_fr = Select(self.browser.find_element_by_class_name("site-header__currency-picker"))
     #select_fr.select_by_index(9)

     # self.browser.find_element_by_link_text("W Nike Air Force 1 '07").click()
     # check amount of products and save
     time.sleep(1)
     while self.found!=True:


         self.links = self.browser.find_elements_by_css_selector("a.grid-view-item__link.grid-view-item__image-container.full-width-link")
         #self.amount = self.browser.find_element_by_class_name("search-results__header")
         self.name = self.browser.find_elements_by_class_name("grid-view-item__title")
         #self.titles = self.browser.find_elements_by_class_name("product__vendor")
         self.shoes = dict(zip(self.name, self.links))


         for info, link in self.shoes.items():
             # edge case, if no Af1 do nothing and refresh
             # check for clot in name, if there send text and click on shoe.
             print(info.text)

             if self.keyword in info.text.lower():
                 # send text, click on link
                 print("SHOE FOUND!....Notifying SASSO")

                 ''' UNCOMMENT ONCE TWILIO IS SETUP
                 message = self.client.messages \
                     .create(body="YO THESE JUST DROPPPED! "+info.text+" " + link.get_attribute("href")
                             ,from_='+13126355487',to=phone
                 )
                 '''
                 time.sleep(.1)
                 self.sold = self.browser.find_elements_by_class_name("unavailable-size")
                 print("Opening "+info.text)
                 self.shoes[info].click()
                 self.found=True
                 break

         time.sleep(2)
         self.browser.refresh()
     print("Sizes avalible")

     self.sizes = self.browser.find_elements_by_class_name("product-option__value")
     #res = list((Counter(self.sizes) - Counter(self.sold)).elements())
     print("size ready")
     for s in self.sizes:
         print(s.text)
     for i in self.sizes:

         if self.targetSize in i.text:
             print("Carting a size "+ self.targetSize)
             i.click()
             break
         '''
         else:
             print(self.targetSize +" is sold out, will cart a size "+self.sizes[i].text)
             i=+1
             self.sizes[i].click()
             break
         '''

     print("Adding item to cart")
     wait = WebDriverWait(self.browser, 10)
     self.cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.btn.product-form__cart-submit.js-add-to-card")))
     self.cart.click()

     wait = WebDriverWait(self.browser, 10)
     self.miniCart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input.btn.btn__checkout")))
     self.miniCart.click()


     print("auto filling shipping....")
     # AUTO FIL PORTION, need to refactor
     wait = WebDriverWait(self.browser, 10)
     self.email = wait.until(EC.element_to_be_clickable((By.ID,"checkout_email")))
     self.email.clear()
     self.email.send_keys("hercules@gmail.com")

     time.sleep(.1)
     wait = WebDriverWait(self.browser, 10)
     first = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_first_name")))
     first.clear()
     first.send_keys("Jonny")

     time.sleep(.1)
     wait = WebDriverWait(self.browser, 10)
     second = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_last_name")))
     second.clear()
     second.send_keys("record")

     time.sleep(.01)
     wait = WebDriverWait(self.browser, 10)
     address = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_address1")))
     address.clear()
     address.send_keys("53 han st")

     time.sleep(.1)
     wait = WebDriverWait(self.browser, 10)
     city = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_city")))
     city.clear()
     city.send_keys("Colon")

     time.sleep(.2)
     wait = WebDriverWait(self.browser, 10)
     code = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_zip")))
     code.clear()
     code.send_keys("21045")

     time.sleep(1)
     wait = WebDriverWait(self.browser, 10)
     phone = wait.until(EC.element_to_be_clickable((By.ID, "checkout_shipping_address_phone")))
     phone.clear()
     phone.send_keys("3452304323")

     time.sleep(.2)
     shipping = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.step__footer__continue-btn.btn ")))
     shipping.click()


     print("Filling in payment info...")
     wait = WebDriverWait(self.browser, 10)
     pay = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.step__footer__continue-btn.btn ")))
     pay.click()
     #witch to iframe
     iframe = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/div/div[1]/iframe")
     self.browser.switch_to.frame(iframe)
     wait = WebDriverWait(self.browser, 10)
     num = wait.until(EC.element_to_be_clickable((By.ID,"number")))
     num.clear()
     time.sleep(1)
     num.send_keys("2343923483726184")


     self.browser.switch_to.default_content()

     iframe = self.browser.find_element_by_xpath(
         "/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[2]/div/div/iframe")
     self.browser.switch_to.frame(iframe)
     cardName = self.browser.find_element_by_id("name")
     cardName.clear()
     cardName.send_keys("Johnny record")

     time.sleep(.1)
     self.browser.switch_to.default_content()


     iframe = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[3]/div/div/iframe")
     self.browser.switch_to.frame(iframe)
     wait = WebDriverWait(self.browser, 10)
     exp = wait.until(EC.element_to_be_clickable((By.ID,"expiry")))
     exp.clear()
     time.sleep(.82)
     exp.send_keys("11/25")

     self.browser.switch_to.default_content()
     time.sleep(.2)


     iframe = self.browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div[2]/div[2]/fieldset/div[3]/div[3]/div[4]/div/div[1]/iframe")
     self.browser.switch_to.frame(iframe)
     wait = WebDriverWait(self.browser, 10)
     sec = wait.until(EC.element_to_be_clickable((By.ID,"verification_value")))
     sec.clear()
     time.sleep(.1)
     sec.send_keys("976")

     self.browser.switch_to.default_content()

     #select same address
     same = self.browser.find_element_by_id("checkout_different_billing_address_false").click()

     wait = WebDriverWait(self.browser, 10)
     finalPay = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.step__footer__continue-btn.btn")))
     finalPay.click()
     print("CHECKING OUT!...")







bot = JuiceBot()
bot.monitor("5552345555")#phone number for Twilio

