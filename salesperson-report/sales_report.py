"""Generate sales report showing total melons each salesperson sold."""

# create a list to hold the salespeople
salespeople = []
# create another list to hold each salesperson's corresponding melon sales
melons_sold = []

# read the text from the sales report and save the list-like object to the 'f' var
f = open('sales-report.txt')

# iterate through each line in the text
for line in f:
    # remove whitespace from the right
    line = line.rstrip()
    #create a list for each line with an index word spearated by '|'
    entries = line.split('|')
    # create a salesperson var to refer to the 0 index of each list
    salesperson = entries[0]
    # create a melons var to refer to the 2 index of each list, converted to an int
    melons = int(entries[2])

    # check if the salesperson is in the salespeople list
    if salesperson in salespeople:
        # if yes, get the index of the salesperson in the list
        position = salespeople.index(salesperson)
        # add the melons from this list to the number in salesperson's index in the melons_sold list
        melons_sold[position] += melons

    # if the salesperson is not in the salespeople list
    else:
        # append the salesperson to the end salespeople list
        salespeople.append(salesperson)
        # append the melon count from the list to the end of the melons_sold list
        melons_sold.append(melons)

#iterate through numbers the length of the salepeople list - 1
for i in range(len(salespeople)):
    # print a message containing the salesperson name from the salespeople list and the count
    # from the melon_count list for the given index
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


# ****OPTIMIZED****

# contain functionality within a function for repeatability and containerizing
def generate_sales_report(filename):

    # create a dict to hold all salesperson and melons_sold all in one structure
    report = {}

    # read the text from the sales report and save the list-like object to the 'f' var
    f = open(filename)

    # iterate over each line of text
    for line in f:
        # remove extra whitespace from the line
        # create a list with a value for each word in the line, split at the '|' character
        # save the list to a new 'sale' variable
        sale = line.strip().split('|')
        # create a salesperson var to refer to the 0 index of each list
        rep = sale[0]
        # create a melons var to refer to the 2 index of each list, converted to an int
        melons_qty = int(sale[2])

        # check if salesperson is in the report dict
        if rep in report:
            # if so, add the melon_qty to the value of that key
            report[rep] += melons_qty
        # if not, create an entry in the report dict
        #   with the rep name as the key and the melon_qty as the initial value
        else: report[rep] = melons_qty

    # sorts reps by top sales based on qty and saves the results to a list of tuples called 'top_sales'
    top_sales = sorted(report.items(), key= lambda item: item[1], reverse=True)

    # iterate over the 'top_sales' list and prints the tuple values for rep and qty value
    print('\n************RANKED REPORT**************\n')
    for sale in top_sales:
        print(f'{sale[0]} sold {sale[1]} melons')


# call the function and pass the sales report as an arg
generate_sales_report("sales-report.txt")