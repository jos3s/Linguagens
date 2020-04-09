import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		Quarto[] q=new Quarto[10];
		int n=sc.nextInt();
		for(int i=0;i<n;i++){
			System.out.print("Nome: ");
			String nome=sc.next();
			System.out.print("Email: ");
			String email=sc.next();
			System.out.print("Quarto: ");
			int quarto=sc.nextInt();
			q[quarto]=new Quarto(nome,email);
		}
		
		for (int i=0; i<10; i++) {
			if (q[i] != null) {
				System.out.println(i + ": " + q[i]);
			}
		}
		sc.close();
	}

}
