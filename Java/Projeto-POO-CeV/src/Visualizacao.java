public class Visualizacao {
	private Gafanhoto expectador;
	private Video filme;
	
	public void avaliar() {
		this.filme.setAvaliacao(5);
	}
	public void avaliar(int nota) {
		this.filme.setAvaliacao(nota);
	}
	public void avaliar(float por) {
		int tot=0;
		if(por<=20){
			tot=3;
		}else if(por<=50) {
			tot=5;
		}else if(por<=80) {
			tot=8;
		}else {
			tot=10;
		}
		this.filme.setAvaliacao(tot);
	}

	public Visualizacao(Gafanhoto expectador, Video filme) {
		super();
		this.expectador = expectador;
		this.filme = filme;
		this.expectador.setTotalAssistido(1);
		this.filme.setViews(1);
	}
	
	public Gafanhoto getExpectador() {
		return expectador;
	}
	public void setExpectador(Gafanhoto expectador) {
		this.expectador = expectador;
	}
	public Video getFilme() {
		return filme;
	}
	public void setFilme(Video filme) {
		this.filme = filme;
	}
	
	@Override
	public String toString() {
		return "Visualizacacao [expectador=" + expectador + ",\n filme=" + filme + "]";
	}
	
}
