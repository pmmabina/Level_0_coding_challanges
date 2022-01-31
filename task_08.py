def time_converter(minutes):
    hour = 60
    hours = 120
    hrs = minutes / hour
    mnts = minutes % hour
    
    if minutes < hour and minutes > 1:
        return (f"{minutes} minutes")
    elif minutes == 1:
        return (f"{minutes} minute")
    else:
        if minutes >= hour and minutes < hours:
            if mnts == 1:
                return (f"{int(hrs)} hour, {mnts} minute")
            else:
                return (f"{int(hrs)} hour, {mnts} minutes")
        else:
            if minutes > hours:
                if mnts == 1:
                    return (f"{int(hrs)} hours, {mnts} minute")
                else:
                    return (f"{int(hrs)} hours, {mnts} minutes")

print(time_converter(121))
