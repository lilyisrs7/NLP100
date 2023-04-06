str1 = "パトカー"
str2 = "タクシー"
print(''.join([''.join(letters) for letters in zip(str1, str2)]))