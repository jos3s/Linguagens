public class Mamifero extends Animal {
	protected String corPelo;
	
	@Override
	public void locomover() {
		System.out.println("Correndo");
	}
	@Override
	public void alimentar() {
		System.out.println("Comendo");
	}
	@Override
	public void emitirSom() {
		System.out.println("Emitindo som de mamífero");
	}

	public String getCorPelo() {
		return corPelo;
	}

	public void setCorPelo(String corPelo) {
		this.corPelo = corPelo;
	}

}
