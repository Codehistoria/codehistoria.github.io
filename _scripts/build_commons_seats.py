"""Build data/commons-seats.json and data/commons-seats.csv: one record per seat won
at each UK general election from 1945 to 2024.

Source: candidates.csv from github.com/Tristan-Hotham/elections-since-1832 (MIT licence),
which compiles UK Parliament's official results for 1832 to 2019
(github.com/ukparliament/uk-general-elections) and the House of Commons Library's 2024
results, both under the Open Parliament Licence v3.0.

Usage: python3 _scripts/build_commons_seats.py path/to/candidates.csv
"""
import json, sys, re
import pandas as pd

ELECTIONS = ["1945", "1950", "1951", "1955", "1959", "1964", "1966", "1970",
             "February 1974", "October 1974", "1979", "1983", "1987", "1992",
             "1997", "2001", "2005", "2010", "2015", "2017", "2019", "2024"]
SHORT = {"February 1974": "Feb 1974", "October 1974": "Oct 1974"}

# Blocs, left to right across the chamber. Each party label in the source maps to one bloc.
BLOCS = [
    ("green", "Green", ["Green Party", "Greens", "Green"]),
    ("left", "Other left", ["Communist", "Common Wealth", "Independent Labour Party",
                             "Independent Labour", "Respect", "Independent Progressive"]),
    ("lab", "Labour", ["Labour", "Labour Co-op", "Labour Co-Op"]),
    ("snp", "SNP", ["SNP", "Scottish National Party"]),
    ("pc", "Plaid Cymru", ["Plaid Cymru"]),
    ("irish", "Irish nationalist", ["Sinn Féin", "SDLP", "Social Democratic & Labour Party",
                                     "Nationalist Party of Northern Ireland", "Republican Labour",
                                     "Irish Labour", "Independent Republican", "Unity"]),
    ("lib", "Liberal / Lib Dem", ["Liberal", "Liberal Democrats", "Liberal Democrat",
                                   "Social Democratic", "SDP-Liberal Alliance"]),
    ("ind", "Independent and other", ["Independent", "Speaker", "Health Concern",
                                       "National Independent", "Independent Liberal",
                                       "Democratic Labour", "Alliance"]),
    ("con", "Conservative", ["Conservative", "Scottish Unionist",
                              "National Liberal and Conservative",
                              "Conservative and National Liberal", "Liberal National",
                              "National Liberal", "National Government"]),
    ("union", "Ulster unionist", ["UUP", "Ulster Unionist Party", "DUP",
                                   "Democratic Unionist Party", "Vanguard",
                                   "United Ulster Unionist", "Ulster Popular Unionist",
                                   "UK Unionist", "Protestant Unionist", "Independent Unionist",
                                   "Traditional Unionist Voice"]),
    ("reform", "Reform UK", ["Reform UK"]),
    ("ukip", "UKIP", ["UKIP"]),
]
LABEL_TO_BLOC = {lab: key for key, _, labels in BLOCS for lab in labels}
ORDER = {key: i for i, (key, _, _) in enumerate(BLOCS)}


def display_name(raw):
    """'Gordon, William' -> 'William Gordon'."""
    raw = str(raw).strip()
    if "," in raw:
        surname, rest = raw.split(",", 1)
        return re.sub(r"\s+", " ", f"{rest.strip()} {surname.strip()}")
    return raw


def main(path):
    k = pd.read_csv(path, low_memory=False, dtype={"election": str})
    k = k[k.election.isin(ELECTIONS)].copy()
    out, rows = {}, []
    for e in ELECTIONS:
        ek = k[k.election == e]
        winners = ek[ek.elected == True]
        unknown = sorted(set(winners.party) - set(LABEL_TO_BLOC))
        if unknown:
            sys.exit(f"{e}: party labels with no bloc: {unknown}")
        seats = []
        for w in winners.itertuples():
            contest = ek[ek.constituency == w.constituency].sort_values("votes", ascending=False)
            n_seats = int(contest.elected.sum())
            unopposed = pd.isna(w.votes)
            majority = None
            if not unopposed and n_seats == 1 and len(contest) > 1:
                majority = int(contest.votes.iloc[0] - contest.votes.iloc[1])
            seats.append({
                "c": w.constituency,
                "m": display_name(w.candidate),
                "p": w.party,
                "b": LABEL_TO_BLOC[w.party],
                "s": None if pd.isna(w.share) else round(float(w.share), 1),
                "j": majority,
                "u": bool(unopposed),
            })
        seats.sort(key=lambda s: (ORDER[s["b"]], s["p"], s["c"], s["m"]))
        out[SHORT.get(e, e)] = seats
        for s in seats:
            rows.append({"election": e, "constituency": s["c"], "mp": s["m"], "party": s["p"],
                         "bloc": dict((b[0], b[1]) for b in BLOCS)[s["b"]],
                         "vote_share_pct": s["s"], "majority": s["j"],
                         "unopposed": s["u"]})
    # Compact page file: party labels listed once; each seat is
    # [constituency, MP, party index, vote share %, majority] (share null = returned unopposed)
    parties = sorted({s["p"] for v in out.values() for s in v}, key=lambda p: (ORDER[LABEL_TO_BLOC[p]], p))
    pidx = {p: i for i, p in enumerate(parties)}
    # A list, not an object: browsers reorder year-like object keys, which would put 1974 last
    compact = [{"name": e, "seats": [[s["c"], s["m"], pidx[s["p"]], s["s"], s["j"]] for s in v]}
               for e, v in out.items()]
    page = {"blocs": [{"key": key, "name": name} for key, name, _ in BLOCS],
            "parties": [[p, LABEL_TO_BLOC[p]] for p in parties],
            "elections": compact}
    with open("data/commons-seats.json", "w", encoding="utf-8") as f:
        json.dump(page, f, ensure_ascii=False, separators=(",", ":"))
    pd.DataFrame(rows).to_csv("data/commons-seats.csv", index=False)
    print({e: len(v) for e, v in out.items()})


if __name__ == "__main__":
    main(sys.argv[1])
