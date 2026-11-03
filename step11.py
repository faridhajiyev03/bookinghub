def is_slot_free(hour:int, booked_hours:list)->bool:
    return 9 <= hour <= 17 and hour not in booked_hours

def free_slots(booked_hours: list) -> list:
    free_hours = []
    for hour in range(9, 18):
        if is_slot_free(hour, booked_hours):
            free_hours.append(hour)
    return free_hours

booked = [10, 13, 15]

print(free_slots(booked))