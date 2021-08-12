from flask import Flask
app = Flask(__name__)

@app.route('/')
fibonacci_cache = {}
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n in fibonacci_cache :
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2 :
        value = (fibonacci(n - 1) + fibonacci (n - 2))
    fibonacci_cache[n] = value
    return value
n = int(input("Enter the limit of fibonacci series "))
for i in range(1, n + 1):
    print(i, ":", fibonacci(i))

if __name__ == "__main__":
    app.run(debug = True)
