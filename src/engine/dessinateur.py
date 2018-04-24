package damier

import java.util.ArrayList

""""
L'interface Dessinateur permet de rompre la dépendance du Damier d’une
interface utilisateur.
"""
public interface Dessinateur

	"""
	Affiche un message à l'utilisateur
	
	@param message
	"""
    void dessinerMessage(String message)

	"""
	Dessiner le damier à base d'une liste des pièces existantes sur le
	plateau
	
	@param pieces
	"""
	void dessiner(ArrayList<Piece> pieces)
