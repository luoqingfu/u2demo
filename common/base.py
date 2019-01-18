

class Base():
    def __init__(self, driver):
        self.d = driver
        self.width = self.get_windowsize()[0]
        self.height = self.get_windowsize()[1]

    def get_windowsize(self):
        '''
        获取屏幕尺寸
        :return:
        '''
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[1])
        return width, height

    def click(self, element):
        self.d(resourceId=element).click()

    def send_keys(self, element, keys):
        self.d(resourceId=element).set_text(keys)
