
class Adj:
    def __init__(self):
        """Construction
        string : tweet한 단어
        count : 단어가 나온 횟수
        next : 다음으로 tweet한 단어
        down : 다음으로 tweet한 사람
        own : 이 단어를 tweet한 사람
        4중 연결 리스트를 만들었다.
        """
        self.string=""
        self.count=1
        self.next=None
        self.prev=None
        self.up=None
        self.down=None
        self.own=None
    def __repr__(self):
        ret = ""
        x = self
        while x != None:
            ret += str(x.string)+"->"
            x= x.next
        return ret
class USER:
    def __init__(self,number):
        self.number=number
        self.nick=""
        self.count_tw=0
        self.count_fr=0
        self.friend=None
        self.head=None
        self.tail=None
    def add_tw(self,string):
        a = Adj()
        a.string = string
        a.own=self
        if self.head is None:
            self.head = self.tail = a
        else:
            a.prev = None
            a.next = self.head
            self.head.prev = a
            self.head = a
        self.count_tw+=1
    def del_tw(self,node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        del node
    def add_fr(self,friend):
        a = Adj()
        a.string = friend
        a.count+=1
        a.next = self.friend
        self.friend=a
        self.count_fr+=1
    def nickname(self,nick):
        self.nick=nick
    def search_st(self,string):
        x = self.head
        while x != None:
            if x.string == string:
                return x
            x = x.next
        return x
    def search_fr(self,number):
        x = self.friend
        while x != None:
            if x.string == number:
                return x
            x = x.next
        return x
    def __repr__(self):
        x = self.head
        string =""
        while x!= None:
            string += x.string+"->"
            x=x.next
        return self.nick +" : "+string
if __name__ =="__main__":
    print("This is for Importing Adj!")
