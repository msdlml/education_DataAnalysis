import csv

with open("C:/intel/singerA.csv", "r") as inFpA :
    with open("C:/intel/singerB.csv", "r") as inFpB:
        with open("C:/intel/singerSum.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            print(header_list)
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                print(row_list)
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                print(row_list)
                csvWriter.writerow(row_list)

print('Save. OK~')