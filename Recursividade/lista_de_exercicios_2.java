/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.copadesoftware;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author barba
 */
public class CopaDeSoftware {
    
    public static int questaoDois(int N){
        if (N >= 0){
            return (N * N * N) + questaoDois(N-1);
        }
        return 0;
    }
    

    public static int questaoTres(int N){
        if (N == 1){
            return 0;
        }
        else if (N == 2){
            return 1;
        }
        else{
            return questaoTres(N-1)+ questaoTres(N-2);
        }
    }
    
    public static int[] questaoSete(int N[]){
        if (N.length > 1){
            if (N[0] < N[N.length - 1]){
                int[] novoArray = Arrays.copyOf(N, N.length -1);
                return questaoSete(novoArray);
            }
            else{
                int[] novoArray = Arrays.copyOfRange(N, 1, N.length);
                return questaoSete(novoArray);
            }
        }
         else{
            return N;
        }
    }
    
    public static int questaoOito (int N){
        if (N > 0){
            int termo = (1+(N*N))/N;
            return termo + questaoOito(N-1);
        }
        return 0;
    }
    
    public static int questaoOnze (int N){
        if (N == 1){
            return 1;
        }
        else if (N == 2){
            return 2;
        }
        else{
            return (2 * questaoOnze(N -1)) + (3 * questaoOnze(N-2));
        }
    }
    
    public static int questaoDoze (int N){
        if (N == 0){
            return 1;
        }
        else if (N == 1){
            return 1;
        }
        else if (N == 2){
            return 1;
        }
        else{
            return questaoDoze(N-2) + questaoDoze(N-3);
        }
        
    }
    
    public static int questaoTreze (int N){
        if (N == 0){
            return 0;
        }
        else if (N == 1){
            return 1;
        }
        else{
            return 2*questaoTreze(N -1) + questaoTreze(N - 2);
        }
    }
    
    
    public static String questaoCatorze(int N){
        if (N == 0){
            return "0";
        }
        else if (N == 1){
            return "1";
        } else{
            int dividendo = N / 2;
            int resto = N % 2;
            return questaoCatorze(dividendo) + Integer.toString(resto);
        }
    }

    public static void main(String[] args) {
        int vetor[] = {4,2,2,7};
            System.out.println(questaoCatorze(119));
    }
}
