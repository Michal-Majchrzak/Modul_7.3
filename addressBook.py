from faker import Faker


class BaseContact:
    @property
    def label_length(self):
        return len(f"{self.name} {self.last_name}")

    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}")


class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.last_name}")


def prefix_check(prefix, text):
    if text[:len(prefix)] != prefix:
        return f"{prefix} {text}"
    else:
        return text


def create_contacts(is_business_type=False, number_of_contacts=1):
    faker_obj = Faker('pl_PL')
    contacts = []

    for counter in range(number_of_contacts):
        _name = faker_obj.first_name()
        _last_name = faker_obj.last_name()
        _phone = prefix_check("+48", faker_obj.phone_number())
        _email = f"{_name.lower()}{_last_name.lower()}@{faker_obj.free_email_domain()}"

        if is_business_type:
            _position = faker_obj.job()
            _company = faker_obj.company()
            _business_phone = prefix_check("+48", faker_obj.phone_number())
            contacts.append(BusinessContact(_position, _company, _business_phone, _name, _last_name, _phone, _email))
        else:
            contacts.append(BaseContact(_name, _last_name, _phone, _email))

    del faker_obj
    return contacts
