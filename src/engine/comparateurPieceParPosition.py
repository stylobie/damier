package damier

import java.util.Comparator

"""
Compare deux pièces par leur position 
@return un numéro positiv si la position de la pièce p1 > position de la
pièce p2, 
ou un numéro négatif si la position de la pièce p1 < position de la
pièce p2
"""
public class ComparateurPiecesParPosition implements Comparator<Piece>

	@Override
	public int compare(Piece p1, Piece p2)
		return p1.getPosition() - p2.getPosition()
