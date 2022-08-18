temp_to_calc = input("Insert the temperature you would like to convert: ")
temp_to_calc = temp_to_calc.upper()
if temp_to_calc[-1] == 'F':
    converted_temp = ((5 * float(temp_to_calc[:len(temp_to_calc)-1])) - 160) / 9
    converted_temp = "{:.2f}".format(converted_temp)
    converted_temp += "C"
    print("Converted temp is: ", converted_temp)
elif temp_to_calc[-1] == 'C':
    converted_temp = ((9 * float(temp_to_calc[:len(temp_to_calc)-1])) + (32 * 5)) / 5
    converted_temp = "{:.2f}".format(converted_temp)
    converted_temp += "F"
    print("Converted temp is: ", converted_temp)
else:
    print("You didn't enter correct temp type")
