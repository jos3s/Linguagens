
public class Quarto {
	public String morador;
	public String email;
				
	public Quarto(String morador, String email) {
		this.morador = morador;
		this.email = email;
	}
	
	public String getMorador() {
		return morador;
	}
	public void setMorador(String morador) {
		this.morador = morador;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	@Override
	public String toString() {
		return "Morador=" + morador + ", Email=" + email;
	}
		
}
