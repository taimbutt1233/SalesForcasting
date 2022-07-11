import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Outlet_Size_Medium','Outlet_Size_NA',
       'Outlet_Size_Small', 'Outlet_Type_Supermarket Type1',
       'Outlet_Type_Supermarket Type2', 'Outlet_Type_Supermarket Type3'})

print(r.json())
