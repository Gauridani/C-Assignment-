
#include <iostream>
using namespace std;
int main() {
// Variable declaration and initialization
string bookTitle = "The God of Small Things"; // String variable for
the book title
string author = "Arundhati Roy"; // String variable for
the author's name
int yearOfPublication = 1997; // Integer
variable for the year of publication
double price = 499.99; // Double
variable for the price in Rupees
bool isAvailable = true; // Boolean
variable for availability
// Display the book information
cout << "Book Title: " << bookTitle << endl;
cout << "Author: " << author << endl;
cout << "Year of Publication: " << yearOfPublication << endl;
cout << "Price: " << price << " Rs." << endl;
cout << "Availability: " << (isAvailable ? "Yes" : "No") << endl;

    return 0;
}