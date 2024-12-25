#include<stdio.h>
void p1(int n){
    for(int i=0;i<n;i++){
        for(int j=-1;j<i;j++)
        printf("* ");
        printf("\n");
    }
    printf("\n");
}
void p2(int n){
    for(int i=0;i<n;i++){
        for(int j=1;j<=n-i;j++)
        printf("%d ",j);
        printf("\n");
    }
    printf("\n");
}
void p3(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++)
        printf(" ");
        for(int j=-1;j<i;j++)
        printf("* ");
        printf("\n");
    }
    printf("\n");
}
void p4(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<i;j++)
        printf(" ");
        for(int j=1;j<=n-i;j++)
        printf("%d ",j);
        printf("\n");
    }
    printf("\n");
}
void p5(){
    for(int i=0;i<4;i++){
        for(int j=0;j<i;j++)
        printf(" ");
        for(int j=1;j<=4-i;j++)
        printf(i==0?"# ":i==1?"* ":i==2?"@ ":"$");
        printf("\n");
    }
    printf("\n");
}
void main(){
    p1(3);
    p2(3);
    p3(3);
    p4(4);
    p5();
}