
import sys
sys.path.append("./")

from aaaa.test111 import LogTest111
LogTest111.v(LogTest111,LogTest111,'eeee中的test444引用aaaa中的test111')

from aaaa.www.test333 import LogTest333
LogTest333.w(LogTest333,LogTest333,'eeee中的test444引用aaaa中的www的test333')
