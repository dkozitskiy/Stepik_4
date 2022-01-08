from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_IN_PP = (By.CSS_SELECTOR, "div.product_main h1")
    MES_ABOUT_ADD = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_IN_PP = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена в карточке товара
    MES_TOTAL = (By.CSS_SELECTOR, "div.alertinner p strong")  # Цена в сообщении


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, "div.basket-mini_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    CONTINUE_SHOP_HREF = (By.CSS_SELECTOR, "div.content>div>p>a")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".table .total")
