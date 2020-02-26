import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		Cliente n1;
		System.out.println("Digite o seu nome: ");
		String nome=sc.next();
		System.out.println("Deseja depositar algum valor? [s/n] ");
		String esc=sc.next();
		if(esc.equals("s")) {
			System.out.println();
			System.out.println("Digite o valor para o deposito: ");
			int saldo=sc.nextInt();
			n1=new Cliente(nome, saldo);
		}else {
			n1=new Cliente(nome);
		}
		System.out.println(n1.toString());
		sc.close();
	}

}
