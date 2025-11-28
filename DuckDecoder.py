############## DuckDecoder ##############
#  
#    Description:   	Python script to decode/ display usb rubber ducky inject.bin files
#    Author(s):  		JPaulMora (@jpaulmora)
#    Conrtibutor(s):   	@mv12star
#    Version:   		0.2
#
#  Program currently supports all characters on an english keyboard mapping, I have been getting trouble identifying key
#  combinations such as ALT ENTER U since its output in hex is the same as of a STRING u command. 
#
#  Arrow keys now working!!

import binascii 
import os
import sys

args = sys.argv

def hexstr(fn):
    with open(fn, 'rb') as f:
        content = f.read()
    payload = binascii.hexlify(content).decode()  # Decode to string
    return payload

def dsem(h, n):
    n = max(1, n)
    return [h[i:i + n] for i in range(0, len(h), n)]

def letiscover(letters, type_, mode):
    delay = 0
    string = 0
    result = []

    letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "/", ";", "'", "[", "]", "\\", "-", "=", " ", "\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "BSPACE", '`', "TAB", "UP", "DOWN", "RIGHT", "LEFT", "DEL"]
    cap_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">", "?", ":", '"', "{", "}", "|", "_", "+", "SPACE", "ENTER", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "BSPACE", '~', "TAB", "UP", "DOWN", "RIGHT", "LEFT"]
    alt_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".", "/", ";", "'", "[", "]", "\\", "-", "=", "SPACE\n", "ENTER", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "BSPACE", '`', "TAB", "UP", "DOWN", "RIGHT", "LEFT", "DEL"]
    hex_letters = ['04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '36', '37', '38', '33', '34', '2f', '30', '31', '2d', '2e', '2c', '28', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '2a', '35', '2b', '52', '51', '4f', '50', '4c']

    if mode == 1:  # Decode mode
        no_str_keys = ['\n', 'BSPACE', 'TAB', 'DEL', 'UP', 'DOWN', 'RIGHT', 'LEFT']
        no_str_k_replace = ['ENTER', 'BACKSPACE', 'TAB', 'DEL', 'UP', 'DOWN', 'RIGHT', 'LEFT']
        for i in range(len(letters)):
            if letters[i] in hex_letters and type_[i] == '00':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                    last_delay = result[-1]
                    if string == 0 and str(letters_list[letter_pos]) != "\n" and result[-1] == last_delay and str(letters_list[letter_pos]) != "BSPACE":
                        result.append("\nSTRING ")
                        string = 1
                        delay = 0
                        result.append(letters_list[letter_pos])
                    else:
                        result.append(letters_list[letter_pos])
                
                elif str(letters_list[letter_pos]) in no_str_keys:
                    result.append("\n" + str(no_str_k_replace[no_str_keys.index(str(letters_list[letter_pos]))]))
                    string = 0

                else:
                    if string == 0:
                        result.append("\nSTRING ")
                        result.append(letters_list[letter_pos])
                        string = 1
                        delay = 0
                    else:
                        result.append(letters_list[letter_pos])
                delay = 0
            
            elif letters[i] in hex_letters and type_[i] == '01':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                result.append("\nCONTROL " + str(alt_letters[letter_pos]))
                delay = 0
                string = 0
            
            elif letters[i] in hex_letters and type_[i] == '02':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                if string == 0 and str(cap_letters[letter_pos]) != "\n":
                    result.append("\nSTRING ")
                    string = 1
                if str(cap_letters[letter_pos]) == "\n":
                    result.append("\nENTER ")
                    string = 0
                elif str(cap_letters[letter_pos]) == "BSPACE":
                    result.append("\nBACKSPACE ")
                    string = 0
                else:
                    result.append(cap_letters[letter_pos])
                delay = 0
            
            elif letters[i] in hex_letters and type_[i] == '04':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                result.append("\nALT " + str(alt_letters[letter_pos]))
                delay = 0
                string = 0
            
            elif letters[i] in hex_letters and type_[i] == '05':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                result.append("\nCTRL-ALT " + str(alt_letters[letter_pos]))
                delay = 0
                string = 0
            
            elif letters[i] in hex_letters and type_[i] == '08':
                letter_pos = hex_letters.index(letters[i])
                if delay != 0:
                    result.append("\nDELAY " + str(delay) + "\n")
                result.append("\nGUI " + str(alt_letters[letter_pos]))
                delay = 0
                string = 0
            
            elif letters[i] == '00':
                delay += int(type_[i], 16)
                string = 0
    else:  # Display mode
        arrows = ["UP", "DOWN", "RIGHT", "LEFT"]
        arrow = 0
        for i in range(len(letters)):
            if letters[i] in hex_letters and type_[i] == '00':  # Lowercase
                letter_pos = hex_letters.index(letters[i])
                if str(letters_list[letter_pos]) == "BSPACE":
                    del result[-1]
                    if arrow == 1:
                        result.append("\n")
                        arrow = 0
                elif str(letters_list[letter_pos]) in arrows:
                    result.append("\n" + str(letters_list[letter_pos]))
                    arrow = 1
                elif str(letters_list[letter_pos]) == "TAB":
                    result.append("     ")
                    if arrow == 1:
                        result.append("\n")
                        arrow = 0
                else:
                    if arrow == 1:
                        result.append("\n")
                        arrow = 0
                    result.append(letters_list[letter_pos])
                
            elif letters[i] in hex_letters and type_[i] == '01':  # Control key
                letter_pos = hex_letters.index(letters[i])
                result.append("\nCONTROL " + str(alt_letters[letter_pos]) + "\n")
            elif letters[i] in hex_letters and type_[i] == '02':  # Caps
                letter_pos = hex_letters.index(letters[i])
                result.append(cap_letters[letter_pos])
            elif letters[i] in hex_letters and type_[i] == '04':  # Alt key
                letter_pos = hex_letters.index(letters[i])
                result.append("\nALT " + str(alt_letters[letter_pos]) + "\n")
            elif letters[i] in hex_letters and type_[i] == '08':  # GUI key
                letter_pos = hex_letters.index(letters[i])
                result.append("\nGUI " + str(alt_letters[letter_pos]))

    result.append("\n\n")
    return result

def usage(reason, ecode):
    print("Usage: " + str(args[0]) + " < display|decode > inject.bin\n\n Example: " + str(args[0]) + " display /Documents/inject.bin\n")
    print(reason + "\n")
    sys.exit(ecode)

########################## End of Functions ###################################

if len(args) > 1 and len(args) < 5:
    try:
        filename = os.path.realpath(args[2])
    except IndexError:
        usage("Error: File not found", 1)

    list_ = dsem(hexstr(filename), 2)
    mode = args[1]
    chars = list_[::2]
    types = list_[1::2]

    if mode == "decode":
        result = letiscover(chars, types, 1)
    elif mode == "display":
        result = letiscover(chars, types, 0)
    else:
        usage("Error: No such option", -1)

    string = ""
    for item in result:
        string += str(item)

    print(string)
else:
    usage("", 2)
