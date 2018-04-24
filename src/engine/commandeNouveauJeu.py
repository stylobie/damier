package damier

"""
Cette classe permet d'initialiser le damier pour un nouveau jeu, quand
l'utilisateur tape le mot clef "nouveau-jeu" en cours de jeu
"""
public class CommandeNouveauJeu implements CommandeJeuConsole
	private final String commande = "nouveau-jeu"

	"""
	(non-Javadoc)
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande()
		return this.commande

	"""
	(non-Javadoc) 
	@see damier.CommandeJeuConsole#execute(damier.Damier). Le damier est
	initialisé pour un nouveau jeu.
	"""
	public Damier execute(Damier courrant) throws DamierException
		Damier d = new Damier(courrant.dessinateur)
		return d

