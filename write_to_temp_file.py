from tempfile import NamedTemporaryFile

temp_file = NamedTemporaryFile('w+t')

temp_file.write('This is an example')

print('Temporary file written to :', temp_file.name)
