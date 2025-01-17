import random as r

cenzura = False

class Room:
    def __init__(self, north, south, east, west, up, down, into, out, scene_name, desc, hidden, item, spec_desc):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.into = into
        self.out = out
        self.scene_name = scene_name
        self.desc = desc
        self.hidden = hidden
        self.item = item
        self.spec_desc = spec_desc

class Item:
    def __init__(self, collected, item_name, item_desc, special_text):
        self.collected = collected
        self.item_name = item_name
        self.item_desc = item_desc
        self.special_text = special_text

def ustawienia():
    global cenzura
    print("Cenzura przekleństw: ")
    if cenzura:
        print("Włączona")
    else:
        print("Wyłączona")
    if int(input("\nBy zmnienić ustawienie wpisz 1"
                 "\nBy wyjść do menu wpisz 2\n")) == 1:
        if cenzura:
            cenzura = False
        else:
            cenzura = True
        print("\n")
        ustawienia()
    print("\n")

hala = Room(None, None, None, None, None, None, None, None, "sali", "Duże pomieszczenie przypominające jaskinie. Podłoga, ściany jak i sufit zbudowane są z kamiennych bloków. Duża część pomieszczenia jest pokryta mchem i dziwnym fioletowym narostem, który oddaje lekkie światło. przez samą ilość narostu pomieszczenie oświetlone jest na tyle że wszystko widać. W suficie jest duża dziura, przez którą widać ciemne, gwieździste niebo. Pomieszczenie to ma dziwną atmosferę, widać że coś dużego miało tu miejsce.", None, None, None)
przedsionek = Room(None, hala, None, None, None, None, None, None, "przedsionku", "Duże pomieszczenie z kilkoma wyjściami, zacementowane z dużymi filarami za którymi widać ciemny świat poza tym dziwnym budynkiem.", None, None, None)
pobojowisko = Room(None, przedsionek, None, None, None, None, None, None, "pobojowisku", "Pierwsze na tej drodze miejsce na otwartej przestrzeni, wychodząc z kamiennego budynku widać ścieżkę z piachu o kolorze popiołu otoczoną z każdej strony przez wielki ocean bladej wody, z której wyrastają drzewa o kolorze kamienia większe niż można sobię wyobrazić. Niebo jest tu ciemne, chociaż że zdajesz sobię sprawę że te wielkie drzewa muszą mieć gdzieś korony stąd na pewno ich nie widać. I co wydaje się w tej panoramie najważniejsze, tłum ludzkich ciał przemienionych w popielne rzeźby, niektóre z twarzami pełnymi złości inne przerażenia.", None, None, None)
puste_drzewo = Room(None, pobojowisko, None, None, None, None, None, None, "pustym drzewie", "Jedno z olbrzymich kamiennych drzew, puste w środku, wielkie grzyby porastające wilgotne ściany pustego drzew. Gdyby się postarać dałoby się wspiąć na górę, kto wie co można tam znaleźć.", None, None, None)
powierzchnia = Room(None, None, None, None, None, puste_drzewo, None, None, "powierzchni", "Świat zewnętrzny... a raczej to co po nim pozostało, wygląda inaczej niż człowiek może go sobie wyobrazić.", None, None, None)
ogrod = Room(pobojowisko, None, przedsionek, None, None, None, None, None, "ogrodzie", "Wygląda jakby dawniej był pięknym miejscem, teraz jednak spustoszały i martwy. Wielka szklarnia, jedyną ostającą się rośliną jest granatowe drzewo którego gałęzie wypuszczają długie fioletowe liście, najpewniej to od niego pochodzi porośl w pokoju do którego prowadzi przedsionek.", None, None, None)
ukryta_sciezka = Room(None, None, ogrod, None, None, None, None, None, "ukrytej ścieżce", "Za konarem starego wielkiego drzewa schowana pod górą popiołu i gruzu, kto wie gdzie prowadzi.", True, None, None)
studnia = Room(None, None, ukryta_sciezka, None, None, None, None, None, "studni", "Wygląda jak wnętrze olbrzymiej kamiennej studni, ściany porośnięte są gigantycznymi korzeniami korzeniami a co najlepsze patrząc w górę widać światło a u dołu nic prócz bezgranicznej ciemności.", None, None, None)
dziura = Room(None, None, None, None, None, None, None, None, "dziurze", "Środek wielkiej dziury po wskoczeniu tu spada się i spada, prędzej umrzesz ze starości niż gdzieś dolecisz. spadanie sprawia że czujesz pewien niepokój. Patrząc w dół masz wrażenie jakby coś odwzajemniało twoje spojrzenie, nie masz pewności co to ale pewne jest to że to nic dobrego.", None, None, None)
otchlan = Room(None, None, None, None, None, None, None, ogrod, "otchłani", "Dzięki bądź przez brak jakiegokolwiek istnienia w tym miejscu, lub wręcz braku miejsca, dostrzegasz wszystko. Wspomnienia powoli powracają i zdajesz sobię sprawę że brak czegokolwiek co mogłoby odwrócić twoją uwagę tutaj wszystko możesz dostrzec, to jak przestrzeń poza przestrzenią, możesz podróżować przez świat nie będąc w nim, myśląc o czymkolwiek w zwykłym świecie przed tobą ukazuję się tego obraz, wygląda bardzo realnie, teraz tylko pytanie jak to wykorzystać.", None, None, None)

brudna_notka = Item(False, "brudną notkę", "Stara brudna notatka, coś jest na niej napisane, wygląda na ważną", "Jest tu napisane o ukrytej ścieżce w ogrodzie, warto się tam udać i się temu przyjrzeć")
zepsute_urzadzenie = Item(False, "zepsute urządzenie", "Dziwne urządzenie, wygląda jakby było połączeniem najwyższej jakości rzemiosła technologicznego i magicznego, jest zepsute ale to na pewno coś ważnego. Jeżeli wiesz jak je naprawić, na pewno zrobi coś przydatnego.", "Nie posiadasz wiedzy wymaganej by nawet pogrzebać w tym urządzeniu, wydaje ci się ono bardzo znajome ale nie możesz sobię przypomnieć o nim niczego, na obecną chwilę nie dasz rady tego naprawić.")
stare_wspomnienia = Item(False, "stare wspomnienia", "", "Wspomnienia ludzkości, stracone dawno temu przez próbę odnowienia świata, uratowania go od śmierci spowodowanej entropią. Niestety uratowanie świata przyszło z kosztem życia, nie tylko ludzkości ale wszelkiej żywej materii. Przypomina ci się obietnica, złożona umierającemu przyjacielowi, jedynemu przyjacielowi... przed jego śmiercią miał prośbę, poprosił cię o nowy świat, żywy i wolny od jakichkolwiek problemów, to właśne ta obietnica cię tutaj przywiodła. Żeby jej dopełnić musisz udać się na powierzchnię, masz wrażenie że sposób na przywrócenie świata powróci do ciebie z czasem, na razie musisz wrócić z tego pustego miejsca, naprawić zepsute urządzenie i użyć go na powierzchni. Przypominasz sobię również swoją przyszłość jako naukowca, wiesz jak naprawić urządzenie, które ocali ten zniszczony świat.")
laska_czasu = Item(False, "laskę czasu", "Urządzenie którym możesz naprawić ten zniszczony świat, wystarczy że użyjesz go na powierzchni a świat powróci do czasów gdy wszystko było prostsze", "Czy to na prawdę koniec tej przygody? Kto wie gdzie dalej potoczą się losy tego świata. Jak daleko w tył cofnął się czas? Czy udało się uniknąć śmierci wszechświata? Kto wie, jedynym sposobem by dowiedzieć się takich rzeczy jest danie studentowi zdać przedmiot i zadać kolejny projekt by uczeń musiał kontynuować kreatywną passę. Dziękuję za granie i czytanie, życzę państu miłego wtorku i pysznej kawusi.")

hala.north = przedsionek
przedsionek.north = pobojowisko
przedsionek.west = ogrod
pobojowisko.north = puste_drzewo
puste_drzewo.up = powierzchnia
ogrod.west = ukryta_sciezka
ukryta_sciezka.west = studnia
studnia.down = dziura
dziura.into = otchlan
otchlan.out = ogrod

otchlan.item = stare_wspomnienia
powierzchnia.item = zepsute_urzadzenie

while 1:
    while 1:
        print("MENU"
              "\n1. Rozpocznij"
              "\n2. Ustawienia"
              "\n3. Napisy"
              "\n4. Wyjdź")
        option = input("Wpisz numer z wybraną funkcją: ")
        if option.isdigit():
            option = int(option)
        match option:
            case 1:
                break
            case 2:
                print("\n")
                ustawienia()
            case 3:
                print("\nFabuła - Jan Włodarski"
                    "\nKodowanie  - Jan Włodarski"
                    "\nBrak muzyki - Jan Włodarski")
                input("\nWpisz cokolwiek by wrócić ")
            case 4:
                exit()
            case _:
                print("nieprawidłowy  wybór\n")
    current_location = hala
    while 1:
        brudna_notka.collected = False
        zepsute_urzadzenie.collected = False
        stare_wspomnienia.collected = False
        laska_czasu.collected = False
        match r.randint(1, 10):
            case 1 | 2:
                hala.item = brudna_notka
            case 3 | 4:
                przedsionek.item = brudna_notka
            case 5 | 6 | 7:
                ogrod.item = brudna_notka
            case 8 | 9 | 10:
                pobojowisko.item = brudna_notka
        print("\nPowoli budzisz się w miejscu dziwnie ci znajomym."
                "\nCzujesz jakbyś już tu był, przed tym jak to miejsce zostało zruinowane... myśląc o tym głębiej zauważasz że nie wiesz gdzie ani kim jesteś."
                "\n>..."
                "\n>Pamiętasz swoje imię?")
        name = input(">")
        while name == "":
            print(">Jeżeli go nie pamiętasz, podaj pierwsze imię które przyjdzie ci do głowy ")
            name = input(">")
        print(">{}... Tak, najwyraźniej coś jeszcze pamiętasz. - mówi znajomy ci głos".format(name))
        print(">Co? Co się dzieje?"
              "\nSpoglądasz się dookoła siebie, ale nikogo nie widzisz.")
        input("\nWpisz cokolwiek by wstać")
        print("\n///////////////////////////////////////////////\n"
              "Powoli stajesz na nogi, jest to dziwnie trudne zadanie, czujesz że twój długi sen dobiegł końca")
        while 1:
            print(f"jesteś w {current_location.scene_name}, co chcesz zrobić?"
                  "\n____________________________________"
                  "\n1. Rozjerzyj się po lokalizacji"
                  "\n2. Poszukaj czegoś przydatnego"
                  "\n3. Przejdź do innego pokoju"
                  "\n4. Ekwipunek"
                  "\n5. Restartuj"
                  "\n6. Wyjdź z gry")
            option = input(">")
            print("///////////////////////////////////////////////")
            if option.isdigit():
                option = int(option)
            match option:
                case 1:
                    print(current_location.desc)
                case 2:
                    if current_location.item is not None:
                        print(f"Znalazłeś {current_location.item.item_name}!")
                        current_location.item.collected = True
                        current_location.item = None
                    else:
                        print("Nic tu nie ma!")
                case 3:
                    if current_location.north is not None:
                        print("By iść na północ wpisz north")
                    if current_location.south is not None:
                        print("By iść na połódnie wpisz south")
                    if current_location.east is not None:
                        print("By iść na wschód wpisz east")
                    if current_location.west is not None:
                        print("By iść na zachód wpisz west")
                    if current_location.up is not None:
                        print("By iść w górę wpisz up")
                    if current_location.down is not None:
                        print("By iść w dół wpisz down")
                    if current_location.into is not None:
                        print("By iść do środka wpisz in")
                    if current_location.out is not None:
                        print("By wyjść wpisz out")
                    while 1:
                        choice = input(">").upper()
                        match choice:
                            case "NORTH":
                                current_location = current_location.north
                                print("///////////////////////////////////////////////")
                                break
                            case "SOUTH":
                                current_location = current_location.south
                                print("///////////////////////////////////////////////")
                                break
                            case "EAST":
                                current_location = current_location.east
                                print("///////////////////////////////////////////////")
                                break
                            case "WEST":
                                current_location = current_location.west
                                print("///////////////////////////////////////////////")
                                break
                            case "UP":
                                current_location = current_location.up
                                print("///////////////////////////////////////////////")
                                break
                            case "DOWN":
                                current_location = current_location.down
                                print("///////////////////////////////////////////////")
                                break
                            case "IN":
                                current_location = current_location.into
                                print("///////////////////////////////////////////////")
                                break
                            case "OUT":
                                current_location = current_location.out
                                print("///////////////////////////////////////////////")
                                break
                            case _:
                                print("\nnieprawidłowy  wybór")
                                break

                case 4:
                    while 1:
                        if brudna_notka.collected:
                            print("Brudna Notatka"
                                  "\n-by przeczytać wpisz READ"
                                  "\n-by obejrzeć wpisz INSPECTNOTE")
                        if zepsute_urzadzenie.collected:
                            print("Zepsute urządzenie"
                                  "\n-by naprawić wpisz FIX"
                                  "\n-by obejrzeć wpisz INSPECTDEVICE")
                        if stare_wspomnienia.collected:
                            print("Stare Wspomnienia"
                                  "\n-by sobie przypomnieć wpisz REMEMBER")
                        if laska_czasu.collected:
                            print("Laska Czasu"
                                  "\n-by użyć wpisz USE"
                                  "\n-by obejrzeć wpisz INSPECTSTAFF")
                        if not brudna_notka.collected and not zepsute_urzadzenie.collected and not stare_wspomnienia.collected and not laska_czasu.collected:
                            print("Nic jeszcze nie znalazłeś!")
                            break
                        else:
                            print("\nBy wyjść wpisz EXIT")
                            choice = input(">").upper()
                            match choice:
                                case "EXIT":
                                    break
                                case "READ":
                                    if brudna_notka.collected:
                                        print("///////////////////////////////////////////////"
                                              f"\n{brudna_notka.special_text}")
                                        ukryta_sciezka.hidden = False
                                case "INSPECTNOTE":
                                    if brudna_notka.collected:
                                        print("///////////////////////////////////////////////"
                                              f"\n{brudna_notka.item_desc}")
                                case "FIX":
                                    if zepsute_urzadzenie.collected:
                                        if stare_wspomnienia.collected:
                                            print("///////////////////////////////////////////////"
                                                  f"\nUdało ci się! Naprawiłeś {laska_czasu.item_name}"
                                                  f"\n{laska_czasu.item_desc}")
                                            laska_czasu.collected = True
                                        else:
                                            print(f"///////////////////////////////////////////////"
                                                  f"\n{zepsute_urzadzenie.special_text}")
                                case "INSPECTDEVICE":
                                    if zepsute_urzadzenie.collected:
                                        print("///////////////////////////////////////////////"
                                              f"\n{zepsute_urzadzenie.item_desc}")
                                case "REMEMBER":
                                    if stare_wspomnienia.collected:
                                        print("///////////////////////////////////////////////"
                                              f"\n{stare_wspomnienia.special_text}")
                                case "USE":
                                    if laska_czasu.collected:
                                        if current_location == powierzchnia:
                                            if not cenzura:
                                                print("\nkurde felek (funkcja ma na celu pokazanie działającego filtru słownego który można zmienić w ustawieniach)\n")
                                            print("///////////////////////////////////////////////"
                                                  f"\n{laska_czasu.special_text}")
                                            wybor = input("\nCzy chcesz zagrać od nowa? Y/N: ")
                                            if wybor == "Y":
                                                break
                                            else:
                                                exit()
                                        else:
                                            print("///////////////////////////////////////////////"
                                                  "\nBy użyć laski wyjdź na powierzchnię")
                                case "INSPECTSTAFF":
                                    if laska_czasu.collected:
                                        print("///////////////////////////////////////////////"
                                              f"\n{laska_czasu.item_desc}")
                                case _:
                                    print("nieprawidłowy  wybór")
                case 5:
                    if input("Na pewno? Y/N: ").upper() == "Y":
                        break
                case 6:
                    if input("Na pewno? Y/N: ").upper() == "Y":
                        exit()
                case _:
                    print("\nnieprawidłowy  wybór")