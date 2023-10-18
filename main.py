zapros = input("запрос (слово-часть ссылки) (ex: vk.)")

try:
    with open(input("входной файл: "),"r+",encoding="utf-8") as inputFile:
        with open(input("выходной файл: "), "w+",encoding="utf-8") as OutFile:
            for line in inputFile:
                line = line.replace("http://","").replace("https://","")
                if line.count(zapros) != 0:
                    split = line.split(":")
                    if len(split) != 3:
                        print("ошибка формата - "+ line)
                        continue
                    OutFile.write(split[1]+":"+split[2])

except Exception as ex:
    print(Exception)