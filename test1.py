
from aaaa.test111 import LogTest111
LogTest111.e(LogTest111,LogTest111,'test1引用aaaa中的test111')

from aaaa.www.test333 import LogTest333
LogTest333.d(LogTest333,LogTest333,'test1引用aaaaa中www的test333')

class logTes1(object):
    def runEror(self,msg):
        print(msg)
if __name__ == '__main__':
    pass