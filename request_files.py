"""
Request Files
You can define files to be uploaded by the client using File.
File is a class that inherits directly from Form.

1. File
Type: Represents raw byte data.
Use Case: Best used when you want to directly handle the file's contents as bytes.
It is suitable for smaller files where you may not need extra metadata.

How It Works:
When you use File(), FastAPI reads the entire contents of the uploaded file into memory and provides
it as bytes in your endpoint function.
This makes it easy to handle the data directly, but it may not be efficient for larger files since
the entire file is loaded into memory.


2. UploadFile
Type: Represents a file upload with metadata.
Use Case: Ideal for larger files or when you need additional information about the uploaded file,
such as the filename, content type, etc.

How It Works:
When you use UploadFile, FastAPI streams the file data, which means it does not load the entire file into
memory at once. Instead, it provides a file-like interface where you can read from the uploaded file in chunks.
This method is more efficient for handling larger files and allows for easier processing of file uploads
without consuming a lot of memory.

Key Differences at a Glance:
Memory Management: File loads the entire file into memory; UploadFile streams the file content,
which is more memory-efficient.
Metadata Access: UploadFile provides access to file metadata (name, content type) while File does not.
File Handling: File returns raw bytes; UploadFile provides a file-like object, allowing for chunked reads.

UploadFile has the following attributes:

filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
file: A SpooledTemporaryFile (a file-like object). This is the actual Python file object that you can pass
directly to other functions or libraries that expect a "file-like" object.

UploadFile has the following async methods.

write(data): Writes data (str or bytes) to the file.
read(size): Reads size (int) bytes/characters of the file.
seek(offset): Goes to the byte position offset (int) in the file.
E.g., await myfile.seek(0) would go to the start of the file.
This is especially useful if you run await myfile.read() once and then need to read the contents again.
close(): Closes the file.
As all these methods are async methods, you need to "await" them.

For example, inside of an async path operation function you can get the contents with:


contents = await myfile.read()
If you are inside of a normal def path operation function, you can access the UploadFile.file directly, for example:


contents = myfile.file.read()
async Technical Details
"""

from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app= FastAPI()

@app.post("/file/")
async def create_file(files:Annotated[list[bytes], File(description="Multiple files as bytes")],):
    return {"file_length": [len(file) for file in files]}

@app.post("/upload_file/")
async def create_upload_files(
        files:Annotated[
            list[UploadFile], File(description="Multiple files as UploadFile")
        ],
    ):
    return {"file_names":[file.filename for file in files]}

