from typing import List

def read_integers() -> List[int]:
    
    my_input = input()
    res = []
    for i in my_input.split(","):
        res.append(int(i))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
