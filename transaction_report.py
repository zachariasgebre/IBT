# 4. Wrap the file read in try / except for a missing file
try:
    customer_spend = {}

    # 1. Read transactions.txt line by line (format: name,amount)
    with open("transactions.txt", "r") as file:
        for line in file:
            # Strip whitespace and skip empty lines
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            
            # Split the line by the comma into name and amount string
            name, amount_str = cleaned_line.split(",")
            amount = float(amount_str)

            # 2. Build a dict mapping each customer to their total spend
            if name in customer_spend:
                customer_spend[name] += amount  # Add to existing total
            else:
                customer_spend[name] = amount   # Initialize new customer

    # 3. Sort each customer and total, highest first
    # sorted() creates a list of tuples like [('Name', total), ...]
    sorted_report = sorted(customer_spend.items(), key=lambda item: item[1], reverse=True)

    # Print results to the console
    print("\n--- Transaction Summary (Console) ---")
    for name, total in sorted_report:
        print(f"{name}: {total:.2f} ETB")

    # 5. Write the summary to report.txt
    with open("report.txt", "w") as output_file:
        output_file.write("--- Customer Total Spend Report ---\n")
        for name, total in sorted_report:
            output_file.write(f"{name}: {total:.2f} ETB\n")
            
    print("\nSuccess! 'report.txt' has been generated.")

except FileNotFoundError:
    print("Error: The file 'transactions.txt' could not be found.")
    print("Please make sure it is placed in the correct folder.")