# PythonAdmin
Run your Python script/other program from cmdline as admin/root
## Usuage
> admin.isUserAdmin()
Check if the Python script run as root or not
Return: True if root and False if not

> admin.runAsAdmin(command and parameter)
Run command (cmd/bash) as root
Return: None

## Example
```python
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
```

## Notes
Some of the code are taken from https://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows (Thanks sundar_ima) and modified for Python 3
