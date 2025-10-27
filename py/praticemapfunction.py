#1.add country code to  phone number:
op=map(lambda x:'+91'+x,[9876543210,7674087681,8501034401,9951935040,8019876813])
print(list(op))
#2.convert prices from dollars to rupees:
rupes=map(lambda product_price: )

# 3.filter gmail IDS:
gemail_id=filter(lambda mail:mail.endswith("@gmail.com"),["harris@gmail.com","abc@gmail.com","xyz@gmail.com"])
print("Gmail IDS:",list(gemail_id))
# 4.Get short product names
names= filter(lambda item: len(item)<=5,["pen","notbook","laptop","charger","bag"])
print("short product names:",list(names))
# 5.convert names to usernames:
user_names=map(lambda name:name.lower()+"@gamil.com",["harish","sushama","nandu"])
print("usernames:",list(user_names))
#6.filter expried products
expriy_years=filter(lambda year:year<2025,[2022,2023,2025,2026])
print("product expiry years:",list(expriy_years))
#7.mask creadit card numbers
masked_card=map(lambda c:"*"*12+c[-4],["1223456765434565","9876545673456543"])
print("masked cards:",list(masked_card))