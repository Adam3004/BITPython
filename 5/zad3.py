from abc import ABC, abstractmethod


# czy mozna lepiej napisac send_email w workAdress
class Adress(ABC):
    def __init__(self, city: str, street: str, number_of_building: int, zip_code: str, phone_number: int, emial: str):
        self.city = city
        self.street = street
        self.number_of_building = number_of_building
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = emial

    def make_email(self, email:str,text: str):
        return (f'Adress: {email}, text: {text}')

    def send_email(self, text: str):
        return self.make_email(self.email, text)

    @abstractmethod
    def __str__(self):
        return (f'Adress: {self.street} {self.number_of_building} {self.city} {self.zip_code}\n'
                f'Phone number: {self.phone_number}\n'
                f'Email: {self.email}')


class HomeAdress(Adress):
    def __init__(self, city: str, street: str, number_of_building: int, zip_code: str, phone_number: int, emial: str,
                 landline_number: int, **kwargs):
        super().__init__(city, street, number_of_building, zip_code, phone_number, emial)
        self.number_of_flat = kwargs.get('number_of_flat', -1)
        self.landline_number = landline_number

    def __str__(self):
        if self.number_of_flat != -1:
            output = (f'{super(HomeAdress, self).__str__()} \n'
                      f'Landline number: {self.landline_number}\n'
                      f'Number of flat: {self.number_of_flat}')
        else:
            output = (f'{super(HomeAdress, self).__str__()} \n'
                      f'Landline number: {self.landline_number}\n')

        return output


class WordAdress(Adress):
    def __init__(self, city: str, street: str, number_of_building: int, zip_code: str, phone_number: int, email: str,
                 company_name: str, room_number: int, official_email: str, working_phone_number: int):
        super(WordAdress, self).__init__(city, street, number_of_building, zip_code, phone_number, email
                                         )
        self.company_name = company_name
        self.room_number = room_number
        self.official_email = official_email
        self.working_phone_number = working_phone_number

    def __str__(self):
        return (f'{super().__str__()} \n'
                f'Name of the company: {self.company_name}\n'
                f"Room's number: {self.room_number}\n"
                f"Official emial: {self.official_email} \n"
                f"Working phone number: {self.working_phone_number}")

    def telephone_call(self):
        return (f'{self.phone_number}{self.working_phone_number}')

    def send_email(self, text: str, offical: bool):
        if offical:
            return super().send_email(super().make_email(self.official_email, text))
        else:
            return super().send_email(text)


class UniversityAddress(Adress):
    def __init__(self, city: str, street: str, number_of_building: int, zip_code: str, phone_number: int, emial: str,
                 faculty: str, cathedral: str):
        super().__init__(city, street, number_of_building, zip_code, phone_number, emial)
        self.faculty = faculty
        self.cathedral = cathedral

    def __str__(self):
        return (f'{super().__str__()}\n'
                f'Faculty: {self.faculty}\n'
                f'Cathedral: {self.cathedral}')


# UniversityAddress:
# atrybuty:
# wydział
# katedra



