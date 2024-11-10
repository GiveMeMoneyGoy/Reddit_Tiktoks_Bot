//arg_checks_tool.h

#include <cstring>

//function to check if string passed to it is filepath
bool is_filepath (const char* var) {

        //get len of var
        size_t len = strlen(var);

        //check if chars are valid
        for (int i = 0; i < (int)len; i++) {

                if (!((int)var[i] >= 33 && (int)var[i] <= 126)) return false;
        }
        return true;
}

//function to check if string passed to it is numeric
bool is_numeric (const char* var) {

        //get len of var
        size_t len = strlen(var);

        //check if chars are valid
        for (int i = 0; i < (int)len; i++) {

                if (!(((int)var[i] >= 48 && (int)var[i] <= 57) || (int)var[i] == 46)) return false;
        }
        return true;
}
