print("Hi")
def square_root(n):
    try:
        n = float(n)
        return n**0.5
    except ValueError:
        raise ValueError("Input is not a number")

print(square_root("7"))
print(square_root("Seven"))