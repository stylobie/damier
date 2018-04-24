package damier

"""
Classe pour gérer les exceptions du jeu de dames.
"""

@SuppressWarnings("serial")
public class DamierException extends Exception

	"""
	Affiche à l'utilisateur un message d'erreur
	
	@param message
	message d'erreur
	"""
	public DamierException(String message)
		super(message)

