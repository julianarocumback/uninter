// Aluna: Juliana Theodoro Rocumback - RU: 4472052 

package Trabalho;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in); 
		Cofrinho cofrinho = new Cofrinho();
		Moeda moeda;
		double valor;

		
		
        // Menu principal
        System.out.printf("┌─────── COFRINHO ────────┐\n"
                        + "│                         │\n"
                        + "│ [1] Adicionar moeda     │\n"
                        + "│ [2] Remover moeda       │\n"
                        + "│ [3] Mostrar moedas      │\n" 
                        + "│ [4] Converter para real │\n"
                        + "├─────────────────────────┤\n"
                        + "│ [0] Esconder o cofrinho │\n"
                        + "└─────────────────────────┘\n");
		System.out.print(">> ");
        
        // Menu de moedas    
        int opcoesMenu = sc.nextInt();     
        while(opcoesMenu != 0) {        
            switch (opcoesMenu) {

            	// 1 - Adicionar moedas
                case 1:                             
                    int tipoMoeda = 0; 
                    while(tipoMoeda <= 0 || tipoMoeda > 3) {
                    	 System.out.printf("┌─────── COFRINHO ────────┐\n"
                			 			 + "│                         │\n"
                			 			 + "│ Escolha o tipo de moeda │\n"
                			 			 + "│ [1] Real                │\n"
                			 			 + "│ [2] Dolar               │\n" 
                			 			 + "│ [3] Euro                │\n"
                			 			 + "└─────────────────────────┘\n");
                    	 
                    	 System.out.print(">> ");
                    	 tipoMoeda = sc.nextInt();  
                    }
                    	
            		System.out.printf("┌─────── COFRINHO ────────┐\n"
    								 +"├─────────────────────────┤\n"
    								 +"│     Digite o valor      │\n"
    								 +"└─────────────────────────┘\n");
					System.out.print(">> ");
                    valor = sc.nextDouble();
                    
                    // Tipos de moedas
                    if (tipoMoeda == 1) {
                    	moeda = new Real(valor);                 	
                		System.out.printf("┌─────────────────────────┐\n" 
                						+ "  Adicionado: R$ %.2f %n"
                						+ "└─────────────────────────┘%n", valor);
                    }
                    
                    else if (tipoMoeda == 2) {
                    	moeda = new Dolar(valor);
                    	System.out.printf("┌─────────────────────────┐\n" 
        								+ "  Adicionado: $ %.2f %n"
        								+ "└─────────────────────────┘%n", valor);
                    }
                    
                    else {
                    	moeda = new Euro(valor);
                    	System.out.printf("┌─────────────────────────┐\n" 
        								+ "  Adicionado: € %.2f %n"
        								+ "└─────────────────────────┘%n", valor);
                    }
                    
                    // Adicionar moeda na lista
                    cofrinho.adicionar(moeda);      
                    break;    
                        
      
     
                // 2 - Remover moeda
                case 2:
                	tipoMoeda = 0 ; 
                    while(tipoMoeda <= 0 || tipoMoeda > 3) {
                    	 System.out.printf("┌─────── COFRINHO ────────┐\n"
                			 			 + "│                         │\n"
                			 			 + "│ Escolha o tipo de moeda │\n"
                			 			 + "│ [1] Real                │\n"
                			 			 + "│ [2] Dolar               │\n" 
                			 			 + "│ [3] Euro                │\n"
                			 			 + "└─────────────────────────┘\n");
                    	 
                    	 System.out.print(">> ");
                    	 tipoMoeda = sc.nextInt();  
                    }
                    	
                    System.out.printf("┌─────── COFRINHO ────────┐\n"
                					 +"├─────────────────────────┤\n"
                					 +"│     Digite o valor      │\n"
                					 +"└─────────────────────────┘\n");
                    System.out.print(">> ");
                    valor = sc.nextDouble();
                    
                    // Tipos de moedas
                    if (tipoMoeda == 1) {
                    	moeda = new Real(valor);
                    	System.out.printf("┌─────────────────────────┐\n" 
        								+ "  Removido: R$ %.2f %n"
        								+ "└─────────────────────────┘%n", valor);
            
                    }
                    
                    else if (tipoMoeda == 2) {
                    	moeda = new Dolar(valor);
                    	System.out.printf("┌─────────────────────────┐\n" 
        								+ "  Removido: $ %.2f %n"
        								+ "└─────────────────────────┘%n", valor);
                 
                    }
                    else {
                    	moeda = new Euro(valor);
                    	System.out.printf("┌─────────────────────────┐\n" 
        								+ "  Removido: € %.2f %n"
        								+ "└─────────────────────────┘%n", valor);
                	
                    }
                    
                    // Remover moeda da lista
                    cofrinho.remover(moeda);
                    break;


                // 3 - Mostrar moedas
                case 3:
                	cofrinho.moedasGuardadas();
                    break;

                // 4 - Converter moedas    
                case 4:               
                	cofrinho.totalConvertido();
                    break;

                // Escolha incorreta
                default:
                    System.out.printf("┌─────── COFRINHO ────────┐\n"
                                    + "├─────────────────────────┤\n"
                                    + "│ Digite um valor correto │\n"
                                    + "├─────────────────────────┤\n"
                                    + "│ [1] Adicionar moeda     │\n"
                                    + "│ [2] Remover moeda       │\n"
                                    + "│ [3] Mostrar moedas      │\n" 
                                    + "│ [4] Converter para real │\n"
                                    + "├─────────────────────────┤\n"
                                    + "│ [0] Guardar o cofrinho  │\n"
                                    + "└─────────────────────────┘\n");

                    opcoesMenu = sc.nextInt();
                    break;
            }
            
            System.out.printf("┌─────── COFRINHO ────────┐\n"
            				+ "│                         │\n"
            				+ "│ [1] Adicionar moeda     │\n"
            				+ "│ [2] Remover moeda       │\n"
            				+ "│ [3] Mostrar moedas      │\n" 
            				+ "│ [4] Converter para real │\n"
            				+ "├─────────────────────────┤\n"
            				+ "│ [0] Esconder o cofrinho │\n"
            				+ "└─────────────────────────┘\n");
            System.out.print(">> ");
            opcoesMenu = sc.nextInt();
        }
        
        // 0 - Esconder o cofrinho
        System.out.printf("┌──────────────────────────┐\n"
                        + "│ O cofrinho foi escondido │\n"
                        + "└──────────────────────────┘\n");
		
        sc.close();
	}
}