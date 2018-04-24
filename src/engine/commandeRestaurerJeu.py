package damier

import tools.Terminal

"""
Cette classe permet restaurer un jeu, quand l'utilisateur tape le mot clef
"restaurer" en cours de jeu
"""
public class CommandeRestaurerJeu implements CommandeJeuConsole
	public final String commande = "restaurer"
	private ArchivesJeux archives

	"""
	@param archives
	les archives du jeu
	"""
	public CommandeRestaurerJeu(ArchivesJeux archives)
		this.archives = archives
	

    """
	(non-Javadoc)
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande()
		return this.commande
	

	"""
	(non-Javadoc)
	
	@see damier.CommandeJeuConsole#execute(damier.Damier). Restaure un jeu s'il
	existe.
	"""
	public Damier execute(Damier courrant) throws DamierException
		String[] listeArchives = this.archives.getListe()
		if (listeArchives.length == 0)
			throw new DamierException("Il n'y a pas de jeu sauvegardé")
		
		System.out.println("Les archives existantes sont: ")
		for (int i = 0; i < listeArchives.length; i++)
			System.out.println(listeArchives[i])
		
		System.out.println("Entrer le nom de la partie à restaurer: ")
		String nom = Terminal.lireString()
		ArchiveJeu archive = archives.getArchive(nom)
		if (archive == null)
			throw new DamierException("partie inexistante !")
		# retourne un nouveau damier à partir de l'archive
		return new Damier(courrant.dessinateur, archive)
