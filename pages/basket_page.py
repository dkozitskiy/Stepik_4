from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_BASKET), \
            "The basket isn't empty"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOP_HREF), \
            "There isn't basket's empty message while it's expected"