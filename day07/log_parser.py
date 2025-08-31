# log_parser.py
from pathlib import Path

LOG_FILE = Path("sample.log")
REPORT_FILE = Path("report.txt")

def parse_logs(path: Path) -> dict:
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "INFO" in line:
                stats["INFO"] += 1
            elif "WARNING" in line:
                stats["WARNING"] += 1
            elif "ERROR" in line:
                stats["ERROR"] += 1
    return stats

def save_report(path: Path, stats: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("Отчёт по логам\n")
        f.write("=================\n")
        for level, count in stats.items():
            f.write(f"{level}: {count}\n")

def main():
    stats = parse_logs(LOG_FILE)
    print("Статистика по логам:", stats)
    save_report(REPORT_FILE, stats)
    print(f"✅ Отчёт сохранён в {REPORT_FILE}")

if __name__ == "__main__":
    main()

