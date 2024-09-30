from email_builder import EmailBuilder


def main():
    email_message = (
        EmailBuilder()
        .add_from("from")
        .add_to("to")
        .add_to("to2")
        .add_subject("sub")
        .add_body("bod")
        .build()
    )
    email_message.send()


if __name__ == "__main__":
    main()
