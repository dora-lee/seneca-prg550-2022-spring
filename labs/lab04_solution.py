# program: L4_solution.py
# author:  Dora Lee
# date:    13-Jun-2022
# purpose: python functions for online submission for PRG550 summer 2022 Lab #4

def getRecord(fileName, date):

    try:
        found_record = False
        fh = open(fileName, "r")
        for line in fh:
            # import pdb; pdb.set_trace()
            
            record = json.loads(line)
            if record['date']==date:
                print("{0},${1:g},{2},${3:g},${4:g},${5:g}".format(
                    record['date'], record['close_price'], record['volume'], record['open']
                    , record['high'], record['low']
                ))
                found_record = True
        fh.close()
        if not found_record:
            print("sorry, record not found...")
    except OSError:
        print(f"error opening file... {fileName}")

def largestVolume(fileName):

    try:
        fh = open(fileName, "r")
        max_record = {'volume':0}
        for line in fh:
            # import pdb; pdb.set_trace()            
            record = json.loads(line)
            if record['volume'] > max_record['volume']:
                max_record = record.copy()
        fh.close()
        print("{0},${1:g},{2},${3:g},${4:g},${5:g}".format(
                    max_record['date'], max_record['close_price'], max_record['volume'], max_record['open']
                    , max_record['high'], max_record['low']
                ))
    except OSError:
        print(f"error opening file... {fileName}")

def averageDailyClose(fileName, year, month = -1):
    try:
        fh = open(fileName, "r")
        record_list = []
        for line in fh:
            # import pdb; pdb.set_trace()            
            record = json.loads(line)
            record_date = datetime.datetime.strptime(record['date'], '%m/%d/%Y')

            if month==-1 and record_date.year==year:
                record_list.append(record)
            elif record_date.month==month and record_date.year==year:
                record_list.append(record)
            
        fh.close()

        avg_sum = 0
        for record in record_list:
            avg_sum += record['close_price']
        avg_close = avg_sum/len(record_list)

        print("{:.4f}".format(avg_close))


    except OSError:
        print(f"error opening file... {fileName}")
