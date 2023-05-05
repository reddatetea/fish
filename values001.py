values = ['ke', 'chang', 'kuan', 'ling']
vs = ['55','787','1092','1000']
for i in range(len(values)):
    m = values[i]
    n = vs[i]
    exec(f"{m} = n")
print(chang)