#1. Add Country Code to Phone Numbers:
op=map(lambda x:+91+x,[9876543210,7674087681,8501034401,9951935040,8019876813])
print(list(op))

#2.conver prices from dollars to rupees

product_prices=map(lambda x:x*83,[10,25,40,100])
print("dollars",list(product_prices))

# 3. Filter Gmail IDs:
gmil_id=filter(lambda mail:mail.endswith("@gmail.com"),["harish@gmail.com","abc@gmail.com","xyz@gmail.com"])
print("gmail ids:",list(gmil_id))

#4 .Get Short Product Names

products = ["pen", "notbook", "laptop", "charger", "bag"]
short_names = filter(lambda item: len(item) <= 5, products)

print("short product names:", list(short_names))
#5.Convert Names to Usernames:
user_name=map(lambda name:name.lower()+"@gmil.com",["harish","sushma","nandu"])
print("use_names:",list(user_name))

#6. Filter Expired Products:
expiry_years=filter(lambda year:year<2025,[2022, 2023, 2025, 2026])
print("product expiry years:",list(expiry_years))

#7. Mask Credit Card Numbers :
masked_cards=map(lambda c:"*"*12+c[-4],["1234567890123456", "9876543210987654"])
print("masked cards:",list(masked_cards))

#8.Filter High Salary Employees
salary_employees=filter(lambda salary:salary>=40000, [25000, 45000, 60000, 80000])
print("high salary employees:",list(salary_employees))

#9. Format Product Labels:
items=map(lambda items:"products"+items,["apple", "mango", "orange"])
print("format product labels:",list(items))

# 10. Students Passed:
student_marks=filter(lambda scored:scored>40,[35, 80, 55, 20, 90])
print("students passed:",list(student_marks))

#11. Filter Strong Passwords :

passwords = ["abc123", "Admin@123", "hello", "Pa$$word"]
strong_passwords = filter(lambda p: len(p) >= 8 and ("@" in p or "$" in p), passwords)
print("strong passwords:", list(strong_passwords))


