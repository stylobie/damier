package damier

"""
Cette interface represente une commande dans la console du jeu
"""
public interface CommandeJeuConsole 
	"""
	@return la commande
	"""
	String getCommande()

	"""
	Execute la commande
	
	@param courrant
	le damier courrant
	@return le damier courrant
	@throws DamierException
	"""
	Damier execute(Damier courrant) throws DamierException

