# 1. Phân tích và thiết kế giải pháp
# 1.1. Phân tích Input / Output
# Chức năng 1: Nhập dữ liệu đơn hàng và xem báo cáo thống kê

# Input

# sender_name (str)
# sender_phone (str)
# pickup_address (str)
# receiver_name (str)
# receiver_phone (str)
# delivery_address (str)
# delivery_note (str)

# Output

# Tên người gửi đã chuẩn hóa
# Tên người nhận đã chuẩn hóa
# Địa chỉ lấy hàng đã chuẩn hóa
# Địa chỉ giao hàng đã chuẩn hóa
# Ghi chú đã chuẩn hóa
# Độ dài ghi chú
# Số lượng từ trong ghi chú
# Ghi chú chữ thường
# Ghi chú chữ hoa
# Chức năng 2: Chuẩn hóa mã đơn hàng

# Input

# order_code (str)

# Output

# Mã đơn hàng ban đầu
# Mã đơn hàng sau chuẩn hóa

# Ví dụ:

# Input:
# gx 12345

# Output:
# GRAB-GX-12345
# Chức năng 3: Ẩn số điện thoại

# Input

# sender_phone (str)
# receiver_phone (str)

# Output

# SĐT người gửi: 098*****21
# SĐT người nhận: 097*****32
# Chức năng 4: Tìm kiếm và thay thế từ khóa

# Input

# keyword_find (str)
# keyword_replace (str)

# Output

# Số lần xuất hiện của từ khóa
# Ghi chú sau khi thay thế
# Chức năng 5: Thoát

# Output

# Thoát chương trình
# 1.2. Đề xuất giải pháp
# Các hàm xử lý chuỗi sử dụng
# Hàm	Mục đích
# strip()	Xóa khoảng trắng đầu cuối
# title()	Viết hoa chữ cái đầu mỗi từ
# lower()	Chuyển chữ thường
# upper()	Chuyển chữ hoa
# split()	Tách chuỗi
# join()	Chuẩn hóa khoảng trắng
# replace()	Thay thế chuỗi
# count()	Đếm số lần xuất hiện
# startswith()	Kiểm tra tiền tố
# isdigit()	Kiểm tra số điện thoại
# len()	Kiểm tra độ dài
# 1.3. Thuật toán (Pseudocode)
# Khai báo:

# sender_name = ""
# sender_phone = ""
# pickup_address = ""

# receiver_name = ""
# receiver_phone = ""
# delivery_address = ""

# delivery_note = ""

# Lặp vô hạn:

#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu không phải số:
#         Báo lỗi
#         tiếp tục

#     Nếu ngoài khoảng 1-5:
#         Báo lỗi
#         tiếp tục

#     Nếu chọn 1:
#         Nhập dữ liệu đơn hàng

#         Kiểm tra dữ liệu rỗng

#         Chuẩn hóa dữ liệu

#         Hiển thị báo cáo

#     Nếu chọn 2:
#         Chuẩn hóa mã đơn hàng

#     Nếu chọn 3:
#         Kiểm tra số điện thoại

#         Nếu hợp lệ:
#             Ẩn số điện thoại

#     Nếu chọn 4:
#         Nếu chưa có ghi chú:
#             Báo lỗi

#         Ngược lại:
#             Tìm kiếm
#             Thay thế
#             Hiển thị kết quả

#     Nếu chọn 5:
#         Thoát chương trình
# 2. Source Code Python Hoàn Chỉnh
# =====================================
# HỆ THỐNG QUẢN LÝ ĐƠN GIAO HÀNG GRAB
# =====================================

sender_name = ""
sender_phone = ""
pickup_address = ""

receiver_name = ""
receiver_phone = ""
delivery_address = ""

delivery_note = ""


# -------------------------------------
# Hàm chuẩn hóa mã đơn hàng
# -------------------------------------
def normalize_order_code(order_code):
    order_code = order_code.strip().upper()

    order_code = "-".join(order_code.split())

    if not order_code.startswith("GRAB-"):
        order_code = "GRAB-" + order_code

    return order_code


# -------------------------------------
# Hàm kiểm tra số điện thoại
# -------------------------------------
def validate_phone(phone):

    if phone.strip() == "":
        return False, "Số điện thoại không được bỏ trống"

    if not phone.isdigit():
        return False, "Số điện thoại không hợp lệ"

    if len(phone) != 10:
        return False, (
            "Số điện thoại không hợp lệ: "
            "Số điện thoại phải có đúng 10 ký tự"
        )

    return True, ""


# -------------------------------------
# Hàm ẩn số điện thoại
# -------------------------------------
def hide_phone(phone):
    return phone[:3] + "*****" + phone[-2:]


# -------------------------------------
# Menu chương trình
# -------------------------------------
while True:

    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu đơn hàng")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")
    print("==========================")

    choice = input("Nhập lựa chọn: ").strip()

    # Bẫy 6
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    # Bẫy 5
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    # =================================
    # CHỨC NĂNG 1
    # =================================
    if choice == 1:

        sender_name = input("Tên người gửi: ")

        if sender_name.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue

        sender_phone = input("SĐT người gửi: ")

        if sender_phone.strip() == "":
            print("SĐT người gửi không được bỏ trống")
            continue

        pickup_address = input("Địa chỉ lấy hàng: ")

        if pickup_address.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue

        receiver_name = input("Tên người nhận: ")

        if receiver_name.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue

        receiver_phone = input("SĐT người nhận: ")

        if receiver_phone.strip() == "":
            print("SĐT người nhận không được bỏ trống")
            continue

        delivery_address = input("Địa chỉ giao hàng: ")

        if delivery_address.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue

        delivery_note = input("Ghi chú giao hàng: ")

        if delivery_note.strip() == "":
            print("Ghi chú giao hàng không được bỏ trống")
            continue

        sender_name_clean = sender_name.strip().title()

        receiver_name_clean = receiver_name.strip().title()

        pickup_address_clean = " ".join(
            pickup_address.strip().split()
        )

        delivery_address_clean = " ".join(
            delivery_address.strip().split()
        )

        note_clean = delivery_note.strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print("Tên người gửi:", sender_name_clean)

        print("Tên người nhận:", receiver_name_clean)

        print("Địa chỉ lấy hàng:", pickup_address_clean)

        print("Địa chỉ giao hàng:", delivery_address_clean)

        print("Ghi chú giao hàng:", note_clean)

        print("Độ dài ghi chú:", len(note_clean))

        print("Số lượng từ:", len(note_clean.split()))

        print("Ghi chú chữ thường:")
        print(note_clean.lower())

        print("Ghi chú chữ hoa:")
        print(note_clean.upper())

    # =================================
    # CHỨC NĂNG 2
    # =================================
    elif choice == 2:

        order_code = input("Nhập mã đơn hàng: ")

        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue

        normalized_code = normalize_order_code(order_code)

        print("Mã đơn hàng ban đầu:", order_code)

        print("Mã đơn hàng chuẩn hóa:", normalized_code)

    # =================================
    # CHỨC NĂNG 3
    # =================================
    elif choice == 3:

        valid_sender, message_sender = validate_phone(
            sender_phone
        )

        if not valid_sender:
            print(message_sender)
            continue

        valid_receiver, message_receiver = validate_phone(
            receiver_phone
        )

        if not valid_receiver:
            print(message_receiver)
            continue

        print("SĐT người gửi:",
              hide_phone(sender_phone))

        print("SĐT người nhận:",
              hide_phone(receiver_phone))

    # =================================
    # CHỨC NĂNG 4
    # =================================
    elif choice == 4:

        # Bẫy 4
        if delivery_note.strip() == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        keyword_find = input(
            "Nhập từ khóa cần tìm: "
        )

        keyword_replace = input(
            "Nhập từ khóa thay thế: "
        )

        count = delivery_note.count(keyword_find)

        if count > 0:

            new_note = delivery_note.replace(
                keyword_find,
                keyword_replace
            )

            print(
                "Số lần xuất hiện của từ khóa:",
                count
            )

            print("Ghi chú giao hàng sau khi thay thế:")
            print(new_note)

            delivery_note = new_note

        else:
            print(
                "Không tìm thấy từ khóa trong ghi chú giao hàng"
            )

    # =================================
    # CHỨC NĂNG 5
    # =================================
    elif choice == 5:

        print("Thoát chương trình")
        break