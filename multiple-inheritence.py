class A:
    def hi(self):
        print("hi from A")


class B:
    def hi(self):
        print("hi from B")

    def here(self):
        print("here in B")


class C(A, B):
    pass


c = C()
c.hi()
c.here()
