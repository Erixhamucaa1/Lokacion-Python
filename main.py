import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("...")# Enter a phone number
print("\n Phone Numbers Lokacion\n")
print(geocoder.description_for_number(phone_number1,"en"));
