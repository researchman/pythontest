#id(object)
#返回的是对象的“身份证号”，且唯一不变
#一个对象的id值在python中代表它在内存中的地址
class Obj():
      def __init__(self, arg):
            self.x = arg
if __name__ == '__main__':

      obj = Obj(1)
      print (id(obj))
      obj.x=2
      print (id(obj))

      s="abc"
      print(id(s))
      s="bcd"
      print( id(s))

      x=1
      print( id(x))
      x=2
      print( id(2))
