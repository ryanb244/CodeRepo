tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def tablePrinter(tableList):
    colWidths = [0] * len(tableList)
    
    for i in range(len(tableList)):
        j=0
        while j < len(tableList[i]):
            length = len(tableList[i][j])
            if length > colWidths[i]:
                colWidths[i] = length
            j+=1

   
    for i in range(len(tableList[i])):
        for j in range(len(tableList)):
            strin = tableData[j][i]
            print(strin.rjust(colWidths[j],' '),end=" ")
        print('')


tablePrinter(tableData)

    


