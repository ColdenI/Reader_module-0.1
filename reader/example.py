from reader import Reader

fail = Reader("My_fail.txt", encoding="utf8")

fail.write(("INT","FLOAT","STRING","BOOLEAN"),(1,3.14,"hello",True),start_text="m")

print(fail.read("STRING"))
print(fail.read_int("INT"))
print(fail.read_float("FLOAT"))


