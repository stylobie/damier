package damier

import java.util.ArrayList

import IG.IG_Dames

"""
La classe DessinateurGraphique fait l’adaptation entre le jeu et la librairie
fournie IG_Dames. L'interface IG_Dames ne sachant pas d'afficher des
messages, on va rédirectionner les messages vers la console
"""

public class DessinateurGraphique implements Dessinateur
	private IG_Dames ig

	public DessinateurGraphique()
		this.ig = new IG_Dames()
	

	public void dessinerMessage(String message)
		System.out.println(message)


	public void dessiner(ArrayList<Piece> pieces)
		String[] tab = new String[50]
		# initialisation d'une table avec des cases vides, representées par
		# ("-")
		for (int i = 0; i < 50; i++)
			tab[i] = "-"

		# on remplace les cases vides par la representation textuelle des
		# pièces en utilisant la fonction convert()
		for (int i = 0; i < pieces.size(); i++) 
			Piece p = pieces.get(i)
			int positionManoury = p.getPosition()
			# les positions Manoury commencent par 1, il faut les décrementer
			# pour trouver l'index dans le tableau
			tab[positionManoury - 1] = DessinateurGraphique.convert(p)
		
		this.ig.dessine(tab)
	

	"""
	Converti dans un string le type et la couleur d'une pièce Pion -> P, Dame
	-> D, Noir -> N, Blance -> B. (Ex: pion noir -> PN)
	@param p
	@return
	"""
	private static String convert(Piece p)
		Couleur couleur = p.getCouleur()
		String type = p.getTypePiece()

		String typeConverti = type.equals("Pion") ? "P" : "D"
		String couleurConvertie = couleur == Couleur.BLANC ? "B" : "N"
		return typeConverti + couleurConvertie
