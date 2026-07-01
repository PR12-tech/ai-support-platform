from app.services.order_service import lookup_order


def main():

    result = lookup_order(
        "ORD1001"
    )

    print("\n========== ORDER TOOL TEST ==========\n")

    print(result)

    print("\n=====================================\n")


if __name__ == "__main__":

    main()