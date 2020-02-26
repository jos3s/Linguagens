public class Gafanhoto extends Pessoa{
	protected String login;
	protected int totalAssistido;
	
	public void viuMaisUm() {
		this.setTotalAssistido(1);
	}
	
	public Gafanhoto(String nome, int idade, String sexo, String login) {
		super(nome, idade, sexo);
		this.setLogin(login);
		this.setTotalAssistido(0);
	}

	@Override
	protected void ganharExp() {
		// TODO Auto-generated method stub
		
	}

	
	@Override
	public String toString() {
		return "Gafanhoto [login=" + login + ", totalAssistido=" + totalAssistido + ", nome=" + nome + ", idade="
				+ idade + ", sexo=" + sexo + ", exp=" + exp + "]";
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public int getTotalAssistido() {
		return totalAssistido;
	}

	public void setTotalAssistido(int totalAssistido) {
		this.totalAssistido += totalAssistido;
	}
	
}

