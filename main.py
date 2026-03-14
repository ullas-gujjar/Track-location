import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Enter the phone number with country code
phone_number=phonenumbers.parse("+919845145637")

# Get timezone
time_zones=timezone.time_zones_for_number(phone_number)
print("Time Zone:",time_zones)

# Get carrier name
sim_carrier=carrier.name_for_number(phone_number,"en")
print("Carrier:",sim_carrier)

# Get country/region
country=geocoder.description_for_number(phone_number,"en")
print("Region:",country)

from opencage.geocoder import OpenCageGeocode
