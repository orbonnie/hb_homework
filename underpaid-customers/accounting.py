melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

def calc_payments(customer, qty, price, payment):
    """Calculates the balance for all customers
    """

    total = qty * price
    cust = customer.ljust(20)
    tot = f"{total:.2f}".rjust(10)
    pay = f"{payment:.2f}".rjust(10)
    bal = f"{(payment - total):.2f}".rjust(10)

    print(cust, tot, pay, bal)

    # if total > payment:
    #     print(f"{customer} owed {total:.2f}, but only paid {payment:.2f}.",
    #     f"They stil owe {(total - payment):.2f}"
    #     )
    # elif total < payment:
    #     print(f"{customer} owed {total:.2f}, but paid {payment:.2f}.",
    #     f"They are owed a credit of {(payment - total):.2f}. "
    #     )
    # else:
    #     print(f"{customer} has a balance of 0")



def read_payments(file, price):
    """reads customer payment report
    """

    print("\nCUSTOMER                  TOTAL     PAYMENT     BALANCE\n".ljust(80))
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        data = line.split("|")
        calc_payments(data[1], int(data[2]), price, float(data[3]))
        #find_under_payment(data[1], int(data[2]), price, float(data[3]))

    the_file.close()

def find_under_payment(customer, qty, price, payment):
    """Finds customers who still owe a balance
    """

    total = qty * price

    if total > payment:
        cust = customer.ljust(20)
        tot = f"{total:.2f}".rjust(10)
        pay = f"{payment:.2f}".rjust(10)
        bal = f"{(payment - total):.2f}".rjust(10)

        print(cust, tot, pay, bal)



read_payments("customer-orders.txt", melon_cost)


# calc_payments(customer1_name, customer1_melons, melon_cost, customer1_paid)
# calc_payments(customer2_name, customer2_melons, melon_cost, customer2_paid)
# calc_payments(customer3_name, customer3_melons, melon_cost, customer3_paid)
# calc_payments(customer4_name, customer4_melons, melon_cost, customer4_paid)
# calc_payments(customer5_name, customer5_melons, melon_cost, customer5_paid)
# calc_payments(customer6_name, customer6_melons, melon_cost, customer6_paid)