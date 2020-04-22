# pythonFildimportTest
python文件引用测试
# 1、引用子文件夹中的文件（参考test.py）
```
from aaaa.test111 import LogTest111

```

# 2、引用父文件夹中的文件（参考test222.py或test444.py）
添加如下代码。无论几层，都可以引用到相应文件。
```
import sys
sys.path.append("./")

```

# 3、引用最外层的文件（参考test222.py）
```
from test1 import logTes1

```