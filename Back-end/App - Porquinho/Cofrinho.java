package Trabalho;

import java.util.ArrayList;

public class Cofrinho {
	// lista de moedas
	ArrayList<Moeda> listaMoeda = new ArrayList<Moeda>();

	// adicionar moeda na lista
	public void adicionar(Moeda x) {
		listaMoeda.add(x);
	}

	// remover moeda da lista
	public void remover(Moeda x) {
		listaMoeda.remove(x);
	}

	// mostrar moedas
	public void moedasGuardadas() {

		System.out.printf("┌─────── GUARDADO ────────┐\n");
		for (Moeda x : listaMoeda) {
			x.info();
		}
		System.out.printf("└─────────────────────────┘\n\n");
	}

	// converter moedas
	public void totalConvertido() {
		double total = 0.0;
		for (Moeda x : listaMoeda) {			
			total += x.converter();
		}
		
		System.out.printf("┌─────────────────────────┐\n");
		System.out.printf("  Convertido: R$ %.2f  %n", total);
		System.out.printf("└─────────────────────────┘\n");
	}
}
