
integer = "tom"
try:
    float(integer)
except ValueError as ve_error:
    print("NONONO")
    ve_error.extra_info("Hello")
    raise
