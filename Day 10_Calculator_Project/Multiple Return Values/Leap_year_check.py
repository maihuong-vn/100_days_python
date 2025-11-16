def is_leap_year(year):
    '''Take a first and last name and 
    format it to return the title case version of the name'''
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    
    elif year % 4 == 0:
        return True
    else:
        return False         #return Boolean, not string!! return "true" is false!

   
   
is_leap_year(2024)


#Alternative: 
def is_leap_year (year):
    return year %4== 0 and (year %100 !=0 or year %400 == 0)


print(is_leap_year (2100))
