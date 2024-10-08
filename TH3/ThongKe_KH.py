import pandas as pd

# Đọc dữ liệu từ file CSV, em có tham khảo cách đọc này trên ChatGPT
df = pd.read_csv(r"E:\KHMT2022.1\MACHINE LEARNING\TH3\input1.csv", 
                      usecols=['CustomerID', 'InvoiceDate'], encoding='ISO-8859-1', parse_dates=['InvoiceDate'])

ngay_mua_cuoi = df.groupby('CustomerID')['InvoiceDate'].max()

ngay_mua_xa_nhat = ngay_mua_cuoi.min()

# Tính điểm (score) là số ngày từ lần mua hàng xa nhất đến lần mua hàng cuối cùng
diem_so = (ngay_mua_cuoi - ngay_mua_xa_nhat).dt.days  

diem_df = pd.DataFrame({'CustomerID': ngay_mua_cuoi.index, 'score': diem_so})
print(diem_df[['CustomerID', 'score']])

# Lệnh tạo file để so sánh với file output
# diem_df[['CustomerID', 'score']].to_csv(r"E:\KHMT2022.1\MACHINE LEARNING\TH3\wecode 3_output.csv", index=False)
