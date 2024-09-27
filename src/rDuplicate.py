import csv

def read_csv(file): #read the csv and create a list of lists where each list is a row
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data


def write_csv(data, file): #write the list of lists to a csv file
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def remove_duplicate(data, titleCol):
    seenRow = {}
    for row in data:
        key = row[titleCol]
        if key in seenRow:
            continue
        seenRow[key] = row

    data = list(seenRow.values())
    return data

def merge_and_remove_duplicate(data1, data2, titleCol):
    data = data1 + data2
    data = remove_duplicate(data, titleCol)
    return data

def get_diffrence(data1, data2, titleCol):
    data = merge_and_remove_duplicate(data1, data2, titleCol)
    diff = []
    for row in data:
        key = row[titleCol]
        if key not in [r[titleCol] for r in data1] and [r[titleCol] for r in data2]:
            diff.append(row)

    return diff

if __name__ == '__main__':
    file1Name = 'data/_4.csv'
    file2Name = 'data/_2.csv'
    titleCol = 4
    resultFileName = 'result.csv'

    data1 = read_csv(file1Name)
    data2 = read_csv(file2Name)
    write_csv(get_diffrence(data1, data2, titleCol), resultFileName)
