"""C3 - tmp_path built-in fixture
Usage of the built-in tmp_path fixture, which provides a temp path to save/read files into/from
https://docs.pytest.org/en/latest/tmpdir.html
"""

from pathlib import Path


def test_write_read_file(tmp_path: Path):
    file_path = tmp_path / "hello.txt"
    file_path = file_path.as_posix()
    lines = [
        "Hello there!",
        "General Kenobi!"
    ]

    print("The file path is", file_path)

    # Write
    with open(file_path, "w") as file:
        file.writelines("\n".join(lines))

    # Read
    with open(file_path, "r") as file:
        file_content = file.read()
        for line in lines:
            assert line in file_content
