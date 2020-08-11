import math

print("\n"+"*"*10+'Welcome To resultant Finder (Beta)'+"*"*10+'\n')

def get_inputs():
    #get Inputs
    first_vector = int(input("Enter Your First Vector : "))
    second_vector = int(input("Enter Your Second Vector : "))
    angle = int(input("Enter The angle between first and second vectors in arc degrees : "))

    return list((first_vector,second_vector,angle))

def calculate_resultant(input_list):
    # slice the input list 
    first_vec = input_list[0]
    second_vec = input_list[1]
    angle = input_list[2]
    angle = math.radians(angle)
    

    # Calculation

    #resultant

    resultant = math.sqrt(pow(first_vec,2)+pow(second_vec,2)+2*first_vec*second_vec*math.cos(angle))
    angle_of_resultant = (second_vec*math.sin(angle))/(first_vec+second_vec*math.cos(angle)) 
    angle_of_resultant = math.degrees(math.atan(angle_of_resultant))

    return list((resultant,angle_of_resultant))


input_list = get_inputs()
return_list = calculate_resultant(input_list)
print(return_list)

