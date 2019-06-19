import csv

sampleFile1 = open('ucom_python\\data\\data2.csv')
sampleReader1 = csv.reader(sampleFile1)
sampleData1 = list(sampleReader1)
sampleFile1.close()

print type(sampleData1)
for l in sampleData1:
    print l
    for c in l:
        print 'col=', c