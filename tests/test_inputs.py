"""校验运营资料的文件结构与已登记引用。"""
import csv
import json
import unittest
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"

class InputFilesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((DATA / "formats.json").read_text(encoding="utf-8"))
        cls.tables = {}
        for name, fields in cls.index["tables"].items():
            with (DATA / f"{name}.csv").open(encoding="utf-8", newline="") as source:
                reader = csv.DictReader(source)
                if reader.fieldnames != fields:
                    raise ValueError(f"{name} 的表头与格式登记不符")
                cls.tables[name] = list(reader)

    def test_records_match_headers(self):
        for name, records in self.tables.items():
            with self.subTest(table=name):
                self.assertTrue(records)
                self.assertTrue(all(None not in row and None not in row.values() for row in records))

    def test_declared_references_exist(self):
        for parent, key, child, ref in self.index["references"]:
            with self.subTest(table=child, column=ref):
                keys = {record[key] for record in self.tables[parent]}
                self.assertIn(False, {"" in keys})
                self.assertTrue(all(record[ref] in keys for record in self.tables[child] if record[ref]))

    def test_agreement_document_is_readable(self):
        agreements = json.loads((DATA / "agreements.json").read_text(encoding="utf-8"))
        self.assertEqual(set(self.index["agreement_keys"]), set(agreements))
