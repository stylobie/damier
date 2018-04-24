package damier

import java.util.ArrayList

"""
La classe Mouvement représente un mouvement complet demandé par un joueur. Il
est constitué d’un enchaînement des mouvements unitaires.

"""
public class Mouvement
	private Damier damier
	private ArrayList<MouvementUnitaire> mouvementsUnitaires
	private String mouvementManoury

	"""
	Crée un mouvement à partir d'un string en format Manoury, initialise les
	positions de déplacement et les mouvements unitaires
	
	@param damier
	le damier
	@param mouvementManoury
	mouvement donnée dans le format Manoury
	"""
	public Mouvement(Damier damier, String mouvementManoury)
		this.mouvementManoury = mouvementManoury
		ArrayList<Integer> positionsDeplacements
		try
			positionsDeplacements = Mouvement.getPositions(mouvementManoury)
		catch (NumberFormatException e)
			positionsDeplacements = new ArrayList<Integer>()
		
		this.damier = damier
		this.mouvementsUnitaires = creerSegments(positionsDeplacements)

	"""
	Vérifie la validité du mouvement et détermine les causes d’invalidité
	
	@throws DamierException
	"""
	public void valider() throws DamierException
		this.verifierSyntaxe()
		this.verifierPiece()
		this.verifierPositionsValides()
		this.verifierDestinationsLibres()

		ArrayList<MouvementUnitaire> mouvementsPossibles = this.getMouvementsPossibles()
		this.verifierMouvementPossible(mouvementsPossibles)
		this.verifierPriseMax()

	"""
	Exécute le mouvement (si valide) en déplaçant la pièce puis retirer les
	captures
	"""
	public void execute() 
		Piece p = this.getPiece()
		for (int i = 0 i < this.mouvementsUnitaires.size() i++) 
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			if (i == this.mouvementsUnitaires.size() - 1) 
				p.deplacer(mu.getPositionDestination())
			else
				p.simuler(mu.getPositionDestination())
			
			this.damier.dessiner(null)
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			if (mu.estCapture())
				this.damier.retirer(mu.getPositionCapturee())
		Couleur prochain = p.getCouleur() == Couleur.BLANC ? Couleur.NOIR : Couleur.BLANC
		this.damier.setProchainMouvement(prochain)

	"""
	Vérifie si la prise est maximale
	@param mouvementsPossibles
	liste des mouvements unitaires possibles
	@throws DamierException
	declanche une exception si la prise n'est pas maximale
	"""
	
    
    """
	@param mouvementsPossibles
	@throws DamierException
	"""
	private void verifierPriseMax() throws DamierException
		# on obtient les mouvements avec prise maximale
		ArrayList<MouvementUnitaire> mouvementsPossibles = this.damier.analyse()
		int maxCaptures = MouvementUnitaire.getMaxCaptures(mouvementsPossibles)
		
		# si le nombre de captures max du mouvement < nombre de captures
		# maximales pour un autre mouvement
		# on va proposer à l'utilisateur les variantes de coup maximal
		if (maxCaptures > this.getCaptures())
			# on transforme l'arbre des mouvements unitaires possibles dans une
			# liste de mouvements Manoury
			ArrayList<String> variantesPossibles = MouvementUnitaire.getVariantes(mouvementsPossibles)
			String variantes
			# si une seule variante
			if (variantesPossibles.size() == 1)
				variantes = variantesPossibles.get(0)
			else
				# si plusieurs variantes, on les affichent concaténées
				variantes = String.join(", ", variantesPossibles)
			throw new DamierException(String.format("Vous devez prendre le coup maximal de pièces: %s", variantes))

	"""
	Obtient le nombre des pièces capturée
    @return
	"""
	private int getCaptures()
		int result = 0
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			if (mu.estCapture())
				result++
		return result


	"""
	Vérifie si le mouvement est possible
	@param mouvementsPossibles
	liste des mouvements possibles
	@throws DamierException
	declanche une exception si le mouvement est invalide
	"""
	private void verifierMouvementPossible(ArrayList<MouvementUnitaire> mouvementsPossibles) throws DamierException
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			# au départ on n'a pas d'erreur
			String erreur = null
			if (mouvementsPossibles == null)
				erreur = String.format("Le mouvement %d -> %d est invalide", mu.getPositionDepart(),
						mu.getPositionDestination())
			else
				boolean leMouvementEstPossible = false
				for (int j = 0 j < mouvementsPossibles.size() j++)
					MouvementUnitaire mouvementPossible = mouvementsPossibles.get(j)
					if (mouvementPossible.getPositionDepart() == mu.getPositionDepart()
							&& mouvementPossible.getPositionDestination() == mu.getPositionDestination())
						leMouvementEstPossible = true
						# on recupère la position de la pièce capturée
						mu.setPositionCapturee(mouvementPossible.getPositionCapturee())
						# on cherche recursivement le segment suivant
						mouvementsPossibles = mouvementPossible.mouvementsSuivants
						break
				if (!leMouvementEstPossible)
					erreur = String.format("Le mouvement %d -> %d est invalide", mu.getPositionDepart(),
							mu.getPositionDestination())
			# si on a une erreur, on déclanche une exception qui arrête
			# l'execution de la méthode
			if (erreur != null)
				throw new DamierException(erreur)

	"""
	Obtient la liste des mouvements possibles
	@return les mouvements possibles
	"""
	private ArrayList<MouvementUnitaire> getMouvementsPossibles()
		Piece p = this.getPiece()
		# true dans le cas de prise maximale, false pour toutes les mouvements
		# possibles sans prise max
		return p.analyse(false)

	"""
	Vérifie si les positions sont valides
	@throws DamierException
    déclanche une exception si la position est invalide
	"""

	private void verifierPositionsValides() throws DamierException
		ArrayList<Integer> positions = new ArrayList<Integer>()
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			positions.add(mu.getPositionDepart())

			if (i == this.mouvementsUnitaires.size() - 1)
				positions.add(mu.getPositionDestination())
		for (int i = positions.size() - 1 i >= 0 i--)
			if (PositionsDamier.estPositionValide(positions.get(i)))
				positions.remove(i)
		switch (positions.size())
		case 0:
			break
		case 1:
			throw new DamierException(String.format("La position %d est invalide", positions.get(0)))
		default:
			throw new DamierException(String.format("Les positions %s sont invalides", Outils.join(", ", positions)))

	"""
	Vérifie si les positions nécessaires au mouvement sont libres. 
	@throws DamierException
	déclanche une exception si la position est ocuppée
	"""
	private void verifierDestinationsLibres() throws DamierException
		ArrayList<Integer> positions = new ArrayList<Integer>()
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			positions.add(mu.getPositionDestination())
		for (int i = positions.size() - 1 i >= 0 i--)
			if (this.damier.estPositionLibre(positions.get(i)))
				positions.remove(i)
		switch (positions.size())
		case 0:
			break
		case 1:
			throw new DamierException(String.format("La position %d est occupée", positions.get(0)))
		default:
			throw new DamierException(String.format("Les positions %s sont occupées", Outils.join(", ", positions)))

	"""
	Vérifie si la case de départ est occupée et si la couleur de la pièce
	n'est pas une adverse
	
	@throws DamierException
	déclanche une exception si la case de départ n'est pas
	occupée et si on essaye de joeur une pièce adverse
	"""
	private void verifierPiece() throws DamierException
		Piece piece = getPiece()
		if (piece == null)
			throw new DamierException("La case de départ n'est pas occupée")
		if (piece.getCouleur() != this.damier.getProchainMouvement())
			throw new DamierException("Vous essayez de jouer une pièce de votre adversaire")

	"""
	Obtient la pièce à jouer du damier
	@return la pièce à jouer
	"""
	private Piece getPiece()
		MouvementUnitaire start = this.mouvementsUnitaires.get(0)
		Piece piece = this.damier.getPiece(start.getPositionDepart())
		return piece

	"""
	Vérifie la syntaxe de la chaîne introduite par l’utilisateur
	
	@throws DamierException
	déclanche une exception si la syntaxe d'un coup est
	incorrecte
	"""
	private void verifierSyntaxe() throws DamierException
		if (this.mouvementsUnitaires.size() == 0)
			throw new DamierException("Syntaxe incorrecte pour la notation d'un coup: " + this.mouvementManoury)

	"""
	(non-Javadoc) 
	@see java.lang.Object#toString()
	"""
	public String toString()
		String result = ""
		for (int i = 0 i < this.mouvementsUnitaires.size() i++)
			MouvementUnitaire mu = this.mouvementsUnitaires.get(i)
			String sep = mu.estCapture() ? "x" : "-"
			result = result + mu.getPositionDepart() + sep
			if (i == this.mouvementsUnitaires.size() - 1)
				result = result + mu.getPositionDestination()
		return result

	"""
	Obtient les positions à partir du mouvement Manoury donné sous forme de
    string
	
	@param mouvementManoury
	representation sous forme d'un string d'un mouvement
	@return les positions d'un mouvement Manoury
	"""
	private static ArrayList<Integer> getPositions(String mouvementManoury)
		ArrayList<Integer> result
		char[] separateurs = { '-', 'x' }
		ArrayList<String> positionsStr = Outils.split(mouvementManoury, separateurs)
		result = Outils.convertToInteger(positionsStr)
		return result

	"""
	Crée des mouvements unitaires à partir d'une liste de positions données
	
	@param positions
	@return mouvements unitaires
	"""
	private static ArrayList<MouvementUnitaire> creerSegments(ArrayList<Integer> positions)
		ArrayList<MouvementUnitaire> mouvementsUnitaires = new ArrayList<MouvementUnitaire>()
		for (int i = 0 i < positions.size() - 1 i++)
			int positionDepart = positions.get(i)
			int positionDestination = positions.get(i + 1)
			# la position capturée n'est pas conue ici, nous allons l'initialiser avec -1==sans capture
			MouvementUnitaire mu = new MouvementUnitaire(positionDepart, positionDestination, -1)
			mouvementsUnitaires.add(mu)
		return mouvementsUnitaires
