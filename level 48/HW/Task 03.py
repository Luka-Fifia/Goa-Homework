def fake_bin(x):
    bin = []
    for i in x:
        if int(i) < 5:
            bin.append("0")
        elif int(i) >= 5:
            bin.append("1")
    return "".join(bin)