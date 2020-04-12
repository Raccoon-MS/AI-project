package com.company;

public class Matrice{
    int colonnes; // nombre de colonnes
    int lignes;   // nombre de lignes
    double m[][]; // matrice de double

    // C O N S T R U C T E U R
    Matrice(int lignes,int colonnes){
        this.colonnes=colonnes;
        this.lignes=lignes;
        this.m = new double[lignes][colonnes];
    }

    // REMPLISSAGE EN LIGNE DE LA MATRICE
    public void Inputdata(double[] data){
        for(int i=0;i<this.lignes;i++){
            this.m[i][0] = data[i];
        }
    }

    // NORMALISATION DE LA MATRICE
    public void initialisation(){
        for(int i=0;i<this.lignes;i++){
            for(int j=0;j<this.colonnes;j++){
                this.m[i][j] = -1 + (Math.random() * (1 - (-1)));
            }
        }
    }

    // AFFICHAGE DE LA MATRICE
    public void Aff(){
        for(int i=0;i<this.lignes;i++){
            for(int j=0;j<this.colonnes;j++){
                System.out.println(this.m[i][j]);
            }
        }
    }
}
