from piece import Piece
from constants import Couleur, Direction


"""
Jeu du Damier
La classe Damier est la classe principale, elle représente le jeu de dames. 
"""
public class Damier
	private ArrayList<Piece> pieces
	private Couleur prochainMouvement

	public final Dessinateur dessinateur

	"""
	Crée un nouveau jeu, la couleur à jouer est le blanc
	"""
	public Damier(Dessinateur dessinateur) {
		# appelle un autre constructeur avec tableVide = false
		this(dessinateur, false, Couleur.BLANC)
	

	"""
	Crée un damier et l'initialise pour une reprise de jeu, avec la liste de
	pièces, données dans l'ordre: pions noirs, pions blancs, dames noires, dames
	blanches
	@param dessinateur
	@param pieces
	tableau des positions des pions noirs, pions blancs, dames noires,
	dames blanches
	@param prochainMouvement
	a couleur de la pièce à jouer
	"""
	public Damier(Dessinateur dessinateur, int[][] pieces, Couleur prochainMouvement)
		this(dessinateur, true, prochainMouvement)
		this.creerPieces(pieces)

	"""
	Crée un damier à partir d'une archive de jeu
	@param dessinateur
	@param archive
	"""
	public Damier(Dessinateur dessinateur, ArchiveJeu archive) 
		this(dessinateur, archive.pieces, archive.prochainMouvement)
	
	"""
	Crée un damier permettant de créer une table vide. Ce constructeur est appelé
	par les 2 autres.
	 
	@param tableVide
	Si table n'est pas vide, le damier est initialisé pour un nouveau
	jeu
	"""
	public Damier(Dessinateur dessinateur, boolean tableVide, Couleur prochainMouvement)
		this.dessinateur = dessinateur
		this.pieces = new ArrayList<Piece>()
		this.prochainMouvement = prochainMouvement
		if (!tableVide) :
			this.nouveauJeu()

	"""
	Initialise le damier pour un nouveau jeu
	"""
	public void nouveauJeu()
		this.pieces.clear()
		# le blanc commence le jeu
		this.prochainMouvement = Couleur.BLANC
		int[] positionsInitialesPionsNoirs = PositionsDamier.getPositionsInitiales(Couleur.NOIR)
		int[] positionsInitialesPionsBlancs = PositionsDamier.getPositionsInitiales(Couleur.BLANC)
		# la méthode "creerPions" pour un nouveau jeu ne peut pas retourner une
		# erreur
		this.creerPions(positionsInitialesPionsNoirs, positionsInitialesPionsBlancs)
		this.dessiner("nouveau jeu")

	"""
	@return la couleur de la pièce à qui est le tour de jouer
	"""
	public Couleur getProchainMouvement() 
		return this.prochainMouvement

	"""
	spécifie la couleur de la pièce à jouer
	 
	@param value
	la couleur de la pièce à qui est le tour de jouer
	"""
	public void setProchainMouvement(Couleur value)
		this.prochainMouvement = value
	

	"""
	Verifie si une partie est terminée (une partie est considérée terminée s'il
    n'y a plus de mouvements possibles)
	 
	@return true si la partie est terminée
	"""
	public boolean getEstTermine() 
		ArrayList<MouvementUnitaire> prochainsMouvements = this.analyse()
		if (prochainsMouvements.size() == 0) 
			return true
		
		return false

	"""
	Vérifie si la position est libre 
	@param position
	position en notation Manoury
	@return true si la position est libre
	"""
	public boolean estPositionLibre(int position)
		Piece p = this.getPiece(position)
		return (p == null)
	
	"""
	Vérifie si la position est occupée
	
	@param position
	position en notation Manoury
	@return true si la position est occupée
	"""
	
    public boolean estPositionOccupee(int position)
		return !this.estPositionLibre(position)

	"""
	Obtient la liste des pièces
	@return la liste des pièces
	"""
	
    public ArrayList<Piece> getPieces() 
		return this.pieces


	"""
	Obtient la liste des pièces pour une couleur donnée
	
	@param couleur
	(noir, ou blanc)
	@return la liste des pièces pour la couleur donnée
	 """
	public ArrayList<Piece> getPieces(Couleur couleur)
		ArrayList<Piece> piecesParCouleur = new ArrayList<Piece>()
		for (int i = 0; i < this.pieces.size(); i++)
			Piece p = this.pieces.get(i)
			if (p.getCouleur() == couleur)
				piecesParCouleur.add(p)
			
	
		return piecesParCouleur
	

	"""
	Obtient une pièce pour une position donnée
	 
	@param position
	la position sur le damier
	@return null si pas de pièce trouvée sur la position donnée ou la pièce
	retrouvée
	"""
	public Piece getPiece(int position)
		if (PositionsDamier.estPositionInvalide(position))
			return null
		
		# on cherche parmis les pièces s'il y a une qui ocupe la position
		# donnée
		for (int i = 0; i < this.pieces.size(); i++) 
			Piece piece = this.pieces.get(i)
			if (piece.getPosition() == position) 
				return piece 
			
		
		return null
	

	"""
	Obtient la liste des positions libres, par rapport à une position et une
	direction données
	
	@param position
	la position sur le damier
	@param direction
	direction de mouvement en diagonale sur le damier vers: Haut à
	Gauche, Haut à Droite, Bas à Gauche, Bas à Droite
	@return liste des positions libres
	"""
	public ArrayList<Integer> getPositionsLibres(int position, Direction direction)
		ArrayList<Integer> result = new ArrayList<Integer>()
		# tant qu'il y a des positions libres sur le damier on les rajoute à la liste de résultat
		while (true) 
			# on obtient la position voisine à un position et direction données
			int positionVoisine = PositionsDamier.getPositionVoisine(position, direction)
			# si elle est valide et libre
			if (PositionsDamier.estPositionValide(positionVoisine) && this.estPositionLibre(positionVoisine)) 
				# on la rajoute à la liste des positions libres
				result.add(positionVoisine)
				# on redefinit la position par la valeur de la positionVoisine
				position = positionVoisine
			else 
				return result


	"""
	Obtient la pièce la plus proche par rapport à une position et direction
	données
	 
	@param position
	la position sur le damier
	@param direction
	direction de mouvement en diagonale sur le damier vers: Haut à
	Gauche, Haut à Droite, Bas à Gauche, Bas à Droite
	@return la position de la première pièce la plus proche par rapport à une
	position et direction données
	"""
	public Piece getPremierePiece(int position, Direction direction)
		int positionPremierePiece
		ArrayList<Integer> positionsLibres = this.getPositionsLibres(position, direction)
		# s'il n'y a pas de position libre par rapport à une position et direction
		# données, on obtient la position de la pièce voisine. C'est cette
		# pièce voisine qui est la pièce la plus proche recherchée.
		if (positionsLibres.size() == 0)
			positionPremierePiece = PositionsDamier.getPositionVoisine(position, direction)
			# s'il y a des positions libres par rapport à une position et direction
			# données, on trouve la pièce voisine à la dernière position libre. C'est cette
			# pièce voisine qui est la pièce la plus proche recherchée.
		else
			int indexDernierePositionLibre = positionsLibres.size() - 1
			int dernierePositionLibre = positionsLibres.get(indexDernierePositionLibre)
			positionPremierePiece = PositionsDamier.getPositionVoisine(dernierePositionLibre, direction)
		return this.getPiece(positionPremierePiece)

	"""
	Analyse une situation de jeu pour déterminer la liste des mouvements
	possibles
	
	@return liste de mouvements unitaires possibles
	"""
	public ArrayList<MouvementUnitaire> analyse()
		ArrayList<MouvementUnitaire> mouvements = new ArrayList<MouvementUnitaire>()

		# on obtient la liste des pièces qu'on peut déplacer au prochain mouvement
		ArrayList<Piece> pieces = this.getPieces(this.prochainMouvement)
		for (int i = 0; i < pieces.size(); i++)
			Piece p = pieces.get(i)
			ArrayList<MouvementUnitaire> mouvementsPiece = p.analyse(true)
			mouvements.addAll(mouvementsPiece)
		
		# on enlève les mouvements qui n'ont pas de prise maximale
		MouvementUnitaire.removeNonMaximal(mouvements)
		return mouvements

	"""
	Retire une pièce depuis une position donnée
	
	@param positionCapturee
	position de la pièce capturée
	"""
	public void retirer(int positionCapturee)
		for (int i = 0; i < this.pieces.size(); i++)
			Piece piece = this.pieces.get(i)
			if (piece.getPosition() == positionCapturee)
				this.pieces.remove(i)
				this.dessiner(null)
				break

	"""
	Dessine le damier à l'aide du dessinateur précisé dans le constructeur
	"""
	public void dessiner(String message)
		if (this.dessinateur != null)
			if (message != null)
				this.dessinateur.dessinerMessage(message)
			# dessine les pièces sur le damier
			this.dessinateur.dessiner(this.getPieces())


	"""
	Archive le jeu sous un nom donnée
	 
	@param nom
	nom du jeu à archiver
	@return une archive du jeu (contenant son nom, la liste des pièces données
	dans l'ordre: position des pions noirs, pions blancs, dames noires,
	dames blanches et la couleur de la pièce du prochain mouvement)
	"""
	public ArchiveJeu archiverJeu(String nom)
		# la liste de pièces, données dans l'ordre: pions noirs, pions blancs, dames
		# noires, dames blanches
		int[][] pieces = new int[4][]

		ArrayList<Integer> pionsNoirs = new ArrayList<Integer>()
		ArrayList<Integer> pionsBlancs = new ArrayList<Integer>()
		ArrayList<Integer> damesNoires = new ArrayList<Integer>()
		ArrayList<Integer> damesBlanches = new ArrayList<Integer>()
		for (int i = 0; i < this.pieces.size(); i++)
			Piece p = this.pieces.get(i)
			ArrayList<Integer> liste
			if (p.getTypePiece().equals(Pion.typePion))
				liste = p.getCouleur() == Couleur.NOIR ? pionsNoirs : pionsBlancs
			else
				liste = p.getCouleur() == Couleur.NOIR ? damesNoires : damesBlanches
			liste.add(p.getPosition())

		pieces[0] = new int[pionsNoirs.size()]
		for (int i = 0; i < pionsNoirs.size(); i++)
			pieces[0][i] = pionsNoirs.get(i)

		pieces[1] = new int[pionsBlancs.size()]
		for (int i = 0; i < pionsBlancs.size(); i++)
			pieces[1][i] = pionsBlancs.get(i)
		
		pieces[2] = new int[damesNoires.size()]
		for (int i = 0; i < damesNoires.size(); i++)
			pieces[2][i] = damesNoires.get(i)
		
		pieces[3] = new int[damesBlanches.size()]
		for (int i = 0; i < damesBlanches.size(); i++)
			pieces[3][i] = damesBlanches.get(i)
		

		ArchiveJeu archive = new ArchiveJeu(nom, pieces, this.prochainMouvement)
		return archive

	"""
	Crée un pion
	
	@param position
	position du pion sur le damier
	@param couleur
	couleur du pion (noir ou blanc)
	"""
	public void creerPion(int position, Couleur couleur)
		Pion pion = new Pion(couleur)
		pion.placer(this, position)

	"""
	Crée une dame
	
	@param position
	position de la damme sur le damier
	@param couleur
	couleur de la damme (noir ou blanc)
	@return "null" si la dame a été créée ou le message d'erreur
	"""
	public String creerDame(int position, Couleur couleur)
		Dame dame = new Dame(couleur)
		return dame.placer(this, position)
	

	"""
	Ajoute sur le damier des pièces données
	
    @param pieces
	position des pions noirs, pions blancs, dames noires, dames
	blanches
	"""
	private void creerPieces(int[][] pieces)
		if (this.pieces == null)
			return
	
		int[] pionsNoirs = pieces.length > 0 ? pieces[0] : new int[0]
		int[] pionsBlancs = pieces.length > 1 ? pieces[1] : new int[0]
		int[] damesNoires = pieces.length > 2 ? pieces[2] : new int[0]
		int[] damesBlanches = pieces.length > 3 ? pieces[3] : new int[0]

		this.creerPions(pionsNoirs, pionsBlancs)
		this.creerDames(damesNoires, damesBlanches)
		this.dessiner("reprise jeu")
	

	"""
	Crée des pions noirs et blancs
	
	@param positionsNoires
	liste des positions des pions noirs
	@param positionsBlanches
	liste des positions des pions blancs
	"""
	private void creerPions(int[] positionsNoires, int[] positionsBlanches)
		this.creerPions(positionsNoires, Couleur.NOIR)
		this.creerPions(positionsBlanches, Couleur.BLANC)

	"""
	Crée des pions d'une seule couleur
	
	@param positions
	liste des positions
	@param couleur
	couleur des pions
	"""
	private void creerPions(int[] positions, Couleur couleur)
		for (int i = 0; i < positions.length; i++)
			int position = positions[i]
			this.creerPion(position, couleur)

	"""
	Crée des dames noires et blanches
	
	@param positionsNoires
	liste des positions des dames noires
	@param positionsBlanches
	liste des positions des dames blanches
	@return "null" ou le message d'erreur
	"""
	private String creerDames(int[] positionsNoires, int[] positionsBlanches)
		ArrayList<String> erreurs = new ArrayList<String>()
		String erreur = this.creerDames(positionsNoires, Couleur.NOIR)
		if (erreur != null)
			erreurs.add(erreur)
		
		erreur = this.creerDames(positionsBlanches, Couleur.BLANC)
		if (erreur != null)
			erreurs.add(erreur)
		
		return erreurs.size() > 0 ? String.join("\n", erreurs) : null

	"""
	Crée des dames d'une seule couleur
	
	@param positions
	liste des positions
	@param couleur
	couleur des dames
	@return "null" si la création est réussie ou le message d'erreur
	"""
	private String creerDames(int[] positions, Couleur couleur)
		ArrayList<String> erreurs = new ArrayList<String>()
		for (int i = 0; i < positions.length; i++)
			int position = positions[i]
			String erreur = this.creerDame(position, couleur)
			if (erreur != null)
				erreurs.add(erreur)
		return erreurs.size() > 0 ? String.join("\n", erreurs) : null
