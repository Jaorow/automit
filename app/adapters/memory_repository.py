import csv
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from app.adapters.repository import AbstractRepository

"""
import domain models
"""



class MemoryRepository(AbstractRepository):
    pass

def populate(data_path: Path,repo:MemoryRepository):
    pass