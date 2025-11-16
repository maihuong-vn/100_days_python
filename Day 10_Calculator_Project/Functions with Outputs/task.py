def format_name(f_name, l_name):
    formated_f_name = f_name.title()              #put input in .title() in a variable called formated_f_name 
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name ("MaI", "NgUyen")    #Mai is f_name, Nguyen is l_name input, title() make mapital letters in Ordnung
print (formated_string)
