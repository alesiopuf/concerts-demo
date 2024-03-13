from domain.exception.Exceptions import ConverterException, ValidationException
from domain.converter.ShowConverter import ShowConverter


class Console:
    def __init__(self, artist_service, show_service):
        self.__artist_service = artist_service
        self.__show_service = show_service

    def __print_menu(self):
        '''
        Prints menu
        :return: None
        '''
        print("\nMENU")
        print("1.Vizualizeaza artistii cu pretul mai mare decat un buget")
        print("2.Programeaza spectacol")
        print("3.Vizualizeaza toate spectacolele programate")
        print("4.IESIRE\n")

    def run(self):
        '''
        Runs the menu console app
        :return: None
        '''
        while True:
            self.__print_menu()
            choice = input("Introduceti optiunea: ")
            choice.strip()
            try:
                match choice:
                    case "1":
                        pret_dorit = float(input("Introduceti pretul dorit: "))
                        print(self.__artist_service.get_artists_with_higher_price(pret_dorit))
                    case "2":
                        string = input("Introduceti spectacolul dorit "
                                       "(id_spectacol, id_artist, oras, data, trupa_live) separate prin virgula: ")
                        show = ShowConverter.to_show(string)
                        response = self.__show_service.book_show(show)
                        print(f'Show-ul {response[0]} a fost programat! Pretul total este: {response[1]}')
                    case "3":
                        print(self.__show_service.get_shows())
                    case "4":
                        break
                    case _:
                        print("Optiune invalida")
            except ConverterException as e:
                print(e.msg)
            except ValidationException as e:
                print(e.msg)
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
