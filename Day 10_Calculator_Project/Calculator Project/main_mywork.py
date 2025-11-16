from art import logo
print (logo)



def add(n1, n2):
    return n1 + n2

def substract (n1, n2):
    return n1 - n2

def multiply (n1,n2):
    return n1*n2

def divide (n1, n2):
    return n1/n2


#TO-DO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add, 
    "-": substract, 
    "*": multiply, 
    "/": divide, 
    }



#Use the dict operation to perform calculation
#print (operations["*"](4,8))    #retrieve to dict, then to def 

#Program works out the result based on the chosen mathematical operator.
def calculation (n1, n2):
    n1 = float(input("Type the first number: "))
    while True: 
        operator = input ("Choose the math operator(+, -, *, /): ")
        n2 = float(input("Type the second number: "))

        if operator in operations:
            result= operations[operator](n1, n2)      #return operations[operator](n1, n2) is possible but we need a variable "result" to hold result, not only return as function will exit!
            print (f"{n1} {operator} {n2} = {result}")
        
        else:
            return "Invalid operator!"

        # Program asks if the user wants to continue working with the previous result.

        continue_with_previous_result = input ("Do you want to continue with the previous result? (y/n): ")
        if continue_with_previous_result.lower() == "y":
            n1 = result                   #use previous result
        else:
            n1 = float(input("Type the first number: "))     #start fresh
         
            



calculation (1,2)

    

