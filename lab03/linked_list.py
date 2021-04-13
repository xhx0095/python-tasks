class Node (object):
  def __init__ ( self , value , next_ = None ):
      self . _value = value
      self . _next = next_
class LinkedList(object):
   def __init__(self,node):
        assert isinstance(node._value,int)
        self.node = node
   @property
   def value(self):
       return self.node._value
   @value.setter
   def setval(self,newval):
       self.node._value=newval
   @property
   def next(self):
       return self.node._next
   @next.setter
   def setnex(self,newval):
       self.node._next=newval
   def __iter__(self):
       if not self.node:
           return 
       cur = self.node
       yield cur._value  
       while cur._next:
             cur = cur._next 
             yield cur.value 

def flatten_linked_list(node):
    a=[]
    for x in linked_list(node):
        if x._next!=none:
           a.append(x._value)
    return a
