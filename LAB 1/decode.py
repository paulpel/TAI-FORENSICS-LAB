import base64


def load(input_path, output_path):
    with open(input_path, 'r') as file:
        raw_content = file.read()

    data = base64.b64decode(raw_content)
    data_str = data.decode('utf-8')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(data_str)


if __name__ == "__main__":
    input_path = "task.txt"
    output_path = "decompressed_task.txt"
    load(input_path, output_path)
