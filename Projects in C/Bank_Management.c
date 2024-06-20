#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

const char* ACCOUNT_NAME="E:\\C\\Projects\\account.dat";

typedef struct{
  char name[50];
  long int acc_no;
  float balance;
}Account;

void create_account(){
  Account acc;
  FILE *file=fopen(ACCOUNT_NAME,"ab+");
  if(file==NULL){
    printf("Unable to open Account!!\n");
    return;
  }
  char c;
  do{
    c=getchar();
  }while(c!='\n' && c!=EOF);

  printf("Enter the name:");
  fgets(acc.name,sizeof(acc.name),stdin);
  int idx=strcspn(acc.name,"\n");
  acc.name[idx]='\0';

  //Account Number Creation
  srand(time(NULL));
  int num;
  float bal;
  while(!(num>1000 && num<9999)){
    num=rand()%10000+1;
  }
  acc.acc_no=num;

  printf("Enter the opening amount balance:");
  scanf("%f",&bal);
  acc.balance=bal;

  fwrite(&acc,sizeof(acc),1,file);
  fclose(file);
  
  printf("Account created Successfully!!\n");
  printf("Your account number is: %ld\n",acc.acc_no);
  printf("Rember Account number for Future Preference!!\n");
}
void deposit_money(){
  int acc_no;
  Account acc_read;
  FILE *file=fopen(ACCOUNT_NAME,"rb+");
  if(file==NULL){
    printf("Unable to Deposit Money!!\n");
    return;
  }

  float money;
  printf("Enter your account number:");
  scanf("%d",&acc_no);
  printf("Enter the amount to be deposited:");
  scanf("%f",&money);

  while(fread(&acc_read,sizeof(acc_read),1,file)!=EOF){
    if(acc_read.acc_no==acc_no){
      acc_read.balance+=money;
      fseek(file,-sizeof(acc_read),SEEK_CUR);
      fwrite(&acc_read,sizeof(acc_read),1,file);
      fclose(file);
      printf("Successfully deposited Rs. %.2f!!\n",money);
      printf("Total Balanace: Rs. %.2f\n",acc_read.balance); 
      return;
    }
  }
  fclose(file);
  printf("Account not found!!\n");
}
void withdraw_money(){
  int acc_no;
  Account acc_read;
  FILE *file=fopen(ACCOUNT_NAME,"rb+");
  if(file==NULL){
    printf("Unable to Withdraw Money!!\n");
    return;
  }

  float money;
  printf("Enter your account number:");
  scanf("%d",&acc_no);
  printf("Enter the amount to be withdrawn:");
  scanf("%f",&money);

  while(fread(&acc_read,sizeof(acc_read),1,file)!=EOF){
    if(acc_read.acc_no==acc_no){
      if(acc_read.balance>=money && money>0){
        acc_read.balance-=money;
        fseek(file,-sizeof(acc_read),SEEK_CUR);
        fwrite(&acc_read,sizeof(acc_read),1,file);
        fclose(file);
        printf("Amount Withdrawn Successfully!!\n");
        printf("Remaining Balanace: Rs. %.2f\n",acc_read.balance); 
        return;
      }
      else{
        printf("Insufficient Balanace!!\n");
        return;
      }
    }
  }
  fclose(file);
  printf("Account not found!!\n");
}
void check_balance(){
  int acc_no;
  Account acc_read;
  FILE *file=fopen(ACCOUNT_NAME,"rb");
  if(file==NULL){
    printf("Unable to Check Balance!!\n");
    return;
  }
  printf("Enter your account number:");
  scanf("%d",&acc_no);

  while(fread(&acc_read,sizeof(acc_read),1,file)){
    if(acc_read.acc_no==acc_no){
      printf("You current balance is Rs. %.2f\n",acc_read.balance);
      fclose(file);
      return;
    }
  }
  fclose(file);
  printf("Account not found!!\n");
}
int main(){
  do{
    printf("\n\n*** BANK MANAGEMENT SYSTEM ***\n");
    printf("Press 1 - To Create Account\n");
    printf("Press 2 - To Deposit Money\n");
    printf("Press 3 - To Withdraw Money\n");
    printf("Press 4 - To Check Balance\n");
    printf("Press 5 - To Exit\n");
    int ch;
    printf("\nEnter your choice:");
    scanf("%d",&ch);
    switch(ch){
      case 1:
        create_account();
        break;
      case 2:
        deposit_money();
        break;
      case 3:
        withdraw_money();
        break;
      case 4:
        check_balance();
        break;
      case 5:
        printf("Thanks for Visiting!!\n");
        return 0;
        break;
      default:
        printf("Invalid choice!!\n");
        break;
    }

  }while(1);
}