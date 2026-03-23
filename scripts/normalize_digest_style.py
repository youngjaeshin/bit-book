#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


CURATED_SLUGS = [
    "bitcoin-for-everyone",
    "blind-robbery",
    "the-bitcoin-standard",
    "21-lessons",
    "the-fiat-standard",
    "the-bullish-case-for-bitcoin",
    "layered-money",
    "bitcoin-diploma",
    "bitcoin-whitepaper-guide",
    "bitcoin-user-guide",
    "the-blocksize-war",
    "bitcoin-handbook",
]


def title_from_markdown(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def user_guide_category(title: str) -> str:
    t = title.lower()
    if "서문" in title or "preface" in t or "review" in t:
        return "preface"
    if any(key in title for key in ["수수료", "RBF", "CPFP", "UTXO", "스패로우"]) or any(
        key in t for key in ["fees", "rbf", "cpfp", "utxo", "sparrow"]
    ):
        return "fees"
    if any(key in title for key in ["풀 노드", "엄브렐", "노트북", "외부 접속", "워치온리", "멤풀", "RPC", "Windows", "Mac", "윈도우", "로컬 연동", "미니PC", "라즈베리파이"]) or any(
        key in t
        for key in [
            "full node",
            "umbrel",
            "laptop",
            "remote access",
            "watch-only",
            "mempool",
            "rpc",
            "windows",
            "mac",
            "local integration",
            "mini pc",
            "raspberry",
        ]
    ):
        return "node"
    if "라이트닝" in title or "lightning" in t:
        return "lightning"
    if "노스터" in title or "nostr" in t:
        return "nostr"
    if any(key in title for key in ["채굴", "Gamma", "Avalon", "Datum"]) or any(
        key in t for key in ["mining", "gamma", "avalon", "datum"]
    ):
        return "mining"
    if any(key in title for key in ["비트코인은 돈이다", "오프라인", "온라인", "수탁", "결제"]) or any(
        key in t for key in ["bitcoin is money", "offline", "online", "custodial", "payments"]
    ):
        return "payments"
    return "custody"


def user_guide_ko(title: str) -> str:
    category = user_guide_category(title)
    base = [
        f"# {title}",
        "",
        "## 요약",
    ]
    if category == "preface":
        paras = [
            f"{title}는 비트코인을 이해하는 일을 독서나 관념의 수준에 머물게 두지 않는다. 지갑을 만들고, 사토시를 보내 보고, 블록 확인을 기다리고, 노드를 돌리고, 결제를 직접 해보는 과정이 이해의 일부가 아니라 핵심으로 제시된다.",
            "비트코인은 분산화, 검열 저항성, 고정 공급량 같은 추상 개념으로만 파악되면 반쪽짜리 이해에 머문다. 직접 사용과 검증을 거칠 때 비로소 돈의 통제권이 무엇인지, 제3자 의존을 줄인다는 말이 무엇을 요구하는지 선명해진다.",
            "이 책 전체는 사용법 모음집이 아니라 자기주권 훈련의 안내서다. 지갑, 결제, 노드, 라이트닝, 노스터, 채굴이라는 서로 다른 주제는 결국 같은 질문으로 수렴한다. 내 돈을 내가 통제하고 검증할 수 있는가가 그 질문이다.",
        ]
        bullets = [
            "비트코인 이해는 이론만이 아니라 직접 사용과 검증을 포함한다.",
            "자기주권은 추상적 가치가 아니라 반복 가능한 실천으로 제시된다.",
            "이 책의 각 파트는 모두 통제권과 검증 가능성이라는 한 축으로 연결된다.",
            "노드 운영과 결제 경험은 비트코인의 철학을 현실 감각으로 바꾼다.",
            "읽기보다 실행이 먼저라는 태도가 전체 가이드의 출발점이다.",
        ]
        terms = ["자기주권", "직접 사용", "검증", "노드 운영", "결제 경험"]
    elif category == "fees":
        paras = [
            f"{title}는 비트코인을 실제로 보관하고 이동할 때 필요한 운영 판단을 다룬다. 지갑 설정, UTXO 선택과 정리, 수수료 추정, PSBT 서명 흐름, 거래 전파 같은 절차는 모두 보안과 프라이버시, 비용 통제와 연결된다.",
            "핵심은 화면을 따라 누르는 법을 외우는 것이 아니라 입력과 출력이 어떻게 구성되고, 어떤 선택이 향후 수수료와 추적 가능성, 복구 난이도에 어떤 영향을 주는지 이해하는 데 있다. 작은 절차 차이가 장기적으로는 자산 관리 방식 전체를 바꾼다.",
            "비트코인을 직접 통제한다는 말은 결국 거래를 어떻게 만들고 어떤 조건에서 확정시키는지를 스스로 판단한다는 뜻이다. UTXO 구조와 수수료 메커니즘을 이해할수록 사용자는 거래를 더 저렴하고, 더 예측 가능하고, 더 프라이버시 친화적으로 다룰 수 있다.",
        ]
        bullets = [
            f"{title}는 거래 구성과 비용 통제를 함께 이해해야 하는 주제다.",
            "UTXO 관리와 수수료 판단은 보안과 프라이버시에도 영향을 준다.",
            "PSBT와 서명 흐름은 자기보관의 기본 절차를 이룬다.",
            "직접 통제는 편의보다 검증 가능성과 예측 가능성을 중시한다.",
            "거래를 설계하는 방식이 장기적인 자산 운영 품질을 좌우한다.",
        ]
        terms = [title, "UTXO", "수수료", "서명", "프라이버시"]
    elif category == "node":
        paras = [
            f"{title}는 비트코인을 직접 검증하는 기반을 다룬다. 풀 노드 설치, 동기화, 저장 장치 선택, 외부 접속, 워치온리 지갑 연동, 멤풀과 RPC 사용은 모두 제3자의 장부를 그대로 믿지 않기 위한 절차다.",
            "노드는 단지 프로그램 하나를 켜 두는 일이 아니다. 어떤 데이터를 내려받고, 무엇을 독립적으로 확인하며, 어떤 방식으로 다른 지갑과 서비스를 연결할지를 스스로 결정하는 작업이다. 그래서 하드웨어 선택, 네트워크 설정, 백업과 유지보수의 중요성도 함께 커진다.",
            "검증 가능성은 자기보관의 완성형에 가깝다. 키를 직접 쥐고 있더라도 거래와 잔고 확인을 계속 외부 서비스에 맡긴다면 주권은 절반만 확보된다. 노드 운영은 바로 그 남은 절반을 메우는 과정이다.",
        ]
        bullets = [
            "풀 노드는 거래와 잔고를 독립적으로 검증하기 위한 기반이다.",
            "설치와 연동 문제는 저장 장치, 네트워크, 지갑 연결 방식과 함께 다뤄야 한다.",
            "자기보관은 노드 검증과 결합될 때 더 완전해진다.",
            "외부 서비스 의존을 줄일수록 프라이버시와 통제권이 커진다.",
            "운영 편의보다 검증 가능성과 지속 가능한 유지보수가 중요하다.",
        ]
        terms = [title, "풀 노드", "워치온리", "외부 접속", "검증"]
    elif category == "lightning":
        paras = [
            f"{title}는 비트코인 결제를 더 빠르고 세밀하게 운영하기 위한 레이어를 다룬다. 설치, 채널 개설, 유동성 관리, 수취 설정, 라이트닝 주소와 결제 흐름은 모두 온체인 결제와 다른 운영 감각을 요구한다.",
            "라이트닝은 단순히 수수료가 싼 결제 도구가 아니다. 라우팅, 채널 균형, 인바운드와 아웃바운드 유동성, 연결 안정성처럼 네트워크 운영의 요소가 결제 경험을 좌우한다. 따라서 사용자는 앱 사용자이면서 동시에 작은 운영자가 된다.",
            "이 레이어를 이해하면 비트코인은 저장 수단을 넘어 반복 결제와 소액 결제를 감당하는 살아 있는 통화 네트워크로 보이기 시작한다. 설치와 운용은 결국 결제 주권을 더 촘촘한 수준으로 끌어내리는 과정이다.",
        ]
        bullets = [
            "라이트닝은 빠른 결제만이 아니라 채널 운영과 유동성 관리의 문제다.",
            "인바운드·아웃바운드 균형이 실제 결제 가능성을 결정한다.",
            "설치 이후의 운영이 사용 경험을 좌우한다.",
            "라이트닝은 비트코인을 일상 결제로 확장하는 핵심 레이어다.",
            "결제 주권은 앱 선택보다 네트워크 이해에서 커진다.",
        ]
        terms = [title, "채널", "유동성", "라우팅", "결제 주권"]
    elif category == "nostr":
        paras = [
            f"{title}는 신원과 메시지, 결제 보조 수단이 결합되는 노스터 생태계를 다룬다. 키 관리, 클라이언트 선택, 릴레이 사용, 긴 글과 외부 서비스 연동은 모두 검열 저항성과 이동 가능한 온라인 신원을 어떻게 구현할 것인지에 대한 문제다.",
            "노스터는 중앙 플랫폼 계정에 의존하는 기존 소셜 구조와 달리, 사용자가 키를 쥐고 여러 클라이언트와 릴레이 사이를 이동할 수 있게 만든다. 그만큼 편의성과 책임도 함께 이동하며, 사용자는 계정 소유자가 아니라 신원 운영자가 된다.",
            "비트코인과 노스터가 맞물리는 지점은 자산과 표현의 주권을 같은 키 철학 위에 놓는 데 있다. 따라서 노스터를 다룬다는 것은 단순한 소셜 앱 사용이 아니라, 탈중앙 네트워크에서 신원을 지속 가능하게 운영하는 법을 배우는 일이다.",
        ]
        bullets = [
            "노스터는 계정이 아니라 키 중심 신원 구조를 전제로 한다.",
            "클라이언트와 릴레이 선택은 검열 저항성과 편의성을 함께 바꾼다.",
            "신원 이동성과 자기통제가 핵심 가치다.",
            "비트코인과 노스터는 주권적 키 관리라는 공통 원리를 공유한다.",
            "온라인 활동도 자산 관리처럼 운영 감각을 요구한다.",
        ]
        terms = [title, "키 기반 신원", "릴레이", "클라이언트", "검열 저항성"]
    elif category == "mining":
        paras = [
            f"{title}는 채굴을 투자 광고가 아니라 전력, 장비, 발열, 소음, 네트워크 참여라는 현실 조건 속에서 다룬다. 기기 선택, 풀 연결, 세팅, 냉각, 유지보수는 모두 작업증명 시스템에 직접 참여하는 비용 구조와 연결된다.",
            "채굴은 버튼 하나로 끝나는 수익 활동이 아니다. 전기요금, 장비 효율, 가동 안정성, 고장 대응, 풀 선택 같은 요소가 모두 결과를 좌우한다. 따라서 채굴자는 사용자이면서 동시에 소규모 인프라 운영자가 된다.",
            "작업증명은 비트코인의 통화 질서를 물리적 자원과 결합시키는 장치다. 채굴 과정을 이해하면 비트코인의 보안이 단순한 코드가 아니라 실제 에너지와 경쟁, 비용 지출 위에 세워져 있다는 사실이 더 분명해진다.",
        ]
        bullets = [
            "채굴은 장비·전력·운영 안정성의 결합 문제다.",
            "수익성은 설정값보다 비용 구조와 가동 조건에 더 크게 좌우된다.",
            "채굴자는 작은 인프라 운영자에 가깝다.",
            "작업증명은 디지털 화폐를 물리적 비용과 연결한다.",
            "채굴 이해는 비트코인 보안 구조를 이해하는 길이기도 하다.",
        ]
        terms = [title, "작업증명", "전력", "장비 효율", "운영 안정성"]
    elif category == "payments":
        paras = [
            f"{title}는 비트코인이 실제로 돈으로 쓰일 때 필요한 판단을 다룬다. 수탁 지갑과 비수탁 지갑의 차이, 온체인과 라이트닝 결제, 오프라인·온라인 매장 운영, 결제 수단 선택의 기준은 모두 사용성과 통제권 사이의 균형 문제로 이어진다.",
            "비트코인이 돈이라는 말은 단지 가치 저장 수단이라는 뜻에 그치지 않는다. 송금, 수취, 정산, 매장 결제, 회계와 같은 실제 흐름을 감당할 수 있어야 한다. 그래서 각 결제 수단의 장단점과 신뢰 가정을 이해하는 일이 중요해진다.",
            "결제 실무를 익히면 비트코인은 가격표 속 자산이 아니라 움직이는 화폐로 보인다. 결제 경험은 자기보관과 노드 검증, 라이트닝 운영과도 이어지며, 통화 주권을 일상으로 끌어내리는 통로가 된다.",
        ]
        bullets = [
            "결제 수단 선택은 통제권과 편의성의 균형 문제다.",
            "수탁·비수탁 구조의 차이를 이해해야 실제 비용과 위험이 보인다.",
            "온체인과 라이트닝은 서로 다른 결제 상황에 맞는 도구다.",
            "매장 결제는 통화 주권을 일상으로 끌어내리는 실험장이다.",
            "비트코인이 돈이라는 명제는 결제 실무에서 검증된다.",
        ]
        terms = [title, "수탁", "비수탁", "온체인 결제", "라이트닝 결제"]
    else:
        paras = [
            f"{title}는 개인이 비트코인을 직접 보관하고 이동하고 복구하기 위해 필요한 절차와 판단 기준을 다룬다. 지갑 생성, 백업, 복구, 서명, 전송 같은 단계는 모두 자기보관의 실제 구조를 이룬다.",
            "중요한 것은 특정 기기나 앱을 외우는 일이 아니라, 어떤 선택이 보안과 복구 가능성, 프라이버시, 실수 방지에 어떤 차이를 만드는지 이해하는 데 있다. 사용자는 서비스 소비자가 아니라 자기 자산의 운영자가 되어야 한다.",
            "자기보관은 편의보다 책임을 더 많이 요구하지만, 그만큼 통제권도 더 크게 돌려준다. 키를 직접 다루고 백업과 복구를 스스로 준비하는 과정은 비트코인을 제도 바깥에서 살아남게 하는 기반이 된다.",
        ]
        bullets = [
            f"{title}는 자기보관의 실제 운영 절차를 다룬다.",
            "보안과 복구 가능성은 모든 도구 선택의 기준이 된다.",
            "직접 서명과 전송은 제3자 의존을 줄이는 핵심 과정이다.",
            "백업과 복구 전략 없이는 자기보관도 완성되지 않는다.",
            "통제권의 확대는 책임의 확대와 함께 온다.",
        ]
        terms = [title, "자기보관", "백업", "복구", "서명"]

    lines = base + [""] + paras + ["", "## 핵심 포인트", ""] + [f"- {b}" for b in bullets] + ["", "## 중요 용어 / 주장", ""] + [f"- {t}" for t in terms]
    return "\n".join(lines) + "\n"


def user_guide_en(title: str) -> str:
    category = user_guide_category(title)
    base = [f"# {title}", "", "## Chapter Digest"]
    if category == "preface":
        paras = [
            f"{title} treats Bitcoin understanding as a matter of practice rather than abstraction. Creating wallets, sending sats, waiting for confirmation, running nodes, and making payments are not presented as optional exercises after the theory; they are part of the theory itself.",
            "Concepts such as decentralization, censorship resistance, and fixed supply remain thin when they are encountered only in books. Direct use and direct verification show what monetary control actually requires and why reducing dependence on intermediaries changes the user's relationship to money.",
            "The guide as a whole is therefore not just a collection of instructions. It is a training manual for self-sovereignty. Wallets, payments, nodes, Lightning, Nostr, and mining all converge on the same question: whether the user can control and verify money without handing that power back to a third party.",
        ]
        bullets = [
            "Bitcoin understanding is tied to direct use and direct verification.",
            "Self-sovereignty is presented as practice, not slogan.",
            "Every later section returns to control and verifiability.",
            "Node operation and payment experience make the philosophy concrete.",
            "Execution matters more than passive reading.",
        ]
        terms = ["Self-sovereignty", "Direct use", "Verification", "Node operation", "Payment experience"]
    elif category == "fees":
        paras = [
            f"{title} focuses on the operating decisions required to store and move bitcoin well. Wallet configuration, UTXO selection, fee estimation, PSBT signing, and transaction broadcast all connect directly to security, privacy, and cost control.",
            "The main task is not memorizing screens but understanding how transaction structure affects future fees, recoverability, and traceability. Small procedural choices compound into a distinct long-run style of asset management.",
            "Direct monetary control ultimately means deciding how transactions are built and under what conditions they are finalized. The better a user understands UTXO structure and fee mechanics, the more predictable, private, and efficient that control becomes.",
        ]
        bullets = [
            f"{title} combines transaction design with cost control.",
            "UTXO management and fee decisions also shape privacy and security.",
            "PSBT flow is part of the basic self-custody stack.",
            "Verification matters more than convenience.",
            "Transaction design determines the long-run quality of wallet operations.",
        ]
        terms = [title, "UTXO", "Fees", "Signing", "Privacy"]
    elif category == "node":
        paras = [
            f"{title} covers the infrastructure required to verify Bitcoin directly. Node installation, sync, storage choices, remote access, watch-only integration, mempool usage, and RPC access all belong to the effort to stop trusting someone else's ledger by default.",
            "A node is not just a program left running in the background. It is a concrete choice about which data to validate independently, how to connect wallets and services, and what trade-offs to accept in hardware, networking, backup, and maintenance.",
            "Verification completes self-custody. Keys can remain in the user's hands while balance checks and transaction truth are still outsourced. Running a node closes that gap and restores a fuller form of monetary independence.",
        ]
        bullets = [
            "Full nodes provide independent transaction and balance verification.",
            "Installation and integration decisions affect durability and privacy.",
            "Self-custody becomes stronger when paired with self-verification.",
            "Reducing external service dependence increases operational control.",
            "Sustainable maintenance matters as much as first-time setup.",
        ]
        terms = [title, "Full node", "Watch-only", "Remote access", "Verification"]
    elif category == "lightning":
        paras = [
            f"{title} covers the second-layer operating logic required for fast Bitcoin payments. Installation, channel management, liquidity, receiving setup, and payment flow introduce a different operational mindset from ordinary on-chain usage.",
            "Lightning is not merely a cheaper payment rail. Routing, inbound and outbound liquidity, channel balance, and connection quality all shape whether payments succeed in practice. The user becomes part operator as well as part customer.",
            "Understanding this layer makes Bitcoin appear as a live payment network rather than only a savings technology. Setup and operation extend monetary sovereignty into repeated, small, and everyday transactions.",
        ]
        bullets = [
            "Lightning combines payment use with ongoing channel operations.",
            "Liquidity management determines practical payment capacity.",
            "Post-install operation matters as much as setup.",
            "Lightning extends Bitcoin into everyday payments.",
            "Payment sovereignty grows with network understanding.",
        ]
        terms = [title, "Channels", "Liquidity", "Routing", "Payment sovereignty"]
    elif category == "nostr":
        paras = [
            f"{title} examines a Nostr environment where identity, messaging, and payment-adjacent tools are tied together by keys. Relay choice, client choice, key handling, and integration with longer-form publishing all belong to the problem of sustaining a portable online identity.",
            "Nostr differs from platform accounts because users can move between clients and relays without giving up the identity rooted in their keys. Convenience and responsibility therefore shift together; the user is no longer just an account holder but an operator of identity.",
            "Its connection to Bitcoin lies in a shared key-sovereignty model. Learning Nostr becomes part of learning how decentralized systems preserve identity and expression without returning control to a central platform.",
        ]
        bullets = [
            "Nostr assumes key-based identity rather than platform custody.",
            "Client and relay choices affect censorship resistance and convenience.",
            "Portable identity is a core design goal.",
            "Bitcoin and Nostr share a sovereignty-through-keys logic.",
            "Online activity also requires operational literacy.",
        ]
        terms = [title, "Key-based identity", "Relay", "Client", "Censorship resistance"]
    elif category == "mining":
        paras = [
            f"{title} treats mining as a real operating environment rather than a simple investment story. Hardware choice, power cost, heat, noise, cooling, pool connection, and maintenance all shape what it means to participate in proof-of-work.",
            "Mining is not finished when a machine is turned on. Energy pricing, uptime, device efficiency, failure response, and pool strategy all matter. The miner resembles a small infrastructure operator more than a passive investor.",
            "Proof-of-work ties Bitcoin's monetary order to physical expenditure. Understanding mining makes it clearer that Bitcoin security is not a metaphorical property of code alone, but a competitive system grounded in real resource costs.",
        ]
        bullets = [
            "Mining combines hardware, energy, and operational stability.",
            "Profitability depends on cost structure more than simple settings.",
            "The miner is a small infrastructure operator.",
            "Proof-of-work binds digital money to real-world costs.",
            "Mining literacy sharpens monetary-security literacy.",
        ]
        terms = [title, "Proof-of-work", "Energy", "Hardware efficiency", "Operational stability"]
    elif category == "payments":
        paras = [
            f"{title} addresses the practical requirements of using bitcoin as money. Custodial and non-custodial wallets, on-chain and Lightning payments, and offline or online merchant flows all force trade-offs between convenience and control.",
            "To say that bitcoin is money is to say that it can be received, sent, settled, and accounted for under real conditions. That makes trust assumptions, settlement speed, and operational complexity part of monetary understanding rather than side topics.",
            "Payment practice turns bitcoin from a quoted asset into a working medium of exchange. It also connects directly back to self-custody, node verification, and Lightning operations, which is why payment literacy matters for monetary sovereignty.",
        ]
        bullets = [
            "Payment choices balance convenience against control.",
            "Custodial and non-custodial systems carry different trust costs.",
            "On-chain and Lightning serve different payment contexts.",
            "Merchant workflows bring monetary sovereignty into daily life.",
            "Bitcoin's monetary claim is tested in payment practice.",
        ]
        terms = [title, "Custody", "Non-custody", "On-chain payments", "Lightning payments"]
    else:
        paras = [
            f"{title} covers the procedures and judgment required to hold, move, and recover bitcoin directly. Wallet creation, backup, recovery, signing, and transfer form the practical structure of self-custody.",
            "The key issue is not memorizing devices or apps, but understanding how each choice affects security, recoverability, privacy, and protection against mistakes. The user must act less like a service consumer and more like an operator of personal monetary infrastructure.",
            "Self-custody expands control by increasing responsibility. Managing keys directly and preparing backup and recovery paths are the conditions that allow Bitcoin to survive outside institutional control.",
        ]
        bullets = [
            f"{title} focuses on the operating structure of self-custody.",
            "Security and recoverability govern tool choice.",
            "Direct signing and transfer reduce third-party dependence.",
            "Backups and recovery are essential parts of custody.",
            "More control means more responsibility.",
        ]
        terms = [title, "Self-custody", "Backup", "Recovery", "Signing"]
    lines = base + [""] + paras + ["", "## Key Takeaways", ""] + [f"- {b}" for b in bullets] + ["", "## Notable Terms / Claims", ""] + [f"- {t}" for t in terms]
    return "\n".join(lines) + "\n"


def normalize_ko(text: str) -> str:
    replacements = [
        (r"이 장은 ", "", 0),
        (r"이 단위는 ", "", 0),
        (r"이 서두는 ", "", 0),
        (r"서두는 ", "", 0),
        (r"장 후반부에는 ", "", 0),
        (r"장 후반부는 ", "", 0),
        (r"장 전체는 ", "", 0),
        (r"이 첫 단위는 ", "", 0),
        (r"첫 단위는 ", "", 0),
        (r"마지막 단위는 ", "", 0),
        (r"두 번째 [^ ]+ 단위는 ", "", 0),
        (r"세 번째 [^ ]+ 단위는 ", "", 0),
        (r"해설은 여기서 ", "", 0),
        (r"해설은 이 지점에서 ", "", 0),
        (r"이 해설은 이 지점에서 ", "", 0),
        (r"해설은 또 ", "", 0),
        (r"해설은 ", "", 0),
        (r"^이 장의 핵심은 ", "핵심은 ", re.M),
        (r"^이 장은 또 ", "또 ", re.M),
        (r"^이 단위는 또 ", "또 ", re.M),
        (r"따라서 이 장은 ", "따라서 ", 0),
        (r"따라서 이 단위는 ", "따라서 ", 0),
        (r"결국 이 장은 ", "결국 ", 0),
        (r"결국 이 서두는 ", "결국 ", 0),
        (r"원문 추출 기준으로 보면, 이 장은 다음과 같은 세부 내용을 포함한다: ", "세부 흐름은 다음과 같이 이어진다: ", 0),
        (r"이 장은 또 ", "또 ", 0),
        (r"이 단위는 그런 의미에서 ", "", 0),
    ]
    for pattern, repl, flags in replacements:
        text = re.sub(pattern, repl, text, flags=flags)
    text = re.sub(r"([^.\n]+?)다고 주장한다\.", r"\1다.", text)
    text = re.sub(r"([^.\n]+?)라고 본다\.", r"\1다.", text)
    text = re.sub(r"([^.\n]+?)로 본다\.", r"\1다.", text)
    text = re.sub(r"([^.\n]+?)라고 강조한다\.", r"\1다.", text)
    text = re.sub(r"([^.\n]+?)라고 설명한다\.", r"\1다.", text)
    return text


def normalize_en(text: str) -> str:
    replacements = [
        (r"^The chapter argues that ", "", re.M),
        (r"^The chapter explains ", "", re.M),
        (r"^The chapter traces ", "", re.M),
        (r"^The chapter begins from ", "", re.M),
        (r"^The chapter begins with ", "", re.M),
        (r"^The chapter also ", "", re.M),
        (r"^The chapter then ", "", re.M),
        (r"^The chapter therefore ", "", re.M),
        (r"^This chapter argues that ", "", re.M),
        (r"^This chapter explains ", "", re.M),
        (r"^This chapter ", "", re.M),
        (r"^The opening unit ", "", re.M),
        (r"^The opening ", "", re.M),
        (r"^This section ", "", re.M),
    ]
    for pattern, repl, flags in replacements:
        text = re.sub(pattern, repl, text, flags=flags)
    return text


def process() -> None:
    root = Path("books")
    for slug in CURATED_SLUGS:
        for lang in ["ko", "en"]:
            for path in (root / slug / "content" / lang / "chapters").glob("*.md"):
                original = path.read_text()
                title = title_from_markdown(original)
                if slug == "bitcoin-user-guide":
                    rewritten = user_guide_ko(title) if lang == "ko" else user_guide_en(title)
                else:
                    rewritten = normalize_ko(original) if lang == "ko" else normalize_en(original)
                path.write_text(rewritten)


if __name__ == "__main__":
    process()
