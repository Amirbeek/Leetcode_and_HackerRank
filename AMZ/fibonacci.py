def fibonacci(n):
    cache = {}

    def helpers(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            cache[n] = helpers(n - 1) + helpers(n - 2)
            return cache[n]

    return helpers(n)


print(fibonacci(10))
