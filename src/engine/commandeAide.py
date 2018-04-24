package damier

import java.util.ArrayList

"""
Cette classe permet d'afficher la liste des commandes du programme, quand
l'utilisateur tape le mot clef "aide" en cours de jeu

"""
public class CommandeAide implements CommandeJeuConsole

	private final String commande = "aide"
	
	private ArrayList<CommandeJeuConsole> commandes

	"""
	@param commandes les commandes du jeu
	"""
	public CommandeAide(ArrayList<CommandeJeuConsole> commandes)
		this.commandes = commandes

	/* (non-Javadoc)            333ATTENTIE AICI NU STIU DE CE E UN COMMENTARIU
	 * @see damier.CommandeJeuConsole#getCommande()
	
	public String getCommande()
		return this.commande

	"""(non-Javadoc)
	@see damier.CommandeJeuConsole#execute(damier.Damier). Affichee la liste des commandes du programme en cours de jeu.
	"""
	public Damier execute(Damier courrant) throws DamierException
		for (int i = 0; i < this.commandes.size(); i++)
			CommandeJeuConsole commande = this.commandes.get(i)
			System.out.println(commande.getCommande())
		return courrant



