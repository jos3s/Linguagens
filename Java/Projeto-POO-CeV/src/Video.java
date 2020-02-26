public class Video implements AcoesVideos{
	private String titulo;
	private int avaliacao, curtidas, views;
	private boolean reproduzindo;
	
	public Video(String titulo) {
		this.setTitulo(titulo);
		this.avaliacao=1;
		this.setCurtidas(0);
		this.setViews(0);
		this.setReproduzindo(false);
	}
	
	@Override
	public void play() {
		this.setReproduzindo(true);
	}
	@Override
	public void pausar() {
		this.setReproduzindo(false);
	}
	@Override
	public void curtir() {
		this.setCurtidas(1);
	}
	
	@Override
	public String toString() {
		return "Video [titulo=" + titulo + ", avaliacao=" + avaliacao + ", curtidas=" + curtidas + ", views=" + views
				+ ", reproduzindo=" + reproduzindo + "]";
	}

	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public int getAvaliacao() {
		return avaliacao;
	}
	public void setAvaliacao(int avaliacao) {
		int nova;
		nova=(this.getAvaliacao()+avaliacao)/this.views;
		this.avaliacao =nova;
	}
	public int getCurtidas() {
		return curtidas;
	}
	public void setCurtidas(int curtida) {
		this.curtidas +=curtida;
	}
	public int getViews() {
		return views;
	}
	public void setViews(int views) {
		this.views += views;
	}
	public boolean isReproduzindo() {
		return reproduzindo;
	}
	public void setReproduzindo(boolean reproduzindo) {
		this.reproduzindo = reproduzindo;
	}
	
}
