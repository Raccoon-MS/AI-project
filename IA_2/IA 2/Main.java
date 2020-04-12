package com.company;

import java.io.*;
public class Main {

    public static void main(String[] args) {

        // I N I T I A L I S A T I O N  D U  R E S E A U
        RN RN = new RN(2,2,1,0.9);

        // On attribut des poids aléatoires à chaque liaison entre les noeuds
        RN.poidsIH.initialisation();
        RN.poidsHO.initialisation();

        // On attribut des biais aléatoires à chaque liaison entre les noeuds
        RN.biaisH.initialisation();
        RN.biaisO.initialisation();

        // On defini une matrice [1][1] pour le noud d'entrée
        RN.Entre = new Matrice(RN.Nentre,1);

        // V A L E U R S  D ' E N T R E E
        double Result = 0.9; // VALEUR ATTENDU
        double x = 0.8;     // Entre 1
        double y = 0.7;     // Entre 2

        // On met les deux entrées dans un tableau afin de les transmettre à la matrice d'entrée
        double[] data = {x,y};

        // On entre les valeurs dans la matrice d'entrée
        RN.Entre.Inputdata(data);
        // On multiplie les valeurs obtenue par leur poids et on y applique la fonction sigmoide sur la matrice d'éntrée
        RN.Temp = RN.multiplication(RN.poidsIH, RN.sigmoid(RN.Entre));
        // On y ajoute le biais de chaque liaison
        RN.Temp = RN.addition(RN.Temp, RN.biaisH);
        // On y applique la fonction sigmoid sur les matrices des noeuds intermediaires
        RN.Temp = RN.sigmoid(RN.Temp);
        // On multiplie les valeurs obtenue par le biais des liaisons
        RN.Sorti = RN.multiplication(RN.poidsHO, RN.Temp);
        //On ajoute le biais de chaque liaison sur la matrice de sortie
        RN.Sorti = RN.addition(RN.Sorti, RN.biaisH);
        // On y applique la fonction sigmoid sur la matrice de sortie
        RN.Sorti = RN.sigmoid(RN.Sorti);

        RN.Retropropagation(RN.Sorti.m[0][0], Result, RN.sigmoid(RN.Entre));


        // A F F I C H A G E  D E S  R E S U L T A T S
        System.out.println("Valeur attendue : " + Result);
        System.out.println("Valeur trouvée : " + RN.Sorti.m[0][0] );
        System.out.println("Fonction d'erreur : " + 0.5*Math.pow(Math.abs(RN.Sorti.m[0][0] - (x+y)),2) );
        System.out.println("Pourcentage d'erreur : " + (int)((100 * Math.abs(RN.Sorti.m[0][0] - Result ))/Result) + "%");

    }
}
