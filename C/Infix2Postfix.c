

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define Lim 100

char stack[Lim];
char infix[Lim], postfix[Lim];
int end = -1;

void push(char); 
char pop();      
int isEmpty();   
void inToPost(); 
int space(char);
void print();         
int precedence(char); 



void inToPost()
{
    int i, j = 0;
    char symbol, next;
    for (i = 0; i < strlen(infix); i++)
    {                      
        symbol = infix[i]; 

        if (!space(symbol)) 
        {
            switch (symbol)
            {
            case '(':
                push(symbol);
                break;

            case ')':                         
                while ((next = pop()) != '(') 
                    postfix[j++] = next;
                break;

            case '^':
            case '/':
            case '*':
            case '+':
            case '-':
                while (!isEmpty() && precedence(stack[end]) >= precedence(symbol))
                    
                    postfix[j++] = pop();
                push(symbol);
                break;

            default: 
                postfix[j++] = symbol;
            }
        }
    }

    while (!isEmpty()) 
        postfix[j++] = pop();
    postfix[j++] = '\0';
}

int space(char c)
{
    if (c == ' ' || c == '\t') 
        return 1;
    else
        return 0;
}

int precedence(char symbol)
{
    switch (symbol)
    {
    case '^':
        return 3;
    case '/':
    case '*':
        return 2;
    case '+':
    case '-':
        return 1;
    default:
        return 0;
    }
}

void print()
{
    int i = 0;
    printf("Equivalent postfix expression is: ");
    while (postfix[i])
    {
        printf("%c", postfix[i++]); 
    }
    printf("\n");
}

void push(char c)
{
    if (end == Lim - 1)
    {
        printf("Stack Overflow."); 
        return;
    }
    end++; 
    stack[end] = c;
}

char pop()
{
    char c;
    if (end == -1)
    {
        printf("Stack Underflow.\n");
        exit(1);
    }
    c = stack[end];
    end = end - 1;
    return c;
}

int isEmpty()
{
    if (end == -1)
        return 1;
    else
        return 0;
}
int main()
{

    printf("Enter  Infix expression: "); 
    gets(infix);

    inToPost();
    print();

    return 0;
}
