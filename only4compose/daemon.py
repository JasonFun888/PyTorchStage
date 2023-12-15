print("Hello docker-compose!")

import time
time.sleep(10)

# Python中的无限数 - https://blog.csdn.net/p15097962069/article/details/103987139

from decimal import Decimal
print(Decimal('Infinity'))
# Infinity

import math
print(math.inf)
# inf
print(math.inf > 9999999999999999999999999999999999999999999999999999999999999999)
# Ture

from numpy import inf
print(inf)
# inf
print(-inf)
# -inf

print(inf - 1)
# inf
print(inf + 1)
# inf
print(inf - inf)
# nan

print(float("inf"))
# inf


# Python中的整数上限 - https://blog.51cto.com/u_16213339/7491312

import sys
print("Integer Limit on 32-bit System:", sys.maxsize) # 输出32位系统上的整数上限
print("Integer Limit on 64-bit System:", sys.maxsize) # 输出64位系统上的整数上限
# Integer Limit on 32-bit System: 2147483647
# Integer Limit on 64-bit System: 9223372036854775807
print(sys.maxsize)
# 9223372036854775807

# 时间戳的最大值

# time.sleep(sys.maxsize) # OverflowError: timestamp too large to convert to C _PyTime_t
# time.sleep(2147483647) # OK
print(0xFFFFFFFF)
# 4294967295
time.sleep(0xFFFFFFFF)