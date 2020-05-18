

import os
import time




fPath = "C:\\PyProjects\\"

dirs = os.listdir( fPath )




gName = "assignment1.txt"

hName = "assignment2.txt"




gPath = os.path.join(fPath, gName)

hPath = os.path.join(fPath, hName)




gTime = os.path.getmtime(gPath)

hTime = os.path.getmtime(hPath)



print(gPath, gTime)
print(hPath, hTime)
