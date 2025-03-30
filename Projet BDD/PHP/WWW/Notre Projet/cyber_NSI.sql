CREATE TABLE Personne(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nom VARCHAR(40),
	prenom VARCHAR(40),
	adresse_mail VARCHAR(40),
  );
  
CREATE TABLE Excuses(
	id INTEGER PRIMARY KEY,
	contenu TEXT,
  );
  
CREATE TABLE Moment(
	id_moment INTEGER PRIMARY KEY AUTOINCREMENT,
	classe VARCHAR(40),
	dateee DATE,
	heure VARCHAR(40),
	nom_prof VARCHAR(40),
	id INTEGER,
	Constraint un_FK FOREIGN KEY(id) references Personne(id)
  );
  
INSERT INTO Excuses(id,contenu) VALUES
(1, "J’ai oublié d’éteindre le four, et comme j’y faisais cuire mes espoirs et mes rêves, je ne pouvais pas prendre le risque."),
(2, "Mon chat s’est mis à parler. Je devais rester pour enregistrer son témoignage révolutionnaire."),
(3, "Mon ordinateur m’a attaqué avec un virus émotionnel. Trop de drames à gérer ce matin."),
(4, "Une tornade de feuilles m’a bloqué sur le chemin."),
(5, "Un nuage particulièrement menaçant s’est posté au-dessus de moi. J’ai préféré ne pas le contrarier."),
(6, "La gravité était plus forte que d’habitude ce matin, impossible de sortir du lit."),
(7, "J’étais en pleine partie de Jumanji, et vous savez comment ça finit si on quitte avant la fin."),
(8, "Un pigeon a volé mon emploi du temps, c’était une conspiration."),
(9, "Mon hamster, nommé Sir Biscuitus, a enfin terminé une thèse révolutionnaire sur la roue infinie. Je devais être présent(e) pour l’aider à projeter les diapositives."),
(10, "Mon GPS s’est rebellé ce matin et m’a guidé(e) directement vers un café au lieu des cours. Il fallait bien y rester pour le réparer."),
(11, "Un embouteillage de coccinelles sur le trottoir m’a ralenti. Impossible de marcher sans risquer un accident de biodiversité."),
(12, "J’ai été appelé(e) en urgence pour empêcher un T-Rex de s’échapper dans la ville. Cela impliquait un duel épique à la hauteur de Jurassic Park."),
(13, "Un super-héros local avait besoin de moi comme assistant(e) pour sauver la ville. La mission a pris plus de temps que prévu."),
(14, "J’ai été retenu(e) par une réunion houleuse avec ma plante verte. Elle menaçait de flétrir si ses revendications n’étaient pas écoutées.");
