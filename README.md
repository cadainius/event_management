# event_management projektas su jango frameworku
 galime kurti renginius, peržiurėti jų informaciją, redaguoti, rašyti įvertinimą, pridėti dalyvius į sąrašą.
 Kaip pasileisti šį projektą ?
 1. projekto dalyje spaudžiame ant event_management dešiniu pelės klavišu ir sukuriame naują failą pavadinimu local_settings.py
 2. jame įrašome SECRET_KEY='=(jūsų sugeneruotas slaptažodis)'
 3. atsidarome settings.py failą ir įvedame SECRET_KEY = local_settings.SECRET_KEY
 4. išsaugojus pakeistus failus atsidarome terminalą ir rašome cd event_management 
 5. paskutinis veiksmas paleidimui, tame pačiame termninale rašome python manage.py runserver
