# function for converting integer to roman 
def roman(num):
    
    values= [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols= ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i=12
    
    if (num>1000):
       print("ERROR, please select value less than or equal to 1000.")
       return
    
    while(num>0):
        div= num // values[i]
        num= num % values[i]
        
        while div:
            print(symbols[i], end='')
            div -= 1
        i -= 1
    return

# driver code
if __name__=="__main__":
    num=int(input("Enter number: "))
    print(f'The roman numeral of {num} is: ', end='')
    roman(num)
