#PROBLEM: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.#
#PURPOSE: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version shows how repeated multiplication works and how functions return results to the main program.


def exponent(base,exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

x = exponent(2,5)
print(x)

