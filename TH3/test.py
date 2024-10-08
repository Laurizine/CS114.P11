import pandas as pd
import sys

# Đọc dữ liệu từ sys.stdin
try:
    df = pd.read_csv(sys.stdin, 
                     usecols=['CustomerID', 'InvoiceDate'], 
                     encoding='utf-8',
                     parse_dates=['InvoiceDate'])
except pd.errors.EmptyDataError:
    print("Không có dữ liệu để đọc")
    sys.exit(1)
except ValueError as e:
    print(f"Lỗi giá trị: {e}")
    sys.exit(1)

# Nhóm theo CustomerID và lấy ngày mua cuối cùng
ngay_mua_cuoi = df.groupby('CustomerID')['InvoiceDate'].max()
ngay_mua_xa_nhat = ngay_mua_cuoi.min()

# Tính điểm (score) là số ngày từ lần mua hàng xa nhất đến lần mua hàng cuối cùng
diem_so = (ngay_mua_cuoi - ngay_mua_xa_nhat).dt.days  

# Tạo DataFrame kết quả
diem_df = pd.DataFrame({'CustomerID': ngay_mua_cuoi.index, 'score': diem_so})

# In kết quả
print(diem_df[['CustomerID', 'score']])
