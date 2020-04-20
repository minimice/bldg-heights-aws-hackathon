import csv

inputFile = 'DC_Buildings_Footprint_4326_test.csv'
outputFile = 'DC_Buildings_Footprint_4326_test_cleaned.csv'

# Build point header
pointheader = ""
for i in range(50):
    pointheader += "point" +str(i+1) + "_x,"
    pointheader += "point" +str(i+1) + "_y"
    if i < 49:
        pointheader += ","
#print(pointheader)
# End point header

cleaned_headers = "EGID,ROOF_TYPE,Shape_Length,Shape_Area,ALTITUDE_M," + pointheader
#print(cleaned_headers)

# Write to cleaned file
fclean = open(outputFile,'w')
fclean.write(cleaned_headers + '\n')

with open(inputFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            rowOutput = str(row[1]) + ","
            rowOutput += str(row[2]) + ","
            rowOutput += str(row[3]) + ","
            rowOutput += str(row[4]) + ","
            rowOutput += str(row[5]) + ","
            # PRINT 
            #print ("EGID: " + str(row[1]))
            #print ("ROOF_TYPE: " + str(row[2]))
            #print ("Shape_Length: " + str(row[3]))
            #print ("Shape_Area: " + str(row[4]))
            #print ("ALTITUDE_M: " + str(row[5]))
            # Process multipolygon
            polygon = row[6]
            polygon = polygon.replace("MULTIPOLYGON (((","")
            polygon = polygon.replace(")))","")
            #print("** Start poly")
            point = 1
            for pg in polygon.split(', '):
                #print(pg)
                #print("point" + str(point))
                x, y = pg.split(' ')
                # PRINT
                #print("point" + str(point) + "_x: " + x)
                #print("point" + str(point) + "_y: " + y)
                rowOutput += x + ","
                rowOutput += y + ","
                point = point + 1
            rowOutput = rowOutput[:-1]
            #print("*** End poly")
            #print(f'{polygon}')
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
            fclean.write(rowOutput + '\n')
            #print(rowOutput)
    print(f'Processed {line_count} lines.')


fclean.close()