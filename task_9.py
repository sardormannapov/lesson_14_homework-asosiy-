string = "ooxx"

cnt_x = string.count("x")
cnt_o = string.count("o")
if cnt_x == cnt_o:
    print(True)

elif cnt_x > cnt_o or cnt_o > cnt_x:
    print(False)

else:
    print(True)