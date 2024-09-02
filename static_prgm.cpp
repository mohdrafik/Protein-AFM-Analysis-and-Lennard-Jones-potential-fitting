#include <iostream>
using namespace std;
// int count = 1000;  we can do in this way also.

/*  static member has one memory in the particular class.
    life time untill the program is finish.
    visiblity inside the class. here each time I call function setvalue(), using the object, it is increasing for each object.
    static function take only the static value.
    They can be called using the class name without creating an object.
*/

class employee
{
    int id;
    // int count;
    int static count;

public:
    void setvalue(void)
    {
        cout << "enter the id" << endl;
        cin >> id;
        count++;
    }

public:
    void getvalue(void)
    {
        cout << "employee id: " << id << " and count: " << count << endl;
    }

    void static staticfun(void)
    {
        cout<<"count value is :"<<count<<endl;
    }
};


int employee::count = 1000;


int main()
{
    employee ariana, andria, udit;

    ariana.setvalue();
    ariana.getvalue();

    andria.setvalue();
    andria.getvalue();

    udit.setvalue();
    udit.getvalue();

    // cout << "how are you:" << endl;
}
