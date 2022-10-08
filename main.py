import phonenumbers
from data import target_phone_number

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

try:
    # get phone number details
    phone_number_detailed = phonenumbers.parse(target_phone_number)
    print(phone_number_detailed)

    valid = phonenumbers.is_valid_number(phone_number_detailed)

    if valid is not True:
        print("Please make sure that you enter the code following by phone number correctly")
    else:
        # get phone number country location

        ch_number = phonenumbers.parse(target_phone_number, "CH")
        country_en = geocoder.description_for_number(ch_number, "en")
        country_ar = geocoder.description_for_number(ch_number, "ar")
        print("Country is {0} {1}".format(country_en, country_ar))

        # get phone number service provider
        ro_number = phonenumbers.parse(target_phone_number, "ro")
        provider_name_en = carrier.name_for_number(ro_number, "en")
        print("Service Provider is {0}".format(provider_name_en))

        # get phone number timeZone
        phone_number_timezone = timezone.time_zones_for_number(phone_number_detailed)
        print("Time Zone is {0}".format(phone_number_timezone))
except:
    print("Invalid Phone Number format")
