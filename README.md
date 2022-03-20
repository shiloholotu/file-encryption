# file-encryption
Simple program that can be used to convert any type of file to string and convert strings into files.

The strings created from files are either representative of base64 text or just normal strings depending on the type of file that is being encrypted

Heres a really simple example of how to use it:
```python
string = file_to_string("\where\the\file\you\want\to\encrypt\is")
#The file is converted into a string, which you can just save somewhere for later or you can convert it back into a file👇
string_to_file(string, "\where\you\want\the\new\file\to\be")
```
