# variable scope 

x = 10 #global variable


def number():
     '''
     Variable declare inside the any function it is local variable

     if local and global both variables are present in same program
     then local variable will only be printed  
     '''

     # x = 5 # local variable 
     y = 15 #local variable
   
     # if you want to change value of global variable use 
     # "global keyword"
   
     global x 
     x = x + 90

     print(x,y)
     
number()
'''
variable inside the function cannot get accessed outside the function
For eg :- if we print y outside the function it will throw an error 
'''

def hemil():
     y = 35 # local variable
     def soni():
          global y 
          y = 70 # becomes global variable with use of "global" keyword
          
          print("value called in nested function name soni()" , y)
     
     print("before calling soni()" , y)
     
     soni()
     
     print("after calling soni()" , y)

hemil()
print("global variable value : ",y)