"""C3 - tmp_path built-in fixture
Usage of the built-in tmp_path fixture, which provides a temp path to save/read files into/from
https://docs.pytest.org/en/latest/tmpdir.html
"""

from pathlib import Path


def test_write_read_file(tmp_path: Path):
    directory = tmp_path / "subdirectory"
    directory.mkdir()
    file_name = directory / "hello.txt"
    lines = [
        "Hello there!",
        "General Kenobi!"
    ]

    print("The filename is", file_name.as_posix())

    # Write
    with open(file_name.as_posix(), "w") as file:
        file.writelines("\n".join(lines))

    # Read
    with open(file_name.as_posix(), "r") as file:
        file_content = file.read()
        for line in lines:
            assert line in file_content
