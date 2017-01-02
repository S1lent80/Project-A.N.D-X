/*
* Data Log  -  C++  -  Version: 1.0.0
*
* By: S1lent
*/

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <string>
using namespace std;
#define TRUE 1;
#define FALSE 0;

// Declare Constants, Integers, Chars
int SIZE = 20;
// ->::
// const int names[SIZE] = {};


// Function Prototypes
void banner(std::string, int a);


// Functions
void banner(std::string author, int a) {
	std::cout << "=========[ Data Log  -  By: " << author << "  -  Log: " << a << " ]==============================================================================\n" << endl;
	// I couldn't help myself with this loop
	for (int i = 0; i < a; i++) {
		fstream data_log;
		data_log.open("log_data.txt", ios::app);
		data_log << "LOG_DATA_ACCESS: " << a << "\n" << endl; 
	}
}

// Check if the file exists
bool file_exists(const char *filename) {
	std::ifstream in_file(filename);
	return (bool)in_file;
}

// Structures



int main() {
	// Internal definitions
	std::string firstname;			// Firstname = String
	std::string lastname;			// Lastname = String
	int SIZE_2 = SIZE + 2;			// The number of charaters to hold
	// -> Files
	std::fstream userdata;
	userdata.open("user_data.txt", ios::app);
	// ***************************************************************************************************************************************
	// Write the following to the log_data.txt and user_data.txt
	// =========================================================
	file_exists("log_data.txt");
	userdata << "===========[ Data Log  -  User Data ]==========================================================\n" << endl;
	// ***************************************************************************************************************************************

	// Clear the Terminal
	system("clear");
	// Call the banner() function
	banner("S1lent", 1);

	// Ask the user for his/her firstname
	std::cout << "What is your firstname: ";
	std::getline(cin, firstname);
	// What if it is the program creators name, log it
	if (firstname == "S1lent" || firstname == "Gleb") {
		// Length = [STRING_VARIABLE].length()
		// Start = [STRING_VARIABLE].find()
		if (firstname.find("Bair") == 0) {
			for (int i = 0; i < 1000; i++) {
				userdata << "Creator lastname  -  Program Accessed  -  " << i << endl;
			}
		}
		userdata << "Creator firstname: " << firstname << "  -  Program Accessed" << endl;
	}
	else {
		userdata << "User firstname: " << firstname << "  -  Program Accessed" << endl;
	}
	// SPACE:TAB
	std::cout << "" << endl;
	// Ask the user for his/her lastname
	
}