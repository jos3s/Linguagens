import java.util.Random;

public class Luta {
	private Lutador desafiante;
	private Lutador desafiado;
	private int rounds;
	private boolean aprovado;
	
	public void marcarLuta(Lutador l1,Lutador l2) {
		if((l1!=l2) && l1.getCategoria().equals(l2.getCategoria())){
			this.setAprovado(true);
			this.setDesafiante(l1);
			this.setDesafiado(l2);
		}else {
			this.setAprovado(false);
			this.setDesafiante(null);
			this.setDesafiado(null);
		}
	}
	public void lutar() {
		if(this.isAprovado()) {
			System.out.println("Desafiante");
			this.desafiante.apresentar();
			System.out.println();
			System.out.println("Desafiado");
			this.desafiado.apresentar();
			System.out.println();
			Random ale=new Random();
			int num = ale.nextInt(3);
			switch(num) {
				case 0: //desafiante perde
					System.out.println("---------------------------------");
					System.out.println("O desafiado venceu. E seu status atual é:");
					this.desafiante.perderLuta();
					this.desafiado.ganharLuta();
					this.desafiado.status();
					break;
				case 1:
					System.out.println("---------------------------------");
					System.out.println("O desafiante venceu. E seu status atual é:");
					this.desafiante.ganharLuta();
					this.desafiado.perderLuta();
					this.desafiante.status();
					break;
				case 2:
					System.out.println("---------------------------------");
					System.out.println("Deu empate.");
					this.desafiante.empatarLuta();
					this.desafiado.empatarLuta();
					break;
			}
		}else {
			System.out.println("Luta não pode acontecer");
		}
		
	}
	
	//gets e setts
	public Lutador getDesafiante() {
		return desafiante;
	}
	public void setDesafiante(Lutador desafiante) {
		this.desafiante = desafiante;
	}
	public Lutador getDesafiado() {
		return desafiado;
	}
	public void setDesafiado(Lutador desafiado) {
		this.desafiado = desafiado;
	}
	public int getRounds() {
		return rounds;
	}
	public void setRounds(int rounds) {
		this.rounds = rounds;
	}
	public boolean isAprovado() {
		return aprovado;
	}
	public void setAprovado(boolean aprovado) {
		this.aprovado = aprovado;
	}

	
}
