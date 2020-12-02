from generic import Generic

class Phone(Generic):

    def carrier(self):
        #Textbox id = jsc_c_98
        return

    def device_name(self):
        #Textbox id = jsc_c_9a
        return

    def fill_all_sections(self)
        super().fill_all_sections()
        self.carrier()
        self.device_name()

