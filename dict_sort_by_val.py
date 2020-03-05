class Element:

    def __init__(self, coef):
        self.coefficient = coef

    def __eq__(self, other):
        return self.coefficient == other.coefficient

    def __lt__(self, other):
        # In terms of letters "a" = 1 and "b" = 2 but "a" should
        #  be more than "b" so 1 > 2
        return self.coefficient > other.coefficient

    def __repr__(self):
        return str(f"{self.__class__}({self.coefficient})")


a = Element(1)
b = Element(2)
c = Element(3)
d = Element(4)
e = Element(5)

meshed = {2: c, 3: a, 4: b, 1: d, 5: e}
res = []

for x, y in meshed.items():
    ind = False
    # If this is the first value, just insert it and continue
    if len(res) == 0:
        res.append((x, y))
        continue
    # If the value should be inserted between get the index
    for i, t in enumerate(list(res)):
        if t[1] < y:
            ind = True
            res.insert(i, (x, y))
            break
    # In case the val should be between, there must be an index
    if ind is None:
        res_iter = list(res)
        for v in res_iter[::-1]:
            n = res_iter.index
            # import pdb; pdb.set_trace()
            next_ind = (n - int(len(res))) + 1
            if len(res) > next_ind:
                res[next_ind] = v
            else:
                res.append(v)
            if n == ind:
                res[ind] = x, y
                break
    # The value should be appended at the end
    if not ind:
        res.append((x, y))

print(res)
