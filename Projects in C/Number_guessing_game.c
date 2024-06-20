#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
  int random,guess;
  int num_guess=10;
  srand(time(NULL));
  printf("********************************************\n");
  printf("\tWelcome to the world of Guess\n");
  printf("\t  ****Guess the Number****\n");
  printf("********************************************\n\n");
  printf("Rules for the game\n");
  printf("1. You have to Guess a number according to the level.\n");
  printf("2. You have total 50 points to Guess the number.\n");
  printf("3. Each wrong Guess will deduct 5 points from total points.\n");
  printf("4. Guess the Right number as soon as possible.\n\n");

  printf("Press 1 - For Easy Level(Guess between 1 to 100)\n");
  printf("Press 2 - For Intermediate Level(Guess between 1 to 300)\n");
  printf("Press 3 - For Hard Level(Guess between 1 to 500)\n\n");
  int level;
  printf("Enter the level:");
  scanf("%d",&level);
  printf("Game Starts now............\n");
  printf("All the Best!!\n\n");
  if(level==1)
    random=rand()%100+1;
  else if(level==2)
    random=rand()%300+1;
  else 
    random=rand()%500+1;
  do{
    printf("\nPlease enter the guess number:");
    scanf("%d",&guess);
    if(guess<random){
      num_guess--;
      printf("Only %d points left!!\n",5*num_guess);
      printf("Guess larger number!!\n");
    }
    else if(guess>random){
      num_guess--;
      printf("Only %d points left!!\n",5*num_guess);
      printf("Guess smaller number!!\n");
    }
    else{
      if(num_guess==10){
        printf("Yay!! You guessed in First Attempt:)\n");
        printf("Total Score: %d\n\n",5*num_guess);
        break;
      }
      else{
        printf("Congratulations!! You guessed the right Number:)\n\n");
        printf("Total Score: %d\n",5*num_guess);
        printf("Numbers of attempts: %d\n\n",10-num_guess);
        break;
      }
    }
  }while(num_guess!=0);
  if(num_guess==0){
    printf("Sorry!! No more attempts Left :(\n");
    printf("The number was: %d\n",random);
    printf("Better Luck Next Time..........\n\n");
  }
  printf("Thanks for Playing\n");
  printf("Visit Us Again\n");
  printf("Develped by: @LuckyVerma");
  return 0;
}