import phonenumbers

from phonenumbers import geocoder
number=input("Enter the PhoneNumber with the country code : ")
ch_nmber=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
ro_number=phonenumbers.parse(number,"RO")
c=carrier.name_for_number(ro_number,"en")
print(c)
