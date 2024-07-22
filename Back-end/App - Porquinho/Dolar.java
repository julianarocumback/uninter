package Trabalho;

public class Dolar extends Moeda {

	// construtores
	public Dolar () {
		super();
	}
	
	public Dolar (double valor) {
		super(valor);
	}
		
	// mostrar informações da moeda
	@Override
	public void info() {
		System.out.printf("          $ %.2f%n", valor);
	}
	
	// converter os valores
	@Override
	public double converter() {
		return valor * 5.00;
	}
}