# 

def square(x):
    return x*x
    
def main():
    for i in range(10):
         print("{} square is {}".format(i,square(i))) 
        #this is jus another way to represent
        # print(f"{i} square is {square(i)}")
if __name__ == '__main__':
    main()
""" 
What we have to know before using function 
1.python should have to know the name of the function before using it just like other languages
2.so if we have used def section below the loop then it will throw the error or exeception called NameError
 """

""" 
What is new in python function ??
==> we can call the python function in another file by importing it event from another peoples program file as well
we will be calling this function square in another file called "modules.py" check that out as well 
 """
