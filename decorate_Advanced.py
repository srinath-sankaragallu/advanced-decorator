def dec(personal):
    def features(fn):
        def add_some_decorations(a, b):
            res = fn(a, b)
            print(personal)
            print(fn.__doc__, f"{fn.__name__}({a}, {b}) - Output: " + str(res))
            return res
        return add_some_decorations
    return features


@dec("=======================")
def add(a, b):
    "Addition of 2 arguments"
    return a + b


@dec("------------------------")
def sub(a, b):
    "Subtraction of 2 arguments"
    return a - b


x = add(5, 2)
print(x)

x = sub(1, 4)
print(x)
