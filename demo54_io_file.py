file1 = open('ucom_python\\data\\Python_Introduction')
readme_txt = file1.read()
file1.close()
print type(readme_txt), len(readme_txt), readme_txt[:21]

with open('ucom_python\\data\\Python_Introduction') as file2:
    readme_txt2 = file2.read().decode('UTF-8')

print type(readme_txt2), len(readme_txt2), readme_txt2[:21]


file3 = open('ucom_python\\data\\clone1','w')
file3.write(readme_txt)
file3.close()

with open('ucom_python\\data\\clone2','w') as file4:
    file4.write(readme_txt2.encode('UTF-8'))
