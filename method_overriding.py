class Father:
    def sleep(self):
        print("Sleeping... from 9:00 PM to 5:00 AM")
class Son(Father):
    # pass
    def sleep(self):
        print("Sleeping... from 9:00 PM to 12:00 AM")

son = Son()
son.sleep()