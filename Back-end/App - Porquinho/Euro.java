package Trabalho;

public class Euro extends Moeda {

	// construtores
	public Euro () {
		super();
	}
	
	public Euro (double valor) {
		super(valor);
	}

	// mostrar informações da moeda
	@Override
	public void info() {
		System.out.printf("          € %.2f%n", valor);
	}
	
	// converter os valores
	@Override
	public double converter() {
		return valor * 5.40; 
	}
}
