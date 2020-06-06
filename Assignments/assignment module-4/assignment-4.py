class book:
    def __init__(self,t,a,publ,pr=0):
        self.title=t
        self.author=a
        self.publisher=publ
        self.price=pr
        self._authorroyality=0
    def get_title(self):
        return self._title
    def set_title(self,t):
        self._title=t
        return
    title=property(get_title,set_title)
    def get_author(self):
        return self._author
    def set_author(self,a):
        self._author=a
        return
    author=property(get_author,set_author)
    def get_publisher(self):
        return self._publisher
    def set_publisher(self,t):
        self._publisher=t
        return
    publisher=property(get_publisher,set_publisher)
    def get_price(self):
        return self._price
    def set_price(self,t):
        self._price=t
        return
    price=property(get_price,set_price)
    def get_authorroyality(self):
        return self._authorroyality
    def set_authorroyality(self,t):
        self._authorroyality=t
        return
    authorroyality=property(get_authorroyality,set_authorroyality)
    
      

    def royalty(self,n):
        if(n<=500):
            self._authorroyality=0.10*self._price*n
        elif(n>500 and n<=1500):
            self._authorroyality=500*.10*self._price + (n-500)*0.125*self._price
        elif n>1500:
            self._authorroyality=500*.10*self._price + 1000*0.125*self._price + (n-1500)*0.15*self._price
        return self._authorroyality
    
class ebook(book) :
    def __init__(self,t,a,publ,pr,frmt):
        super().__init__(t,a,publ,pr=0)
        self.format=frmt
    def get_format(self):
        return self._format
    def set_format(self,f):
        self._format=f
        return
    formatt=property(get_format,set_format)
    def royalty(self,n):
        r=super().royalty(n)
        r=r-0.12*r
        self._authorroyality=r
        return self._authorroyality    
        
