import sys

def turn_clockwise(point):
    """ Determine the next clockwise corresponding point."""
    points = {"N": "E", "E": "S", "S": "W", "W": "N"}

    if point not in points: return 
    return points[point]

def day_name(num): 
    """ Given a week number, find day name."""
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday"}

    if num not in days: return 
    return days[num]

def day_num(day): 
    """ Given a day name, find corresponding number."""
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday"}

    for k,v in days.items():
        if day == v:
            return k
    return None 

def day_add(string,t1):
    """ Given a date trajectory, find the corresponding day name."""
    
    d = (day_num(string) + t1) % 7
    return day_name(d)

def days_in_month(month):
    """ Given a month, return number of days."""

    months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
                "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
                "November": 30, "December": 31}

    if month not in months: return 
    return months[month]

def to_secs(hours, minutes, seconds):

    sec_hour = (hours * 60) * 60
    sec_minutes = minutes * 60

    total = sec_hour + sec_minutes + seconds

    return total 

################## TESTING ##################

def test(did_pass):
    """ Print test results."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} okay.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.").format(linenum)
    print(msg)

def test_suite():
    """ Run test suite for code in this module."""

    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("A") == None)
    test(turn_clockwise(42) == None)

    test(day_name(3) == "Wednesday")
    test(day_name(24) == None)
    test(day_name(1) == "Monday")

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")

    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")

    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_suite()
