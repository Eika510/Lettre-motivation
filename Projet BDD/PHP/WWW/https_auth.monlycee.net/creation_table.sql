CREATE TABLE Connexions(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ville VARCHAR(40),
  departement INTEGER
  );
  
CREATE TABLE Regles(
  id INTEGER,
  Images VARCHAR(40),
  Nom VARCHAR(40),
  Enonce TEXT
  );
  
INSERT INTO Regles(id,Images,Nom,Enonce) VALUES 
(1,"Phishing.png","Phishing","Avant de cliquer sur un lien douteux, positionnez le curseur de votre souris sur ce lien (sans
cliquer) ce qui affichera alors l’adresse vers laquelle il pointe réellement afin d’en vérifier la
vraisemblance ou allez directement sur le site de l’organisme en question par un lien favori que vous aurez vous-même créé"),
(2,"faux.png","Faux site frauduleux","Vérifiez l’adresse du site qui s’affiche dans votre
navigateur. Si cela ne correspond pas exactement au site concerné, c’est très certainement
un site frauduleux. Parfois, un seul caractère peut changer dans l’adresse du site pour vous tromper");  


