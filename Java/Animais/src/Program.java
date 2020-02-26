public class Program {

	public static void main(String[] args) {
		//Animal an=new Animal();
		Mamifero m=new Mamifero();
		Reptil r=new Reptil();
		Peixe p=new Peixe();
		Ave a=new Ave();
		
		Canguru c=new Canguru();
		c.locomover();
		Arara ar=new Arara();
		ar.emitirSom();
		Tartaruga t=new Tartaruga();
		t.locomover();
		
		Lobo l=new Lobo();
		l.emitirSom();
		Cachorro ca=new Cachorro();
		ca.emitirSom();
		ca.reagir(true);
		ca.reagir(14);
		ca.reagir("Oi");
	}

}
