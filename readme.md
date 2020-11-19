# Testy witryn internetowych

Każdy krok testu jest zapisywany w pliku tests.log z datą, informacją w jakiej przeglądarce się odbył i z jakim efektem.

### www.speedtest.pl
Każdy test poprawności działania tej strony musi zacząć się od otwarcia strony i kliknięcia w popup "Rodo", dopiero wtedy można przejść do poszczególnych scenariuszy. Wszystkie testy należy wykonać w przeglądarkach:
1. Chrome
2. Firefox
3. Edge

Kończymy zamknięciem przeglądarki.

##### Scenariusz 1
Sprawdzamy walidację maila w opcji logowania się na stronie. 
Scenariusz ma objąć natępujące kroki:
1. Otwarcie w przeglądarki strony https://www.speedtest.pl.
2. Wejść na https://www.speedtest.pl/account przez pozycję w menu głównym "Moje konto".
3. W pozycji "E-mail:" należy wprowadzić "adsefg.pl".
4. W pozycji "Hasło" należy wprowadzić "xxxxxxx".
5. Kliknąć "Zaloguj się".
6. Sprawdzić czy pojawił się komunikat "Nieprawidłowy e-mail lub hasło."
7. Zamykamy przeglądarkę.
##### Scenariusz 2
Sprawdzamy poprawność opcji Wycena stron.
Scenariusz ma objąć natępujące kroki:
1. Otwarcie w przeglądarki strony https://www.speedtest.pl.
2. Wejść na https://www.speedtest.pl/wycena przez pozycję w menu głównym "Wycena stron".
3. W formularzu w polu "Podaj adres strony internetowej do wyceny..." należy wprowadzić "www.rykoszet.info".
4. Kliknąć "Rozpocznij wycenę".
5. Sprawdzić czy pojawił się rezultat.
6. Zamykamy przeglądarkę.
