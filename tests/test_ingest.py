import json

def test_load_csv(tmp_path):
    csv_content = "col1,col2\n1,2\n3,4\n"
    path = tmp_path / "data.csv"
    path.write_text(csv_content)
    from agents.ingest import load_file
    data = load_file(str(path))
    assert isinstance(data, list)
    assert data[0]["col1"] == "1"
    assert data[1]["col2"] == "4"


def test_load_json(tmp_path):
    obj = [{"a": 1}]
    path = tmp_path / "data.json"
    path.write_text(json.dumps(obj))
    from agents.ingest import load_file
    data = load_file(str(path))
    assert data == obj
