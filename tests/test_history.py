import os
import pytest
from app.history import HistorySubject, HistoryManager, AutoSaveObserver, Observer
from app.calculation import Calculation

class MockObserver(Observer):
    def __init__(self):
        self.notified = False

    def update(self, event_type, data):
        self.notified = True

def test_history_subject_observers():
    subject = HistorySubject()
    obs = MockObserver()
    subject.attach(obs)
    subject.notify("test", {})
    assert obs.notified

    obs.notified = False
    subject.detach(obs)
    subject.notify("test", {})
    assert not obs.notified

def test_history_manager_save_load(tmp_path):
    hm = HistoryManager()
    hm.filepath = str(tmp_path / "test_calc_history.csv")
    
    calc = Calculation("add", 1.0, 2.0, 3.0)
    hm.save_history([calc])
    
    loaded = hm.load_history()
    assert len(loaded) == 1
    assert loaded[0].operation == "add"

def test_auto_save_observer(tmp_path):
    hm = HistoryManager()
    hm.filepath = str(tmp_path / "autosave_calc.csv")
    observer = AutoSaveObserver(hm)
    
    calc = Calculation("add", 1.0, 1.0, 2.0)
    observer.update("add", {"history": [calc]})
    
    assert os.path.exists(hm.filepath)

def test_history_manager_load_nonexistent(tmp_path):
    hm = HistoryManager()
    hm.filepath = str(tmp_path / "nonexistent.csv")
    assert hm.load_history() == []

def test_history_manager_load_corrupted(tmp_path):
    hm = HistoryManager()
    file = tmp_path / "corrupt.csv"
    file.write_text("corrupted,data\n123")
    hm.filepath = str(file)
    assert hm.load_history() == []

def test_history_manager_save_error(monkeypatch):
    hm = HistoryManager()
    def mock_to_csv(*args, **kwargs):
        raise Exception("Disk write error")
    monkeypatch.setattr("pandas.DataFrame.to_csv", mock_to_csv)
    with pytest.raises(RuntimeError):
        hm.save_history([Calculation("add", 1, 1, 2)])
