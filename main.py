import os

zapros = input("запрос (слово-часть ссылки) (ex: vk.)")


try:
    count = 0
    with open(input("входной файл: "),"r+",encoding="utf-8") as inputFile:
        with open("tmp.txt", "w+", encoding="utf-8") as tmpFile:
                for line in inputFile:
                    line = line.replace("http://","").replace("https://","")
                    if line.count(zapros) != 0:
                        split = line.split(":")
                        if len(split) != 3:
                            print("ошибка формата - "+ line)
                            continue

                        tmpFile.write(split[1]+":"+split[2]+"\r\n")
    with open(zapros + ".txt", "w+", encoding="utf-8") as OutFile:
        lines = list(set(open("tmp.txt", "r+").readlines()))
        for line in lines:
            if len(line) < 2 and line.count(":") != 2:
                continue
            count += 1
            OutFile.write(line)

    print(f"Закончил! Всего {count} Выходной файл - " +zapros+".txt")
    os.remove("tmp.txt")
    input()
except Exception as ex:
    print(ex)
    input()
