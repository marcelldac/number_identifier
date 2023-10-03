import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

print('Padrão de número: +5571992760849')
number = input('Digite o número desejado no padrão determinado: ')

ch_number = phonenumbers.parse(number, "CH") #localização
ro_number = phonenumbers.parse(number, "RO") #operadora

print(geocoder.description_for_number(ch_number, "pt-br"))
print(carrier.name_for_number(ro_number, "pt-br"))
