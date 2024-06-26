class rANS_old:
    def __init__(self):
        self.literki = []
        self.proba = []
        self.bagno = {}
        self.proba_d = {}
        self.range = 1

        self.encoded = 1
        self.decoded = ""

    def set_proba(self, probablilities):
        self.proba = probablilities

    def set_alfabet(self, alfabet):
        self.literki = alfabet

    def function(self):
        tmp = 0
        bagno = 1
        self.range = 0
        for i in range(len(self.literki)):
            self.bagno[self.literki[i]] = [tmp + bagno, bagno]
            tmp = tmp + self.proba[i]
            self.proba_d[self.literki[i]] = self.proba[i]
            bagno = bagno % 1

        self.range = tmp

    def code(self, message):
        val = 1
        print(message, "------------")
        for symbol in message:
            tmp = (val - 1 + self.bagno[symbol][1]) // self.proba_d[symbol]
            print(tmp)
            r = (val - 1 + self.bagno[symbol][1]) % self.proba_d[symbol] + 1 - self.bagno[symbol][1]
            print(r)
            tmp = tmp * self.range + r + self.bagno[symbol][0]
            print(tmp)
            val = tmp
        self.encoded = val
        return val

    def unode(self):
        pass

    def show_bagno(self):
        print("offset ", self.bagno)
        print("proba", self.proba_d)
        print("range_len", self.range)


###################
class rANS:
    def __init__(self):
        self.literki = []
        self.proba = []
        self.offset = {}
        self.proba_d = {}
        self.decode_d = {}
        self.range = 1

        self.encoded = 1
        self.decoded = ""

    def set_proba(self, probablilities):
        self.proba = probablilities

    def set_alfabet(self, alfabet):
        self.literki = alfabet

    def function(self):
        tmp = 0

        self.range = 0
        for i in range(len(self.literki)):
            self.offset[self.literki[i]] = tmp
            tmp = tmp + self.proba[i]
            self.proba_d[self.literki[i]] = self.proba[i]

        self.range = tmp
        tmpi = 0
        for l in self.literki:
            for _ in range(self.proba_d[l]):
                self.decode_d[tmpi] = l
                tmpi = (tmpi + 1)



    def code(self, message):
        val = self.range
        print(message, "------------")
        for symbol in message:
            tmp = val // self.proba_d[symbol]
            print(tmp)
            r = val % self.proba_d[symbol]
            print(r)
            tmp = tmp * self.range + self.offset[symbol] + r
            print(tmp)
            val = tmp
        self.encoded = val
        return val

    def unode(self):
        decoded = ""
        while self.encoded > self.range:
            symbol = self.decode_d[self.encoded % self.range]
            decoded = symbol + decoded

            completedevision = self.encoded // self.range
            wholesteps = completedevision * self.proba_d[symbol]
            fractionalsteps = self.encoded % self.range - self.offset[symbol]
            self.encoded = wholesteps + fractionalsteps
        self.decoded = decoded
        return decoded

    def show_bagno(self):
        print("offset ", self.offset)
        print("proba", self.proba_d)
        print("range_len", self.range)
        print("decode_d", self.decode_d)


l = ["A", "B", "C"]
p = [5, 2, 1]

# rans = rANS_old()
# rans.set_alfabet(l)
# rans.set_proba(p)
# rans.function()
# rans.show_bagno()
# print('|', rans.code(""))

rans = rANS()
rans.set_alfabet(l)
rans.set_proba(p)
rans.function()
rans.show_bagno()
print('encoded |', rans.code("ABBA"))
print('decoded |', rans.unode())
