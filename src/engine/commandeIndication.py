package damier

import java.util.ArrayList

import tools.Terminal

"""
Cette classe permet d'afficher les variantes des mouvements possibles pour le
joueur courrant, en tappant "?" en cours de jeu. Si un seul mouvement est
possible, il l'effectue

"""
public class CommandeIndication implements CommandeJeuConsole
	private final String commande = "?"
	private JeuConsole jeu

	"""
	@param jeu
	"""
	public CommandeIndication(JeuConsole jeu)
		this.jeu = jeu
	

	"""
	(non-Javadoc)
	 
	@see damier.CommandeJeuConsole#getCommande()
    """
	public String getCommande()
		return this.commande
	

	"""
	(non-Javadoc)
	 
	@see damier.CommandeJeuConsole#execute(damier.Damier). Affiche les variantes
	des mouvements possibles pour le joueur courrant. Si un seul mouvement est
	possible, il sera executé
	"""
	public Damier execute(Damier courrant) throws DamierException
		ArrayList<MouvementUnitaire> mu = courrant.analyse()
		ArrayList<String> variantes = MouvementUnitaire.getVariantes(mu)
		for (int i = 0 i < variantes.size() i++)
			String variante = variantes.get(i)
			System.out.println(i + " => " + variante)
		
		String variante = null
		# Si un seul mouvement est possible, il sera executé
		if (variantes.size() == 1)
			variante = variantes.get(0)
			# si plusieurs mouvements possibles, on pourra les executer avec leur numéro
		 else
			try
				int var = Terminal.lireInt()
				variante = variantes.get(var)
			 catch (Exception e)
				throw new DamierException(e.getMessage())
			
		
		System.out.println(variante)
		this.jeu.mouvement(variante)
		return courrant
	


