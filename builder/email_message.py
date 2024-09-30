class EmailMessage:
    def __init__(self) -> None:
        self._from = ""
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ""
        self._body = ""

    def set_from(self, from_address: str):
        # validation
        self._from = from_address

    def set_subject(self, subject_address: str):
        # validation
        self._subject = subject_address

    def set_body(self, body_address: str):
        # validation
        self._body = body_address

    def get_to(self):
        return self._to

    def get_cc(self):
        return self._cc

    def get_bcc(self):
        return self._bcc

    def send(self):
        print("email sent")
        print(f"from {self._from}")
        print(f"to {self._to}")
        print(f"cc {self._cc}")
        print(f"bcc {self._bcc}")
        print(f"body {self._body}")
