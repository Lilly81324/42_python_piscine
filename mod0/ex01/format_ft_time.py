from time import time, strftime, gmtime

epoch_time_str = strftime("Seconds since %B %d, %Y: ", gmtime(0))
s_passed = time()
time_passed = f"{s_passed:,.4f} or {s_passed:.2e} in scientific notation"
print(epoch_time_str + time_passed)
print(strftime("%b %d %Y", gmtime(0)))
