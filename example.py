import os
import admin
print("Are you root? ", end="")
# Check if root or not
if not admin.isUserAdmin():
    print("No")
    print("Getting root...")
    admin.runAsAdmin("python example.py") # Run command as root
else:
    print("Now you are root!")
    input("")
