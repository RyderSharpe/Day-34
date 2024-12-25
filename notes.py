# def police_check(age):
#     if age > 18:
#         can_drive = True
#     else:
#         can_drive = False
#     return can_drive
#
# # print(police_check(12)) # Prints True or False.
#
# if police_check(19):
#     print("you may pass")
# else:
#     print("Straight to jail")
#
# ======================================================================

# ===============TYPE HINTS=========================
# defines age as an int, expects a bool output
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# print(police_check(12)) # Prints True or False.

if police_check("twelve"):
    print("you may pass")
else:
    print("Straight to jail")