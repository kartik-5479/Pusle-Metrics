import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


DB_PATH = Path(__file__).resolve().parents[1] / "data" / "pulse_metrics.db"


def initialize_database() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                report_name TEXT NOT NULL,
                report_type TEXT,
                overall_status TEXT,
                normal_count INTEGER NOT NULL,
                borderline_count INTEGER NOT NULL,
                abnormal_count INTEGER NOT NULL,
                analysis_json TEXT NOT NULL
            )"""
        )
        connection.commit()


def save_analysis(report_name: str, analysis: Dict[str, Any]) -> int:
    initialize_database()
    patient = analysis.get("patient_information", {})
    summary = analysis.get("summary", {})
    stats = analysis.get("statistics", {})
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """INSERT INTO analyses
            (timestamp, report_name, report_type, overall_status, normal_count,
             borderline_count, abnormal_count, analysis_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                datetime.now(timezone.utc).isoformat(),
                report_name,
                patient.get("report_type", "Not available"),
                summary.get("overall_status", "Not available"),
                stats.get("normal", 0),
                stats.get("borderline", 0),
                stats.get("abnormal", 0),
                json.dumps(analysis),
            ),
        )
        connection.commit()
        return int(cursor.lastrowid)


def list_analyses() -> List[Dict[str, Any]]:
    initialize_database()
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT * FROM analyses ORDER BY timestamp DESC"
        ).fetchall()
    return [dict(row) for row in rows]


def get_analysis(analysis_id: int) -> Optional[Dict[str, Any]]:
    initialize_database()
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute(
            "SELECT * FROM analyses WHERE id = ?", (analysis_id,)
        ).fetchone()
    if row is None:
        return None
    result = dict(row)
    result["analysis"] = json.loads(result.pop("analysis_json"))
    return result
