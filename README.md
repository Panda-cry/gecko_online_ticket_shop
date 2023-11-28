# Online Kupovina - Dokumentacija

## 1. Opis zadatka
Realizovati aplikaciju za online kupovinu. Postoje tri vrste korisnika ovog sistema:
1. Administrator
2. Prodavac
3. Kupac

## 2. Funkcije sistema
### 2.1. Prikaz informacija neregistrovanim korisnicima
- Prva stranica omogućava neregistrovanim korisnicima prijavu ili registraciju na sistem.

### 2.2. Registracija korisnika i prijavljivanje na sistem
- Registracija i prijava putem email adrese i lozinke.
- Klasična registracija sa unosom ličnih podataka.
- Registracija putem društvenih mreža.
- Autentifikacija i autorizacija korisnika na serverskoj strani.

### 2.3. Profil korisnika
- Azuriranje ličnih podataka na stranici profila.

### 2.4. Postupak verifikovanja registracije
- Administrator pregleda podatke i potvrđuje/odbija registraciju.
- Verifikacija je potrebna za prodavce.

### 2.5. Dashboard
- Različite funkcionalnosti zavisno o tipu korisnika.
- Elementi uključuju Profil, Dodavanje artikla (Prodavac), Nova porudžbina (Kupac), Prethodne porudžbine (Kupac), Verifikacija (Admin), Nove Porudžbine (Prodavac), Moje porudžbine (Prodavac), Sve porudžbine (Admin).

#### 2.5.1. Profil
- Prikaz i izmena profila korisnika.

#### 2.5.2. Dodavanje artikla
- Prodavac dodaje, menja ili briše artikle sa podacima kao što su naziv, cena, količina, opis i fotografija.

#### 2.5.3. Nova porudžbina
- Kupac kreira porudžbinu sa odabirom proizvoda, unosom količine, komentara i adrese dostave.
- Cena se računa na osnovu poručenih proizvoda i količine, plus cena dostave.

#### 2.5.4. Verifikacija
- Administrator pregleda i odobrava/odbija status prodavaca.

#### 2.5.5. Prethodne porudžbine
- Kupac pregleda listu svojih prethodnih porudžbina.

#### 2.5.6. Nove porudžbine
- Prodavac vidi listu novih porudžbina sa vremenom dostave.

#### 2.5.7. Moje porudžbine
- Prodavac pregleda svoje prethodne porudžbine.

#### 2.5.8. Sve porudžbine
- Administrator ima uvid u sve porudžbine i njihov status.

## 3. Implementacija sistema
### 3.1. Serverske platforme
- Python

### 3.2 Klijentske platforme
- Single-page interface aplikacija u Reactu

### 3.3 Slanje e-maila
- Za slanje emaila koristiti sopstveni email nalog.

### 3.4 Konkurentni pristup resursima
- Osigurati da više istovremenih korisnika ne može raditi nad istim elementom u istom vremenskom periodu.

---

*Projekat treba čuvati na GitHub repozitoriju koristeći Git za kontrolu verzija.*
