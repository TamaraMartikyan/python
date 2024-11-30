def sum_of_elements(numbers,exclude_negative=False):
    sum=0
    for num in numbers:
        if exclude_negative:
             if num>=0:
                sum+=num
                return sum
            
        else:
            sum+=num
            return sum

    

numbers=input('Enter a list of numbers separated by spaces: ')
numbers=list(map(int,numbers.split()))

choice=input('Shall we include negative numbers? yes or no: ')

if choice=='yes':
    result=sum_of_elements(numbers,exlcude_negative=False)
else:
    result=sum_of_elements(numbers,exclude_negative=True)

print(result)
