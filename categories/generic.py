
class Generic:

    #TODO: Potentially replace search with the following:
    # eles = browser.find_elements_by_xpath("//*[starts-with(@id, \"jsc\")]")
    # that should contain all non-photos selections
    # for ele in eles:
    #   id = ele.get_attribute('id')
    #   parent = ele.find_element_by_xpath("./..")
    #   parentsChildren = parent.find_elements_by_css_selector("*")
    #   parentsChildren[0] should be the label of the item
    #   parentsChildren[1] should be the item to be filled in


    def add_photos(self, browser):
        #Button to open seelctor
        #xpath = /html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div
        return

    #Ids may be in base36 (i.e., jsc_c_19) may change to jsc_c_1b (+2)
    #Base
    def title(self, browser, title):
        xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[3]/div/div/label/div/div'
        xppth = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div/label/div/div'
        xppth = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div/label/div/div'
        fill_textbox(browser, xpath, title, "Title")

    #+2
    def price(self, browser, price):
        xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[4]/div[1]/div/label/div/div'
        fill_textbox(browser, xpath, price, "Price")

    #+4
    def category(self, browser, selection):
        #dropdown
        xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div/label/div/div[1]'
        select_dropdown(browser, xpath, selection, "Category")

    #+2
    def condition(self, browser):
        #searchable dropdown
        xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[6]/div/div/div/label/div/div[1]'
        return

    #+2 
    def description(self, browser, description):
        xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[7]/div/div/label/div/div'
        fill_textbox(browser, xpath, description, "Description")

    def fill_all_sections(self, browser):
        self.add_photos()
        self.title()
        self.price()
        self.category()
        self.condition()
        self.description()


def fill_textbox(browser, xpath, text, assertLabel):
    containerDiv = browser.find_element_by_xpath(xpath)
    divChildren = containerDiv.find_elements_by_xpath(".//*")
    # divchildren[0] = the label
    # divchildren[1] = the textbox
    
    if(assertLabel != None):
        assert(divChildren[0].text == assertLabel)
        print("Filling ", assertLabel, " with ", text)

    divChildren[1].send_keys(text)

def select_dropdown(browser, xpath, selection, assertLabel):
    containerDiv = browser.find_element_by_xpath(xpath)
    divChildren = containerDiv.find_elements_by_xpath(".//*")

    if(assertLabel != None):
        assert(divChildren[0].text == assertLabel)
        print("Selecting", selection, " in ", assertLabel)

    divChildren[1].send_keys(selection)

