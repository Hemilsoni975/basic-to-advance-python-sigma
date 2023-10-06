import time
import datetime
#
# k= 0
# wow = time.time()
#
# for x in range(45):
#     print("hey hemil!!")
# print("time taken : ", time.time() - wow)
# wow1 = time.time()
#
# while(k<2):
#     print("hey hemil!!")
#     time.sleep(2)  # works as per seconds user provide
#     k = k+1
# print("hey hemil!!", time.time() - wow1)
#
# local_time = time.asctime(time.localtime(time.time()))  # to see present time and date
# print("present time : ", local_time)
#
# def for_loop():
#     for x in range(5000):
#         print("for loop :", x)
#
#
# def while_loop():
#     i = 0
#     while (i<5000):
#         i = i+1
#         print("while loop : ", i)
#
# wow = time.time()
# for_loop()
# t1 = (time.time() - wow)
# print("time taken by for_loop : ", t1)
#
# wow1 = time.time()
# while_loop()
# t2 = (time.time() - wow1)
# print("time taken by while_loop : ", t2)

print("----------DATE-TIME----------")
print()

x = datetime.datetime.now()
print("Current time : ", x)
print("Current year : ", x.year)

print()
print("----------DATETIME-METHODS----------")
print()

y = datetime.datetime(2003, 4, 12)
print(y)
print("weekday in full : ", y.strftime("%A"))
print("weekday in short : ", y.strftime("%a"))
print("month in full : ", y.strftime("%B"))
print("month in short : ", y.strftime("%b"))
print("weekday as number : ", y.strftime("%W"))
print("day of month : ", y.strftime("%d"))
print("month as number : ", y.strftime("%m"))
print("year in short : ", y.strftime("%y"))
print("year in full : ", y.strftime("%Y"))
print("24 hour : ", y.strftime("%H"))
print("12 hour : ", y.strftime("%I"))
print("AM/PM : ", y.strftime("%p"))
print("minutes : ", y.strftime("%M"))
print("seconds : ", y.strftime("%S"))
print("microsecond : ", y.strftime("%f"))
# print(y.strftime("%z"))
# print(y.strftime("%Z"))
print("day number out of 365 : ", y.strftime("%j"))
print("week number out of 53 sunday as 1st : ", y.strftime("%U"))
print("week number out of 53 monday as 1st : ", y.strftime("%W"))
print("local version of date-time : ", y.strftime("%c"))
print("century : ", y.strftime("%C"))
print("local version of date : ", y.strftime("%x"))
print("local version of time : ", y.strftime("%X"))
print("ISO 8601 year : ", y.strftime("%G"))
print("ISO 8601 weekday (1-7)", y.strftime("%G"))
print("ISO 8601 weeknumber (01-53) : ", y.strftime("%V"))

