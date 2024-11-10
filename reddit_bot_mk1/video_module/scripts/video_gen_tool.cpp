//vid_gen_tool.cpp

#include <iostream>
#include <cassert>
#include <random>

#include "arg_checks.h"
#include "video_editor.h"

using namespace std;

#define VIDEO_LEN_S 10

/*	ARGUMENT 1 : FILEPATH OF BACKGROUND VIDEO */



// main function

int main (int argc, char* argv[]) {

	//assert arguments are correct
	assert(argc == 2);
	assert(is_filepath(argv[1]));

	//get arguments as var
	const char* background_vid_fp = argv[1];

	//Create video obj and set/get fp and duration
	VideoObj background_vid;

	background_vid.set_filepath(background_vid_fp);
	string fp = background_vid.get_filepath();

	background_vid.calc_duration();
	float backgr_len = background_vid.get_duration();
	
	//obtain random number between 0 and background video length
	random_device rd;
	mt19937 gen(rd());
	uniform_real_distribution<float> distr(0.0, backgr_len - VIDEO_LEN_S);

	//create output filepaths
	string output_fp_1 = "../../final_products/output_1.mp4";
	string output_fp_2 = "../../final_products/output_2.mp4";

	//cut background video
	background_vid.cut_video(distr(gen), VIDEO_LEN_S, output_fp_1.c_str());
	background_vid.set_filepath(output_fp_1.c_str());

	//crop background video
	background_vid.crop_video(608, 1080, output_fp_2.c_str());
	background_vid.set_filepath(output_fp_2.c_str());

	return 0;
}
