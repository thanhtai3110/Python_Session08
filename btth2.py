# 1. Phân tích và thiết kế giải pháp
# 1.1. Phân tích Input / Output
# Chức năng 1: Nhập dữ liệu sản phẩm và xem báo cáo thống kê

# Input

# shop_name (str)
# product_name (str)
# product_description (str)
# category (str)
# keywords (str, các từ khóa cách nhau bởi dấu phẩy)

# Output

# Tên shop đã chuẩn hóa khoảng trắng
# Tên sản phẩm viết hoa chữ cái đầu mỗi từ
# Mô tả đã chuẩn hóa
# Độ dài mô tả
# Danh mục viết thường
# Danh sách từ khóa sau khi chuẩn hóa
# Số lượng từ khóa
# Mô tả chữ thường
# Mô tả chữ hoa
# Chức năng 2: Chuẩn hóa tên Shop

# Input

# shop_name (str)

# Output

# Tên shop ban đầu
# Tên shop sau chuẩn hóa

# Ví dụ:

# Input:
# " Rikkei Education Mall "

# Output:
# "shop-rikkei-education-mall"
# Chức năng 3: Kiểm tra mã giảm giá

# Input

# discount_code (str)

# Output

# Thông báo hợp lệ hoặc lỗi cụ thể
# Nếu hợp lệ thì thêm vào danh sách mã giảm giá
# Chức năng 4: Tìm kiếm và thay thế từ khóa

# Input

# keyword_find (str)
# keyword_replace (str)

# Output

# Số lần xuất hiện
# Mô tả sau khi thay thế
# Chức năng 5: Thoát

# Output

# Thoát chương trình
# 1.2. Đề xuất giải pháp
# Các phương thức xử lý chuỗi sử dụng
# Hàm	Công dụng
# strip()	Xóa khoảng trắng đầu cuối
# title()	Viết hoa chữ cái đầu mỗi từ
# lower()	Chuyển chữ thường
# upper()	Chuyển chữ hoa
# split()	Tách chuỗi
# join()	Ghép chuỗi
# replace()	Thay thế chuỗi
# count()	Đếm số lần xuất hiện
# startswith()	Kiểm tra chuỗi bắt đầu
# isalnum()	Kiểm tra chữ và số
# isdigit()	Kiểm tra nhập số menu
# 1.3. Thuật toán (Pseudocode)
# Khai báo:

# shop_name = ""
# product_name = ""
# product_description = ""
# category = ""
# keywords = []
# discount_codes = []

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
#         Nhập thông tin sản phẩm

#         Kiểm tra shop rỗng
#         Kiểm tra mô tả rỗng

#         Chuẩn hóa dữ liệu

#         Hiển thị báo cáo

#     Nếu chọn 2:
#         Chuẩn hóa tên shop

#     Nếu chọn 3:
#         Kiểm tra mã giảm giá

#         Nếu hợp lệ:
#             Thêm vào danh sách

#     Nếu chọn 4:
#         Tìm từ khóa trong mô tả

#         Nếu tìm thấy:
#             Thay thế
#             Hiển thị kết quả

#         Ngược lại:
#             Thông báo không tìm thấy

#     Nếu chọn 5:
#         Thoát chương trình
# 2. Source Code Python Hoàn Chỉnh
# =====================================
# HỆ THỐNG QUẢN LÝ THÔNG TIN SẢN PHẨM
# =====================================

shop_name = ""
product_name = ""
product_description = ""
category = ""

keywords = []
discount_codes = []


# -------------------------------------
# Hàm chuẩn hóa tên shop
# -------------------------------------
def normalize_shop_name(shop_name):
    shop_name = shop_name.strip().lower()

    shop_name = "-".join(shop_name.split())

    if not shop_name.startswith("shop-"):
        shop_name = "shop-" + shop_name

    return shop_name


# -------------------------------------
# Hàm kiểm tra mã giảm giá
# -------------------------------------
def validate_discount_code(code):

    code = code.strip()

    if code == "":
        return False, "Mã giảm giá không được rỗng"

    if " " in code:
        return False, "Mã giảm giá không được chứa khoảng trắng"

    if len(code) < 6 or len(code) > 12:
        return False, "Mã giảm giá phải có độ dài từ 6 đến 12 ký tự"

    if not code.isupper():
        return False, "Mã giảm giá phải viết hoa toàn bộ"

    if not code.isalnum():
        return False, "Mã giảm giá chỉ được chứa chữ cái và chữ số"

    if not code.startswith("SALE"):
        return False, "Mã giảm giá phải bắt đầu bằng SALE"

    return True, "Mã giảm giá hợp lệ"


# -------------------------------------
# Menu chương trình
# -------------------------------------
while True:

    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")
    print("==========================")

    choice = input("Nhập lựa chọn: ").strip()

    # Bẫy 4
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")
        continue

    choice = int(choice)

    # Bẫy 3
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")
        continue

    # =================================
    # CHỨC NĂNG 1
    # =================================
    if choice == 1:

        shop_name = input("Nhập tên shop: ")

        # Bẫy 1
        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Nhập tên sản phẩm: ")

        product_description = input("Nhập mô tả sản phẩm: ")

        # Bẫy 2
        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category = input("Nhập danh mục sản phẩm: ")

        keyword_input = input(
            "Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): "
        )

        # Chuẩn hóa dữ liệu
        shop_clean = shop_name.strip()

        product_clean = product_name.strip().title()

        description_clean = product_description.strip()

        category_clean = category.strip().lower()

        keywords = [
            keyword.strip()
            for keyword in keyword_input.split(",")
            if keyword.strip() != ""
        ]

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print("Tên shop:", shop_clean)

        print("Tên sản phẩm:", product_clean)

        print("Mô tả sản phẩm:", description_clean)

        print("Độ dài mô tả:", len(description_clean))

        print("Danh mục:", category_clean)

        print("Danh sách từ khóa:", keywords)

        print("Số lượng từ khóa:", len(keywords))

        print("Mô tả chữ thường:")
        print(description_clean.lower())

        print("Mô tả chữ hoa:")
        print(description_clean.upper())

    # =================================
    # CHỨC NĂNG 2
    # =================================
    elif choice == 2:

        shop_input = input("Nhập tên shop: ")

        if shop_input.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        normalized_shop = normalize_shop_name(shop_input)

        print("Tên shop ban đầu:", shop_input)

        print("Tên shop chuẩn hóa:", normalized_shop)

    # =================================
    # CHỨC NĂNG 3
    # =================================
    elif choice == 3:

        code = input("Nhập mã giảm giá: ")

        is_valid, message = validate_discount_code(code)

        if is_valid:

            discount_codes.append(code)

            print("Mã giảm giá hợp lệ")

            print("Danh sách mã giảm giá hiện tại:")

            for discount_code in discount_codes:
                print("-", discount_code)

        else:
            print(message)

    # =================================
    # CHỨC NĂNG 4
    # =================================
    elif choice == 4:

        if product_description.strip() == "":
            print("Chưa có mô tả sản phẩm.")
            continue

        keyword_find = input("Nhập từ khóa cần tìm: ")

        keyword_replace = input("Nhập từ khóa thay thế: ")

        count = product_description.count(keyword_find)

        if count > 0:

            new_description = product_description.replace(
                keyword_find,
                keyword_replace
            )

            print("Số lần xuất hiện của từ khóa:", count)

            print("Mô tả sau khi thay thế:")
            print(new_description)

            product_description = new_description

        else:
            print("Không tìm thấy từ khóa trong mô tả sản phẩm.")

    # =================================
    # CHỨC NĂNG 5
    # =================================
    elif choice == 5:

        print("Thoát chương trình")
        break