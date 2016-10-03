import sys

def turn_clockwise(point):
    points = {"N": "E", "E": "S", "S": "W", "W": "N"}

    if point not in points: return 
    return points[point]

def day_name(num): 
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday"}

    if num not in days: return 
    return days[num]

def day_num(day): 
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday"}

    for k,v in days.items():
        if day == v:
            return k 

def day_add(delta):
    


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

test_suite()







