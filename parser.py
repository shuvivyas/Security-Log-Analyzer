def parse(line):
    data = {}
    word = line.strip().split()
    data["date"] = word[0]
    data["event"] = word[1] + " "+ word[2]

    for i in word[3:]:
        if "=" in i:
            key,value = i.split("=")
            data[key] = value
    return data
  
