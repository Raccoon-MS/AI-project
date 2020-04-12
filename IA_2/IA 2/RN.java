package com.company;

import java.lang.Math;

public class RN{
    int Nentre;
    int Ntemp;
    int Nsort;
    Matrice Temp;
    Matrice Entre;
    Matrice Sorti;
    Matrice poidsHO;
    Matrice poidsIH;
    Matrice biaisH;
    Matrice biaisO;
    double Objectif;

    // C O N S T R U C T E U R
    RN(int NombreEntre,int NombreTemp, int NombreSort,double Result){
        this.Nentre = NombreEntre;
        this.Ntemp = NombreTemp;
        this.Nsort = NombreSort;
        this.poidsIH = new Matrice(NombreTemp,NombreEntre);
        this.poidsHO = new Matrice(NombreSort,NombreTemp);
        this.biaisH = new Matrice(NombreTemp,1);
        this.biaisO = new Matrice(NombreSort,1);
        this.Objectif = Result;

    }
    public double[] ColtoRow(Matrice tab,int col){
        double m[] = new double[tab.lignes];
        for(int i=0;i<tab.lignes;i++){
            m[i] = tab.m[i][col];
        }
        return m;
    }

    // M U L T I P L I C A T I O N   L I G N E  x  C O L O N N E
    public double rowxcol(double[] A, double[] B){
        double result=0;
        if(A.length>=B.length){
            for(int i=0;i<A.length;i++){
                result+=A[i]*B[i];
            }
        }
        else{
            for(int i=0;i<B.length;i++){
                result+=A[i]*B[i];
            }
        }
        return result;
    }

    // C O N C A T E N A T I O N
    public Matrice ResultMatrice(Matrice Left,Matrice Right){
        return new Matrice(Left.lignes,Right.colonnes);
    }

    public Matrice multiplication(Matrice A,Matrice B){
        Matrice result = ResultMatrice(A,B);
        for(int i=0;i<result.colonnes;i++){
            for(int j=0;j<result.lignes;j++){
                result.m[j][i] = rowxcol(A.m[i],ColtoRow(B,i));
            }
        }
        return result;
    }
    public Matrice addition(Matrice A,Matrice B){
        Matrice r = new Matrice(A.lignes,A.colonnes);
        for(int i=0;i<r.lignes;i++){
            for(int j=0;j<r.colonnes;j++){
                r.m[i][j] = A.m[i][j] + B.m[i][j];
            }
        }
        return r;
    }
    public Matrice sigmoid(Matrice A){
        for(int i=0;i<A.lignes;i++){
            for(int j=0;j<A.colonnes;j++){
                A.m[i][j] = (1/( 1 + Math.pow(Math.E,(-1*A.m[i][j]))));
            }
        }
        return A;
    }
    public void Retropropagation(double Sorti,double answer,Matrice Entre){
      for(int i=0; i<this.poidsHO.lignes ;i++){
              for(int j=0; j<this.poidsHO.colonnes ;j++){
                  double delta = (-1*(answer-Sorti)) * (Sorti *(1-Sorti)) * (this.Temp.m[j][0]);
                  this.poidsHO.m[i][j] -= delta * this.Objectif;
              }
          }
      for(int i=0; i<this.poidsIH.lignes ;i++){
              for(int j=0; j<this.poidsIH.colonnes ;j++){
                  double delta = (-1*(answer-Sorti)) * (Sorti *(1-Sorti)) * (this.Temp.m[j][0]) * (this.Temp.m[j][0] *(1-this.Temp.m[j][0])) * Entre.m[i][0];
                  this.poidsIH.m[i][j] -= delta * this.Objectif;
              }
          }
    }
    
}
