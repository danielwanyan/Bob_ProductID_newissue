import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT / "pir_rules_structured_v4.2.json"
COMPRESSED_PATH = ROOT / "judgment_criteria_pir_v4.2_compressed.txt"


REQUIRED_ISSUE_TYPES = [
    "suspected_ipr",
    "low_quality",
    "new_issue_supplement",
    "no_package",
    "uncomfortable",
    "new_guest_vulgar_visual",
    "strict_vulgar_or_ansa",
    "prohibited",
    "sensitive_word",
    "crude",
    "lgbt_related",
    "novelty",
    "child_sexualization",
    "politically_sensitive",
]


REQUIRED_RULE_SNIPPETS = {
    "lgbt_related": ["GAY", "six-color Pride", "novelty"],
    "uncomfortable": ["severe hair loss", "skeleton", "body-condition"],
    "prohibited": [
        "replica currency",
        "prop money",
        "COPY",
        "water gun",
        "high-pressure water gun",
        "copper/brass",
        "decorative",
        "miniature",
        "does not exempt",
    ],
    "crude": ["bitch", "PLOUISE", "brand whitelist"],
    "new_guest_vulgar_visual": ["shapewear", "mannequin lower-body", "new_guest_vulgar_visual"],
    "strict_vulgar_or_ansa": ["Do not upgrade", "body-focused", "explicit private-part exposure"],
    "no_package": ["cover image", "exposed food", "hygiene"],
}


COMPRESSED_SNIPPETS = [
    "replica currency",
    "water gun",
    "high-pressure water gun",
    "copper/brass",
    "decorative weapon-shaped",
    "severe hair loss",
    "six-color Pride",
    "PLOUISE",
    "Do not upgrade to strict_vulgar_or_ansa only because",
]


def flatten(value):
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def main():
    rules = json.loads(RULES_PATH.read_text(encoding="utf-8"))
    issue_types = rules.get("issue_types", {})
    missing = [key for key in REQUIRED_ISSUE_TYPES if key not in issue_types]
    if missing:
        raise AssertionError(f"missing issue types in structured rules: {missing}")

    for issue_type, snippets in REQUIRED_RULE_SNIPPETS.items():
        issue_text = flatten(issue_types[issue_type])
        absent = [snippet for snippet in snippets if snippet not in issue_text]
        if absent:
            raise AssertionError(f"{issue_type} missing snippets: {absent}")

    prohibited = issue_types["prohibited"]
    if prohibited.get("business_layer") != "new_guest_only":
        raise AssertionError("prohibited business_layer must remain new_guest_only")
    prohibited_text = flatten(prohibited)
    for snippet in (
        "Water-gun, water/foam cleaning-tool",
        "Copper/brass gun-shaped products also remain prohibited",
        "This exception does not apply to water guns",
    ):
        if snippet not in prohibited_text:
            raise AssertionError(f"prohibited boundary missing exact guard: {snippet}")

    compressed = COMPRESSED_PATH.read_text(encoding="utf-8")
    absent_compressed = [snippet for snippet in COMPRESSED_SNIPPETS if snippet not in compressed]
    if absent_compressed:
        raise AssertionError(f"compressed rules missing snippets: {absent_compressed}")

    print("PIR v4.2 rules regression checks passed")


if __name__ == "__main__":
    main()
