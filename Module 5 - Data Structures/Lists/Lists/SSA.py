def input_sales() :
    sales = []
    n = int(input("How many months of sales do you want to analyze? Please enter the number of months: "))
    for i in range(0, n) :
        a = int(input(f"Enter the sales of month {i+1}:"))
        sales.append(a)
    return sales

def calculate_statistics(sales) :
    total = sum(sales)
    months = len(sales)
    average = total / months
    highest = max(sales)
    lowest = min(sales)
    return total, average, highest, lowest

def display_result(sales, total, average, highest, lowest) :
    print(f"Monthly Sales : {sales}")
    print("--------- Sales Statistics ----------")
    print(f"Total Sales : {total}")
    print(f"Average Sales: {average :.2f}")
    print(f"Highest Sales: {highest}")
    print(f"Lowest Sales: {lowest}")


def main() :
    sales = input_sales()
    total, average, highest, lowest = calculate_statistics(sales)
    display_result(sales, total, average, highest, lowest)

main()
