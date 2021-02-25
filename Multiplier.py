
def multiplier ():
    """
    This function has a algorithm which allow us to multiply 30 digit numbers without
    having a math library or direct multiplication or recursion. This algorithm is multiplying
    every digit of the first number with other one's every digit. So as conclusion, function returns
    result of multiplication of these two numbers
    Also user can choose whether using default numbers or Entering 2 numbers. Default numbers are
    2 numbers with 30 digit.

    Returns
    -------
    TYPE: String
        Result of multiplication.

    """
    print("Choose one of them:\n1-Enter 2 number\n2-Use default numbers.(defaults are 30 digit numbers)\n")
    choose = input("Enter your decision here:")
    if choose == "1":
        number1 = input("Enter first number:")
        number2 = input("Enter second number")
    elif choose == "2":
        number1 = "123456789012345678901234567890"
        number2 = "234567890123456789012345678901"
    to=0
    for i in range(len(number1)-1,-1,-1):
        for j in range(len(number2)-1,-1,-1):
            to += int(str(int(number1[i])*int(number2[j]))+((len(number2)+len(number1)-2-(i+j))*"0"))
            
    return "Multiplication of these two numbers equal to:\n" + str(to)     
      
print(multiplier())