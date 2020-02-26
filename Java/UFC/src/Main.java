
public class Main {

	public static void main(String[] args) {
		Lutador l[]=new Lutador[2];
		l[0]= new Lutador("Jose","Brasil",25,70,1.75,7,1,0);
		l[1]=new Lutador("Lucas","Espanha", 28,69.9,1.69,3,0,2);
		
		Luta UFC=new Luta();
		UFC.marcarLuta(l[0], l[1]);
		UFC.lutar();
	}

}
