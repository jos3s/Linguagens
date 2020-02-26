import java.util.Random;

public class Cliente {
	private String nome;
	private int saldo, nconta;
	
	public Cliente(String nome, int saldo) {
		this.nome = nome;
		this.saldo = saldo;
		Random r= new Random();
		int conta=r.nextInt(8001)+1000;
		this.setNconta(conta);
	}
	public Cliente(String nome) {
		this.nome = nome;
		this.setSaldo(0);
		Random r= new Random();
		int conta=r.nextInt(8001)+1000;
		this.setNconta(conta);
	}
	
	public void deposito(int valor) {
		this.setSaldo(this.getSaldo()+valor);
		System.out.println("Você depositou R$"+ valor +" o saldo atual é de R$"+this.getSaldo());
	}
	
	public void sacar(int valor) {
		this.setSaldo(this.getSaldo()-valor-5);
		System.out.println("Você sacou R$"+ valor +" o saldo atual é de R$"+this.getSaldo());
	}
	
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	private int getSaldo() {
		return saldo;
	}
	private void setSaldo(int saldo) {
		this.saldo = saldo;
	}
	private void setNconta(int nconta) {
		this.nconta = nconta;
	}
	
	@Override
	public String toString() {
		return "Cliente [Nome=" + nome + ", Saldo=" + saldo + ", Numero da conta=" + nconta + "]";
	}
	
}
