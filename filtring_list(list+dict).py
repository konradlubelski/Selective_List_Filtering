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
number_of_single_elements):
    main_list = [generator_of_random_nested_dictionary(number_of_dictionaries) 
    for x in range (number_of_big_dictionaries)]
    
    for _x in range(number_of_single_elements):
        main_list.append(random.choices(list_of_surname,k=5)) 

    for _x in range(number_of_single_elements):
        main_list.append(random.choices(list_of_name,k=3))
    pprint(main_list)
    print("")
    return main_list

def selective_filtering(big_list,filtr):
    dictionary = [element_in_big_list for element_in_big_list in big_list if type(element_in_big_list)==type({})]
    for x in dictionary:
        for _key, value in x.items():
            for _key_1, value_1 in value.items():
                if filtr == value_1:
                    print(value)
                    print(_key)
    
selective_filtering(generator_of_main_list(2,3,4),"Gates")



