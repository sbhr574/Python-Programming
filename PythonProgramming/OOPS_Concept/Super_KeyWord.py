class rik:
    def roy(self):
        print("Rik khub valo.")

    def bye(self):
        print("bye from rik")

class rai(rik):
    def roy(self):
        super().roy()
        super(rai, self).bye()
        print("rai khub valo.")

obj = rai()
obj.roy()