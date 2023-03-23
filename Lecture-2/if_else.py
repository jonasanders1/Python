import math
# 1. What do these code fragments print?

# A)
n = 1
m = -1
if n < -m:
    print(n)
else:
    print(m)

# B)
if -n >= m:
    print(n)
else:
    print(m)

# C)
x = 0.0
y = 1.0
# abs(x - y) = 1 ---> 1 < 1 returns false ---> y gets pritned out
if abs(x - y) < 1:
    print(x)
else:
    print(y)

# D)
x = math.sqrt(2.0)
y = 2.0

if x * x == y:
    print(x)
else:
    print(y)
