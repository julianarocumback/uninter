package Trabalho;

public abstract class Moeda {
	
	// Variável
	double valor;
	
	
	//Construtores
	public Moeda() {
	}
	
	public Moeda(double valorDaMoeda) {
		this.valor = valorDaMoeda;
	}

	// Comparar valores
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Moeda other = (Moeda) obj;
		return Double.doubleToLongBits(valor) == Double.doubleToLongBits(other.valor);
	}

	// Métodos para informação e converter valores
	public abstract void info();
	
	public abstract double converter();
}
