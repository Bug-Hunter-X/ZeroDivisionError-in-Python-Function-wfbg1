def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or some other appropriate handling like raising a custom exception

result = function(10, 0)
print(result) 