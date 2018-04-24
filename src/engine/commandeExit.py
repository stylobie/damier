package damier

"""
Cette classe permet de quitter un jeu
"""
public class CommandeExit implements CommandeJeuConsole
	
	private final String commande = "exit"

	""" (non-Javadoc)
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande() 
		return this.commande

	""" (non-Javadoc)
	@see damier.CommandeJeuConsole#execute(damier.Damier). La commande fait sortir du programme.
	"""
	public Damier execute(Damier courrant) throws DamierException
		System.exit(0)
		return courrant

