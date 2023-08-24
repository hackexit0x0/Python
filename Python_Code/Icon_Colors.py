import os
import time

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
RESET = "\033[0m"



time.sleep(0.1)
print(black+"[1]  Running")
time.sleep(0.1)
print(red+"[2]  Running")
time.sleep(0.1)
print(bred+"[3]  Running")
time.sleep(0.1)
print(green+"[4]  Running")
time.sleep(0.1)
print(bgreen+"[5]  Running")
time.sleep(0.1)
print(yellow+"[6]  Running")
time.sleep(0.1)
print(byellow+"[7]  Running")
time.sleep(0.1)
print(blue+"[8]  Running")
time.sleep(0.1)
print(bblue+"[9]  Running")
time.sleep(0.1)
print(purple+"[10] Running")
time.sleep(0.1)
print(bpurple+"[11] Running")
time.sleep(0.1)
print(cyan+"[12] Running")
time.sleep(0.1)
print(bcyan+"[13] Running")
time.sleep(0.1)
print(white+"[14] Running")
time.sleep(0.1)
print(nc+"[15] Running"+RESET+"\n")
time.sleep(0.1)
# Regular Snippets



ask  = "{}[{}?{}] {}{}".format(green,white,green,yellow,RESET)
success = "{}[{}√{}] {}{}".format(yellow,white,yellow,green,RESET)
error  = "{}[{}!{}] {}{}".format(blue,white,blue,red,RESET)
info  = "{}[{}+{}] {}{}".format(yellow,white,yellow,cyan,RESET)
info2  = "{}[{}•{}] {}{}".format(green,white,green,purple,RESET) 


print(ask,red+"Icons"+RESET)

print(ask,success,error,info,info2,RESET)


