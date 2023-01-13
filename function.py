# def multiply(num1,num2):
#     result = num1*num2
#     print(result)

# multiply(2, 3)
employee_list = [
    {
        "name": "Tony Stark",
        "emp_id": 3,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            }
        ]
    },
    {
        "name": "Steve Rogers",
        "emp_id": 6,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700117"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700127"
            }
        ]
    }
]

# # Create a list of dictionaries containing individual employees and their
# # corresponding pincodes from the above employee_list
# emp_pin_list = []
# for emp in employee_list:
#     # print("Name: ", emp["name"])
#     # print("ID: ", emp["emp_id"])
#     emp_pin_list.append({"name": emp["name"]})
#     print(emp_pin_list)
#     print(employee_list.index(emp))
#     emp_pin_list[employee_list.index(emp)]["pincode"] = []
    
#     for address in emp["address"]:
#         # print(employee_list.index(emp))
        
#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["Pincode"])
#         print("Pindcode: ", address["Pincode"])

def get_employee_address_details(employee_list, key):
    emp_address_list = []
    for emp in employee_list:
        emp_address_list.append({"name": emp["name"]})
        emp_address_list[employee_list.index(emp)][key] = []

        for address in emp["address"]:
            emp_address_list[employee_list.index(emp)][key].append(address[key])
    return emp_address_list