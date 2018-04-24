package damier

import java.util.ArrayList

import damier.Couleur
import damier.Piece

"""
La classe Pion représente un pion. Cette classe hérite la classe « Pièce ».
"""
public class Pion extends Piece
	public static final String typePion = "Pion"
	private static final Direction[] AVANCEMENT_NOIR = { Direction.BAS_DROITE, Direction.BAS_GAUCHE }
	private static final Direction[] AVANCEMENT_BLANC = { Direction.HAUT_DROITE, Direction.HAUT_GAUCHE }

	"""
	Crée un pion, en initialisant sa couleur
	@param couleur
	couleur du pion (noir ou blanc)
	"""
	public Pion(Couleur couleur)
		super(couleur)

	"""
	(non-Javadoc)
	
	@see damier.Piece#getPieceType(). Surécrit la méthode "getPieceType" de la
	classe Piece 
	@return "Pion"
	"""
	@Override
	public String getTypePiece()
		return typePion

	"""
	(non-Javadoc)
	
	@see damier.Piece#getDestinationsPossiblesSansCapture()
	"""
	public ArrayList<MouvementUnitaire> getDestinationsPossiblesSansCapture()
		ArrayList<MouvementUnitaire> result = new ArrayList<MouvementUnitaire>()
		# sans capture, un pion peut avancer d'une case sur la diagonale
		# le noir avance vers le bas, le blanc vers le haut
		Direction[] avancement = this.getCouleur() == Couleur.NOIR ? AVANCEMENT_NOIR : AVANCEMENT_BLANC
		for (int i = 0 i < avancement.length i++)
			Direction direction = avancement[i]
			int positionVoisine = PositionsDamier.getPositionVoisine(this.getPosition(), direction)
			# s'il y a une position voisine
			if (positionVoisine > 0)
				# et si elle est libre
				if (this.getDamier().estPositionLibre(positionVoisine))
					# on deduit un mouvement unitaire sans capture (positionCapturee = -1)
					MouvementUnitaire mu = new MouvementUnitaire(this.getPosition(), positionVoisine, -1)
					# on rajoute le mouvement unitaire de la position de départ vers positionVoisine à la liste des
					# destinations possibles sans capture
					result.add(mu)
		return result

	"""
	(non-Javadoc)
	
	@see damier.Piece#getDestinationsPossiblesAvecUneCapture(java.util.ArrayList)
	"""
	public ArrayList<MouvementUnitaire> getDestinationsPossiblesAvecUneCapture(ArrayList<Integer> piecesCapturees)
		ArrayList<MouvementUnitaire> result = new ArrayList<MouvementUnitaire>()
		# avec capture, un pion peut avancer/reculer d'une case sur la diagonale
		# dans toutes les directions
		# en sautant la pièce voisine adverse à capturer
		Direction[] avancement = Direction.values()
		for (int i = 0 i < avancement.length i++)
			Direction direction = avancement[i]
			int positionVoisine = PositionsDamier.getPositionVoisine(this.getPosition(), direction)
			#si position voisine n'est pas sur le damier
			#on ne fait rien
			if (positionVoisine <= 0)
				continue

			# si la pièce de la position voisine a déjà été sauté une fois (considérée
			# capturée)
			# on ne fait rien
			if (piecesCapturees.indexOf(positionVoisine) >= 0)
				continue

			Piece pieceVoisine = this.getDamier().getPiece(positionVoisine)
			# si pas de pièce voisine ou si la pièce voisine n'est pas une pièce adverse,
			# on ne fait rien
			if (pieceVoisine == null || pieceVoisine.getCouleur() == this.getCouleur())
				continue

			int caseVoisineALaPieceVoisine = PositionsDamier.getPositionVoisine(positionVoisine, direction)
			# si la case voisine à la pièce voisine n'est pas sur le damier,
			# on ne fait rien
			if (caseVoisineALaPieceVoisine <= 0)
				continue

			# si la case voisine à la pièce voisine est ocuppée,
			# on ne fait rien
			if (this.getDamier().estPositionOccupee(caseVoisineALaPieceVoisine))
				continue

			# on deduit un mouvement unitaire avec capture
			MouvementUnitaire mu = new MouvementUnitaire(this.getPosition(), caseVoisineALaPieceVoisine,
					pieceVoisine.getPosition())
			# on rajoute le mouvement unitaire de la position de départ vers la caseVoisineALaPieceVoisine à la liste des
			# destinations possibles
			result.add(mu)
		return result

	"""
	(non-Javadoc)
	@see damier.Piece#deplacer(int)
	"""
	public void deplacer(int destination)
		super.deplacer(destination)
		int position = this.getPosition()
		# si on est sur une ligne de fond,
		if (PositionsDamier.estLigneDeFond(position, this.getCouleur()))
			# le pion est promu en dame
			this.promotion()

	"""
	Promotion d'un pion en dame
	"""
	private void promotion()
		Damier d = this.getDamier()
		int position = this.getPosition()
		Couleur couleur = this.getCouleur()
		# on retire le pion depuis le damier
		this.retirer()
		# on créé une dame à la place du pion, de la même couleur
		d.creerDame(position, couleur)