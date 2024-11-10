//str_builder.cpp

#include <iostream>
#include <fstream>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>

#include "arg_checks.h"

using namespace std;



/*	ARGUMENT 1 : FILEPATH TO CONTENT.TXT
 *	ARGUMENT 2 : MAX NUMBER OF WORDS PER SUBTITLE
 *	ARGUMENT 3 : MAX NUMBER OF CHARS PER SUBTITLE
 *	ARGUMENT 4 : NUMBER OF SECONDS TO READ FOR
 *	ARGUMENT 5 : MULTIPLIER FOR SUBTITLES SPEED
 *	ARGUMENT 6 : SECOND TO START DISPLAYING SUBTITLES 
 *	ARGUMENT 7 : FILEPATH TO OUTPUT .srt */



// pre-declare functions and declare objs

string get_txt_content (const char* fp);

vector<string> split_string_params(string str, int n_words_substr_max, int n_chars_substr_max);

int get_n_words_string(string str);

string get_time_row(int n_words_sub_row, float tpw, float& begg_sec, float sub_speed_mult);

string float_to_srt_time(float fl);

typedef struct srt_subtitle {

	int index;
	string time_row;
	string subtitle_row;
} srt_subtitle_t;

void write_srt(vector<srt_subtitle> subs, const char* target_fp);



// main function

int main (int argc, char* argv[]) {

	//assert arguments are correct
	assert(argc == 8);
	assert(is_filepath(argv[1]));
	assert(is_numeric(argv[2]));
	assert(is_numeric(argv[3]));
	assert(is_numeric(argv[4]));
	assert(is_numeric(argv[5]));
	assert(is_numeric(argv[6]));
	assert(is_filepath(argv[7]));

	//get arguments as vars
	const char*	content_txt_fp =	argv[1];
	const int 	n_words_sub_max = stoi(argv[2]);
	const int 	n_chars_sub_max = stoi(argv[3]);
	const float len_audio_s = 		stof(argv[4]);
	const float subs_speed_mult = stof(argv[5]);
	float 			start_sec = 			stof(argv[6]);
	const char* output_fp =				argv[7];

	//get content of content.txt as string and split into subtitle strings
	string content = get_txt_content(content_txt_fp);
	vector<string> subtitle_strs = split_string_params(content, n_words_sub_max, n_chars_sub_max);

	float n_words_per_minute = (float)get_n_words_string(content) / (len_audio_s / 60.0);
	const float time_per_word = len_audio_s / (float)get_n_words_string(content);
	cout << "n_words: " << get_n_words_string(content) << "  n wpm: " << n_words_per_minute << "\n";

	//create srt_subtitle_t struct for every subtitle string and calculate
	vector<srt_subtitle_t> subs_vec;
	float& curr_sec_ref = start_sec;
	for (int i = 0; i < subtitle_strs.size(); i++) {

		srt_subtitle sub_block;
		sub_block.index = i + 1;
		sub_block.subtitle_row = subtitle_strs[i];
		int n_words = get_n_words_string(sub_block.subtitle_row);
		sub_block.time_row = get_time_row(n_words, time_per_word, curr_sec_ref, subs_speed_mult);
		subs_vec.push_back(sub_block);
	}

	//write .srt
	write_srt(subs_vec, output_fp);

	//flush output and return
	cout << endl;
	return 0;
}



//functions

//function that writes .srt
void write_srt(vector<srt_subtitle_t> subs, const char* target_fp) {

	ofstream srt_file(target_fp);

	for (int i = 0; i < subs.size(); i++) {

		srt_subtitle_t sub = subs[i];
		srt_file << sub.index << "\n" << sub.time_row << "\n" << sub.subtitle_row;
		if (i != subs.size() - 1) srt_file << "\n\n";
	}

	srt_file.close();
}

//function that returns string formatted as time row
string get_time_row(int n_words_sub_row, float tpw, float& begg_sec, float sub_speed_mult) {

	//calculate total seconds to read sub and second to end on
	float secs_to_read = (float)n_words_sub_row * tpw;

	//get time to begin and end as srt time strings and get final string
	string begin_str = float_to_srt_time(begg_sec);
	string end_str = float_to_srt_time(begg_sec + secs_to_read);
	string final_str = begin_str + " --> " + end_str;

	//update second to begin from for next function call and return
	begg_sec += secs_to_read;
	return final_str;
}

string float_to_srt_time(float fl) {

	//calcualte number of hours, minutes and seconds
	int n_hours = 0;
	int n_minutes = 0;
	int n_secs = 0;
	while (fl >= 1.0) {

		if (fl >= 3600.0) {

			n_hours += 1;
			fl -= 3600.0;
			continue;

		} else if (fl >= 60.0) {

			n_minutes += 1;
			fl -= 60.0;
			continue;

		} else if (fl >= 1.0) {

			n_secs += 1;
			fl -= 1.0;
			continue;
		}
	}

	//build hours, minutes, seconds and milliseconds strings
	string hours_str, minutes_str, seconds_str, millisec_str;

	//hours
	if (n_hours < 10) {

		hours_str += '0';
		hours_str += to_string(n_hours);

	} else {

		hours_str += to_string(n_hours);
	}
	
	//minutes
	if (n_minutes < 10) {

		minutes_str += '0';
		minutes_str += to_string(n_minutes);

	} else {

		minutes_str += to_string(n_minutes);
	}

	//seconds
	if (n_secs < 10) {

		seconds_str += '0';
		seconds_str += to_string(n_secs);

	} else {

		seconds_str += to_string(n_secs);
	}

	//milliseconds
	millisec_str += to_string(fl);
	millisec_str.erase(millisec_str.begin());
	millisec_str.erase(millisec_str.begin());
	while (millisec_str.length() > 3 || millisec_str.length() < 3) {

		if (millisec_str.length() > 3) {

			millisec_str.pop_back();
			continue;

		} else if (millisec_str.length() < 3) {

			millisec_str += '0';
			continue;

		} else break;
	}

	//final string
	string final_str = hours_str + ":" + minutes_str + ":" + seconds_str + "," + millisec_str;
	return final_str;
}

//function that returns amount of words in a string
int get_n_words_string(string str) {

	//bool to see if string contains ASCII valid chars and int to store n words
	bool chars_detected = false;
	int n_words = 0;

	for (int i = 0; i < str.length(); i++) {

		//check if str contains chars
		if (!chars_detected) {

			if ((int)str[i] >= 33 && (int)str[i] <= 126) { 

				chars_detected = true;
				n_words = 1;
			}
		}

		//update words if not on last letter
		if (i != str.length() - 1 && chars_detected) {

			if (str[i] == ' ' && ((int)str[i + 1] >= 33 && (int)str[i + 1] <= 126)) n_words++;
		}
	}

	//return
	if (chars_detected == false) return 0;
	return n_words;
}

//function that splits string into strings that are n words long
vector<string> split_string_params(string str, int n_words_substr_max, int n_chars_substr_max) {

	//vector of strings for results
	vector<string> results = {};

	//divide into subtrings and append to results
	string temp;
	int n_words = 1;
	int n_chars = 0;
	bool should_reset = false;
	for (int i = 0; i < str.length(); i++) {

		//update should_reset if too many words/chars
		if (n_words > n_words_substr_max || n_chars > n_chars_substr_max) {

			should_reset = true;
		}

		//upon word end, update n_words and reset if its time
		if (str[i] == ' ') {

			if (should_reset == true) {

				results.push_back(temp);
				temp = "";
				n_words = 1;
				n_chars = 0;
				should_reset = false;
				continue;

			} else n_words++;
		}

		//update n_chars and append to temp
		n_chars++;
		temp += str[i];

		//reset if end of str reached
		if (i == str.length() - 1) {

			results.push_back(temp);
			temp = {0x0};
			n_words = 1;
			n_chars = 0;
		}
	}
	return results;
}

//function that opens file and returns contents of file as string
string get_txt_content (const char* fp) {

	//string to store result
	string result;

	//open file, assert valid fp and save into result
	ifstream content_txt_file(fp);

	if (!content_txt_file) {

		cout << "!!! invalid content.txt filepath passed to srt_handler.cpp";
		return "";
	}

	string line;
	while (!content_txt_file.eof()) {

		getline(content_txt_file, line);
		result.append(line);
	}

	//close file
	content_txt_file.close();

	return result;
}
