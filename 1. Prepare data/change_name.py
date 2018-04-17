import csv
 
csvFile = open("data/test.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
csvFile2 = open('data/test_labels.csv','w', newline='') 
writer = csv.writer(csvFile2)

for item in reader:
    if(item[0]!='filename'):
        item[0]=item[0]+'.jpg'
    writer.writerow(item)

csvFile.close()
csvFile2.close()

print('Successfully change the test.csv.')

 
csvFile = open("data/train.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
csvFile2 = open('data/train_labels.csv','w', newline='') 
writer = csv.writer(csvFile2)

for item in reader:
    if(item[0]!='filename'):
        item[0]=item[0]+'.jpg'
    writer.writerow(item)

print('Successfully change the train.csv.')

csvFile.close()
csvFile2.close()

