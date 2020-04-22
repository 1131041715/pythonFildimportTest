
import sys
sys.path.append("./")

from aaaa.test111 import LogTest111
LogTest111.v(LogTest111,LogTest111,'qqqq中的test222引用aaaa中的test111')


from aaaa.www.test333 import LogTest333
LogTest333.d(LogTest333,LogTest333,'qqqq中的test222引用aaaa中的www的test333')


from test1 import logTes1
logTes1.runEror(logTes1,'qqqq中的test222引用最外层的test1')