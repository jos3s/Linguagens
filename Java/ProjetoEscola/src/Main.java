
public class Main {

	public static void main(String[] args) {
		Visitante v=new Visitante();
		v.setNome("Carlos");
		v.setIdade(30);
		v.setSexo("M");
		Aluno a=new Aluno();
		a.setNome("Luis");
		a.setCurso("ES");
		a.setMatricula(1000);
		a.setIdade(16);
		a.setSexo("M");
		Bolsista b=new Bolsista();
		b.setMatricula(1231);
		b.setNome("Ana");
		b.setIdade(21);
		b.setBolsa(25.5f);
		System.out.println(v.toString());
		System.out.println(a.toString());
		System.out.println(b.toString());
	}

}
