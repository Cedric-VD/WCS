def squareNb(number):
  return(number**2)  
  
  
def cubeNb(number):
  return(number**3)
   
  
def valAbs(number):
  if number >= 0 :
    return number
  else :
    return -number
    
    
def factorial (number):
  factorial = number
  for i in range(number-1):
    number -= 1
    factorial = factorial * number
  return factorial


def mode(numbers) :
  mode = 1
  for i in numbers :
    if numbers.count(i) > mode :
      mode = i
    if mode == 1 :
      return None
    else :
      return mode
      
      
      
def average(numbers) :
  total = 0
  for i in numbers :
    total += i
  return total / len(numbers)
  

def minimum(numbers) :
  min = numbers[0]
  for i in numbers:
    if i < min :
      min = i
  return min
  
  
def maximum(numbers) :
  max = numbers[0]
  for i in numbers:
    if i > max :
      max = i
  return max
