
public class Main {

	public static void main(String[] args) {
		Pessoa[] p=new Pessoa[2];
		Livro[] l=new Livro[4];
		
		p[0]=new Pessoa("José", 19,"M");
		p[1]=new Pessoa("Lucas", 22,"M");
		
		l[0]=new Livro("Aprenda Java", "José Antônio",300,p[0]);
		l[1]=new Livro("HTML: Do básico ao avançado", "Maria Carla",200,p[0]);
		l[2]=new Livro("MIPS", "Alexandre Matos",350,p[1]);
		l[3]=new Livro("C/C++: Linguagens poderosas", "Luiza Delmondes",500,p[1]);
		
		l[0].abrir();
		l[0].folhear(200);
		l[0].detalhes();
		System.out.println();
		l[1].detalhes();
		System.out.println();
		l[2].detalhes();
		System.out.println();
		l[3].detalhes();
	
	}

}
