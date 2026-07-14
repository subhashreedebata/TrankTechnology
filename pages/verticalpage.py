class verticalpage:
    def __init__(self, page):
        self.page = page

        self.verticals = page.locator('(//a[text() = "Verticals"])[1]')

#Trading
        self.trading = page.locator('//strong[text()="Trading"]')
        self.trading_stock = page.locator('(//a[text()="Stock Trading"])[1]')
        self.trading_algo = page.locator('//a[text()="Algo Trading"]')
        self.trading_paper = page.locator('//a[text()="Paper Trading"]')
        self.trading_custom = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.trading_cfd = page.locator('//a[text()="CFD Trading"]').first
        self.trading_web_portal = page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.trading_trading_app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trading_list = [self.trading_stock,self.trading_algo, self.trading_paper, self.trading_custom, self.trading_cfd, self.trading_web_portal,
                        self.trading_trading_app_dev]

#Retail & Ecommerce
        self.retail_ecommerce = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.retail_ecommerce_website_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.retail_ecommerce_app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.retail_list = [self.retail_ecommerce_website_dev, self.retail_ecommerce_app_dev]

#HealthCare
        self.healthcare = page.locator('//strong[text()="Healthcare"]')
        self.healthcare_diet = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthcare_tracking_app = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_list = [self.healthcare_diet, self.healthcare_tracking_app]

#Fintech
        self.fintech = page.locator('//strong[text()="Fintech"]')
        self.fintech_pos_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fintech_crypto = page.locator('(//a[text() = "Crypto"])[1]')

        self.fintech_list = [self.fintech_pos_dev, self.fintech_crypto]

#CustomApp
        self.custom_app = page.locator('//strong[text() ="Custom App"]')
        self.custom_desktop_app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.custom_CRM_Dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.custom_hrm_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.custom_erp_app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.custom_travel = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.custom_elearning = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.custom_dating_app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.custom_real_estate = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_CRM_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_list = [self.custom_desktop_app_dev, self.custom_CRM_Dev, self.custom_hrm_dev,
                            self.custom_erp_app_dev,
                            self.custom_travel, self.custom_elearning, self.custom_dating_app_dev,
                            self.custom_real_estate,
                            self.custom_CRM_dev]

    def trading_submenus_clicking(self):
        for i in self.trading_list:
            self.verticals.hover()
            self.trading.hover()
            if i.is_visible():
                i.click()
                self.page.wait_for_timeout(1000)
                self.page.go_back()
            else:
                self.page.refresh()
            # i.click()
            # self.page.wait_for_timeout(1000)
            # self.page.go_back()



    def retail_submenus_clicking(self):
        for i in self.retail_list:
            self.verticals.hover()
            self.retail_ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def healthcare_submenus_clicking(self):
        for i in self.healthcare_list:
            self.verticals.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def fintech_submenus_clicking(self):
        for i in self.fintech_list:
            self.verticals.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def customapp_submenus_clicking(self):
        for i in self.custom_list:
            self.verticals.hover()
            self.custom_app.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()