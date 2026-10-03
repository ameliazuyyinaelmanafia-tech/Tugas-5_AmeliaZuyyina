from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class AttendancePeriod:
    id: int
    month: int
    year: int
    created_at: datetime

@dataclass
class AttendanceRecord:
    id: int
    period_id: int
    employee_code: str
    present: int
    absent: int
    not_fulfilled: int
    work_hour_percentage: float
    attendance_percentage: float

@dataclass
class ClusteringRun:
    id: int
    period_id: int
    k: int = 3
    iteration_count: int = 0
    status: str = "completed"

@dataclass
class Centroid:
    run_id: int
    cluster_code: str
    x1: float
    x2: float
    iteration: int

@dataclass
class ClusterResult:
    run_id: int
    employee_code: str
    cluster_code: str
    discipline_level: str

@dataclass
class Evaluation:
    run_id: int
    silhouette_score: float
    details: Any = None
