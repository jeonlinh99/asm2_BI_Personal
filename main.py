import pandas as pd
while True:
    print("Please choose the function: ")
    print("1: Print original dataset")
    print("2: Print dataset that pre-processed ")
    print("3: Exit")
    n = int(input())
    new_sales_record = pd.read_csv('Sales-Records.csv')
    if n == 1:
        print(new_sales_record)
        break
    if n == 2:
# Remove rows that have null Unit Price, Unit cost, Units Sold, Total Cost
        new_sales_record.dropna(subset=["Unit Price", "Unit Cost", "Total Cost","Units Sold"], inplace= True)
# Remove rows that have special characters(!@#$%^&*) in columns: Item Type
        speChars = ["!",'@','#','$','%','^','&','*']
        for char in speChars:
            new_sales_record['Item Type'] = new_sales_record['Item Type'].str.replace(char, '',regex= True)
# Replace wrong data to default: negative value in column Total Profit to 0:
        for x in new_sales_record.index:
          if new_sales_record.loc[x, "Total Profit"] < 0:
            new_sales_record.loc[x, "Total Profit"] = 0
        print(new_sales_record)
# save new_sales_record to a new file "New_sales_record.csv":
        new_sales_record.to_csv('New_sales_record.csv', index=False)
        break
    if n==3 :
        print("Thank for using us")
        break









