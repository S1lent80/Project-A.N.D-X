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
#define TRUE 01;
#define FALSE 00;

// ********************************************************************************************************************************************
// Declare Constants, Integers, Chars
int SIZE = 20;
// ->::
// const int names[SIZE] = {};


// Function Prototypes
void banner(std::string, int a);
void write_data(std::string, int a2, int b);
void data_num(int a3, int b2, int c);
void param_get(std::string, char, int a, int b, std::fstream, std::fstream, std::fstream);


// Functions
void banner(std::string author, int a) 
{
	std::cout << "=========[ Data Log  -  By: " << author << "  -  Log: " << a << " ]==============================================================================\n" << endl;
	// I couldn't help myself with this loop
	for (int i = 0; i < a; i++) 
	{
		fstream data_log;
		data_log.open("log_data.txt", ios::app);
		data_log << "LOG_DATA_ACCESS: " << a << "\n" << endl; 
	}
}

// Check if the file exists
bool file_exists(const char *filename) 
{
	std::ifstream in_file(filename);
	return (bool)in_file;
}

// This function might not work yet...
void write_data(std::string data, int a2, int b) 
{
	// Write data in Programming Language: Scorpion
	fstream data2;
	data2.open("data2.txt", ios::app);
	if (data.length() == 0 || data == "NULL") 
	{
		for (b == a2; b < SIZE; b++) 
		{
			data2 << data << b << endl;
		}
	}
	else if (data == "write_data") 
	{
		// Empty for now
	}
	else 
	{
		for (b == a2; b < SIZE || b < 30; b++) 
		{
			data2 << data << b << endl;
		}
	}

}

void data_num(int a3, int b2, int c) 
{
	// Need to enter data in a combination
	if (a3 == '1' && b2 != '1' && c == '0') 
	{
		if (a3 != '1' || a3 > 1 && b2 == '1' && c == '1') 
		{
			std::cout << "Position [1] in function: { data_num(" << a3 << b2 << c << ") } is out of bounds, must be less then 2 or 1 or 0" << endl;
			std::cout << "                                           ^" << endl;
			if (a3 < 2 || a3 == 1 || a3 == 0 && b2 > 1 && c < 1) 
			{
				std::cout << "Position [2] in function: { data_num(" << a3 << b2 << c << ") } is out bounds, must be less then 2 or 1 or 0" << endl;
				std::cout << "                                                 ^" << endl;
				if (a3 < 2 || a3 == 1 || a3 == 0 && b2 < 2 || b2 == 1 || b2 == 0 && c > 1 || c != 0 || c != 1) 
				{
					std::cout << "Position [3] in function: { data_num(" << a3 << b2 << c << ") } is out of bounds, must be less then 2 or 1 or 0" << endl;
					std::cout << "                                                      ^" << endl;
				}
				else 
				{
					// Empty for now
				}  
			}
			else 
			{
				// Empty for now
			} 
		}
		else 
		{
			// Empty for now
		}
	}
	else 
	{
		// Empty for now
	}
}

void param_get(std::string param, char assign_char, int a, int b) 
{
	// The parameter will be the string folowed by a assigning character, followed by integer[0-1] and another integer[0-20]
	while (param.length() == 0 || param.length() > 5) 
	{
		// This will be altered
		std::cout << "The paramter is too short must be greater than 5 characters..." << endl;
		break;
	}
	// Charaters
	if (assign_char == 'A' || assign_char == 'B') 
	{
		for (a == 0; a < SIZE + 2 || a < 18; a++) 
		{
			// Empty for now
		}
		// Mainly the user will not know about this function...Why? Well it was not in the description...I wrote this function for myself but others can use it withing this script...
		// char_data << "X.CHAR[$1:'1']._input_value_.char = " << assign_char << " -> x.class(CALL='c++'.'cpp' >> $char([$] -> assign_char));" << endl;
		data_num(0, 0, 1);
	}
	else if (assign_char == 'C' || assign_char == 'D')
	{
		for (a == 0; a < SIZE + 2 || a < 18; a--)
		{
			// Empty for now
		}
		// char_data << "X.CHAR[$1:'1:2']._input_value_.char = " << assign_char << " -> call_action('-')" << endl;
		data_num(0, 1, 0);
	}
	else
	{
		// char_data << "X.CHAR[$@:'@$']._input_value_.char = " << assign_char << " -> x.main($func.call['main']);" << endl;
		data_num(1, 0, 0);
	}
	// String
	if (param.length() < 1 || param.length() < 10) 
	{
		if (param.length() == 0)
		{
			// param_data << "X.STRING[$@] -> call_action($string_get.input() -> true)._value_.char[$] = 0" << endl;
			data_num(0, 0, 0);
		}
		else
		{
			// param_data << "X.STRING[$@] -> call_action($string_get.input() -> true)._value_.char[$] = " << param << endl;
		}
		// param_data << "X.STRING[$@] -> call_action($string_get.input(" << param << ") -> true)._value_.char.length(" << param.length() << ")" << endl;
	}
	// Integers
	if (a == '2' && b == '4')
	{
		if (a == '1')
		{
			// int_data << "X.INT([$]:int)._bool_value_.value = true" << endl;
		}
		else
		{
			// int_data << "X.INT([$]:int)._bool_value_.value = false" << endl;
		}
		/// int_data << "X.INT([$]:int)._value_.length = 0" << endl;
		data_num(0, 0, 0);
	}
	if (b == '0') 
	{
		if (b < 1) 
		{
			// int_data << "X.INT([$]:int)._int_value_.value = " << b << endl;
		}
		else
		{
			// Empty
		}
		// int_data << "X.INT([$]:int)._int_bool_value_.value = false" << endl;
	}
	else
	{
		// Empty
	}
}

// Structures



// **********************************************************************************************************************************************

int main() {
	// Internal definitions
	std::string firstname;			// Firstname = String
	std::string lastname;			// Lastname = String
	std::string test_full_name;		// Test Name (Full) = String
	int SIZE_2 = SIZE + 2;			// The number of charaters to hold
	int a, b, c;					// For the function data_num()
	// -> Files
	std::fstream userdata;
	std::fstream data_conf;
	std::fstream param_data;
	std::fstream char_data;
	std::fstream int_data;
	param_data.open("data/param_data.txt", ios::app);
	char_data.open("data/char_data.txt", ios::app);
	int_data.open("data/int_data.txt", ios::app);
	userdata.open("user_data.txt", ios::app);
	data_conf.open("conf/data_conf.txt", ios::app);
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
	if (firstname == "S1lent" || firstname == "Gleb") 
	{
		// Length = [STRING_VARIABLE].length()
		// Start = [STRING_VARIABLE].find()
		if (firstname.find("Bair") == 0) 
		{
			for (int i = 0; i < 1000; i++) 
			{
				userdata << "Creator lastname  -  Program Accessed  -  " << i << endl;
				data_conf << "X.STRING._char_.$val[$] = ${CALL=$['c++'.'cpp' >> '`firstname.find($val='lastname')`']}" << endl;
				data_num(1, 1, 0);
				param_get("Creator firstname", 'A', 1, 1);
			}
		}
		userdata << "Creator firstname: " << firstname << "  -  Program Accessed" << endl;
		data_conf << "X.STRING._char_.$val[$] = ${CALL=$['c++'.'cpp' >> ${var} << $@ >> 'else {$val='creator_firstname'}']}" << endl;
		data_num(1, 0, 0);
	}
	else 
	{
		userdata << "User firstname: " << firstname << "  -  Program Accessed" << endl;
		data_conf << "X.STRING._char_.$val[$] = ${CALL=$['c++'.'cpp'::regular_user >> ${var} << $@ >> 'else {$val='firstname'}']}" << endl;
		data_num(1, 0, 0);
	}
	// SPACE:TAB
	std::cout << "" << endl;
	// Ask the user for his/her lastname
	std::cout << "What is your last name: ";
	std::getline(cin, lastname);
	if (lastname.find("core") == true || lastname.find("Core") == true) 
	{
		// Empty for now
		if (lastname == "Bair" || lastname == "bair") 
		{
			// Call, write_data function here
			write_data("X.IDENT._Xval_.userLastName($) = !$", 1, 1);
			data_num(1, 1, 0);
		}
	}
	else 
	{
		userdata << "User lastname: " << lastname << "  -  Main Program Accessed" << endl;
	}
	// SPACE:TAB
	// Ask the user of the full test name
	std::cout << "\nPlease enter the full name of the test: ";
	std::getline(cin, test_full_name);
	while (test_full_name.length() == 0 || test_full_name == "help") 
	{
		std::cout << "\n-> Please enter the name of the Pentest: ";
		std::getline(cin, test_full_name);
	}
	userdata << "Full Name of Test: " << test_full_name << "  -  $NAME_LENGTH = " << test_full_name.length() << endl;
	// Continue to write to files

	// ********************************************************************************************************************************
	std::cout << "" << endl;
	/*
	** std::cout << "Please enter the code sequence (as a test for the function data_num): ";
	** cin >> a >> b >> c;
	** // This loop isn't working, I need to look into it...
	** while (a == '2' && b == '2' && c == '2') {
	** 	std::cout << "\nPlease enter 3 numbers all less than 2..." << "\n" << endl;
	**	cin >> a >> b >> c;
	** }
	** data_num(a, b, c);
	*/
	// ********************************************************************************************************************************
	// Call function param_get()
	
}