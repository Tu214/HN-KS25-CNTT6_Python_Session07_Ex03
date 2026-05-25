# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# - INPUT/OUTPUT: Input: Chuỗi thô `raw_data` (str), lựa chọn menu và ID tìm kiếm từ bàn phím (str). 
#                 Output: Menu điều hướng, bảng báo cáo căn lề chuẩn (f-string) và thông tin tìm kiếm/báo lỗi.
# - GIẢI PHÁP: Dùng `while True` + `match-case` chạy menu. Lưu dữ liệu sạch vào `list` chứa các `dict` để tối ưu tìm kiếm.
#              Dùng `.split()`, `.strip()`, `.upper()`, `.title()` xử lý chuỗi. Xóa '-' bằng `.replace()`, check `.isdigit()` để che số.
# - LUỒNG CHƯƠNG TRÌNH: Khởi tạo dữ liệu -> Hiển thị menu -> Nhận lựa chọn -> Khớp case:
#   + Case "1": In chuỗi thô.
#   + Case "2": Reset db -> Tách chuỗi bằng '|' và ';' -> Chuẩn hóa định dạng -> Xử lý/che SĐT -> Lưu vào db -> In bảng f-string.
#   + Case "3": Nhận ID -> Ép chữ hoa, xóa khoảng trắng -> Duyệt db: Nếu trùng -> In kết quả & break; Hết db không thấy -> Báo lỗi.
#   + Case "4": Báo thoát chương trình -> `break` dừng vòng lặp.
#   + Case _  : Báo lựa chọn không hợp lệ -> Tiếp tục vòng lặp menu.

# (2) Triển khai code
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
cleaned_database = []

while True:
    print("\n" + "="*10 + " HỆ THỐNG QUẢN LÝ NHÂN SỰ " + "="*10)
    print("1. Hiển thị chuỗi dữ liệu gốc\n2. Chuẩn hóa dữ liệu và in báo cáo\n3. Tìm kiếm nhân viên theo mã ID\n4. Thoát chương trình")
    print("=" * 46)
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    match user_choice:
        case "1":
            print(f"\n[DỮ LIỆU GỐC TỪ CRM]:\n{raw_data}")
            
        case "2":
            cleaned_database.clear()
            for emp_raw in raw_data.split("|"):
                info_parts = emp_raw.split(";")
                if len(info_parts) == 4:
                    # Chuẩn hóa văn bản và xử lý bẫy số điện thoại (Bẫy 1)
                    phone_processed = info_parts[2].strip().replace("-", "")
                    secured_phone = "******" + phone_processed[6:] if phone_processed.isdigit() else "Invalid Format"
                    cleaned_database.append({
                        "id": info_parts[0].strip().upper(),
                        "name": info_parts[1].strip().title(),
                        "phone": secured_phone,
                        "department": info_parts[3].strip().upper()
                    })
            # In báo cáo dạng bảng căn lề tự động
            print("\n" + "-"*68)
            print(f"| {'MÃ ID':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10} |")
            print("-"*65)
            for emp in cleaned_database:
                print(f"| {emp['id']:<10} | {emp['name']:<20} | {emp['phone']:<15} | {emp['department']:<10} |")
            print("-"*68 + "\n=> Chuẩn hóa dữ liệu thành công!")
        case "3":
            # Bẫy nhập liệu tìm kiếm (Bẫy 2)
            search_id = input("Nhập mã nhân viên cần tìm (Ví dụ: emp-002): ").strip().upper()
            if not cleaned_database:
                print("\n[!] Cảnh báo: Vui lòng chạy chức năng 2 để chuẩn hóa dữ liệu trước!")
                continue
            is_found = False
            for emp in cleaned_database:
                if emp['id'] == search_id:
                    print(f"\n[KẾT QUẢ]:\n+ ID: {emp['id']}\n+ Tên: {emp['name']}\n+ SĐT: {emp['phone']}\n+ Phòng: {emp['department']}")
                    is_found = True
                    break
            if not is_found:
                print("Không tìm thấy nhân viên")
        case "4":
            print("\nThoát chương trình. Hẹn gặp lại!")
            break
        case _: # Xử lý bẫy nhập sai menu (Bẫy 3)
            print("\n[!] Lựa chọn không hợp lệ, vui lòng nhập lại!")