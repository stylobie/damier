package damier

import java.util.ArrayList

public class CommandeZero implements CommandeJeuConsole

	private JeuConsole jeu

	public CommandeZero(JeuConsole jeu)
		this.jeu = jeu
	public String getCommande()
		return "zero"

	public Damier execute(Damier courrant) throws DamierException
		while(!courrant.getEstTermine())
			ArrayList<MouvementUnitaire> mu = courrant.analyse()
			ArrayList<String> variantes = MouvementUnitaire.getVariantes(mu)
			String variante = variantes.get(0)
			System.out.println(variante)
			this.jeu.mouvement(variante)
		
		return courrant
