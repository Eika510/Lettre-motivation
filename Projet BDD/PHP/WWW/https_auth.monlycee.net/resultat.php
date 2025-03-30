<!doctype html>

<!-- CODE PHP qui récupère le formulaire de la 2ème page -->
<!-- 1er code en PHP ATTENTION à la syntaxe particulière -->
	<?php	
	if (isset($_POST['login2'])) {
		//on récupère les valeurs entrées par l'utilisateur
		 $ville = $_POST["ville"];
		 $departement = $_POST["dep"];
		// on se connecte à la base
		 $base = new SQLites(__DIR__.'/Cyber.db');
		//commandes SQL d'insertion, valeur 0 pour auto incrémentation
		 $sql = 'INSERT INTO Connexions (ville,departement)
		 VALUES("'.$ville.'","'.$departement.'");';
		// . = concaténation en PHP, simple cote pour avoir un str
		// On lance la requête (mysql_query) 
        // la flèche fonctionne comme le point en python en POO
		$req = $base->mysql_query($sql);
		if (!$req)   // si la requete a envoyé une erreur
		{echo '<p>Erreur SQL !<br />'.$base->error.'</p>';}            
			//on ferme la connexion à la base
        $base->close();
		
		}
	?>	




<html>
    <head>
        
        <meta http-equiv="content-type" content="text/html"; charset="utf-8" />
        <title>TP BDD</title>
		<link href="style.css" rel="stylesheet" media="all" type="text/css">
    </head>
    <body>
	<!-- div principale pour l'adaptation aux écrans -->
	<div id="container">
	<!-- header -->
	<div>
        <div class="header">
            <img src="./images/logo-idf-vertical.svg">
        </div>
    </div>
    <header>
        <header class="banner">
            <img id="logo" src="./images/logo.png">
            <div>
                <h1>Vous venez de vous faire hacker vos données personnelles</h1>
				<br>
                <h2>Heureusement ce site est un faux, codé dans le cadre pédagogique<br>
				<!-- PHP affichage des données récupérées -->
				<?php
				echo "<p> ville : '.$ville.'
					<br> departement : '.$departement.'
					</p> ";	
				
				?>
				<!-- fin PHP -->
				
				</h2>
				
            </div>
        </header>
    </header>
	<!-- fin header -->
	
	<!-- resultats -->
	<div>
	
	<!-- php affichage des résultats -->
	<?php	
	// on se connecte à la base
	
	//On crée la requête SQL
	
	// On lance la requête (mysql_query) 
	$req1 = $base->query($sql1); // la flèche fonctionne comme le point en python en POO
	if ($req1)   // si la requete a fonctionné, on recupère les données dans $data
					{
				// Parcourir les résultats
		while ($row = $req1->fetchArray(SQLITE3_ASSOC)) { // On récupère un dictionnaire dont la clé est l alias ou chaque attribut
					// on écrit du HTML 
					echo 				
					} //fin du while
					} //fin du if
	else //message d'erreur si la requete n'a pas fonctionné
					{echo '<p>Erreur SQL !<br />'.$base->error.'</p>';}
	// on pourrait continuer à récupérer des données	
	echo '<p class="resultat"> Nombre de personnes de votre ville : </p>';

		
	//maintenant on scanne la table Regles
	$sql2 = 'SELECT *  FROM Regles';
	// On lance la requête (mysql_query) 
	$req2 = $base->query($sql2); // la flèche fonctionne comme le point en python en POO
	if ($req2)   // si la requete a fonctionné, on recupère les données dans $data
					{
				// Parcourir les résultats
		echo '<table class="resultat">'; //tableau pour les résultats
		while ($row = $req2->fetchArray(SQLITE3_ASSOC)) { // On récupère un dictionnaire dont la clé est chaque attribut
					//on recupere les donnees dans des variables
					$im =  
					$nom =  
					$Enonce =  
					//Ecriture des lignes tr et des cellules td
					echo 


					
					} //fin du while
		echo '</table>' ; //fin du tableau
					} //fin du if
	else //message d'erreur si la requete n'a pas fonctionné
					{echo '<p>Erreur SQL !<br />'.$base->error.'</p>';}
					
					
					
					
					
	$base->close();				
	?>	
	

	</div>
	<!-- fin résultats -->
	
	<!-- footer -->
		<footer id="footer">
                <div >
                    <div ><img src="./images/horizontal.svg" alt="Logo région île de france">
                        <div>
						<br>
                            <p>Conseil des Hackers-Ethiques</p>
                            <p>10 rue Jean Moulin 91540 Arpajon</p>
						<br>
                        </div>
						
                        <ul class="logo-list">
                            <li><img src="./images/facebook.svg"></li>
                            <li><img src="./images//instagram.svg"></li>
                            <li><img src="./images/linkedin.svg"></li>
                            <li><img src="./images/x.svg"></li>
                        </ul>
                    </div>
                   
                </div>
				<p><span>2024 </span><span>Région Sud Sud Essonne. Tous droits réservés.</span></p>
		</footer>
	<!-- fin footer -->			
            
		</div>			
	<!-- fin div principale -->
</body>
</html>