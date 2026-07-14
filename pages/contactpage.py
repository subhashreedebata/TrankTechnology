class contactpage:
    def __init__(self,page):
        self.page = page
        self.contact = page.locator('(//a[text()="Contact us"])[1]')

        self.name = page.locator('(//input[@name="name"])[2]')
        self.email = page.locator('(//input[@name="email"])[2]')
        # self.send_OTP =page.locator('//button[text() = "Send OTP"]')
        # self.otp = page.locator('(//input[@name="otp"])[2]')
        self.company = page.locator('(//input[@name="company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone_number = page.locator('(//input[@name="phone"])[2]')
        self.message = page.locator('(//textarea[@name="message"])[2]')
        # self.robot = page.locator('(//div[@class="recaptcha-checkbox-border"])[1]')
        self.submit = self.page.locator('(//input[@type="submit"])[1]')


    def contact_clicking(self):
        self.contact.click()
        self.page.wait_for_timeout(1000)
        self.name.fill('Subhashree')
        self.email.fill('sim@gmail.com')
        # self.send_OTP.click()
        # self.otp.fill()
        self.company.fill('Merkle')
        self.service.select_option("App Development")
        self.phone_number.fill('9035198296')
        self.message.fill('I am trying to contact trank technology')
        # self.robot.click()
        # self.submit.click()

        self.page.wait_for_timeout(1000)
        self.page.go_back()