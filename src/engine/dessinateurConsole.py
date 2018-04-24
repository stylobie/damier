package damier

import java.util.ArrayList

"""
La classe DessinateurConsole affiche la représention du jeu à la console
"""
public class DessinateurConsole extends DessinateurTexte
	
	@Override
	public void dessiner(ArrayList<Piece> pieces)
		super.dessiner(pieces)
		System.out.println(this.getTexte())
		System.out.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

	@Override
	public void dessinerMessage(String message)
		super.dessinerMessage(message)
		System.out.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		System.out.println(message)
		System.out.println(".")

