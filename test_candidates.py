

from diastaseis import getCandidates, betterUse, getScheme, getSchemeOptions, getAllowedSignatureSizes, getSignatureYield, getSchemeOptions

papers = [
    [700, 1000],
    [640, 900],
    [610, 860]
]

candidates = getCandidates(
    papers=papers,
    page=[210, 280],
    monofyllo=True,
    bleed=3,
    gap=8
)
getScheme(132)

for i, candidate in enumerate(candidates, start=1):
    print(
        f'{i}. Χαρτί: {candidate["paper"]} | '
        f'Διάταξη: {candidate["grid"]} | '
        f'Σελίδες/φύλλο: {candidate["pages_per_sheet"]} | '
        f'Αξιοποίηση: {candidate["utilization_percent"]:.2f}%'
    )
print("\nΈλεγχος υπάρχουσας betterUse:")

best = betterUse(
    papers,
    [210, 280],
    True,
    3,
    8
)

print("Επιστροφή:", best)

print("\nΈλεγχος αναπτύγματος:")

spread_candidates = getCandidates(
    papers=papers,
    page=[210, 280],
    monofyllo=False,
    bleed=3,
    gap=8
)

for i, candidate in enumerate(spread_candidates, start=1):
    print(
        f'{i}. Χαρτί: {candidate["paper"]} | '
        f'Διάταξη: {candidate["grid"]} | '
        f'Σελίδες/φύλλο: {candidate["pages_per_sheet"]} | '
        f'Αξιοποίηση: {candidate["utilization_percent"]:.2f}%'
    )

print("\nΚατανομές για έντυπο 20 σελίδων:")

print("\nΧαρτί που επιτρέπει έως 16σέλιδο:")
for option in getSchemeOptions(
    20,
    allowed_signature_sizes=(16, 8, 4)
):
    print(option["signatures"])

print("\nΧαρτί που επιτρέπει έως 8σέλιδο:")
for option in getSchemeOptions(
    20,
    allowed_signature_sizes=(8, 4)
):
    print(option["signatures"])

print("\nΕιδική περίπτωση με 12σέλιδο:")
for option in getSchemeOptions(
    20,
    allowed_signature_sizes=(16, 8, 4),
    allow_12=True
):
    print(option["signatures"])

print("\nΈλεγχος κανόνων χαρτιού:")

test_cases = [
    ("Κοινό χαρτί 100 g", 100, "standard", None),
    ("Κοινό χαρτί 112 g", 112, "standard", None),
    ("Κοινό χαρτί 150 g", 150, "standard", None),
    ("Χαρτί 190 g", 190, "standard", 8),
    ("Χαρτί γραφής 120 g", 120, "writing", 8),
]

for label, weight, paper_type, manual_limit in test_cases:

    allowed = getAllowedSignatureSizes(
        paper_weight=weight,
        paper_type=paper_type,
        max_signature_size=manual_limit
    )

    options = getSchemeOptions(
        pages=20,
        allowed_signature_sizes=allowed
    )

    schemes = [option["signatures"] for option in options]

    print(f"\n{label}:")
    print("Επιτρεπόμενα μεγέθη:", allowed)
    print("Κατανομές 20 σελίδων:", schemes)

print("\nΈλεγχος παραγωγικής απόδοσης:")

spread_candidates = getCandidates(
    papers=[[700, 1000]],
    page=[168, 240],
    monofyllo=False,
    bleed=3,
    gap=8
)

best_layout = spread_candidates[0]

print("Καλύτερη γεωμετρική διάταξη:", best_layout["grid"])

for signature_size in (16, 8, 4):
    result = getSignatureYield(
        best_layout,
        signature_size
    )

    print(
        f'{signature_size}σέλιδο: '
        f'{result["copies_per_sheet"]} αντίτυπα/φύλλο, '
        f'{result["salons_per_sheet"]} σαλόνια συνολικά'
    )
