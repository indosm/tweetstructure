class Node(object):
    def __init__(self, string,user=None):
        """Construct.
        string = tweet한 단어
        user = tweet한 유저들을 double linked list로 연결
        count = tweet된 갯수
        나머지는 rbtree의 기본 형태이다.
        """
        self._string = string
        self._red = False
        self._left = None
        self._right = None
        self._p = None
        self._user = user
        self._count = 1
    string = property(fget=lambda self: self._string, doc="The node's key")
    red = property(fget=lambda self: self._red, doc="Is the node red?")
    left = property(fget=lambda self: self._left, doc="The node's left child")
    right = property(fget=lambda self: self._right, doc="The node's right child")
    p = property(fget=lambda self: self._p, doc="The node's parent")
    user = property(fget=lambda self: self._user, doc="The node's tw user")
    count = property(fget=lambda self: self._count, doc="The node's tw number")
    def __str__(self):
        "String representation."
        return str(self.string)

    def __repr__(self):
        "String representation."
        return str(self.string)

class Tweet(object):
    def __init__(self, create_node=Node):
        self._nil = create_node(string=None)
        "Our nil node, used for all leaves."
        self._root = self.nil
        "The root of the tree."
        self._create_node = create_node
        "A callable that creates a node."

    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")

    def search(self, string, x=None):
        if None == x:
            x = self.root
        while x != self.nil and string != x.string:
            if string < x.string:
                x = x.left
            else:
                x = x.right
        if x.count==0:
            x=self.nil
        return x


    def minimum(self, x=None):
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x


    def maximum(self, x=None):
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    def insert_key(self, string,user):
        "Insert the key into the tree."
        self.insert_node(self._create_node(string=string,user=user))

    def insert_node(self, z):
        "Insert node z into the tree."
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.string < x.string:
                x = x.left
            else:
                x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.string < y.string:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        #rb_print(self.root, 0)
        #print("")
        self._insert_fixup(z)
        #rb_print(self.root, 0)
        #print("")
        #print("")

    def _insert_fixup(self, z):
        "Restore red-black properties after insert."
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False


    def _left_rotate(self, x):
        "Left rotate x."
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y._left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y


    def _right_rotate(self, y):
        "Left rotate y."
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x
    def _Transplant(self,u,v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p._left = v
        else :
            u.p._right = v
        v._p = u.p
    def delete_node(self,z):
        y = z
        y_ori_color = y.red
        if z.left == self.nil:
            x = z.right
            self._Transplant(z,z.right)
        elif z.right == self.nil:
            x = z.left
            self._Transplant(z,z.left)
        else:
            y = self.minimum(z.right)
            y_ori_color = y.red
            x = y.right
            if y.p == z:
                x._p = y
            else:
                self._Transplant(y,y.right)
                y._right = z.right
                y._right._p = y
            self._Transplant(z,y)
            y._left = z.left
            y.left._p = y
            y._red = z.red
        if not y_ori_color:
            self._delete_fixup(x)
    def _delete_fixup(self,z):
        while z != self.root and not z.red:
            if z == z.p.left:
                y = z.p.right
                if y.red:
                    y._red = False
                    z._p._red = True
                    self._left_rotate(z.p)
                    y = z.p.right
                if not y.left.red and not y.right.red:
                    y._red = True
                    z =z.p
                elif not y.right.red:
                    y._left._red = False
                    y._red = True
                    self._right_rotate(y)
                    y = z.p.right
                if y.right.red:
                    y._red = z.p.red
                    z._p._red = False
                    y._right._red = False
                    self._left_rotate(z.p)
                    self._root = z
            else:
                y = z.p.left
                if y.red:
                    y._red = False
                    z._p._red = True
                    self._right_rotate(z.p)
                    y = z.p.left
                if not y.left.red and not y.right.red:
                    y._red = True
                    z = z.p
                elif not y.left.red:
                    y._right._red = False
                    y._red = True
                    self._left_rotate(y)
                    y = z.p.left
                if y.left.red:
                    y._red = z.p.red
                    z._p._red = False
                    y._left._red = False
                    self._right_rotate(z.p)
                    self._root = z
        z._red = False
        
if __name__=="__main__":
    print("This is for Importing rbtree!")
