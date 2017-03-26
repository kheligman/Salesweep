__author__ = 'Kathryn'

class Item(object):
    name = ""
    link = ""
    picLink = ""
    price = ""
    origPrice = ""

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __str__(self):
        return str(self.name)+" "+str(self.link)

