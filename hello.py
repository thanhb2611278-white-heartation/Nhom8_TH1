import os
# Mở/Tạo file 'large_script.py' với dung lượng > 1MB
with open("large_script.py", "w", encoding="utf-8") as f:
    f.write("# File Python dung lượng lớn thử nghiệm Notepad++\n")
    
    # Tạo một chuỗi cực dài trên một dòng (Notepad++ rất dễ đơ khi gặp 1 dòng quá dài)
    f.write("LONG_STRING = '" + "A" * 1000000 + "'\n\n")
    
    # Tạo thêm 20,000 dòng code lặp đi lặp lại để tăng số lượng dòng
    for i in range(20000):
        f.write(f"print('Đang kiểm tra hiệu năng Notepad++ với dòng số: {i}')\n")

print("Đã tạo file large_script.py thành công!")

# In ra đường dẫn tuyệt đối của file ngay sau khi tạo
print("File được lưu tại:", os.path.abspath("large_script.py"))