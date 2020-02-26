
public final class Bolsista extends Aluno{
	private float bolsa;
	
	public void renovarBolsa() {
		System.out.println("Renovando bolsa");
	}
	
	@Override 
	public void pagarMensalidade() {
		System.out.println("Pagar mensalidade");
	}

	public float getBolsa() {
		return bolsa;
	}

	public void setBolsa(float bolsa) {
		this.bolsa = bolsa;
	}

	@Override
	public String toString() {
		return "Bolsista [bolsa=" + bolsa + ", toString()=" + super.toString() + "]";
	}
	
}
