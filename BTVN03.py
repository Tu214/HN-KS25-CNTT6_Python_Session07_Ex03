# (1) Phân tích và thiết kế giải pháp (Bắt buộc)
# - Input: + `raw_data` (str): Chuỗi thô chứa thông tin nhân viên.
#          + `choice` (str): Lựa chọn menu từ bàn phím.
#          + `search_id` (str): Mã nhân viên cần tìm kiếm.
# - Output: In trực tiếp ra console chuỗi gốc, bảng báo cáo chuẩn hóa hoặc kết quả tìm kiếm.
# - Giải pháp: Không dùng List/Dict. Xử lý "on-the-fly" trực tiếp trên chuỗi:
#          + Tách dữ liệu bằng `.split("|")` và `.split(";")`.
#          + Loại bỏ khoảng trắng bằng `.strip()`.
#          + Định dạng chữ hoa/thường: ID/Phòng ban dùng `.upper()`, Tên dùng `.title()`.
#          + Bẫy SĐT: Xóa dấu `-` bằng `.replace("-", "")`, kiểm tra số bằng `.isdigit()`,
#            hợp lệ thì che bằng `"******" + phone[6:]`, sai thì gán `"Invalid Format"`.
# - Thuật toán (Luồng): Vòng lặp vô hạn hiển thị menu -> Nhận lựa chọn -> Dùng `match-case`
#   để điều hướng -> Duyệt cắt chuỗi thô để in báo cáo (Case 2) hoặc so khớp ID để tìm kiếm 
#   (Case 3) -> Thoát (Case 4) -> Bắt lỗi nhập sai menu bằng case mặc định `case _`.


# (2) Triển khai code
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    # Hiển thị Menu hệ thống
    print("\n" + "="*5 + " HỆ THỐNG QUẢN LÝ NHÂN SỰ " + "="*5)
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # Sử dụng cấu trúc match - case để điều hướng chức năng
    match choice:
        # CHỨC NĂNG 1: Hiển thị dữ liệu gốc
        case "1":
            print("\n--- DỮ LIỆU GỐC ---")
            print(raw_data)
            
        # CHỨC NĂNG 2: Chuẩn hóa dữ liệu và in báo cáo (Xử lý trực tiếp từ chuỗi)
        case "2":
            print("\n" + "-"*65)
            print(f"{'MÃ NV':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
            print("-"*65)
            
            # Tách chuỗi theo dấu "|" để duyệt từng nhân viên
            for emp_str in raw_data.split("|"):
                info = emp_str.split(";")
                if len(info) < 4:
                    continue
                    
                # Chuẩn hóa dữ liệu đầu ra trực tiếp
                emp_id = info[0].strip().upper()
                name = info[1].strip().title()
                dept = info[3].strip().upper()
                
                # Xử lý bẫy số điện thoại (Edge Case 1)
                phone_raw = info[2].strip().replace("-", "")
                if phone_raw.isdigit():
                    phone = "******" + phone_raw[6:]
                else:
                    phone = "Invalid Format"
                    
                # In dòng kết quả trực tiếp bằng f-string
                print(f"{emp_id:<10} | {name:<20} | {phone:<15} | {dept:<10}")
            print("-"*65)
            
        # CHỨC NĂNG 3: Tìm kiếm nhân viên bằng cách quét chuỗi trực tiếp
        case "3":
            # Nhập ID và tự động sửa bẫy định dạng nhập sai (Edge Case 2)
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
            found = False
            
            # Quét tìm trực tiếp trên chuỗi thô
            for emp_str in raw_data.split("|"):
                info = emp_str.split(";")
                if len(info) < 4:
                    continue
                    
                current_id = info[0].strip().upper()
                
                # So sánh ID nếu trùng khớp thì thực hiện chuẩn hóa để in
                if current_id == search_id:
                    name = info[1].strip().title()
                    dept = info[3].strip().upper()
                    
                    phone_raw = info[2].strip().replace("-", "")
                    if phone_raw.isdigit():
                        phone = "******" + phone_raw[6:]
                    else:
                        phone = "Invalid Format"
                        
                    print("\n--- THÔNG TIN NHÂN VIÊN TÌM THẤY ---")
                    print(f"Mã NV: {current_id}\nHọ tên: {name}\nSĐT: {phone}\nPhòng: {dept}")
                    found = True
                    break # Thoát vòng lặp ngay khi tìm thấy nhân viên
                    
            if not found:
                print("\nKhông tìm thấy nhân viên")
                
        # CHỨC NĂNG 4: Thoát chương trình
        case "4":
            print("\nThoát chương trình")
            break
            
        # XỬ LÝ BẪY 3: Người dùng nhập sai lựa chọn menu (Ký tự khác 1-4)
        case _:
            print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")