#importing necessary libraries
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

#adding relevant workbook to code
wb = load_workbook('C:\\Code\\SQL projects\\Bike store database\\temp_py_code.xlsx')
wb.active = wb['Sheet1']
ws = wb.active

#checking if the data file has empty cells or not
f = 0
for row in range(2,ws.max_row+1):
    for col in range(1,ws.max_column+1):
        char = get_column_letter(col)
        if ws[char + str(row)].value is None:
            print ("Data file has empty cells")
            f=1
            break
    if f == 1:
        break

#checking if key data is empty or not
f = 0
temp_list = ["product_id", "brand_id", "category_id", "product_list_price", "order_id", "order_item_quantity", "order_item_list_price", "discount", "customer_id", "store_id", "staff_id", "customer_first_name", "customer_last_name"]
for col in range(1,ws.max_column+1):
    for row in range(2,ws.max_row+1):
        char = get_column_letter(col)
        if ws[char + str(1)].value in temp_list and ws[char + str(row)].value is None:
            print ("Data file is missing crucial information")
            f=1
            break
    if f == 1:
        break
if f == 0:
    print ("Data file has all the necessary information")


#column sum checks
#range checks
#text or number checks
