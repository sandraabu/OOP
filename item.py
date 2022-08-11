class Item():

    def __init__(self):
        self.name = None
        self.description = None
        self.shape = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def get_shape(self):
        return self.shape

    def set_shape(self, item_shape):
        self.shape = item_shape