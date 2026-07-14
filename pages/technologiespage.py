class technologiespage:
    def __init__(self, page):
        self.page = page

        self.technologies = page.locator('(//a[text() = "Technologies"])[1]')

        self.ecomm_dev = page.locator('//strong[text()="eCommerce Development"]')
        self.magneto = page.locator('//a[text()="Magento Development"]')
        self.opencart = page.locator('(//a[text()="Opencart Development"])[1]')
        self.codeigniter = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.wordPress = page.locator('(//a[text()="WordPress Development"])[1]')
        self.BigCommerce = page.locator('(//a[text()="Big Commerce"])[1]')
        self.Shopify = page.locator('(//a[text()="Shopify Development"])[1]')
        self.CS_Cart = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.Node_JS = page.locator('(//a[text()="Node JS Development"])[1]')
        self.nopcommerce = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Woo_Commerce = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.Laravel = page.locator('(//a[text()="Laravel Development"])[1]')
        self.Prestashop = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.Drupal = page.locator('(//a[text()="Drupal Development"])[1]')
        self.Wix = page.locator('(//a[text()="Wix Development"])[1]')
        self.Joomla = page.locator('(//a[text()="Joomla Development"])[1]')
        self.React_JS = page.locator('(//a[text()="React JS Development"])[1]')
        self.Express_JS = page.locator('(//a[text()="Express JS Development"])[1]')

        self.ecomm_develop_list = [self.magneto, self.opencart, self.codeigniter, self.wordPress,
                                   self.BigCommerce, self.Shopify, self.CS_Cart, self.Node_JS,
                                   self.nopcommerce, self.Woo_Commerce, self.Laravel,
                                   self.Prestashop, self.Drupal, self.Wix, self.Joomla, self.React_JS, self.Express_JS]

        self.mobile_app = page.locator('//strong[text()="Mobile App Development"]')
        self.react_mobile = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamrian = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.iconic = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appoint_book = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.artificial_Intelligence = page.locator('//strong[text()="Artificial Intelligence"]')

        self.mobile_app_list = [self.react_mobile, self.enterprise, self.xamrian,
                                self.kotlin, self.flutter, self.iconic, self.swift,
                                self.appoint_book, self.artificial_Intelligence]

    def ecomdev_submenus_clicking(self):
        for i in self.ecomm_develop_list:
            self.technologies.hover()
            self.ecomm_dev.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
    def mobile_app_submenus_clicking(self):
        for i in self.mobile_app_list:
            self.technologies.hover()
            self.mobile_app.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()



