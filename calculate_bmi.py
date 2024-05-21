
# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


# def bmi(weight, height):
    
#     bmi_num = round(weight / (height)**2)

#     print (bmi_num)

#     match bmi_num:

#         case bmi_num if bmi_num <= 18.5:

#             print ("Underweight")

#         case bmi_num if bmi_num <= 25:

#             print ("Normal")

#         case bmi_num if bmi_num <= 30:

#             print ("Overweight")

#         case bmi_num if bmi_num > 30:

#             print ("Obese")


# Pythonic Solution


def bmi(weight, height):
    
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

print (bmi(110, 1.80))