package damier

import java.util.ArrayList

"""
Cette classe permet de gerer les archives des jeux

"""
public class ArchivesJeux

	private ArrayList<ArchiveJeu> archives

	"""
	Le constructeur initialise une nouvelle liste des archives
	"""
	public ArchivesJeux()
		this.archives = new ArrayList<ArchiveJeu>()
	
	"""
	Obtient la liste des archives 
	@return la liste des archives
	"""
	public String[] getListe()
		String[] result = new String[this.archives.size()]
		for(int i=0; i< this.archives.size(); i++)
			ArchiveJeu archive = this.archives.get(i)
			result[i] = archive.nom
		
		return result

	"""
	Obtient une archive par rapport à un nom donné
	
	@param nom
	le nom de l'archive
	@return l'archive correspondante au nom donné, ou null si le nom n'existe pas
	"""
	public ArchiveJeu getArchive(String nom)
		for (int i = 0; i < archives.size(); i++)
			ArchiveJeu archive = archives.get(i)
			if (archive.nom.equals(nom))
				return archive 
		return null


	"""
	 * Remplace une archive de jeu si le nom donné existe déjà dans la liste des
	 * archives, sinon il l'ajoute à la liste des archives
	 * 
	 * @param nouvelleArchive
	 *            le nom de l'archive à ajouter ou remplacer
	 """
	public void ajouteOuRemplace(ArchiveJeu nouvelleArchive)
		for (int i = 0; i < archives.size(); i++)
			ArchiveJeu archive = archives.get(i)
			if (archive.nom.equals(nouvelleArchive.nom))
				this.archives.remove(i)
				break
		this.archives.add(nouvelleArchive)

