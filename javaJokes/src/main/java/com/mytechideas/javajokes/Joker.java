package com.mytechideas.javajokes;

import java.util.Random;

public class Joker {
    public static String[] jokes={ "Q: Which dog breed is guaranteed to laugh at all of your jokes?\n" +
            "\n" +
            "A: A Chi-ha-ha!\n" +
            "\n", "Why do we tell actors to break a leg?\nBecause every play has a cast.","Did you hear about the claustrophobic astronaut?\nHe just needed a little space."};

    public String getJoke(){
        int index=new Random().nextInt(jokes.length);
        return jokes[index];
    }
}
