
quantity =int(input('Enter purchase quantity: '))
price=int(input('Enter price per unit: '))
total_amount = quantity*price
if quantity>200:
    total_amount = quantity*price*0.20
else:
    total_amount = price*quantity
    gst=total_amount*0.18
    final_amount=total_amount+gst
    print(final_amount)
    
    
