import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+355677408989")
print("\n Phone Numbers Lokacion\n")
print(geocoder.description_for_number(phone_number1,"en"));