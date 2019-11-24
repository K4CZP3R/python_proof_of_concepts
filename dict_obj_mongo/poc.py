import poc_objects

# Create phone logs
my_phone_logs = poc_objects.PhoneLogs(list())

phone_log_1 = poc_objects.PhoneLog("out", 1)
phone_log_2 = poc_objects.PhoneLog("in", 2)

my_phone_logs.add_log(phone_log_1)
my_phone_logs.add_log(phone_log_2)

# Add it to an Phone

my_phone = poc_objects.Phone(my_phone_logs, "+3100000000")

print(f"This phone nr. ({my_phone.phone_number}) does have {my_phone.PhoneLogs.get_logs_amount()} log(s)")
print(f"First log is in this direction:{my_phone.PhoneLogs.get_log(0).direction} and happend @{my_phone.PhoneLogs.get_log(0).time}")


print("="*16)
mongo_update_insert_ready = my_phone.toDict()
print(mongo_update_insert_ready)
print("="*16)


phone_from_find_one_mongo = poc_objects.Phone.fromDict(mongo_update_insert_ready)
print(f"This phone nr. ({phone_from_find_one_mongo.phone_number}) does have {phone_from_find_one_mongo.PhoneLogs.get_logs_amount()} log(s)")
print(f"First log is in this direction:{phone_from_find_one_mongo.PhoneLogs.get_log(0).direction} and happend @{phone_from_find_one_mongo.PhoneLogs.get_log(0).time}")
