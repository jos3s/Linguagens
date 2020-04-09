import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		Produtos[] p=new Produtos[n];
		for(int i=0;i<p.length;i++) {
			String nome=sc.next();
			double preco=sc.nextDouble();
			p[i]=new Produtos(nome,preco);
		}
		double media=0;
		for(int i=0;i<n;i++) {
			media+=p[i].getPreco();
		}
		media/=p.length;
		System.out.println("A media de preços é:" +media);
		sc.close();
	}

}
