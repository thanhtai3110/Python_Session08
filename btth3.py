# ===== KHOI TAO =====

sender_name = ""
sender_phone = ""
pickup_address = ""

receiver_name = ""
receiver_phone = ""
delivery_address = ""

delivery_note = ""

# ===== MENU =====

while True:

    print("\n========== HE THONG GRAB EXPRESS ==========")
    print("1. Nhap du lieu don hang")
    print("2. Chuan hoa ma don hang")
    print("3. An so dien thoai")
    print("4. Tim kiem va thay the trong ghi chu")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    # EDGE CASE: khong phai so
    if not choice.isdigit():
        print("Lua chon khong hop le")
        continue

    choice = int(choice)

    match choice:

        # ================= CHUC NANG 1 =================

        case 1:

            print("\n===== NHAP DON HANG =====")

            sender_name = input("Ten nguoi gui: ")

            if sender_name.strip() == "":
                print("Ten nguoi gui khong duoc bo trong")
                continue

            sender_phone = input("SDT nguoi gui: ")

            if sender_phone.strip() == "":
                print("SDT nguoi gui khong duoc bo trong")
                continue

            pickup_address = input("Dia chi lay hang: ")

            if pickup_address.strip() == "":
                print("Dia chi lay hang khong duoc bo trong")
                continue

            receiver_name = input("Ten nguoi nhan: ")

            if receiver_name.strip() == "":
                print("Ten nguoi nhan khong duoc bo trong")
                continue

            receiver_phone = input("SDT nguoi nhan: ")

            if receiver_phone.strip() == "":
                print("SDT nguoi nhan khong duoc bo trong")
                continue

            delivery_address = input("Dia chi giao hang: ")

            if delivery_address.strip() == "":
                print("Dia chi giao hang khong duoc bo trong")
                continue

            delivery_note = input("Ghi chu giao hang: ")

            if delivery_note.strip() == "":
                print("Ghi chu giao hang khong duoc bo trong")
                continue

            # ===== XU LY =====

            clean_sender = sender_name.strip().title()

            clean_receiver = receiver_name.strip().title()

            clean_pickup = " ".join(
                pickup_address.strip().split()
            )

            clean_delivery = " ".join(
                delivery_address.strip().split()
            )

            clean_note = delivery_note.strip()

            note_length = len(clean_note)

            note_word_count = len(clean_note.split())

            note_lower = clean_note.lower()

            note_upper = clean_note.upper()

            # ===== BAO CAO =====

            print("\n===== BAO CAO =====")

            print("Nguoi gui:", clean_sender)

            print("Nguoi nhan:", clean_receiver)

            print("Dia chi lay hang:", clean_pickup)

            print("Dia chi giao hang:", clean_delivery)

            print("Ghi chu:", clean_note)

            print("Do dai ghi chu:", note_length)

            print("So luong tu:", note_word_count)

            print("Ghi chu chu thuong:")
            print(note_lower)

            print("Ghi chu chu hoa:")
            print(note_upper)

        # ================= CHUC NANG 2 =================

        case 2:

            print("\n===== CHUAN HOA MA DON =====")

            order_code = input("Nhap ma don hang: ")

            if order_code.strip() == "":
                print("Ma don hang khong duoc bo trong")
                continue

            original_code = order_code

            order_code = order_code.strip()

            order_code = order_code.upper()

            order_code = "-".join(
                order_code.split()
            )

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Ma don ban dau:", original_code)

            print("Ma don sau chuan hoa:",
                  order_code)

        # ================= CHUC NANG 3 =================

        case 3:

            print("\n===== AN SO DIEN THOAI =====")

            # ---- nguoi gui ----

            if sender_phone == "" or receiver_phone == "":
                print("Chua co du lieu so dien thoai")
                continue

            if not sender_phone.isdigit():
                print("So dien thoai nguoi gui khong hop le")

            elif len(sender_phone) != 10:
                print("So dien thoai khong hop le: So dien thoai phai co dung 10 ky tu")

            else:

                hidden_sender = (
                    sender_phone[:3]
                    + "*****"
                    + sender_phone[-2:]
                )

                print("SDT nguoi gui:",
                      hidden_sender)

            # ---- nguoi nhan ----

            if not receiver_phone.isdigit():
                print("So dien thoai nguoi nhan khong hop le")

            elif len(receiver_phone) != 10:
                print("So dien thoai khong hop le: So dien thoai phai co dung 10 ky tu")

            else:

                hidden_receiver = (
                    receiver_phone[:3]
                    + "*****"
                    + receiver_phone[-2:]
                )

                print("SDT nguoi nhan:",
                      hidden_receiver)

        # ================= CHUC NANG 4 =================

        case 4:

            print("\n===== TIM KIEM GHI CHU =====")

            if delivery_note.strip() == "":
                print("Chua co ghi chu giao hang de tim kiem")
                continue

            find_word = input(
                "Nhap tu khoa can tim: "
            )

            replace_word = input(
                "Nhap tu khoa thay the: "
            )

            current_note = delivery_note.strip()

            if find_word in current_note:

                count_word = current_note.count(
                    find_word
                )

                new_note = current_note.replace(
                    find_word,
                    replace_word
                )

                print("So lan xuat hien:",
                      count_word)

                print("Ghi chu sau thay the:")

                print(new_note)

            else:

                print("Khong tim thay tu khoa")

        # ================= CHUC NANG 5 =================

        case 5:

            print("Thoat chuong trinh")

            break

        # ================= EDGE CASE =================

        case _:

            print("Lua chon khong hop le")