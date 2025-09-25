import re
regex1= r"^[A-Z]{5}[0-9]{4}[A-Z]$"
pan="abcde1234f"
op=re.serch(regex1,pan)
if(op):
    print("valide pan card")
else:
    print("invalied pan card")