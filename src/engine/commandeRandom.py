package damier

import java.util.ArrayList

public class CommandeRandom implements CommandeJeuConsole

	private JeuConsole jeu

	public CommandeRandom(JeuConsole jeu)
		this.jeu = jeu

	public String getCommande()
		return "random"
	

	public Damier execute(Damier courrant) throws DamierException
		while(!courrant.getEstTermine())
			ArrayList<MouvementUnitaire> mu = courrant.analyse()
			ArrayList<String> variantes = MouvementUnitaire.getVariantes(mu)
			int max = variantes.size()
			int i = (int)(Math.random() * max)
			String variante = variantes.get(i)
			System.out.println(variante)
			this.jeu.mouvement(variante)
		return courrant
