public class Lutador {
	
	private String nome,nacionalidade,categoria;
	private int idade;
	private double peso,altura;
	private int vitorias,derrotas,empates;
	
	
	public void apresentar() {
		System.out.println("---------------------------------");
		System.out.println("Apresentando o lutador "+this.getNome());
		System.out.println("Diretamente de "+this.getNacionalidade()); 
		System.out.println("com "+this.getIdade()+" anos e "+this.getAltura()+" de altura"); 
		System.out.println("com um peso de "+this.getPeso()); 
		System.out.println(this.getVitorias()+" vitórias"); 
		System.out.println(this.getDerrotas()+" derrotas"); 
		System.out.println("e com "+this.getEmpates()+" empates"); 
	}
	public void status() {
		System.out.println("---------------------------------");
		System.out.println(this.getNome() +" é um peso "+this.getCategoria()); 
		System.out.println("Ganhou "+this.getVitorias()+" vezes"); 
		System.out.println("Perdeu "+this.getDerrotas()+" vezes"); 
		System.out.println("Empatou "+this.getEmpates()+" vezes"); 
	}
	public void ganharLuta() { 
		this.setVitorias(this.getVitorias()+1);
	}
	public void perderLuta() {
		this.setDerrotas(this.getDerrotas()+1);
	}
	public void empatarLuta() {
		this.setEmpates(this.getEmpates()+1);
	}
	
	public Lutador(String nome, String nacionalidade, int idade,  double peso, double altura, 
			int vitorias, int derrotas, int empates) {
		this.nome = nome;
		this.nacionalidade = nacionalidade;
		this.idade = idade;
		this.vitorias = vitorias;
		this.derrotas = derrotas;
		this.empates = empates;
		this.setPeso(peso);
		this.altura = altura;
	}
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getNacionalidade() {
		return nacionalidade;
	}
	public void setNacionalidade(String nacionalidade) {
		this.nacionalidade = nacionalidade;
	}
	
	public String getCategoria() {
		return categoria;
	}
	private void setCategoria() {
		if( this.peso >52.2 && this.peso<=70.3){
			this.categoria="Leve";
		}else if(this.peso<=83.9){
			this.categoria="Médio";
		}else if(this.peso<=120.2){
			this.categoria="Pesado";
		}else {
			this.categoria="Inválido";
		}
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso = peso;
		this.setCategoria();
	}
	
	public double getAltura() {
		return altura;
	}
	public void setAltura(double altura) {
		this.altura = altura;
	}
	
	public int getVitorias() {
		return vitorias;
	}
	public void setVitorias(int vitorias) {
		this.vitorias = vitorias;
	}
	
	public int getDerrotas() {
		return derrotas;
	}
	public void setDerrotas(int derrotas) {
		this.derrotas = derrotas;
	}
	
	public int getEmpates() {
		return empates;
	}
	public void setEmpates(int empates) {
		this.empates = empates;
	}
	
	
	
	
}
