
public class Reptil extends Animal {
	private String corEscama;
	
	@Override
	public void locomover() {
		System.out.println("Rastejando");		
	}
	@Override
	public void alimentar() {
		System.out.println("Comendo");	
	}
	@Override
	public void emitirSom() {
		System.out.println("Emitindo som de réptil");		
	}
	
	public String getCorEscama() {
		return corEscama;
	}
	public void setCorEscama(String corEscama) {
		this.corEscama = corEscama;
	}

}
