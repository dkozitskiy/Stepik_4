from .base_page import BasePage
from .locators import ProductPageLocators
from .basket_page import BasketPage


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_a_mes_with_title(self):
        assert self.is_element_present(*ProductPageLocators.MES_ABOUT_ADD), "Message about adding is not presented"

    def should_be_a_mes_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MES_TOTAL), "Message with total price is not presented"

    def compare_titles(self):
        title_in_m = self.browser.find_element(
            *ProductPageLocators.MES_ABOUT_ADD)
        title_in_pp = self.browser.find_element(
            *ProductPageLocators.TITLE_IN_PP)
        print(title_in_pp.text)
        print(title_in_m.text)
        assert title_in_pp.text == title_in_m.text, "The titles are not compared"

    def compare_prices(self):
        price_in_m = self.browser.find_element(
            *ProductPageLocators.MES_TOTAL)
        price_in_pp = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_PP)
        print(price_in_m.text)
        print(price_in_pp.text)
        assert price_in_pp.text == price_in_m.text, "The prices are not compared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MES_ABOUT_ADD), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MES_ABOUT_ADD), \
            "Success message isn't disappeared, but should be"