def is_slot_free(hour:int, booked_hours:list)->bool:
    return 9 <= hour <= 17 and hour not in booked_hours


booked = [10, 13, 15]

print(is_slot_free(11, booked))
print(is_slot_free(10, booked))
print(is_slot_free(20, booked))




