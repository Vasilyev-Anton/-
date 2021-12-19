import copy
import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list.sort()
# print(contacts_list)

pattern = r"([А-Я][а-я]+)[,\ ]([А-Я][а-я]+)[ |,]([А-Я][а-я]+)?(,{1,4})?"
res = r"\1,\2,\3\4"

contacts_list_splited = []
for name in contacts_list:
    info_string = ','.join(name)
    result = re.sub(pattern, res, info_string)
    info_list = result.split(',')
    contacts_list_splited.append(info_list)
# print(contacts_list_splited)

pattern_1 = r"(\+7|8)[ \s]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2}) ?\(?(доб.)? ?(\d{4})?\)?"
res_1 = r"+7(\2)\3-\4-\5 \6\7"

contacts_list_mod_tel = []
for telephone in contacts_list_splited:
    telephone_string = ','.join(telephone)
    result_1 = re.sub(pattern_1, res_1, telephone_string)
    telephone_list = result_1.split(',')
    contacts_list_mod_tel.append(telephone_list)
print(contacts_list_mod_tel)
fin_list = []
result_list = []


for string in contacts_list_mod_tel:
    i = 2
    for str in fin_list:
        if (string[0] and string[1]) in str[:]:
            for el in str:
                if str[i] == '':
                    str[i] = string[i]
                    i +=1
    else:
        fin_list.append(string)
# print(fin_list)

result_date = ()
for it in fin_list:
    a = tuple(it)
    result_date += a
set_result = set()
set_result.update(result_date)
# print(set_result)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(res)   # Вместо contacts_list подставьте свой список
