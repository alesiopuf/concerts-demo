from repository.ArtistRepository import ArtistRepository
from repository.ShowRepository import ShowRepository
from service.ArtistService import ArtistService
from service.ShowService import ShowService
from test.ArtistFlowTest import ArtistFlowTest
from test.ShowFlowTest import ShowFlowTest
from ui.Console import Console

# teste
try:
    show_tests = ShowFlowTest()
    show_tests.run()
    artist_test = ArtistFlowTest()
    artist_test.run()
    print("Testele au trecut!")
except AssertionError:
    print("ATENTIE! Testele nu au trecut! Verifica fisierul artisti.txt!")

# program principal
artist_repo = ArtistRepository()
artist_service = ArtistService(artist_repo)

show_repo = ShowRepository()
show_service = ShowService(show_repo, artist_repo)

console = Console(artist_service, show_service)

console.run()
