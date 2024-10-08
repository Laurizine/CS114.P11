import pandas as pd

# Đọc hai file CSV
output_de = pd.read_csv(r"E:\KHMT2022.1\MACHINE LEARNING\TH3\output1.csv")
output_chay = pd.read_csv(r"E:\KHMT2022.1\MACHINE LEARNING\TH3\ThongKe_KH_output.csv")

# So sánh hai file
if output_de.equals(output_chay):
    print("Hai file giống nhau.")
else:
    print("Hai file khác nhau.")
