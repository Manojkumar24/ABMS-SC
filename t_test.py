import csv
from time import sleep
from scipy import stats

def getResults(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        nonZeros = 0

        falseResults,trueResults = [],[]

        for row in csv_reader:
            if line_count < 27:
                line_count += 1
                continue
            else:
                if float(row[1]) != 2048:
                    # false_val = (float(row[1])+float(row[2])+float(row[3]))/3
                    # true_val = (float(row[4])+float(row[5])+float(row[6]))/3
                    # falseResults.append(false_val)
                    # trueResults.append(true_val)

                    trueResults.append(float(row[1]))

                    nonZeros += 1
                
                line_count += 1
        
        print(f'Processed {line_count} lines.')

        return trueResults


trueResults1 = getResults('SC-Main exp_parking_true-spreadsheet.csv')
trueResults2 = getResults('SC-Main exp_parking_false-spreadsheet.csv')

statistic, pvalue = stats.ttest_ind(trueResults1, trueResults2, equal_var=False)

print(statistic,pvalue)