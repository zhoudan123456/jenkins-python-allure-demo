import pytest
from src.calculator import add


def test_add_success():
    """测试正常加法"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_add_failure():  # 故意写一个失败用例（演示流程）
    assert add(1, 1) == 3  # 预期2，实际3 → 测试失败