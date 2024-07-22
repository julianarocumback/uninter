package Trabalho;

public class Real extends Moeda {
	
	// construtores
	public Real () {
		super();
	}
	
	public Real(double valor) {
		super(valor);
	}

	// mostrar informações da moeda
	@Override
	public void info() {
		System.out.printf("         R$ %.2f%n", valor);
	}
	
	// converter os valores
	@Override
	public double converter() {
		return valor;
	}
}