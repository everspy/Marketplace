from selenium.webdriver.common.keys import Keys
class Generic:

    #TODO: Potentially replace search with the following:
    # XPaths seem to change slightly.
    # eles = browser.find_elements_by_xpath("//*[starts-with(@id, \"jsc\")]")
    # that should contain all non-photos selections
    # for ele in eles:
    #   id = ele.get_attribute('id')
    #   parent = ele.find_element_by_xpath("./..")
    #   parentsChildren = parent.find_elements_by_css_selector("*")
    #   parentsChildren[0] should be the label of the item
    #   parentsChildren[1] should be the item to be filled in


    base = None

    offsets = {
        'title': 0,
        'price': 2,
        'category': 6,
        'condition': 8,
        'description': 2,
    }

    class Condition():
        new = 0
        like_new = 1
        good = 2
        fair = 3

    # Finds the ID of the title section. The offsets are based off of this id.
    # Example id jsc_c_##
    def find_base(self, browser):
        eles = browser.find_elements_by_xpath("//*[starts-with(@id, \"jsc\")]")

        for ele in eles:
            id = ele.get_attribute('id')
            parent = ele.find_element_by_xpath("./..")
            parentsChildren = parent.find_elements_by_css_selector("*")

            if len(parentsChildren) > 0 and parentsChildren[0].text == 'Title':
                print("Found base with id=", id)
                self.base = id
                return self.base

    # Returns id of section when passed name of the section. Name should match value stored in offsets
    def get_id(self, name):
        if self.base == None:
            print("Cannot call get_id before base has been found!")
            return None

        base_split = self.base.split('_')
        adjusted_val = int(base_split[2], 36) + self.offsets[name]

        id = "{}_{}_{}".format(base_split[0], base_split[1], base36encode(adjusted_val))

        return id


    def add_photos(self, browser):
        #Button to open selector
        #xpath = /html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div
        return

    #Ids may be in base36 (i.e., jsc_c_19) may change to jsc_c_1b (+2)
    #Base
    def title(self, browser, title):
        #xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[3]/div/div/label/div/div'
        #xppth = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div/label/div/div'
        
        id = self.get_id('title')
        fill_textbox(browser, id, title, "Title")

    #+2
    def price(self, browser, price):
        #xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[4]/div[1]/div/label/div/div'
        id = self.get_id('price')
        fill_textbox(browser, id, price, "Price")

    #+4
    def category(self, browser, selection):
        #dropdown
        #xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div/label/div/div[1]'
        id = self.get_id('category')
        select_search_dropdown(browser, id, selection, "Category")

    #+2
    def condition(self, browser, condition):
        #searchable dropdown
        #xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[6]/div/div/div/label/div/div[1]'
        id = self.get_id('condition')
        select_dropdown(browser, id, condition, 'Condition')
    #+2 
    def description(self, browser, description):
        #xpath = '/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[7]/div/div/label/div/div'
        id = self.get_id('description')
        fill_textbox(browser, id, description, "Description")

    def fill_all_sections(self, browser):
        self.find_base(browser)
        self.add_photos(browser)
        self.title(browser, 'TitleFill')
        self.price(browser, '1543')
        self.category(browser, 'Cell Phones')
        self.condition(browser, 'Like New')
        self.description(browser, "Good condition")


def fill_textbox(browser, id, text, assertLabel):
    print("attempting to fill {} with id={} with data={}".format(assertLabel, id, text))
    textbox = browser.find_element_by_id(id)
    #divChildren = containerDiv.find_elements_by_xpath(".//*")
    ## divchildren[0] = the label
    ## divchildren[1] = the textbox
    
    if(assertLabel != None):
        parent = textbox.find_element_by_xpath("./..")
        label = parent.find_elements_by_css_selector("*")[0]
        assert(label.text == assertLabel)
        print("Filling ", assertLabel, " with ", text)

    textbox.send_keys(text)

def select_search_dropdown(browser, id, selection, assertLabel):
    selectBox = browser.find_element_by_id(id)
    #containerDiv = browser.find_element_by_xpath(xpath)
    #divChildren = containerDiv.find_elements_by_xpath(".//*")

    if(assertLabel != None):
        parent = selectBox.find_element_by_xpath("./..")
        label = parent.find_elements_by_css_selector("*")[0]
        assert(label.text == assertLabel)
        print("Selecting", selection, " in ", assertLabel)

    selectBox.send_keys(selection)
    selectBox.send_keys(Keys.UP)
    selectBox.send_keys(Keys.ENTER)

def select_dropdown(browser, id, selection, assertLabel):
    selectBox = browser.find_element_by_id(id)
    #containerDiv = browser.find_element_by_xpath(xpath)
    #divChildren = containerDiv.find_elements_by_xpath(".//*")

    if(assertLabel != None):
        parent = selectBox.find_element_by_xpath("./..")
        label = parent.find_elements_by_css_selector("*")[0]
        assert(label.text == assertLabel)
        print("Selecting", selection, " in ", assertLabel)

    #TODO: Select box using up/down arrows to find correct position
    selectBox.send_keys(selection)
    selectBox.send_keys(Keys.UP)
    selectBox.send_keys(Keys.ENTER)

def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, int):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36



