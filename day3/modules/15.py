import sys

extra_path = '/Users/shobhit/Desktop/qualcomm/day3/sample'

sys.path.append(extra_path)

for p in sys.path:
    print(p)

import hello

hello.greet()
