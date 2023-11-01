import base64
import zlib

def load(input_path, output_path):
    with open(input_path, 'r') as file:
        raw_content = file.read()

    compressed_data = base64.b64decode(raw_content)
    decompressed_data_bytes = zlib.decompress(compressed_data, 16+zlib.MAX_WBITS)
    decompressed_data_str = decompressed_data_bytes.decode('utf-8')
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(decompressed_data_str)

if __name__ == "__main__":
    input_path = "task.txt"
    output_path = "decompressed_task.txt"
    load(input_path, output_path)
