class footerpage:
    def __init__(self, page):
        self.page = page
#webdevelopement:
        self.cms_website_dev = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommerce_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.custome_web_portal_dev = page.locator(
            '//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

# UI/UX Design :
        self.mobile_app_design = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_app_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_identity_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

# App Developement :

        self.ios_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.android_app_dev = page.locator(
            '//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.hybrid_mobile_dev = page.locator(
            '//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_platform_app_dev = page.locator(
            '//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive_web_app_dev = page.locator(
            '//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

# Graphics Designing :

        self.logo_design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner_design = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging_design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business_cards_design = page.locator(
            '//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.footer_web_developement_links = [self.cms_website_dev, self.ecommerce_dev, self.custome_web_portal_dev]
        self.website_dev = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')

        self.footer_UI_Links = [self.mobile_app_design, self.responsive_app_design, self.brand_identity_design]

        self.footer_app_developement_links = [self.ios_app_dev, self.android_app_dev, self.hybrid_mobile_dev,
                                              self.cross_platform_app_dev, self.progressive_web_app_dev]
        self.android_app_dev2 = page.locator(
            '//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_dev = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')

        self.footer_android_app_dev = [self.android_app_dev2, self.app_dev]

        self.footer_graphics_design = [self.logo_design, self.banner_design, self.packaging_design,
                                       self.business_cards_design]

# Follow Us
        self.facebook = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.linkedin = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.instagram = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.pinterest = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.x_com = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
        self.youtube = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
        self.quora = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')

        self.follow_us_links = [self.facebook, self.linkedin, self.instagram,
                                self.pinterest, self.x_com, self.youtube, self.quora]


    def webelement_submenus_clicking(self):
        for k in self.footer_web_developement_links:
            if k == self.ecommerce_dev:
                k.click()
                self.page.go_back()
                self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
                with self.page.expect_popup() as popup_info:
                    self.website_dev.click()
                    new_tab = popup_info.value
                    new_tab.wait_for_load_state()
                    print(new_tab.title())
                    new_tab.close()
                    continue
            else:
                k.click()
                self.page.wait_for_timeout(2000)
                self.page.go_back()


    def uiux_submenus_clicking(self):
        for k in self.footer_UI_Links:
            k.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()



    def appdevelopement_submenus_clicking(self):
        for k in self.footer_app_developement_links:
            if k == self.android_app_dev:
                k.click()
                self.page.go_back()
                self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]').click()

                for i in self.footer_android_app_dev:
                    with self.page.expect_popup() as popup_info:
                        i.click()
                        new_tab = popup_info.value
                        new_tab.wait_for_load_state()
                        print(new_tab.title())
                        new_tab.close()
                        continue
            else:
                k.click()
                self.page.wait_for_timeout(2000)
                self.page.go_back()


    def graphics_submenus_clicking(self):
        for k in self.footer_graphics_design:
            k.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()

    def followuslink_submenus_clicking(self):
        for k in self.follow_us_links:
            with self.page.expect_popup() as popup_info:
                k.scroll_into_view_if_needed(timeout=10000)
                k.click()
                new_tab = popup_info.value
                new_tab.wait_for_load_state()
                print(new_tab.title())
                new_tab.close()
            self.page.wait_for_timeout(2000)

