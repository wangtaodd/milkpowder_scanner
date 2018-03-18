class product(object):
    def __init__(self):
        self.url = ""
        self.name = ""
        self.isAvailable = False
        self.isAvailableLast = False
        self.maxAmount = 0

    def setUrl(self, url):
        self.url = url
        return self.url

    def setName(self, name):
        self.name = name
        return self.name

    def setIsAvailable(self, isAvailable):
        self.isAvailable = isAvailable
        return self.isAvailable

    def setMaxAmount(self, num):
        self.maxAmount = num
        return self.maxAmount

