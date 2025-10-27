# # pancard
# import re
# regex1= r"^[A-Z]{5}[0-9]{4}[A-Z]$"
# pan="abcde1234f"
# op=re.search(regex1,pan)
# if(op):
#     print("valide pancard")
# else:
#     print("invalied pancard")


# # mobilenumber
# regex=r"^(\+91)\s[6-9]{1}[0-9]{9}$"
# ip="+91 6543234576"
# op=re.search(regex,ip)
# if(op):
#     print("valid mobile number")
# else:
#     print("invalid mobile number")


# # pin code
# regex=r"^[1-9]{1}[0-9]{5}"
# code="507112"
# op=re.search(regex,code)
# if(op):
#     print("valid pincode")
# else:
#     print("invalid pincode")


# # 
# regex=r"^[0-9]{4}-[1-9]{1}-[1-30]{2}"
# date="2025-09-26"
# op=re.search(regex,date)
# if(op):
#     print("valid date")
# else:
#     print("invalid date")


import re

regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

date = "2025-09-26"
op = re.search(regex, date)

if op:
    print("valid date")
else:
    print("invalid date")
