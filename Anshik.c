#include <stdio.h> // mandatory include

int birt(int XX, int YY, int ZZZZ, int AA, int BB, int CCCC){   // function you have to implement
    int c=0,x,y,s,t[]={3,0,3,2,3,2,3,3,2,3,2,3};
    // sample variable - you can change this according to your need
    if(YY>BB or (YY==BB and XX>AA)){
        CCCC+=1;}
    s=0;
    if(BB<YY){
        x=BB+12;}
    else{
        x=BB;}
    for(i=ZZZZ+1;i<CCCC;i++){
        y=s;
        for(j=YY;j<x;j++){
            y=y+t[j%12];
            if(YY<2){
                if((ZZZZ-1)%4==0){
                    y+=1;
                    s+=2;}
                else{
                    s=s+1;}
            }
            else{
                if(ZZZZ%4==0){
                    y+=1;
                    s+=2;}
                else{
                    s+=1;}
            if ((XX==29) && (YY==02) && (i%4==0)){
                y+=1;}
            if(y%7==2){
                c+=1;}
                }
            }
    //printf("%d-%d-%d and %d-%d-%d \n",XX, YY, ZZZZ, AA, BB, CCCC);
    return c;                 // return statment
}

int main()                       // mandatory main function
{
    int XX, YY, ZZZZ, AA, BB, CCCC;             // variable 
    scanf("%d", &XX);           // input of Date of birth
    scanf("%d", &YY);            // input of Month of birth
    scanf("%d", &ZZZZ);           // input of Year of birth
    scanf("%d", &AA);           // input of Date of death
    scanf("%d", &BB);            // input of Month of death
    scanf("%d", &CCCC);            // input of Year of death
    //printf("%d-%d-%d and %d-%d-%d \n",XX, YY, ZZZZ, AA, BB, CCCC);
    int result = birt(XX, YY, ZZZZ, AA, BB, CCCC);  // calling function
    printf("%d",result);               // printing result
    return 0;                   // return statment
}
