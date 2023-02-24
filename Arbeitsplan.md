Noch ausstehende Aufgaben:


1.) Ordnerstruktur erstellen. (ERLEDIGT)

2.) Methode erstellen. dass zu einer Ressource den passenden Zielordner auf Panopto ausfindig macht.

3.) Hochladen eines Videos in den passenden Zielordner

Nützliche Links:

https://demo.hosted.panopto.com/Panopto/Api/Docs/index.html#/Sessions/Sessions_GetSessionById

https://gist.github.com/Panopto

https://github.com/Panopto/panopto-api-python-examples

ich denke wir brauchen diese Auth: https://github.com/Panopto/panopto-api-python-examples/tree/master/auth-user-based-app

Änderungen: 2 csv Tabellen, eine für Beitrag und eine für Profs. Jeder Beitrag ist eine Veranstaltung und die Vorlesungen sind Playlists. PDFD Download über panopto

Hinweis: Erst Profs anlegen, dann wieder exportieren und die links zu den Prof beiträgen in die Veranstaltungs Tabelle

Layout der Beitragsseite:

- Beschreibung 70 Prozent, Profs 30 Prozent in der breite
- pdf entfernen
- 
Informationen Veranstaltung-Tabelle:

- Name der Veranstaltung
- Beschreibung: Beschreibung von Veranstaltung über get_collection(collection_id)
- iFrame: Dafür wird die viewerURL aus der public Panopto API benötigt
- User: Sind Professoren. Dafür wird der Link zum Professoren Profil aus der Professor-csv benötigt
- Semester
- Kategorie (Fachbereich)
- rawFileDir (noch benötigt?)

Informationen Professoren-Tabelle:

Problem: Wie verknüpft man diesen wordpress Beiträg auf den anderen?

Alle Infos von https://openlearnware.de/olw-rest-db/api/user/61, https://openlearnware.de/olw-rest-db/api/user/1/photo

- Foto: muss über ID mit neuem Link abgefragt werden und dann per html eingefügt
- Name: String aus title + firstName + lastName
- website: Website
- Beschreibung: about info
- Organization: 
- ID

Mergen von Tabellen: die beiden Tabellen müssen über die ID der Profs gemerged werden, damit man nachher den korrekten Wordpress Link zum Professoren Profil in den Beiträgen anhängen kann

Vorgehensweise: 
1.Erstelle Professoren Beiträge auf Wordpress über import
2.Exportiere diese Beiträge um die Links zu bekommen
3.Merge Professoren export mit import
4.Merge die Tabelle aus 3. mit der Tabelle der Beiträge über Prof ID