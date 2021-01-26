class BaseContact:
    @property
    def label_length(self):
        print(self.name)
        print(self.last_name)
        return len(f"{self.name} {self.last_name}")

    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def contact(self):
        print(f"Wybieram numer +48 {self.phone} i dzwonię do {self.name} {self.last_name}")


class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer +48 {self.business_phone} i dzwonię do {self.name} {self.last_name}")
