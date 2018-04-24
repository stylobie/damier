package damier

import java.util.ArrayList

import damier.ComparateurPiecesParPosition
import damier.Dessinateur
import damier.Piece

"""
Dessine un Damier sous format textuel, à la console
"""
public class DessinateurTexte implements Dessinateur

	private String message
	private String texte

	"""
	
	@return le texte
	"""
	public String getTexte()
		return this.texte

	public String getMessage()
		return this.message

	"""
	(non-Javadoc)
	
	@see damier.Dessinateur#dessiner(damier.Damier)
	Ecrit la liste des pièces en format text dans le champ "texte"
	"""
	@Override
	public void dessiner(ArrayList<Piece> pieces)
		ArrayList<String> lignesTexte = new ArrayList<String>()
		# nous allons créer une copie de la liste des pièces, car nous allons la trier
		ArrayList<Piece> piecesADessiner = new ArrayList<Piece>(pieces)
		# trier les pièces dans l'ordre croissant des positions
		piecesADessiner.sort(new ComparateurPiecesParPosition())

		for (int i = 0; i < piecesADessiner.size(); i++)
			Piece piece = piecesADessiner.get(i)
			lignesTexte.add(this.getPieceTexte(piece))
		
		this.texte = String.join("\n", lignesTexte)

	@Override
	public void dessinerMessage(String message)
		this.message = message

	"""
	Obtient un text pour une pièce donnée
	
	@param piece
	la pièce sur le damier
	@return position: type et couleur de la pièce
	"""
	private String getPieceTexte(Piece piece)
		return String.format("%d : %s %s", piece.getPosition(), piece.getTypePiece()
				piece.getCouleur().toString())

