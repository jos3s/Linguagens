
public class Program {

	public static void main(String[] args) {
		Video v[]=new Video[3];
		v[0]=new Video("Aula 1 de Java");
		v[1]=new Video("Aula 2 de Java");
		v[2]=new Video("Aula 3 de Java");
		
		Gafanhoto g=new Gafanhoto("Jose", 18,"M", "jos3s");
				
		Visualizacao vis[]=new Visualizacao[2];
		vis[0]=new Visualizacao(g,v[0]);
		vis[0].avaliar();
		System.out.println(vis[0].toString());
		vis[1]=new Visualizacao(g,v[1]);
		vis[1].avaliar(67.0f);
		System.out.println(vis[1].toString());
	}

}
