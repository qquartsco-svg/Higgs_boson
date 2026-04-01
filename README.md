> **한국어 (정본).** English: [README_EN.md](README_EN.md)

# Higgs_Phenomenology_Foundation v0.3.0

**`Higgs_Phenomenology_Foundation`는 “힉스란 무엇인가?”라는 질문을 장(field), 전약 대칭 깨짐(EWSB), 질량 생성 구조, 보손 현상론, 주장 스크리닝으로 분해해 보수적으로 읽는 기초 레이어**입니다.

이 패키지는 힉스를 “신비한 입자 하나”로 다루지 않습니다. 핵심 대상은

- 힉스 **장**
- 진공기대값(**VEV**)
- 전약 대칭 깨짐(**EWSB**)
- 게이지 보손과 페르미온의 질량 구조
- 힉스 보손이라는 **장의 excitation**

입니다.

즉 이 저장소는 “힉스 보손 설명서”이기보다, **힉스 개념을 오해 없이 구조적으로 이해하기 위한 phenomenology foundation**에 가깝습니다.

## 힉스란 무엇인가

아주 짧게 말하면:

- 힉스 **장**은 우주 진공의 한 성질입니다.
- 힉스 **보손**은 그 장의 양자적 excitation입니다.
- 전약 대칭이 깨진 뒤, 힉스 장의 진공기대값 `v ≈ 246 GeV`가
  - `W`, `Z` 보손 질량
  - 기본 페르미온의 Yukawa 질량 항
  와 연결됩니다.

하지만 여기서 가장 중요한 보수적 포인트가 하나 있습니다.

**힉스가 “모든 질량”을 만들어주는 것은 아닙니다.**

예를 들어 양성자와 중성자의 질량 대부분은 힉스보다 **QCD 결합 에너지**에서 옵니다. 이 엔진은 바로 이 흔한 오해를 잡아내도록 설계돼 있습니다.

## 왜 중요한가

힉스 문제는 현대 물리학에서 여러 질문과 맞닿아 있습니다.

- 왜 `W`, `Z`는 무겁고 광자는 질량이 없는가
- 왜 전자, 쿼크, 뮤온 같은 기본 입자들의 질량 스케일이 제각각인가
- 표준모형의 EWSB 설명은 어디까지 성공했고, 어디서부터 열린 질문이 남는가
- 힉스 질량, 진공 안정성, hierarchy/naturalness 같은 문제는 어떤 맥락에서 나오는가

즉 힉스는 단순한 “새 입자 하나”가 아니라, **표준모형의 질량 구조와 진공 구조를 읽는 핵심 관문**입니다.

## 왜 이 엔진이 필요한가

실무적으로 보면 “힉스”라는 단어는 자주 과장되거나 잘못 쓰입니다.

- “힉스가 중력을 만든다”
- “힉스가 우주의 모든 질량을 완전히 설명한다”
- “힉스 발견으로 표준모형이 완전히 끝났다”
- “히트뉴스 한 줄로 BSM이 입증됐다”

이 엔진은 그런 식의 서술을 바로 수용하지 않고,

1. 무엇이 **장**의 이야기인지
2. 무엇이 **보손**의 이야기인지
3. 무엇이 **질량 구조**의 이야기인지
4. 무엇이 **실험적 발견 문맥**인지
5. 무엇이 **열린 질문**인지

를 분리해서 봅니다.

즉 목적은 “큰 주장”이 아니라 **개념 정렬, 교육, 구조적 스크리닝**입니다.

## 무엇을 하는가

이 패키지는 다음을 합니다.

- 힉스 장과 힉스 보손을 구분합니다.
- 전약 대칭 깨짐을 L1 개념축으로 설명합니다.
- 기본 페르미온 질량, `W/Z` 질량, 핵자 질량(QCD 우세)을 분리합니다.
- 생산/붕괴 채널을 태그 수준에서 정리합니다.
- 흔한 오해를 `ATHENA 4단 판정`으로 보수적으로 분류합니다.
- 열린 질문을 로드맵 태그로 남깁니다.

## 무엇을 하지 않는가

이 패키지는 다음을 하지 않습니다.

- LHC Monte Carlo 시뮬레이터를 대체하지 않습니다.
- 분기비 정밀 피팅, EFT global fit, PDF/parton 수준 계산을 하지 않습니다.
- 협력실험의 공식 결론을 대신하지 않습니다.
- SUSY/2HDM/복합 힉스 수치 해를 직접 풀지 않습니다.
- “힉스가 모든 질량의 전부” 같은 과장된 단정을 지지하지 않습니다.

즉 이 저장소는 **precision collider tool**이 아니라 **foundation/screening layer**입니다.

## 단독 클론 사용자에게

이 저장소는 단독으로도 작동합니다. 다만 `00_BRAIN` 우산 구조 안에서 읽을 때 더 자연스러운 sibling references가 일부 문서에 등장할 수 있습니다. 공개 저장소만 단독 클론한 경우, 그런 로컬 경로 참조는 없거나 생략될 수 있습니다.

## 레이어 구조

| Layer | 역할 | 모듈 |
|------|------|------|
| `L0` | 계약 / 타입 | `contracts.py` |
| `L1` | 장, VEV, EWSB, 대칭 깨짐 | `field_symmetry.py`, `mechanism.py` |
| `L2` | 질량 생성 구조 | `mass_generation.py`, `mass_and_couplings.py` |
| `L3` | 힉스 보손 현상론 | `boson_phenomenology.py`, `discovery_context.py` |
| `L4` | 주장 스크리닝 / ATHENA 판정 | `screening.py` |
| `L5` | 열린 질문 / 형제 엔진 연결 메모 | `open_questions.py`, `extension_hooks.py` |

상세 레이어 노트는 [docs/LAYER_STACK.md](docs/LAYER_STACK.md) 를 참고하면 됩니다.

## 핵심 모듈

### `field_symmetry.py`

- 힉스 장을 진공 속성으로 서술
- `VEV`
- `SSB`
- 전약군 서사

### `mechanism.py`

- `SU(2) × U(1)_Y -> U(1)_em`
- `W/Z`는 massive
- 광자는 massless
- 힉스 장과 힉스 보손의 층위 구분

### `mass_generation.py`

- 질량 생성의 pedagogical ledger
- `gauge_higgs_mechanism`
- `yukawa_fermion`
- `qcd_binding_nucleon`

### `mass_and_couplings.py`

- Yukawa 질량 스케일 직관
- coupling order-of-magnitude 보조 설명

### `boson_phenomenology.py`

- 생산 채널 태그
  - `ggF`
  - `VBF`
  - `VH`
  - `ttH`
- 붕괴 채널 태그
  - `gamma gamma`
  - `ZZ*`
  - `WW*`
  - `bb`
  - `tau tau`

### `discovery_context.py`

- 왜 힉스가 “발견됐다”고 말하는지
- 어떤 collider 문맥에서 확인되는지
- 특히 “발견”이란 단어가 단순 직관이 아니라, 특정 생산/붕괴 채널에서의 excess와 collider 통계 문맥 안에서 쓰인다는 점을 정리

### `open_questions.py`

- hierarchy / naturalness
- vacuum stability
- BSM extension prompts

### `screening.py`

- 흔한 오해, 과장, misleading payload를 보수적으로 걸러냄

### `foundation.py`

- 위 모든 층을 묶어 `HiggsFoundationReport`로 롤업

## 기초 수식과 직관

이 엔진은 정밀 계산 코드가 아니라 **개념을 구조화하는 수식 뼈대**를 씁니다.

- 포텐셜 만화:
  - `V(phi) = mu^2 |phi|^2 + lambda |phi|^4`
  - `mu^2 < 0` 이면 자발적 대칭 깨짐 그림과 연결
- 진공기대값:
  - `v ≈ 246 GeV`
- 트리 수준 Yukawa 질량:
  - `m_f = y_f v / sqrt(2)`
  - 여기서 `y_f` 는 **무차원 Yukawa coupling**, 출력 질량은 **GeV** 단위입니다.
- 트리 수준 힉스 질량 관계:
  - `m_H^2 = 2 lambda v^2`

중요한 점은, 이 수식들은 이 저장소에서 **현상론적 구조와 교육용 직관**을 제공하기 위한 것이지, 실험 적합이나 고정밀 계산을 위한 완전한 툴셋이 아니라는 점입니다.

## ATHENA 4단 판정

`screening.py`는 힉스 관련 서술을 다음 4단계로 읽습니다.

- `positive`
  - 표준모형 수준에서 교육적으로 정합적인 설명
- `neutral`
  - 정보가 부족하거나 실험적 불확실성만 남긴 설명
- `cautious`
  - BSM, composite Higgs, second Higgs 등 확장은 가능하지만 보수적으로 읽어야 하는 설명
- `negative`
  - 힉스=중력, 초광속, 에너지 비보존, 모든 질량의 전부 같은 물리적으로 부정확한 설명

이 판정은 “진리 선언”이 아니라 **설명 구조에 대한 보수적 screening language**입니다.

## foundation 출력

`assess_higgs_foundation(...)` 는 다음을 요약합니다.

- `omega_foundation_0_1`
- `summary`
- `key_risk`
- `recommendation`
- `evidence_tags`

즉 이 엔진은 “힉스를 정의한다”기보다, **어떤 설명이 어떤 층위를 놓치고 있는지**를 요약합니다.

현재 foundation 출력은 **단일 `omega_foundation_0_1` + 설명 필드** 중심입니다. 즉 이 엔진은 아직 `field_score`, `mass_structure_score`, `phenomenology_score`, `claim_consistency_score` 같은 하위 점수를 분리해서 내지는 않습니다. 대신 `evidence_tags`, `key_risk`, `recommendation`으로 왜 그런 판정이 나왔는지를 남깁니다.

자연스러운 다음 확장 방향은 이 단일 `omega`를 유지하되, 그 아래에

- `field_symmetry_score`
- `mass_structure_score`
- `boson_phenomenology_score`
- `claim_consistency_score`

같은 하위 점수를 추가하는 것입니다.

## 빠른 시작

```bash
cd Higgs_Phenomenology_Foundation   # 또는 클론한 디렉토리 경로
python3 -m pip install -e ".[dev]"
python3 -m pytest tests/ -q
python3 scripts/verify_package_identity.py
```

```python
from higgs_phenomenology import (
    HiggsClaimPayload,
    assess_higgs_foundation,
    fermion_mass_gev_from_yukawa,
    screen_higgs_claim,
)

electron_mass = fermion_mass_gev_from_yukawa(y_f=2.94e-6)
print(electron_mass)

claim = HiggsClaimPayload(says_higgs_gives_all_mass=True)
screened = screen_higgs_claim(claim)
print(screened.tier, screened.athena_verdict)

report = assess_higgs_foundation(claim_payload=claim)
print(report.omega_foundation_0_1, report.key_risk)
```

## 테스트와 정합성

현재 포함된 검증은 다음과 같습니다.

- 단위 테스트
- import/패키지 정합성 검사
- SHA-256 서명 검증
- 릴리스 체크

실행:

```bash
python3 -m pytest tests/ -q
python3 scripts/verify_package_identity.py
python3 scripts/verify_signature.py
python3 scripts/release_check.py
```

현재 기준선은 `23 passed` 입니다.

## 블록체인 서명

이 저장소에서 말하는 “블록체인 서명”은 실제 온체인 합의 시스템이 아니라, 루트의 `SIGNATURE.sha256` 에 기록된 **파일별 SHA-256 무결성 매니페스트**를 뜻합니다.

- [BLOCKCHAIN_INFO.md](BLOCKCHAIN_INFO.md)

검증:

```bash
python3 scripts/verify_signature.py
```

재생성:

```bash
python3 scripts/generate_signature.py
```

## 활용성

이 패키지는 다음 용도에 적합합니다.

- 교육용 힉스 개념 엔진
- 에이전트/옵저버의 physics claim screening
- “힉스가 뭔가”를 구조적으로 설명하는 API 백엔드
- 표준모형 설명 계층과 BSM 로드맵 태그를 분리한 foundation
- 다른 엔진에서 힉스 개념을 안전하게 참조하는 공통 레이어

## 확장성

자연스러운 다음 확장은 다음과 같습니다.

- `Higgs_Confinement` 같은 이름의 공학 엔진이 아니라
  - `Higgs_Precision_Fit_Foundation`
  - `Electroweak_Symmetry_Foundation`
  - `BSM_Higgs_Extension_Kernel`
  같은 **정밀 phenomenology 또는 확장모형 보조 레이어**
- collider report parser
- EFT / coupling deviation tag layer
- vacuum stability / RG running note layer
- sibling engine bridge
  - antimatter asymmetry 문맥
  - frequency/observer systems의 pedagogy bridge

## 현재 한계

이 엔진은 의도적으로 보수적입니다.

- collider event generation 없음
- detector simulation 없음
- precision fit 없음
- branching ratio global fit 없음
- BSM 수치 모델 해석 없음
- 표준모형을 넘는 주장에 대해 보수적으로만 태그를 남김

즉 **“힉스에 대한 생각의 구조를 정리하는 엔진”이지, 힉스 physics 전부를 계산하는 엔진은 아닙니다.**

## 저장소 파일

- [docs/LAYER_STACK.md](docs/LAYER_STACK.md)
- [README_EN.md](README_EN.md)
- [CHANGELOG.md](CHANGELOG.md)
- [BLOCKCHAIN_INFO.md](BLOCKCHAIN_INFO.md)

## 라이선스

MIT
