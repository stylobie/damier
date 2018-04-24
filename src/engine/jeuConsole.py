package damier

import java.util.ArrayList

import tools.Terminal

"""
Cette classe a la responsabilité d'initialiser le jeu. Elle contient aussi la
classe "main" permetant d'executer un jeu avec des commandes données à la
console
"""
public class JeuConsole
	private Damier damier
	private DessinateurGraphique dg

	public ArrayList<CommandeJeuConsole> commandes
	private ArchivesJeux archives
	private ArrayList<ArchiveJeu> historique

	"""
	Prépare un jeu avec des commandes console, avec des coups introduits au
	terminal
	"""
	public JeuConsole() 
		this.dg = new DessinateurGraphique()
		this.damier = new Damier(this.dg)
		this.archives = new ArchivesJeux()
		this.historique = new ArrayList<ArchiveJeu>()

		this.initialiserCommandes()

	"""
	Charge la liste des commandes
	"""
	private void initialiserCommandes() 
		this.commandes = new ArrayList<CommandeJeuConsole>()

		this.commandes.add(new CommandeNouveauJeu())
		this.commandes.add(new CommandeArchiverJeu(this.archives))
		this.commandes.add(new CommandeRestaurerJeu(this.archives))
		this.commandes.add(new CommandeDemoCoupTurc())
		this.commandes.add(new CommandeExit())
		this.commandes.add(new CommandeAide(this.commandes))
		this.commandes.add(new CommandeUndo(this.historique))
		this.commandes.add(new CommandeIndication(this))
		this.commandes.add(new CommandeZero(this))
		this.commandes.add(new CommandeRandom(this))


	"""
	Jouer à l'infini, sauf si une commande arrête le processus
	"""
	public void jouer()
		while (true)
			this.jouerCoup()

	"""
	Lire un string introduit par un des joueurs. Si c'est une commande valide
	elle va s'executer, sinon la méthode présume qu'il s'agit d'un mouvement
	qu'elle va essyer d'executer.
	"""
	private void jouerCoup()
		# indiquer la couleur à jouer
		Couleur c = this.damier.getProchainMouvement()
		int numeroJoueur = c == Couleur.BLANC ? 1 : 2
		System.out.print(String.format("Joueur %d (%s) : ", numeroJoueur, c))
	    # lire une commande/mouvement introduite
		String input = Terminal.lireString()

		try
			# si c'est une commande, la méthode executeCommande va retourner true
			if (this.executeCommande(input))
				return
			
		catch (DamierException e)
			System.out.println(e.getMessage())
			return
		
		# on sait maintenant que le string introduit (input) n'est pas une commande
		# effectuer le mouvement demandé
		this.mouvement(input)

	"""
	Vérifie si le mouvement est valide, si oui il archive la position et execute
	le mouvement. Si la partie est considérée terminée, affiche "Fin de la
	partie"
	
    @param input
	un mouvement donné en format Manoury
	"""
	public void mouvement(String input)
		Mouvement m = new Mouvement(this.damier, input)
		# si le mouvement est valide
		try 
			m.valider()
		catch (DamierException e)
			System.out.println(e.getMessage())
			return
		
		# archiver la position
		this.archiverPosition()
		# executer le mouvement
		m.execute()

		# si la partie est terminée
		if (this.damier.getEstTermine())
			System.out.println("Fin de la partie")

	"""
	Archive dans l'historique du jeu les dernièrs 5 coups effectués pour
	permettre à revenir en arrière si besoin
	"""
	private void archiverPosition()
		int nbCoupsAArchiver = 5
		ArchiveJeu archive = this.damier.archiverJeu(null)
		# le dernier coup est ajouer à la liste archive, en position 0
		this.historique.add(0, archive)
		# on ne garde qu'un nombre limité des dernièrs coups effectués
		while (this.historique.size() > nbCoupsAArchiver)
			this.historique.remove(this.historique.size() - 1)

	"""
	Execute la commande si la valeur introduite fait partie de la liste de
	commandes
	@param input
    commande introduite sous forme texte
	@return true si une commande a été trouvée et executée
	"""

	private boolean executeCommande(String input) throws DamierException
		for (int i = 0 i < commandes.size() i++)
			CommandeJeuConsole commande = commandes.get(i)
			if (commande.getCommande().equals(input))
				# une commande peut ou non remplacer le damier courrant
				# par ex: la commande "aide" ne modifie pas le damier courrant elle va
				# retourner le même, reçu en paramètre dans la méthode "execute"
				# une autre commande "restaurer" va créer et retourner un nouveau damier qui
				# remplacera l'ancien
				this.damier = commande.execute(this.damier)
				return true
		return false

	public static void main(String[] args)
		JeuConsole jeu = new JeuConsole()
		jeu.jouer()
