#!/usr/bin/env python3
"""
Generate one quiz JSON per Principles of Economics chapter.
"""

from __future__ import annotations

import json
from pathlib import Path


QUIZZES = [
    {
        "chapter_id": "01-human-action",
        "question_en": "What is economics primarily defined as in Chapter 1?",
        "choices_en": [
            "The study of purposeful human action under scarcity",
            "The study of physical objects alone",
            "The management of government aggregates",
            "The prediction of history by equations",
        ],
        "question_ko": "1장에서 경제학은 주로 무엇으로 정의되는가?",
        "choices_ko": [
            "희소성 아래의 목적 있는 인간 행동을 연구하는 학문",
            "물리적 사물만 연구하는 학문",
            "정부 집계를 관리하는 학문",
            "방정식으로 역사를 예측하는 학문",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter grounds economics in purposeful human action rather than aggregates or material objects alone.",
        "explanation_ko": "이 장은 경제학의 출발점을 집계나 물질 자체가 아니라 목적 있는 인간 행동에 둔다.",
    },
    {
        "chapter_id": "02-value",
        "question_en": "How is value treated in Chapter 2?",
        "choices_en": [
            "As a subjective judgment made by acting individuals",
            "As an objective property inside goods",
            "As a number fixed by the state",
            "As a quantity measured by labor hours alone",
        ],
        "question_ko": "2장에서 가치는 어떻게 다뤄지는가?",
        "choices_ko": [
            "행동하는 개인이 내리는 주관적 판단",
            "재화 내부에 있는 객관적 속성",
            "국가가 고정하는 숫자",
            "노동시간만으로 측정되는 양",
        ],
        "answer_index": 0,
        "explanation_en": "Value is presented as subjective and rooted in individual valuation.",
        "explanation_ko": "가치는 개인의 평가에 뿌리를 둔 주관적 판단으로 제시된다.",
    },
    {
        "chapter_id": "03-time",
        "question_en": "What ultimate scarce resource stands behind all economic action in Chapter 3?",
        "choices_en": [
            "Time",
            "Gold",
            "Land",
            "Labor unions",
        ],
        "question_ko": "3장에서 모든 경제 행동의 배후에 있는 궁극적 희소 자원은 무엇인가?",
        "choices_ko": [
            "시간",
            "금",
            "토지",
            "노동조합",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter argues that time is the ultimate scarce resource behind economic choice.",
        "explanation_ko": "이 장은 시간 자체가 경제 선택의 배후에 있는 궁극적 희소 자원이라고 본다.",
    },
    {
        "chapter_id": "04-labor",
        "question_en": "How is labor described in Chapter 4?",
        "choices_en": [
            "As a means to attain ends, not an end in itself",
            "As a sacred end in itself",
            "As something technology makes permanently irrelevant",
            "As an activity outside economic analysis",
        ],
        "question_ko": "4장에서 노동은 어떻게 설명되는가?",
        "choices_ko": [
            "목적 달성을 위한 수단이지 그 자체가 목적은 아님",
            "그 자체로 신성한 목적",
            "기술이 영구히 무의미하게 만드는 것",
            "경제 분석 바깥의 활동",
        ],
        "answer_index": 0,
        "explanation_en": "Labor is treated as purposeful effort used to achieve chosen ends.",
        "explanation_ko": "노동은 선택된 목적을 이루기 위한 목적 있는 노력으로 다뤄진다.",
    },
    {
        "chapter_id": "05-property",
        "question_en": "Why does Chapter 5 treat property as foundational?",
        "choices_en": [
            "Because scarcity requires rules for exclusive control",
            "Because property eliminates all conflict automatically",
            "Because property matters only after production ends",
            "Because property is unrelated to ethics",
        ],
        "question_ko": "5장이 재산권을 기초적 제도로 다루는 이유는 무엇인가?",
        "choices_ko": [
            "희소성이 배타적 통제 규칙을 요구하기 때문",
            "재산권이 자동으로 모든 갈등을 없애기 때문",
            "생산이 끝난 뒤에만 중요하기 때문",
            "윤리와 무관하기 때문",
        ],
        "answer_index": 0,
        "explanation_en": "Property is foundational because scarce means require clear rules of control to avoid conflict.",
        "explanation_ko": "희소한 수단을 둘러싼 갈등을 피하려면 명확한 통제 규칙이 필요하기 때문에 재산권이 기초가 된다.",
    },
    {
        "chapter_id": "06-capital",
        "question_en": "What does capital mainly represent in Chapter 6?",
        "choices_en": [
            "Advance provision and saving for future production",
            "Only government spending",
            "Immediate consumption with no delay",
            "A rejection of planning",
        ],
        "question_ko": "6장에서 자본은 주로 무엇을 의미하는가?",
        "choices_ko": [
            "미래 생산을 위한 선행 준비와 저축",
            "오직 정부 지출",
            "지연 없는 즉각적 소비",
            "계획의 거부",
        ],
        "answer_index": 0,
        "explanation_en": "Capital is presented as future-oriented provision built through saving and planning.",
        "explanation_ko": "자본은 저축과 계획을 통해 형성된 미래지향적 준비로 제시된다.",
    },
    {
        "chapter_id": "07-technology",
        "question_en": "What is technology primarily treated as in Chapter 7?",
        "choices_en": [
            "Human reason applied to production",
            "A force unrelated to institutions",
            "A purely state-driven phenomenon",
            "An enemy of innovation",
        ],
        "question_ko": "7장에서 기술은 주로 무엇으로 다뤄지는가?",
        "choices_ko": [
            "생산에 적용된 인간 이성",
            "제도와 무관한 힘",
            "순전히 국가 주도 현상",
            "혁신의 적",
        ],
        "answer_index": 0,
        "explanation_en": "Technology is described as reason and innovation applied within production.",
        "explanation_ko": "기술은 생산에 적용된 이성과 혁신으로 설명된다.",
    },
    {
        "chapter_id": "08-energy-and-power",
        "question_en": "Why is energy treated as central in Chapter 8?",
        "choices_en": [
            "Because it expands the quantity and quality of human action",
            "Because it replaces all capital",
            "Because it makes trade unnecessary",
            "Because it removes scarcity entirely",
        ],
        "question_ko": "8장에서 에너지가 중심적으로 다뤄지는 이유는 무엇인가?",
        "choices_ko": [
            "인간 행동의 양과 질을 확장하기 때문",
            "모든 자본을 대체하기 때문",
            "무역을 불필요하게 만들기 때문",
            "희소성을 완전히 없애기 때문",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter treats energy as a key economic input that broadens productive possibilities.",
        "explanation_ko": "이 장은 에너지를 생산 가능성을 넓히는 핵심 경제 투입요소로 본다.",
    },
    {
        "chapter_id": "09-trade",
        "question_en": "What makes trade beneficial in Chapter 9?",
        "choices_en": [
            "Voluntary exchange and specialization",
            "One side defeating the other",
            "The elimination of division of labor",
            "Central planners fixing every price",
        ],
        "question_ko": "9장에서 무역이 유익한 이유는 무엇인가?",
        "choices_ko": [
            "자발적 교환과 특화",
            "한쪽이 다른 쪽을 패배시키기 때문",
            "분업을 없애기 때문",
            "중앙계획자가 모든 가격을 고정하기 때문",
        ],
        "answer_index": 0,
        "explanation_en": "Trade benefits both sides through specialization and voluntary exchange.",
        "explanation_ko": "무역은 특화와 자발적 교환을 통해 양측 모두에게 이익을 준다.",
    },
    {
        "chapter_id": "10-money",
        "question_en": "How does Chapter 10 characterize money?",
        "choices_en": [
            "As the most marketable good that coordinates exchange",
            "As a quantity planners can optimize by decree",
            "As a purely state-created fiction",
            "As a substitute for all production",
        ],
        "question_ko": "10장은 화폐를 어떻게 규정하는가?",
        "choices_ko": [
            "교환을 조정하는 가장 높은 시장성의 재화",
            "정책 당국이 명령으로 최적화할 수 있는 양",
            "순전히 국가가 만든 허구",
            "모든 생산을 대체하는 것",
        ],
        "answer_index": 0,
        "explanation_en": "Money is presented as the most marketable good that emerges to facilitate exchange.",
        "explanation_ko": "화폐는 교환을 원활하게 하기 위해 등장한 가장 높은 시장성의 재화로 제시된다.",
    },
    {
        "chapter_id": "11-markets",
        "question_en": "What does Chapter 11 say markets do?",
        "choices_en": [
            "Coordinate decentralized action into social order",
            "Destroy all information signals",
            "Eliminate private ownership",
            "Require central control to function",
        ],
        "question_ko": "11장은 시장이 무엇을 한다고 설명하는가?",
        "choices_ko": [
            "분산된 행동을 사회적 질서로 조정한다",
            "모든 정보 신호를 파괴한다",
            "사적 소유를 제거한다",
            "작동하려면 중앙 통제가 필요하다",
        ],
        "answer_index": 0,
        "explanation_en": "Markets are described as discovery and coordination processes under private property.",
        "explanation_ko": "시장은 사적 소유 아래에서 발견과 조정을 수행하는 과정으로 설명된다.",
    },
    {
        "chapter_id": "12-capitalism",
        "question_en": "What institutional combination defines capitalism in Chapter 12?",
        "choices_en": [
            "Private property, voluntary exchange, and capital accumulation",
            "State monopoly, rationing, and coercion",
            "No prices and no profit signals",
            "Permanent hostility to entrepreneurship",
        ],
        "question_ko": "12장에서 자본주의를 규정하는 제도적 결합은 무엇인가?",
        "choices_ko": [
            "사적 소유, 자발적 교환, 자본 축적",
            "국가 독점, 배급, 강제",
            "가격도 손익 신호도 없는 체제",
            "기업가정신에 대한 영구적 적대",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter defines capitalism through private property, exchange, and capital accumulation.",
        "explanation_ko": "이 장은 자본주의를 사적 소유, 교환, 자본 축적의 결합으로 설명한다.",
    },
    {
        "chapter_id": "13-time-preference",
        "question_en": "What does lower time preference support according to Chapter 13?",
        "choices_en": [
            "Saving, capital accumulation, and longer planning horizons",
            "Only immediate consumption",
            "The rejection of civilization",
            "The elimination of future-oriented action",
        ],
        "question_ko": "13장에 따르면 낮은 시간선호는 무엇을 뒷받침하는가?",
        "choices_ko": [
            "저축, 자본 축적, 더 긴 계획 지평",
            "즉각적 소비만",
            "문명의 거부",
            "미래지향적 행동의 제거",
        ],
        "answer_index": 0,
        "explanation_en": "Lower time preference makes longer-term saving and civilization-building possible.",
        "explanation_ko": "낮은 시간선호는 장기 저축과 문명적 축적을 가능하게 한다.",
    },
    {
        "chapter_id": "14-credit-and-banking",
        "question_en": "When does banking become dangerous in Chapter 14?",
        "choices_en": [
            "When claims grow beyond real savings",
            "When credit reflects actual savings",
            "When savers and borrowers are coordinated",
            "When money maintains integrity",
        ],
        "question_ko": "14장에서 은행이 위험해지는 때는 언제인가?",
        "choices_ko": [
            "청구권이 실제 저축을 넘어설 때",
            "신용이 실제 저축을 반영할 때",
            "저축가와 차입자가 조정될 때",
            "화폐가 무결성을 유지할 때",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter warns that banking becomes dangerous when claims multiply beyond real saved resources.",
        "explanation_ko": "이 장은 청구권이 실제 저축 자원을 넘어 증식할 때 은행이 위험해진다고 본다.",
    },
    {
        "chapter_id": "15-monetary-expansion",
        "question_en": "What does monetary expansion fail to create, according to Chapter 15?",
        "choices_en": [
            "Real capital",
            "New bank claims",
            "Short-run euphoria",
            "Distorted price signals",
        ],
        "question_ko": "15장에 따르면 통화 팽창이 만들어내지 못하는 것은 무엇인가?",
        "choices_ko": [
            "실제 자본",
            "새로운 은행 청구권",
            "단기적 환호",
            "왜곡된 가격 신호",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter insists that credit expansion cannot substitute for real capital.",
        "explanation_ko": "이 장은 신용 팽창이 실제 자본을 대신할 수 없다고 강조한다.",
    },
    {
        "chapter_id": "16-violence",
        "question_en": "How is violence positioned in Chapter 16?",
        "choices_en": [
            "As the opposite principle to voluntary cooperation",
            "As a natural extension of market exchange",
            "As economically irrelevant",
            "As a form of peaceful specialization",
        ],
        "question_ko": "16장에서 폭력은 어떻게 위치 지워지는가?",
        "choices_ko": [
            "자발적 협력의 반대 원리",
            "시장 교환의 자연스러운 연장",
            "경제적으로 무관한 것",
            "평화적 특화의 한 형태",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter treats violence as the coercive opposite of voluntary order.",
        "explanation_ko": "이 장은 폭력을 자발적 질서의 강제적 반대 원리로 본다.",
    },
    {
        "chapter_id": "17-defense",
        "question_en": "What question drives Chapter 17?",
        "choices_en": [
            "Whether defense must be monopolized by the state",
            "Whether trade should be abolished",
            "Whether money should be ignored",
            "Whether all law should disappear instantly",
        ],
        "question_ko": "17장을 이끄는 핵심 질문은 무엇인가?",
        "choices_ko": [
            "방어가 반드시 국가 독점이어야 하는가",
            "무역을 폐지해야 하는가",
            "화폐를 무시해야 하는가",
            "모든 법이 즉시 사라져야 하는가",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter examines whether defense and law must be monopolized by the state.",
        "explanation_ko": "이 장은 방어와 법이 국가 독점이어야 하는지를 검토한다.",
    },
    {
        "chapter_id": "18-civilization",
        "question_en": "What does Chapter 18 present as the foundation of civilization?",
        "choices_en": [
            "Reason, property, division of labor, and peaceful cooperation",
            "Permanent coercion and monetary distortion",
            "The abolition of all institutions",
            "Instinct alone",
        ],
        "question_ko": "18장은 문명의 기초를 무엇으로 제시하는가?",
        "choices_ko": [
            "이성, 재산권, 분업, 평화적 협력",
            "영구적 강제와 통화 왜곡",
            "모든 제도의 폐지",
            "오직 본능",
        ],
        "answer_index": 0,
        "explanation_en": "The chapter closes by presenting civilization as the result of rational cooperation under supporting institutions.",
        "explanation_ko": "이 장은 문명을 제도에 의해 뒷받침되는 합리적 협력의 결과로 제시하며 끝난다.",
    },
]

OUT_DIR = Path("books/principles-of-economics/quiz/chapters")
OUT_DIR.mkdir(parents=True, exist_ok=True)

schema = {
    "type": "object",
    "required": [
        "chapter_id",
        "question_en",
        "choices_en",
        "question_ko",
        "choices_ko",
        "answer_index",
        "explanation_en",
        "explanation_ko",
    ],
    "notes": {
        "one_question_per_file": True,
        "choices_length": 4,
        "answer_index_zero_based": True,
    },
}

Path("books/principles-of-economics/quiz/schema.json").write_text(
    json.dumps(schema, ensure_ascii=False, indent=2) + "\n"
)

for quiz in QUIZZES:
    out = OUT_DIR / f"{quiz['chapter_id']}.quiz.json"
    out.write_text(json.dumps(quiz, ensure_ascii=False, indent=2) + "\n")

print(f"Wrote schema and {len(QUIZZES)} quiz files")
