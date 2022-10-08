import csv

file = open('progLang_male.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

empty_profile_count =0
lang_dict ={}

for row in csvreader:
        if row:
                row =' '.join(row).split("\"")
                for eachString in row:
                        if ('{' not in eachString) and (':' not in eachString):
                                if eachString in lang_dict.keys():
                                        lang_dict[eachString] +=1
                                else:
                                        lang_dict[eachString]=1
        else:
                empty_profile_count += 1

print("empty_profile_count - ", empty_profile_count)
print("language Dict - ", lang_dict)
