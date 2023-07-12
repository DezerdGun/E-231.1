# print("hello")
# import time
# seconds = time.time()
# print("Secondsv since epoch =", seconds)
import time
seconds = 1689177877.1346107
local_time = time.ctime(seconds)
print("Local time:", local_time)


file = open("blabla.txt", "w")
file.write("This is blabla taxi")
file.close()
file = open('blabl.txt', "r")
print(file.read())