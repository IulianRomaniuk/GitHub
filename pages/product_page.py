from .base_page import BasePage
from .locators import BasketLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        
        
    def should_be_product_url(self):
        self.browser.current_url
        assert ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
        
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*BasketLocators.BASKET_FORM)
        add_to_basket.click()