import pinyin


def convertName(name, target="pinyin"):
    if target == "pinyin":
        converted = pinyin.get(name, format="strip", delimiter=" ").split(" ")

    # 2-character name
    if len(converted) == 2:
        last_name = converted[0]
        first_name = converted[1]

    # 3-character name
    elif len(converted) == 3:
        last_name = converted[0]
        first_name = "".join(converted[-2:])

    # 4-character name (e.g. 歐陽, 司馬, 司徒, ...)
    else:
        last_name = "".join(converted[0:2])
        first_name = "".join(converted[-2:])

    # Capitalize last name
    last_name = last_name.capitalize()
    first_name = first_name.capitalize()
    return "%s %s" % (last_name, first_name)


if __name__ == "__main__":
    with open("names.txt", "r", encoding="utf-8") as inp:
        with open("convertednames.txt", "w", encoding="utf-8") as outp:
            for line in inp:
                outp.write(convertName(line.replace(
                    "\ufeff", "").replace("\n", "")) + "\n")
