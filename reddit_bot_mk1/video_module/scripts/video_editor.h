//video_edit_tool.h

#include <iostream>
#include <string>
#include <cstring>

using namespace std;



// pre-declare
string call_process(string command);
string call_process(const char* command);

float ffmpeg_time_str_to_seconds(string str);
float ffmpeg_time_str_to_seconds(const char* str);

string seconds_to_ffmpeg_time_str(float seconds);

class VideoObj;



// declare

// classes 
class VideoObj {

	private:
		string filepath;
		float duration;

	public:

		//video display functions

		//function to crop video using ffmpeg terminal API
		void crop_video(int x, int y, const char* out_fp) {


			string command = "ffmpeg -y ";

			//input filepath
			command += "-i ";
			command += this->filepath;

			//crop
			command += " -vf \"crop=";
			command += to_string(x);
			command += ':';
			command += to_string(y);
			command += "\" ";

			//output filepath and execute
			command += out_fp;
			string result = call_process(command);
			cout << command << "\n";
			cout << result << "\n";
		}

		//video length functions

		//function to cut video using ffmpeg terminal API
		void cut_video(float from_seconds, float n_seconds, const char* out_fp) {

			string command = "ffmpeg -y ";

			//cut
			command += " -ss ";
			command += to_string(from_seconds);
			command += " -t ";
			command += to_string(n_seconds);

			//do not cut frames necessary for temporal compression
			command += " -avoid_negative_ts make_zero";

			//self as input source
			command += " -i ";
			command += this->filepath;

			//copy video and audio codec if specified to not reencode
			command += " -c:v copy";
			command += " -c:a copy";

			//output fp
			command += " ";
			command += out_fp;

			string result = call_process(command);
			cout << result << "\n";
		}

		//function to set length of video using ffmpeg
		void calc_duration() {

			//call command
			string command = "ffmpeg -i " + filepath + " 2>&1 | grep \"Duration\"";
			string result = call_process(command);
			string durr_str = "";

			//exctract duration string and attempt to save
			size_t found = result.find("Duration: ");
			if (found != string::npos) {

				for (int i = 12; i < 23; i++) {

					durr_str += result[i];
				}
			} else {

				cout << "!!! COULD NOT FIND \"Duration: \" IN OUTPUT OF calc_duration() IN video_editor.h";
				exit(1);
			}
			this->duration = ffmpeg_time_str_to_seconds(durr_str);
		}

		//function that returns length of video as string
		float get_duration() {
			return this->duration;
		}

		//video filepath functions

		//function to set fp to video
		void set_filepath(const char* fp) {
			this->filepath = "";
			this->filepath += fp;
		}

		//function that returns filepath of video as string
		string get_filepath() {
			return this->filepath;
		}
};


// functions

//function to call process, wait to finish and return output
string call_process(string command) {

	FILE* cmd_pipe = popen(command.c_str(), "r");
	string output = "";
	char result[24] = {0x0};
	while (fgets(result, sizeof(result), cmd_pipe) != NULL) output += result;
	pclose(cmd_pipe);
  return output;
}
string call_process(const char* command) {

	FILE* cmd_pipe = popen(command, "r");
	string output = "";
	char result[24] = {0x0};
	while (fgets(result, sizeof(result), cmd_pipe) != NULL) output += result;
	pclose(cmd_pipe);
  return output;
}

//function to convert ffmpeg time formatted string to float
float ffmpeg_time_str_to_seconds(string str) {

	//get n hours, minutes, seconds and milliseconds
	int n_hours = 0, n_minutes = 0, n_seconds = 0, n_msecs = 0;
	for (int i = str.length() - 1; i >= 0; i--) {

		switch(i) {
			case 11: 	n_msecs += str[i] - '0'; 					break;
			case 10: 	n_msecs += (str[i] - '0') * 10; 	break;
			case 9: 	n_msecs += (str[i] - '0') * 100; 	break;

			case 7: 	n_seconds += (str[i] - '0'); 			break;
			case 6: 	n_seconds += (str[i] - '0') * 10; break;

			case 4: 	n_minutes += (str[i] - '0'); 			break;
			case 3:	 	n_minutes += (str[i] - '0') * 10; break;

			case 1: 	n_hours += (str[i] - '0'); 				break;
			case 0:		n_hours += (str[i] - '0') * 10; 	break;
		}
	}

	//format final float and return
	return (float)n_hours * 3600 + (float)n_minutes * 60 + (float)n_seconds + (float)n_msecs / 1000;
}
float ffmpeg_time_str_to_seconds(const char* str) {

	//get n hours, minutes, seconds and milliseconds
	int n_hours = 0, n_minutes = 0, n_seconds = 0, n_msecs = 0;
	for (int i = strlen(str) - 1; i >= 0; i--) {

		switch(i) {
			case 11: 	n_msecs += str[i] - '0'; 					break;
			case 10: 	n_msecs += (str[i] - '0') * 10; 	break;
			case 9: 	n_msecs += (str[i] - '0') * 100; 	break;

			case 7: 	n_seconds += (str[i] - '0'); 			break;
			case 6: 	n_seconds += (str[i] - '0') * 10; break;

			case 4: 	n_minutes += (str[i] - '0'); 			break;
			case 3:	 	n_minutes += (str[i] - '0') * 10; break;

			case 1: 	n_hours += (str[i] - '0'); 				break;
			case 0:		n_hours += (str[i] - '0') * 10; 	break;
		}
	}

	//format final float and return
	return (float)n_hours * 3600 + (float)n_minutes * 60 + (float)n_seconds + (float)n_msecs / 1000;
}

//function to convert float to ffmpeg time formatted string
string seconds_to_ffmpeg_time_str(float seconds) {

	//get n hours, minutes, seconds and milliseconds
	int n_hours = 0, n_minutes = 0, n_seconds = 0, n_milliseconds = 0;
	while (seconds >= 0.001) {

		if (seconds >= 3600.0) {
			seconds -= 3600.0;
			n_hours++;
			continue;

		} else if (seconds >= 60.0) {
			seconds -= 60.0;
			n_minutes++;
			continue;

		} else if (seconds >= 1) {
			seconds -= 1.0;
			n_seconds++;
			continue;

		} else if (seconds >= 0.001) {
			seconds -= 0.001;
			n_milliseconds++;
			continue;
		}
	}

	//format final string and return
	string result;
	if (n_hours < 10) {
		result += '0';
		result += to_string(n_hours);
	} else if (n_hours >= 10) result += to_string(n_hours);

	result += ':';
	if (n_minutes < 10) {
		result += '0';
		result += to_string(n_minutes);
	} else if (n_minutes >= 10) result += to_string(n_minutes);

	result += ':';
	if (n_seconds < 10) { 
		result += '0';
		result += to_string(n_seconds);
	} else if (n_seconds >= 10) result += to_string(n_seconds);

	result += ',';
	if (n_milliseconds < 10) {
		result += "00";
		result += to_string(n_milliseconds);
	} else if (n_milliseconds >= 10 && n_milliseconds <= 99) {
		result += '0';
		result += to_string(n_milliseconds);
	} else if (n_milliseconds >= 100) result += to_string(n_milliseconds);

	return result;
}
