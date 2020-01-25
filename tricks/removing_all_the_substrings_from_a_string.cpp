#include<bits/stdc++.h>
using namespace std;

/* Erase First Occurrence of given  substring from main string.
 */
void eraseSubStr(string & mainStr, const string & toErase)
{
	// Search for the substring in string
	size_t pos = mainStr.find(toErase);
 
	if (pos != string::npos)
	{
		// If found then erase it from string
		mainStr.erase(pos, toErase.length());
	}
}
 
/*
 * Erase all Occurrences of given substring from main string.
 */
void eraseAllSubStr(string & mainStr, const string & toErase)
{
	size_t pos = string::npos;
 
	// Search for the substring in string in a loop untill nothing is found
	while ((pos  = mainStr.find(toErase) )!= string::npos)
	{
		// If found then erase it from string
		mainStr.erase(pos, toErase.length());
	}
}
 
/*
 * Erase all Occurrences of all given substrings from main string using C++11 stuff
 */
void eraseSubStrings(std::string & mainStr, const std::vector<std::string> & strList)
{
	// Iterate over the given list of substrings. For each substring call eraseAllSubStr() to
	// remove its all occurrences from main string.
	std::for_each(strList.begin(), strList.end(), std::bind(eraseAllSubStr, std::ref(mainStr), std::placeholders::_1));
}
 
/*
 * Erase all Occurrences of all given substrings from main string using Pre C++11 stuff
 */
void eraseSubStringsPre(std::string & mainStr, const std::vector<std::string> & strList)
{
	// Iterate over the given list of substrings. For each substring call eraseAllSubStr() to
	// remove its all occurrences from main string.
	for (std::vector<std::string>::const_iterator it = strList.begin(); it != strList.end(); it++)
	{
		eraseAllSubStr(mainStr, *it);
	}
 
}
 
int main()
{
	std::string str = "Hi this is a sample string is for is testing is.";
 
	eraseAllSubStr(str, "this");
 
	std::cout << str << std::endl;
 
	eraseSubStringsPre(str, { "for", "is", "testing" });
 
	std::cout << str << std::endl;
	return 0;
}

