package damier

"""
Cette classe archive un jeu en sauvegardant son nom, la liste des pièces et
la couleur de la pièce à qui est le tour de jouer
"""
public class ArchiveJeu
	String nom
	int[][] pieces
	Couleur prochainMouvement

	"""
	@param nom
	le nom du jeu archivé
	@param pieces
	position des pions noirs, pions blancs, dames noires, dames
	blanches
	@param prochainMouvement
	la couleur de la pièce à jouer
	"""
	public ArchiveJeu(String nom, int[][] pieces, Couleur prochainMouvement)
		this.nom = nom
		this.pieces = pieces
		this.prochainMouvement = prochainMouvement
