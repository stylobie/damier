package damier

import tools.Terminal

"""
Cette classe a la repsonsabilité d'archiver un jeu, quand l'utilisateur tape
"archiver" en cours d'une partie

"""
public class CommandeArchiverJeu implements CommandeJeuConsole
	public final String commande = "archiver"
	private ArchivesJeux archives

	"""
	@param archives
	les archives du jeu
	"""
	public CommandeArchiverJeu(ArchivesJeux archives) 
		this.archives = archives

    """
	(non-Javadoc)
	
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande()
		return this.commande

	"""
	(non-Javadoc) 
	@see damier.CommandeJeuConsole#execute(damier.Damier). Archive un jeu sous un
	nom introduit à la console. Si le nom existe déjà il remplace l'archive
	existante, sinon il rajoute l'archive aux archives du jeu
	"""
	public Damier execute(Damier courrant) throws DamierException
		System.out.println("Entrez un nom pour l'archive :")
		String nom = Terminal.lireString()
		ArchiveJeu archive = courrant.archiverJeu(nom)
		archives.ajouteOuRemplace(archive)
		return courrant

