package damier

import java.util.ArrayList

"""
Cette classe permet de revenir en arrière en anulant le dernier coup dans une
partie, quand l'utilisateur tape le mot clef "undo" en cours de jeu. On peut
revenir en arrière un nombre limité de coups.

"""
public class CommandeUndo implements CommandeJeuConsole
	String commande = "undo"
	ArrayList<ArchiveJeu> historique

	"""
	@param historique
    l'historique d'un nombre predéfini de coups archivés
	"""
	public CommandeUndo(ArrayList<ArchiveJeu> historique)
		this.historique = historique
	

	"""
	(non-Javadoc)
	
	@see damier.CommandeJeuConsole#getCommande()
	"""
	public String getCommande()
		return this.commande

	"""
	(non-Javadoc)
	@see damier.CommandeJeuConsole#execute(damier.Damier). 
	Annule le dernier coup en le supprimant de l'historique
	"""
	public Damier execute(Damier courrant) throws DamierException
		if (this.historique.size() > 0)
			ArchiveJeu archive = this.historique.get(0)
			this.historique.remove(0)
			# restaure un damier à partir d'une archive
			Damier restaure = new Damier(courrant.dessinateur, archive)
			return restaure
		else
			return courrant
