
public class Livro implements Publicacao {
	private String titulo;
	private String autor;
	private int totalPag;
	private int pagAtual;
	private boolean aberto;
	private Pessoa leitor;
	
	public void detalhes() {
		System.out.println("Titulo: "+this.getTitulo());
		System.out.println("Autor: "+this.getAutor());
		System.out.println("Total de páginas: "+this.getTotalPag());
		System.out.println("Página atual: "+this.getPagAtual());
		System.out.println("Aberto: "+this.isAberto());
		System.out.println("Leitor: "+this.leitor.getNome());
	}
	
	
	public Livro(String titulo, String autor, int totalPag,Pessoa leitor) {
		this.titulo = titulo;
		this.autor = autor;
		this.totalPag = totalPag;
		this.setLeitor(leitor);;
	}
	
	
	@Override
	public void abrir() {
		this.setAberto(true);
	}
	@Override
	public void fechar() {
		this.setAberto(false);
	}
	@Override
	public void folhear(int p) {
		if(p>this.totalPag) {
			this.pagAtual=0;
		}else {
			this.setPagAtual(p);
		}
	}
	@Override
	public void avancarPag() {
		this.setPagAtual(this.getPagAtual()+1);
	}
	@Override
	public void voltarPag() {
		this.setPagAtual(this.getPagAtual()-1);
	}
	
	
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public String getAutor() {
		return autor;
	}
	public void setAutor(String autor) {
		this.autor = autor;
	}
	public int getTotalPag() {
		return totalPag;
	}
	public void setTotalPag(int totalPag) {
		this.totalPag = totalPag;
	}
	public int getPagAtual() {
		return pagAtual;
	}
	public void setPagAtual(int pagAtual) {
		this.pagAtual = pagAtual;
	}
	public boolean isAberto() {
		return aberto;
	}
	public void setAberto(boolean aberto) {
		this.aberto = aberto;
	}
	public Pessoa getLeitor() {
		return leitor;
	}
	public void setLeitor(Pessoa leitor) {
		this.leitor = leitor;
	}
	
	
	
}
