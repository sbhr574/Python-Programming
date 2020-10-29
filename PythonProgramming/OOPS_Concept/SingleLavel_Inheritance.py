class Base:
    fname = 'Subhajit'
    def from_Base(self):
        print("Executing from base")

class child(Base):
    lname = 'Roy'
    def from_child(self):
        print("Executing from child")

c=child()
c.from_child()
c.from_Base()
print(c.fname)
print(c.lname)