import csv

with open('clippings_export.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        (title, author, category, created, location, page, content, tags, 
                notes) = tuple(row);
        print("%s (%s)" % (title, author))
        print("- Your Highlight on page %s | Location %s | Added on Tuesday, " 
                "April 4, 2017 2:02:15 AM" % (page, location))
        print("\n%s" % (content))
        print("==========")
        

