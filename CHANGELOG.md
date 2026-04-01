# CHANGELOG

## v0.3.0 (patch — ATHENA audit)

- **ATHENA 4단 전체 점검 후 수정**
- `boson_phenomenology.py`: ttH를 VH에서 분리, 독립 `HiggsProcessFact`로 추가
- `constants.py`: `HIGGS_BOSON_MASS_GEV` 125.1 → 125.20 (PDG 2022 기준), 연도 주석 추가
- `mass_and_couplings.py`: `from math import sqrt` 함수 바디에서 모듈 레벨로 이동
- `mass_generation.py`: `mass_generation_axes()` 반환 타입 어노테이션 추가, `ConceptLayer` 임포트 보강
- `foundation.py`: base omega 계산식을 투명하게 재작성 (`0.75 + 0.01 * min(layers, 10)`)
- `README.md`, `README_EN.md`: 빠른 시작의 절대 경로(`/Users/jazzin/...`) 제거
- `tests/test_higgs_foundation.py`: 4개 테스트 추가 (기본 POSITIVE, NEEDS_NUANCE, CAUTIOUS, aether 패널티)
- `tests/test_package_integrity.py` 신규: 패키지 정체성 보호 (foreign symbol 감지, `__version__` 검증)
- 테스트 기준선: 14 → 23 passed

## v0.3.0 (initial)

- expanded public README and English README
- added SHA-256 integrity manifest workflow
- added `generate_signature.py`, `verify_signature.py`, `cleanup_generated.py`, and `release_check.py`
- fixed standalone test import path via `tests/conftest.py`
- fixed direct execution path handling in `scripts/verify_package_identity.py`
- aligned package version metadata for public release
