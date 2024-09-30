from email_message import EmailMessage


# builder
class EmailBuilder:
    def __init__(self) -> None:
        self._email_message = EmailMessage()

    def add_from(self, from_address: str):
        self._email_message.set_from(from_address)
        return self

    def add_subject(self, subject_address: str):
        self._email_message.set_subject(subject_address)
        return self

    def add_body(self, body_address: str):
        self._email_message.set_body(body_address)
        return self

    def add_to(self, to_address: str):
        self._email_message.get_to().append(to_address)
        return self

    def add_cc(self, cc_address: str):
        self._email_message.get_cc().append(cc_address)
        return self

    def add_bcc(self, bcc_address: str):
        self._email_message.get_bcc().append(bcc_address)
        return self

    def build(self):
        return self._email_message
