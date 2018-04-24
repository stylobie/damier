package damier

import java.util.ArrayList

import damier.Couleur
import damier.Direction
import damier.Piece

""""
La classe Dame représente une dame. Cette classe hérite la classe « Pièce ».
"""
public class Dame extends Piece
	public static final String typeDame = "Dame"

	"""
	Crée une dame, en initialisant sa couleur
	 
	@param couleur
	couleur de la dame
	"""
	public Dame(Couleur couleur)
		super(couleur)

	"""
	(non-Javadoc) 
	@see damier.Piece#getPieceType() Surécrit la méthode "getPieceType" de la
    classe Piece
	@return "Dame"
	@Override
	"""

    public String getTypePiece()
		return typeDame

	"""
	(non-Javadoc)
	
	@see damier.Piece#getDestinationsPossiblesSansCapture()
	"""
	public ArrayList<MouvementUnitaire> getDestinationsPossiblesSansCapture()
		ArrayList<MouvementUnitaire> result = new ArrayList<MouvementUnitaire>()
		# sans capture, une dame peut avancer/reculer d'une ou plusieurs cases
		# sur n'importe quelle diagonale
		Direction[] avancement = Direction.values()
		for (int i = 0; i < avancement.length; i++)
			Direction direction = avancement[i]
			int positionTemp = this.getPosition()
			boolean positionVoisineOccupeeOuInexistante
			# tant qu'une position voisine est occupée ou inexistante
			do
				int positionVoisine = PositionsDamier.getPositionVoisine(positionTemp, direction)
				# si une position voisine existe
				if (positionVoisine > 0)
					# et si elle est libre
					if (this.getDamier().estPositionLibre(positionVoisine))
						# on deduit un mouvement unitaire sans capture (positionCapturee = -1)
						MouvementUnitaire mu = new MouvementUnitaire(this.getPosition(), positionVoisine, -1)
						# on rajoute le mouvement unitaire de la position de départ à la positionVoisine à la liste des
						# destinations possibles sans capture
						result.add(mu)
						positionVoisineOccupeeOuInexistante = false
						positionTemp = positionVoisine
					else
						positionVoisineOccupeeOuInexistante = true
				
				else
					positionVoisineOccupeeOuInexistante = true
				
			while (!positionVoisineOccupeeOuInexistante)
		
		return result

	"""
	(non-Javadoc)
	
	@see damier.Piece#getDestinationsPossiblesAvecUneCapture(java.util.
	ArrayList)
	"""
	public ArrayList<MouvementUnitaire> getDestinationsPossiblesAvecUneCapture(ArrayList<Integer> piecesCapturees)
		ArrayList<MouvementUnitaire> result = new ArrayList<MouvementUnitaire>()
		# avec capture, une dame peut avancer/reculer sur la diagonale
		# dans toutes les directions d'une ou plusieurs cases libres
		# en sautant la pièce adverse à capturer. La case destination doit se
		# trouver
		# sur
		# la même direction, entre la pièce à capturer et une autre case
		# occupée.
		Direction[] avancement = Direction.values()
		for (int i = 0; i < avancement.length; i++)
			Direction direction = avancement[i]
			this.getDestinationsPossiblesAvecUneCapture(result, direction, piecesCapturees)
		return result

	"""
	Obtient la liste des destinations possibles dans le cas d'un coup avec une
	capture
	
	@param liste
	liste des mouvements unitaires
	@param direction
	direction du mouvement
	@param piecesCapturees
	positions des pieces capturées
	"""
	private void getDestinationsPossiblesAvecUneCapture(ArrayList<MouvementUnitaire> liste, Direction direction,
			ArrayList<Integer> piecesCapturees) 
		Piece premierePieceTrouvee = this.getDamier().getPremierePiece(this.getPosition(), direction)
		# s'il n'y a pas de pièce proche trouvée
		# on ne fait rien
		if (premierePieceTrouvee == null)
			return
		
		# si la couleur de la pièce proche trouvée n'est pas celle d'une pièce adverse
		# on ne fait rien
		if (premierePieceTrouvee.getCouleur() == this.getCouleur())
			return
		
		# si la pièce trouvée a déjà été sautée une fois (considérée
		# capturée)
	    #on ne fait rien
		if (piecesCapturees.indexOf(premierePieceTrouvee.getPosition()) >= 0)
			return

		ArrayList<Integer> positionsLibresApresPremierePieceTrouvee = this.getDamier()
				.getPositionsLibres(premierePieceTrouvee.getPosition(), direction)
		for (int i = 0; i < positionsLibresApresPremierePieceTrouvee.size(); i++)
			int positionLibreApresPremierePieceTrouvee = positionsLibresApresPremierePieceTrouvee.get(i)
			# on deduit un mouvement unitaire avec capture
			MouvementUnitaire mu = new MouvementUnitaire(this.getPosition(), positionLibreApresPremierePieceTrouvee,
					premierePieceTrouvee.getPosition())
			# on rajoute le mouvement unitaire de la position de départ vers la
			# positionLibreApresPremierePieceTrouvee à la liste des
			# destinations possibles
			liste.add(mu)
