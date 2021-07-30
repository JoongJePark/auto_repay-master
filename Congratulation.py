class JS_Yoo:
    def __init__(self, univ, degree):
        self.univ = univ
        self.degree = degree
    def message(self, name):
        print("Hello", self.univ)
        print(self.degree, name)
Congrats = JS_Yoo("UCI", "Ph.D")
Congrats.message("Yoo")



    