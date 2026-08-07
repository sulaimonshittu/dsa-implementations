## Understanding Base Case & Recursive Case
## Base Case is the termination
## Recursive case enables the recursion

def shortRecursive(value):
    print(f"shortRecursive({value}) called!")
    if not value:
        ### Base case
        print("Returning from base case")
        return
    else:
        ### recursive case
        shortRecursive(False)
        print("returning from recursive call")
        return

print(f"calling shortRecursive(False):")
shortRecursive(False)
print()
print(f"calling shortRecursive(True):")
shortRecursive(True)
print()

## After the execution of the base case
## The code doesn't just stop running
## The remaining code of the previous recursive case are executed in
## in a last in first out order as they are in the stack.
## That is why after printing: 5, 4, 3, 2, 1, 0, reached base case
## it comes to print 1 returning, 2 returning, 3 returning, 4 returning, 5 returning

def countDownAndUp(number):
    print(number)
    if number == 0:
        ## base case
        print("reached the base case")
        return
    else:
        ## recursive case
        countDownAndUp(number - 1)
        print(number, "returning")
        return

countDownAndUp(5)

## Iterative factorial
def i_factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

print()
print(i_factorial(5))

## Recursive factorial The multiplication is done after the execution of the recursive call
## it computed from the base case then all the frames in the call stack are computed with
## their recursive call then popped of until it ends at 5 * 24 -> 120

def r_factorial(n):
    if n == 1:
        return n
    return n * r_factorial(n - 1)

print()
print(r_factorial(4))

## Iterative fibonacci
def i_fibb(num):
    ans = [1, 1]
    for i in range(num):
        a, b = ans[-2], ans[-1]
        ans.append(a + b)
    return ans

print(i_fibb(5))

## Recursive fibonacci
def r_fibb(num, ans=[1,1]):
    if num == 0:
        return
    r_fibb(num - 1, ans)
    a, b = ans[-2], ans[-1]
    ans.append(a + b)

output = [1, 1]
r_fibb(5, output)
print(output)

def fibb(num):
    if num == 1 or num == 2:
        return 1
    return fibb(num - 1) + fibb(num - 2)

print(fibb(10))