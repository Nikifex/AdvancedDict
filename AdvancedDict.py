class AdvacedDict():
    def InviteDict(self,invdict):
        """transfers the dictionary for further use"""
        self.invdict=invdict

    def GetAllKeys(self):
        """apparently this method return all keys"""
        return self.invdict.keys()

    def GetKeyForDigit(self,keyys,digit):
        """return only one key (first key in dictionary with this element) """
        for i in keyys:
            if self.invdict[i] == digit:
                Truekey = i
            break
        return Truekey

    def KeyAndDigit(self,Truekey):
        """the returned element is equal to this key"""
        return self.invdict[Truekey]
