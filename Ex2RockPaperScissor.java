import java.util.Random;
import java.util.Scanner;

public class Ex2RockPaperScissor {
    public static void main(String[] args) {
        //0 for Rock
        //1 for Paper
        //2 for Scissor
        System.out.println("Enter 0 for Rock , 1 for Paper and 2 for Scissor");
        int userInput;
        int computerInput;
        Scanner sc = new Scanner(System.in);
        userInput=sc.nextInt();

        Random r=new Random();
        computerInput = r.nextInt(3);

        if(userInput==computerInput){
            System.out.println("The match is Draw");
        }
        else if (userInput==0 && computerInput==2 && userInput==1 && computerInput==0 && userInput==2 && computerInput==1) {
            System.out.println("You win");
        }
        else{
            System.out.println("Computer win");
        }
            if(computerInput==0) {
                System.out.println("Computer Choice:Rock");
            }
            else if (computerInput==1){
                    System.out.println("Computer Choice:Paper");
                }

            else{
                    System.out.println("Computer Choice:Scissor");
        }
    }
}
