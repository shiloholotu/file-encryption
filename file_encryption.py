import base64



#convert file to base64 string
def file_to_b64(location):
    read_data = []
    with open(location, 'rb') as a_file:
        while True:
            data = a_file.read(32)
            if not data:
                break
            read_data.append(base64.b64encode(data).decode("utf-8"))


    read_data = " ".join(read_data)
    return "!!!-NOT A UTF-8 FILE-!!!" + read_data

#convert base64 string to file data
def b64_to_file_data(string):
    string_data = string.split(" ")
    byte_data = []
    for i in string_data:
        byte_data.append(base64.b64decode(i))

    return byte_data


#write b64 file data to file
def b64_data_to_file(data, file_location):
    with open(file_location, 'wb') as a_file:
        for i in data:
            a_file.write(i)


#convert file to a string format depending on encoding
def file_to_string(location):
    try:
        #is a utf-8 file
        with open(location) as a_file:
            lines = a_file.readlines()
            lines = "".join(lines)
            return lines
            print("Is utf-8")

    except:
        #isn't a utf-8 file
        print("Not utf-8")
        return file_to_b64(location)

#convert string to file data depending on encoding
def string_to_file_data(string):
    if string[:24] == "!!!-NOT A UTF-8 FILE-!!!":
        return b64_to_file_data(string[24:])

    else:
        return string

#write file data to file depending on enconding
def data_to_file(data, file_location):
    if isinstance(data, str):
        with open(file_location, "w") as a_file:
            a_file.write(data)

    else:
        b64_data_to_file(data, file_location)


#string to file
def string_to_file(string, location):
    data = string_to_file_data(string)
    data_to_file(data,location)



    


