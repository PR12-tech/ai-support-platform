from app.services.ticket_service import lookup_ticket


def main():

    result = lookup_ticket(
        "TKT1001"
    )

    print("\n========== TICKET TOOL TEST ==========\n")

    print(result)

    print("\n======================================\n")


if __name__ == "__main__":

    main()