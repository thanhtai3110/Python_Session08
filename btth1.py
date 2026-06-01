# 1. Phân tích và thiết kế giải pháp
# A. Input / Output
# Chức năng 1: Nhập dữ liệu và xem báo cáo thống kê

# Input

# username (str)
# video_title (str)
# video_description (str)
# hashtags (str, nhập cách nhau bởi dấu phẩy)

# Output

# Username đã chuẩn hóa
# Tiêu đề đã chuẩn hóa
# Mô tả đã chuẩn hóa
# Độ dài mô tả
# Số lượng từ trong mô tả
# Danh sách hashtag sau chuẩn hóa
# Số lượng hashtag
# Mô tả chữ thường
# Mô tả chữ hoa
# Chức năng 2: Chuẩn hóa tên tài khoản TikTok

# Input

# username (str)

# Output

# Username ban đầu
# Username chuẩn hóa

# Ví dụ:

# Rikkei Education

# Kết quả:

# @rikkei education
# Chức năng 3: Kiểm tra hashtag hợp lệ

# Input

# hashtag (str)

# Output

# Thông báo hợp lệ hoặc lỗi cụ thể
# Nếu hợp lệ thì thêm vào danh sách hashtag
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
# B. Giải pháp
# Các phương thức xử lý chuỗi sử dụng
# Phương thức	Mục đích
# strip()	Xóa khoảng trắng đầu cuối
# title()	Viết hoa chữ cái đầu mỗi từ
# lower()	Chuyển chữ thường
# upper()	Chuyển chữ hoa
# split()	Tách chuỗi
# join()	Ghép chuỗi
# replace()	Thay thế chuỗi
# count()	Đếm số lần xuất hiện
# startswith()	Kiểm tra ký tự đầu
# isalnum()	Kiểm tra chữ và số
# C. Thuật toán (Pseudocode)
# Khai báo:
#     username = ""
#     title = ""
#     description = ""
#     hashtags = []

# Lặp vô hạn:

#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu lựa chọn không phải số:
#         Thông báo lỗi
#         tiếp tục

#     Nếu lựa chọn = 1:
#         Nhập username
#         Kiểm tra rỗng

#         Nhập title

#         Nhập description
#         Kiểm tra rỗng

#         Nhập hashtag

#         Chuẩn hóa dữ liệu

#         Hiển thị báo cáo

#     Nếu lựa chọn = 2:
#         Chuẩn hóa username
#         Hiển thị kết quả

#     Nếu lựa chọn = 3:
#         Nhập hashtag

#         Kiểm tra:
#             không rỗng
#             bắt đầu #
#             không chứa khoảng trắng
#             độ dài >= 2
#             ký tự hợp lệ

#         Nếu hợp lệ:
#             thêm vào danh sách

#     Nếu lựa chọn = 4:
#         Nhập từ khóa tìm
#         Nhập từ khóa thay thế

#         Nếu từ khóa tồn tại:
#             thay thế
#             hiển thị kết quả
#         Ngược lại:
#             thông báo không tìm thấy

#     Nếu lựa chọn = 5:
#         Thoát

#     Ngược lại:
#         thông báo nhập từ 1 đến 5
# ==========================
# HỆ THỐNG KIỂM DUYỆT NỘI DUNG TIKTOK
# ==========================

username = ""
video_title = ""
video_description = ""
hashtags = []

def validate_hashtag(hashtag):
    hashtag = hashtag.strip()

    if hashtag == "":
        return False, "Hashtag không được rỗng"

    if not hashtag.startswith("#"):
        return False, "Hashtag phải bắt đầu bằng ký tự #"

    if " " in hashtag:
        return False, "Hashtag không được chứa khoảng trắng"

    if len(hashtag) < 2:
        return False, "Hashtag phải có ít nhất 2 ký tự"

    for char in hashtag[1:]:
        if not (char.isalnum() or char == "_"):
            return False, (
                "Hashtag chỉ được chứa chữ cái, "
                "chữ số hoặc dấu gạch dưới"
            )

    return True, "Hashtag hợp lệ"


# --------------------------
# Menu
# --------------------------
while True:

    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")
    print("==========================")

    choice = input("Nhập lựa chọn: ").strip()

    # Bẫy 4
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
        continue

    choice = int(choice)

    # Bẫy 3
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")
        continue

    # =====================
    # Chức năng 1
    # =====================
    if choice == 1:

        username = input("Tên tài khoản: ")

        # Bẫy 1
        if username.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        video_title = input("Tiêu đề video: ")

        video_description = input("Mô tả video: ")

        # Bẫy 2
        if video_description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input(
            "Nhập hashtag (cách nhau bởi dấu phẩy): "
        )

        # Chuẩn hóa dữ liệu
        username_clean = username.strip()

        title_clean = video_title.strip().title()

        description_clean = video_description.strip()

        hashtags = [
            tag.strip()
            for tag in hashtag_input.split(",")
            if tag.strip() != ""
        ]

        # Thống kê
        description_length = len(description_clean)

        word_count = len(description_clean.split())

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print("Tên tài khoản:", username_clean)

        print("Tiêu đề:", title_clean)

        print("Mô tả:", description_clean)

        print("Độ dài mô tả:", description_length)

        print("Số lượng từ:", word_count)

        print("Danh sách hashtag:", hashtags)

        print("Số lượng hashtag:", len(hashtags))

        print("Mô tả chữ thường:")
        print(description_clean.lower())

        print("Mô tả chữ hoa:")
        print(description_clean.upper())

    # =====================
    # Chức năng 2
    # =====================
    elif choice == 2:

        account = input("Nhập tên tài khoản: ")

        if account.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        normalized_account = "@" + account.strip().lower()

        print("Tên tài khoản ban đầu:", account)

        print("Tên tài khoản chuẩn hóa:",
              normalized_account)

    # =====================
    # Chức năng 3
    # =====================
    elif choice == 3:

        hashtag = input("Nhập hashtag: ")

        is_valid, message = validate_hashtag(hashtag)

        if is_valid:
            hashtags.append(hashtag.strip())

            print("Hashtag hợp lệ")

            print("Đã thêm vào danh sách hashtag.")
        else:
            print(message)

    # =====================
    # Chức năng 4
    # =====================
    elif choice == 4:

        if video_description.strip() == "":
            print("Chưa có mô tả video.")
            continue

        keyword_find = input(
            "Nhập từ khóa cần tìm: "
        )

        keyword_replace = input(
            "Nhập từ khóa thay thế: "
        )

        count = video_description.count(keyword_find)

        if count > 0:

            new_description = video_description.replace(
                keyword_find,
                keyword_replace
            )

            print("\nSố lần xuất hiện:", count)

            print("Mô tả sau khi thay thế:")
            print(new_description)

            video_description = new_description

        else:
            print("Không tìm thấy từ khóa trong mô tả.")

    # =====================
    # Chức năng 5
    # =====================
    elif choice == 5:

        print("Thoát chương trình")
        break