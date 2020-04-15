import random
from pprint import pprint

list_of_surname = ["Gates", "Bezos", "Buffett", "Zuckerberg", "Arnault", 
"Page", "Sołowow", "Solorz"]

list_of_name = ["Bill", "Jeff", "Warren ", "Mark ", "Bernard", "Larry ",
 "Michał", "Zygmunt"]

list_of_age = [73, 24, 35, 76, 64, 75, 86, 45]

list_of_profession = ["businessman", "chairman", "inventor", "pioneer", 
 "speculator", "programmer"]

def generator_of_random_nested_dictionary(number_of_dictionaries):
    nested_dictionary = {f'person_{number_of_dictionaries}' :
    {"surname":random.choice(list_of_surname),
     "name":random.choice(list_of_name),
     "age":random.choice(list_of_age),
     "profession":random.choice(list_of_profession)} 
     for number_of_dictionaries in range (1,number_of_dictionaries+1)}
    
    return (nested_dictionary)

def generator_of_main_list(number_of_big_dictionaries,number_of_dictionaries,
number_of_single_dictionary):

    main_list = [generator_of_random_nested_dictionary(number_of_dictionaries) 
    for x in range (number_of_big_dictionaries)]
    
    for _x in range(number_of_single_dictionary):
        main_list.append({"surname":random.choice(list_of_surname),
     "name":random.choice(list_of_name),
     "age":random.choice(list_of_age),
     "profession":random.choice(list_of_profession)} ) 
    
    return main_list

def check_append (value_checked):
    return isinstance(value_checked,dict)
        
def selective_filtering(big_list,filtr):
    filtering_list= []
    if type(filtr)==str:

        if len(filtr)==0:
            return big_list

        elif (len(filtr)>0 and len(filtr)<=3):
            print("the function does not filter anything for this parameter")  

        elif len(filtr)>3:

            for _x in big_list:

                for _key, _value in _x.items():

                    if (check_append(_value) == False  and filtr == _value):
                        filtering_list.append(_x)

                    elif check_append(_value):
                        filtering_list =[_value for _key_1, _value_1 
                        in _value.items() if _value_1 == filtr]
                            
            return filtering_list

    elif type(filtr)!= str:
        print("please enter a filter variable in a string type")
  
x=selective_filtering(generator_of_main_list(3,3,6),"Gates")
print(x)






