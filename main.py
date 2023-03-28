import phonenumbers
from numero import number
from phonenumbers import geocoder
from phonenumbers import carrier

ch_number = phonenumbers.parse(number, "CH") #localização
ro_number = phonenumbers.parse(number, "RO") #operadora

print(geocoder.description_for_number(ch_number, "pt-br"),"\n", carrier.name_for_number(ro_number, "pt-br"))
