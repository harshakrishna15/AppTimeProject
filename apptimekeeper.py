def hoursToMinutes(hours):
    return hours * 60


def AppTimeKeeper():
    check = "check"

    hours = []
    minutes = []
    hoursMinutes = 0
    timeTotalHours = 0
    timeTotalMinutes = 0
    totalAppTime = ""
    lastItemInList = len(hours)-1
    moreHours = 0

    # checkTrue = True

    print("Press q to the next minute or hour")

    while True:
        hoursInput = input("How many hours: ")
        hours.append(hoursInput)
        print(hours)
        if hours[len(hours)-1] == "q":
            hours.pop()
        elif hours[len(hours)-1] != "q":
            continue
        for i in range(len(hours)):
            print(hours)
            timeTotalHours = timeTotalHours + int(hours[i])
            timeTotalMinutes = hoursToMinutes(timeTotalHours)
            print(timeTotalMinutes)
        break

    while True:
        minutesInput = input("How many Minutes: ")
        minutes.append(minutesInput)
        print(minutes)
        if minutes[len(minutes)-1] == "q":
            minutes.pop()
        elif minutes[len(minutes)-1] != "q":
            continue
        for i in range(len(minutes)):
            print(minutes)
            timeTotalMinutes = timeTotalMinutes + int(minutes[i])
            print(timeTotalMinutes)
        break
    print(str(timeTotalHours) + "hr")
    print(str(timeTotalMinutes) + "min")

    if timeTotalMinutes >= 60:
        moreHours = timeTotalMinutes // 60
        timeTotalHours = moreHours
        print(moreHours)
    timeTotalMinutes = timeTotalMinutes % 60

    print(str(timeTotalHours) + "hr")

    totalAppTime = "Your ran the application for " + \
        str(timeTotalHours) + " hours and " + \
        str(timeTotalMinutes) + " minutes."

    return totalAppTime


print(AppTimeKeeper())
