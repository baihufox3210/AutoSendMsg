from src.utils.time_utils import get_next_custom_run_time
from datetime import datetime

def test_scheduling():
    # 模擬 2026-01-03 21:00 Saturday (5)
    base_time = datetime(2026, 1, 3, 21, 0, 0).timestamp()
    
    # 測試1: 下週一 (0)
    next_time = get_next_custom_run_time(base_time, [0])
    next_dt = datetime.fromtimestamp(next_time)
    print(f"Base: {datetime.fromtimestamp(base_time)}")
    print(f"Scheduled for Mon: {next_dt} (Weekday: {next_dt.weekday()})")
    assert next_dt.weekday() == 0
    assert next_dt.day == 5 # Jan 5th 2026 is Monday
    
    # 測試2: 下週三 (2) 和 週五 (4)
    next_time = get_next_custom_run_time(base_time, [2, 4])
    next_dt = datetime.fromtimestamp(next_time)
    print(f"Scheduled for Wed, Fri: {next_dt} (Weekday: {next_dt.weekday()})")
    assert next_dt.weekday() == 2 # 應該是最近的週三
    assert next_dt.day == 7
    
    # 測試3: 跨週測試（今天週六，找週五）
    next_time = get_next_custom_run_time(base_time, [4])
    next_dt = datetime.fromtimestamp(next_time)
    print(f"Scheduled for Fri (Next Week): {next_dt} (Weekday: {next_dt.weekday()})")
    assert next_dt.weekday() == 4
    assert next_dt.day == 9
    
    print("\n[✓] 所有時間推算測試通過！")

if __name__ == "__main__":
    try:
        test_scheduling()
    except Exception as e:
        print(f"[✗] 測試失敗: {e}")
