#include <iostream>
#include <string>
using namespace std;

class Stack {

    public:
        int* arr;
        int size = 0; 
        int capacity = 1;

        // Constructor
        Stack(){
            arr = new int[capacity];    
        }

        // Destructor
        ~Stack(){
            delete arr;
        }

        void push(int value){
            // Head of stack is the size of the array
            arr[size] = value;
            size++;
        }
        
        int pop(){
            size--;
            return arr[size];
        }

        int peek(){
            return arr[size-1];
        }

        bool isEmpty(){
            if(size == 0)
                return true;
            else
                return false;        
        }

        void display(){

            for(int i = 0; i < size; i++){
                std::cout<< arr[i] << " -> ";
            }
            std::cout<<endl;

        }

};

bool isValid(string str){

    // enum open { a = '(', b = '[', c = '{' };
    // enum closed { a = ')', b = ']', c = '}' };
    Stack check_stack;
    int popped = 0;

    for (int i = 0; i < str.length(); i++){

        if (str[i] == '(' || str[i] == '[' || str[i] == '{')
            check_stack.push(str[i]);
        else{
            popped = check_stack.pop();
        }    
        
        check_stack.display();

    }

    return false;
}

main(){

    string s = "([(]{)})";
    

}