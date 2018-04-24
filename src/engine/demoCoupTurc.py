package damier

"""
Cette classe permet de reprendre un jeu pour jouer le "Coup turc", quand
l'utilisateur tape le mot clef "coup-turc" en cours de jeu
"""
public class CommandeDemoCoupTurc implements CommandeJeuConsole
	private final String commande = "coup-turc"

	"""
	(non-Javadoc)
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande()
		return this.commande


	"""
	(non-Javadoc) 
	@see damier.CommandeJeuConsole#execute(damier.Damier). Reprend un jeu pour
	jouer le "coup-turc"
	"""
	public Damier execute(Damier courrant) throws DamierException
		int[][] coupTurc = { {}, // pions noirs
				{ 23, 29, 30, 38, 39 }, // pions blancs
				{ 35 }, // dames noires
				{}, // dames blanches
		Damier d = new Damier(courrant.dessinateur, coupTurc, Couleur.NOIR)
		return d
