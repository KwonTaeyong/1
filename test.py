import pandas as pd
from openpyxl import load_workbook
import json

wb = load_workbook('form.xlsx')
ws = wb.active

filename = 'code_table.xlsx'
column = 'name', 'code', 'option'
df = pd.read_excel(filename, sheet_name='Sheet1', dtype='str')

router_sample = df

ds = pd.DataFrame(router_sample)

print(ds['code']=='31504')

# js = df.to_json(orient='records')
#
# print(json.loads(js))
exit()

wb.save('form1.xlsx')
