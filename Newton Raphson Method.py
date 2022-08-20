'''x = float(input('Enter a floating decimal: '))
if x>=0:
  ans = round(x**(1/3),5)
else:
  ans = round(-(-x)**(1/3),5)
print('Cube root of ' + str(x) + ' is ' + str(ans))'''



'''x = float(input('Enter the first number: '))
y =float(input('Enter the second number: '))
z =float(input('Enter the third number: '))
if x>y and x>z:
  print("x is the greatest")
elif y>z and y >x:
  print("y is the greatest")
else:
  print("z is the greatest")'''

#Function for Newton Raphson Method is x^3-5x+1 = 0 Interval [0,1]

def f(x):
    return(x**3-5*x+1)
def fprime(x):
    return(3*x**2 -5)

#print(f(3))
#print(fprime(3))


def NewtonRaphson(tol = 0.001,maxiter = 100):
    guess = 0.5

    for i in range(maxiter):
        nextguess = guess - f(guess)/fprime(guess)
        if abs(nextguess-guess)<tol: break
        print(nextguess)
        guess = nextguess
    print(f"the root is {nextguess} at {i} iterations.")


print(NewtonRaphson())
