# ====== KHOI TAO DU LIEU ======

shop_name = ""
product_name = ""
product_description = ""
product_category = ""
keyword_list = []
discount_code_list = []

# ====== MENU ======

while True:

    print("\n========== HE THONG QUAN LY SAN PHAM ==========")
    print("1. Nhap du lieu san pham va xem bao cao")
    print("2. Chuan hoa ten Shop")
    print("3. Kiem tra ma giam gia hop le")
    print("4. Tim kiem va thay the tu khoa trong mo ta")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    # EDGE CASE: menu khong phai so
    if not choice.isdigit():
        print("Lua chon khong hop le!")
        continue

    choice = int(choice)

    match choice:

        # ================= FUNCTION 1 =================
        case 1:

            print("\n===== NHAP DU LIEU SAN PHAM =====")

            shop_name = input("Nhap ten shop: ")

            # EDGE CASE SHOP RONG
            if shop_name.strip() == "":
                print("Ten shop khong duoc bo trong")
                continue

            product_name = input("Nhap ten san pham: ")

            product_description = input("Nhap mo ta san pham: ")

            # EDGE CASE MO TA RONG
            if product_description.strip() == "":
                print("Mo ta san pham khong duoc rong")
                continue

            product_category = input("Nhap danh muc san pham: ")

            keywords = input(
                "Nhap danh sach tu khoa (cach nhau boi dau phay): "
            )

            # ===== XU LY =====

            clean_shop = shop_name.strip()

            clean_product = product_name.strip().title()

            clean_description = product_description.strip()

            description_length = len(clean_description)

            clean_category = " ".join(
                product_category.strip().split()
            ).lower()

            keyword_list = []

            for keyword in keywords.split(","):
                keyword = keyword.strip()

                if keyword != "":
                    keyword_list.append(keyword)

            description_lower = clean_description.lower()
            description_upper = clean_description.upper()

            # ===== BAO CAO =====

            print("\n===== BAO CAO THONG KE =====")

            print("Ten shop:", clean_shop)

            print("Ten san pham:", clean_product)

            print("Mo ta:", clean_description)

            print("Do dai mo ta:", description_length)

            print("Danh muc:", clean_category)

            print("Danh sach tu khoa:", keyword_list)

            print("So luong tu khoa:", len(keyword_list))

            print("Mo ta chu thuong:")
            print(description_lower)

            print("Mo ta chu hoa:")
            print(description_upper)

        # ================= FUNCTION 2 =================
        case 2:

            print("\n===== CHUAN HOA TEN SHOP =====")

            original_shop = input("Nhap ten shop: ")

            if original_shop.strip() == "":
                print("Ten shop khong duoc bo trong")
                continue

            normalized_shop = original_shop.strip()

            normalized_shop = normalized_shop.lower()

            normalized_shop = "-".join(
                normalized_shop.split()
            )

            if not normalized_shop.startswith("shop-"):
                normalized_shop = "shop-" + normalized_shop

            print("Ten shop ban dau:", original_shop)

            print("Ten shop sau chuan hoa:",
                  normalized_shop)

        # ================= FUNCTION 3 =================
        case 3:

            print("\n===== KIEM TRA MA GIAM GIA =====")

            discount_code = input("Nhap ma giam gia: ")

            if discount_code == "":
                print("Ma giam gia khong duoc rong")

            elif " " in discount_code:
                print("Ma giam gia khong duoc chua khoang trang")

            elif len(discount_code) < 6 or len(discount_code) > 12:
                print("Do dai phai tu 6 den 12 ky tu")

            elif discount_code != discount_code.upper():
                print("Ma phai viet hoa toan bo")

            elif not discount_code.isalnum():
                print("Chi duoc chua chu cai va chu so")

            elif not discount_code.startswith("SALE"):
                print("Ma phai bat dau bang SALE")

            else:

                print("Ma giam gia hop le")

                discount_code_list.append(
                    discount_code
                )

                print("Danh sach ma giam gia:")

                print(discount_code_list)

        # ================= FUNCTION 4 =================
        case 4:

            print("\n===== TIM KIEM VA THAY THE =====")

            if product_description.strip() == "":
                print("Chua co mo ta san pham.")
                continue

            find_keyword = input(
                "Nhap tu khoa can tim: "
            )

            replace_keyword = input(
                "Nhap tu khoa thay the: "
            )

            current_description = product_description.strip()

            if find_keyword in current_description:

                count_keyword = current_description.count(
                    find_keyword
                )

                new_description = current_description.replace(
                    find_keyword,
                    replace_keyword
                )

                print("So lan xuat hien:",
                      count_keyword)

                print("Mo ta sau thay the:")

                print(new_description)

            else:
                print("Khong tim thay tu khoa.")

        # ================= FUNCTION 5 =================
        case 5:

            print("Thoat chuong trinh")

            break

        # ================= EDGE CASE =================
        case _:

            print("Lua chon khong hop le!")