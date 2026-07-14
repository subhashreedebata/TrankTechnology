class abt_blog_portfolio_page:
    def __init__(self, page):
        self.page = page
        self.about_us = page.locator('(//a[text()="About us"])[1]')
        self.blog = page.locator('(//a[text()="Blog"])[1]')
        self.portfolio = page.locator('//a[text()="Portfolio"]')

        self.abp_list = [self.about_us, self.blog, self.portfolio]

    def abp_clicking(self):
        for i in self.abp_list:
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()