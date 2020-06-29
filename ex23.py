import sys
script, input_encoding, error = sys.argv


def main(language_files, encoding, errors):
    line = language_files.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_files, encoding, errors)
        # basically a recursive loop for a function call... so possible here tooo......


def print_line(line, encoding, errors):
    next_lang = line.strip()
    # strip functions remove the /n at the end of the line.. ive to check id there is usually /n present at the end though
    # here the end line has a /n present like discussed in the seek function program... need to remove that.. dont know if it strips out the other escapte sequences.. mostly does this at the end and starting of the text...

    # here pass the thing you have to strip from the string in the function parameter.. if null passed then it causes to strip the /n at the end of it...
    raw_bytes = next_lang.encode(encoding, errors)
    cooked_string = raw_bytes.decode(encoding, errors)
    # remember that we need to decode to see the human version and encode to convert to machine format here..
    print(raw_bytes, "<=====>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)
print(error)


# error tells the encoding system about how to manage the errors. if strict encoding or replace it or anything else,, its not actually a thing in which you can store the errors shown on the encoding system


# Other encondigs include ASCII but it does only encode English in 8 bit
# the one that encompasses all is called UNICODE but it takes up way too much space and much of it is even empty for new characers of the world to get into it.. it is 32 bit or 4 byte....
# convention in python is to use UTF-8 in most common things and then escape to other encondigs if we need to use higher conventions here and other languages on need to use basis... it is unicode only but UTF is unicode transformation Format for most common uses and then likewise
# also there is big5 ... no idea about it...

#  in python to tell the system we are using raw bytes we use b'/x2.........' like this format... tells we are using bytes and not normal language..
