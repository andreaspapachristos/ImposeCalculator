# from itertools import chain
'''''
Copyright 2021 Andreas Papachristos

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''''

def find4up(diaireteos, dieretis):
    an = (12, 9, 8, 6, 4, 3, 2)

    for i in an:
        if (diaireteos // dieretis) >= i:
            return i
    return 0



def matchMontaz(**kwargs):
    if 'bleed' in kwargs:
        bleed = kwargs.get('bleed') *2
    else: bleed = 6
    ph = kwargs.get('pageHeight') + bleed #kwargs.get('bleed') *2
    #else: ph = kwargs.get('pageHeight') + 6
    if 'gap' in kwargs:
        gap = kwargs.get('gap')
    else:
        gap = 10
    if kwargs.get('paperHeight') < kwargs.get('paperWidth'):

        pph = kwargs.get('paperHeight') - gap
        #else: pph = kwargs.get('paperHeight') - 10
    else:
        pph = kwargs.get('paperWidth') - gap #kwargs.get('gap')

    temp = []
    if kwargs.get('monofyllo', True):
        pw = kwargs.get('pagewidth') + bleed//2 #kwargs.get('bleed') * 2
        if (kwargs.get('paperHeight') < kwargs.get('paperWidth')):
            ppw = kwargs.get('paperWidth')
        else:
            ppw = kwargs.get('paperHeight')
        #ppw = kwargs.get('paperWidth')
        temp.append([ppw // pw, pph // ph, 0])
        temp.append([ppw // ph, pph // pw, 1])
        #print(temp)
        return (temp)
    else:
        pw = (kwargs.get('pagewidth') * 2) + bleed #kwargs.get('bleed') *2
        #ppw = kwargs.get('paperWidth')  # /2
        if kwargs.get('paperHeight') < kwargs.get('paperWidth'):
            ppw = kwargs.get('paperWidth')
        else:
            ppw = kwargs.get('paperHeight')
        temp.append([ppw // pw, find4up(pph, ph), 0])  # pph//ph]
        temp.append([find4up(ppw, ph), pph // pw, 1])  # ppw//ph
        #print(temp)
        return (temp)


def betterUse(papers, page, monofyllo, bleed, gap):
    embadonp = page[0] * page[1]
    temp = 0
    result = []
    for n in papers:
        m = matchMontaz(pagewidth=page[0], pageHeight=page[1], paperWidth=n[0], paperHeight=n[1], monofyllo=monofyllo, bleed=int(bleed), gap=int(gap))
        embadon = (n[0] * n[1]) #- (gap * n[0])
        #print(p)
        for p in m:
            if monofyllo:
                y = (p[0] * p[1]) * embadonp
                #pages = p[0] * p[1]
            else:
                y = (p[0] * p[1]) * embadonp * 2
            #print(format(y / embadon, '.2f'))
            if float(format(y / embadon, '.4f')) >= float(temp):
                temp = format(y/embadon,'.2f')
                xarti = n[0], n[1]
                grid = p[0], p[1], p[2]
                if(monofyllo):
                    pages = p[0] * p[1]
                else:
                    pages = p[0] * p[1] * 2
    result.append(temp)
    result.append(xarti)
    result.append(pages)
    result.append(grid)
    print(result[0], result[1], result[2], result[3])
    return result


def getCandidates(papers, page, monofyllo, bleed, gap):
    """
    Συγκεντρώνει τις υποψήφιες διατάξεις μοντάζ
    για όλα τα διαθέσιμα χαρτιά.
    """

    candidates = []

    page_area = page[0] * page[1]

    if page_area <= 0:
        return candidates

    for paper in papers:
        paper_width = paper[0]
        paper_height = paper[1]

        if paper_width <= 0 or paper_height <= 0:
            continue

        layouts = matchMontaz(
            pagewidth=page[0],
            pageHeight=page[1],
            paperWidth=paper_width,
            paperHeight=paper_height,
            monofyllo=monofyllo,
            bleed=int(bleed),
            gap=int(gap)
        )

        paper_area = paper_width * paper_height

        for layout in layouts:
            columns = layout[0]
            rows = layout[1]
            rotation = layout[2]

            if columns <= 0 or rows <= 0:
                continue

            if monofyllo:
                pages_per_sheet = columns * rows
            else:
                pages_per_sheet = columns * rows * 2

            used_area = pages_per_sheet * page_area
            utilization = used_area / paper_area

            candidate = {
                "paper": (paper_width, paper_height),
                "grid": (columns, rows, rotation),
                "pages_per_sheet": pages_per_sheet,
                "utilization": utilization,
                "utilization_percent": utilization * 100
            }

            candidates.append(candidate)

    candidates.sort(
        key=lambda candidate: candidate["utilization"],
        reverse=True
    )

    return candidates

def getScheme(pages):
    sixteen = pages // 16
    remainder = pages % 16

    eight = remainder // 8
    remainder = remainder % 8

    four = remainder // 4
    remainder = remainder % 4

    if remainder:
        raise ValueError(
            f"Σφάλμα: περισσεύουν {remainder} σελίδες "
            "και δεν μπορούν να βιβλιοδετηθούν."
        )

    return sixteen, eight, four


def preparePageCount(pages):
    """
    Προσθέτει νοητά λευκές σελίδες στο τέλος,
    ώστε το σύνολο να είναι πολλαπλάσιο του 4.
    Δεν αλλάζει το αρχικό αρχείο ή το περιεχόμενο.
    """

    if not isinstance(pages, int) or isinstance(pages, bool) or pages <= 0:
        raise ValueError("Ο αριθμός σελίδων πρέπει να είναι θετικός ακέραιος.")

    # Πόσες λευκές σελίδες χρειάζονται;
    blank_pages = (-pages) % 4

    # Συνολικός αριθμός μετά την προσθήκη λευκών.
    padded_pages = pages + blank_pages

    return {
        "requested_pages": pages,
        "blank_pages": blank_pages,
        "padded_pages": padded_pages
    }


def getSchemeOptions(
    pages,
    allowed_signature_sizes=(16, 8, 4),
    allow_12=False
):
    """
    Επιστρέφει όλους τους δυνατούς συνδυασμούς
    αναπτυγμάτων που καλύπτουν τις σελίδες του εντύπου.

    Τα μεγέθη δίνονται σε σελίδες ανά ανάπτυγμα.
    Οι κατανομές εμφανίζονται από τα μεγαλύτερα
    προς τα μικρότερα αναπτύγματα.
    """

    if (
        not isinstance(pages, int)
        or isinstance(pages, bool)
        or pages <= 0
    ):
        raise ValueError(
            "Ο αριθμός σελίδων πρέπει να είναι θετικός ακέραιος."
        )

    valid_sizes = {4, 8, 12, 16, 24, 32}
    sizes = set(allowed_signature_sizes)

    if allow_12:
        sizes.add(12)
    else:
        sizes.discard(12)

    invalid_sizes = sizes - valid_sizes

    if invalid_sizes:
        raise ValueError(
            f"Μη έγκυρα μεγέθη αναπτυγμάτων: {invalid_sizes}"
        )

    if 4 not in sizes:
        raise ValueError(
            "Στα επιτρεπόμενα μεγέθη πρέπει να υπάρχει το 4σέλιδο."
        )

    # Προσθέτουμε λευκές σελίδες μέχρι το σύνολο
    # να γίνει πολλαπλάσιο του 4.
    blank_pages = (-pages) % 4
    total_pages = pages + blank_pages

    # Εξετάζουμε πρώτα τα μεγαλύτερα αναπτύγματα.
    sizes = sorted(sizes, reverse=True)

    schemes = []

    def find_schemes(remaining, start_index, current):
        # Βρέθηκε συνδυασμός που καλύπτει όλες τις σελίδες.
        if remaining == 0:
            schemes.append(tuple(current))
            return

        # Επιτρέπουμε επανάληψη του ίδιου μεγέθους,
        # αλλά όχι αλλαγή σε αύξουσα σειρά.
        for index in range(start_index, len(sizes)):
            size = sizes[index]

            if size > remaining:
                continue

            current.append(size)

            find_schemes(
                remaining - size,
                index,
                current
            )

            current.pop()

    find_schemes(total_pages, 0, [])

    # Κρατάμε μία εγγραφή ανά διαφορετικό συνδυασμό.
    options = []

    for scheme in schemes:
        options.append({
            "requested_pages": pages,
            "blank_pages": blank_pages,
            "total_pages": total_pages,
            "preferred_signature_size": scheme[0],
            "signatures": list(scheme)
        })

    return options

def getAllowedSignatureSizes(
    paper_weight,
    paper_type="standard",
    max_signature_size=None,
    allow_12=False
):
    """
    Επιστρέφει τα επιτρεπόμενα μεγέθη αναπτυγμάτων.

    Για κοινό εκτυπωτικό χαρτί χρησιμοποιεί τα αρχικά
    όρια γραμμαρίων που ορίσαμε.

    Για χαρτί γραφής, ειδικό χαρτί ή βάρος εκτός
    των γνωστών ορίων απαιτεί ρητή επιλογή μέγιστου
    αναπτύγματος.
    """

    standard_sizes = (32, 24, 16, 8, 4)
    valid_sizes = (32, 24, 16, 12, 8, 4)

    paper_type = paper_type.strip().lower()

    # Αν έχει δοθεί ρητό όριο, αυτό υπερισχύει.
    if max_signature_size is not None:

        if max_signature_size not in valid_sizes:
            raise ValueError(
                f"Μη έγκυρο μέγεθος αναπτύγματος: "
                f"{max_signature_size}"
            )

        maximum = max_signature_size

    else:
        # Δεν αποφασίζουμε αυτόματα για χαρτιά
        # με ειδική συμπεριφορά στο δίπλωμα.
        if paper_type in ("writing", "special"):
            raise ValueError(
                "Για χαρτί γραφής ή ειδικό χαρτί "
                "όρισε το max_signature_size χειροκίνητα."
            )

        if paper_weight <= 110:
            maximum = 32
        elif paper_weight <= 115:
            maximum = 24
        elif paper_weight <= 170:
            maximum = 16
        else:
            raise ValueError(
                "Για βάρος πάνω από 170 g/m² "
                "όρισε το max_signature_size χειροκίνητα."
            )

    # Τα συνηθισμένα μεγέθη είναι 32, 24, 16, 8 και 4.
    allowed = [
        size for size in standard_sizes
        if size <= maximum
    ]

    # Το 12σέλιδο προστίθεται μόνο κατ' εξαίρεση.
    if allow_12 and maximum >= 12:
        allowed.append(12)

    return tuple(sorted(allowed, reverse=True))
